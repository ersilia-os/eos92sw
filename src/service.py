from typing import List

from bentoml import BentoService, api, artifacts
from bentoml.adapters import JsonInput
from bentoml.types import JsonSerializable

import shutil
import os
import csv
import tempfile
import subprocess
import pickle

from bentoml.service import BentoServiceArtifact

CHECKPOINTS_BASEDIR = "checkpoints"
CHECKPOINT_FILE = "etoxpred_best_model.joblib"
FRAMEWORK_BASEDIR = "framework"


def load_etox_model(framework_dir, checkpoints_dir):
    mdl = EToxModel()
    mdl.load(framework_dir, checkpoints_dir)
    return mdl


class EToxModel(object):
    def __init__(self):
        self.DATA_FILE = "_data.csv"
        self.OUTPUT_FILE = "_output.csv"
        self.RUN_FILE = "_run.sh"
        self.LOG_FILE = "run.log"

    def load(self, framework_dir, checkpoints_dir):
        self.framework_dir = framework_dir
        self.checkpoints_dir = checkpoints_dir

    def set_checkpoints_dir(self, dest):
        self.checkpoints_dir = os.path.abspath(dest)

    def set_framework_dir(self, dest):
        self.framework_dir = os.path.abspath(dest)

    def run(self, input_list):
        tmp_folder = tempfile.mkdtemp(prefix="eos-")
        data_file = os.path.join(tmp_folder, self.DATA_FILE)
        output_file = os.path.join(tmp_folder, self.OUTPUT_FILE)
        log_file = os.path.join(tmp_folder, self.LOG_FILE)
        with open(data_file, "w") as f:
            f.write("input" + os.linesep)
            for inp in input_list:
                f.write(inp + os.linesep)
        run_file = os.path.join(tmp_folder, self.RUN_FILE)
        with open(run_file, "w") as f:
            lines = [
                "bash {0}/run.sh {0} {1} {2}".format(
                    self.framework_dir, data_file, output_file
                )
            ]
            f.write(os.linesep.join(lines))
        cmd = "bash {0}".format(run_file)
        with open(log_file, "w") as fp:
            subprocess.Popen(
                cmd, stdout=fp, stderr=fp, shell=True, env=os.environ
            ).wait()
        with open(output_file, "r") as f:
            reader = csv.reader(f)
            h = next(reader)
            result = []
            for r in reader:
                result += [{h[1]: float(r[1]), h[2]: float(r[2])}] 
        shutil.rmtree(tmp_folder)
        print('returning result')
        print(result)
        return result

class EToxArtifact(BentoServiceArtifact):
    """Dummy ETox artifact to deal with file locations of checkpoints"""

    def __init__(self, name):
        super(EToxArtifact, self).__init__(name)
        self._model = None
        self._extension = ".pkl"

    def _copy_checkpoints(self, base_path):
        src_folder = self._model.checkpoints_dir
        dst_folder = os.path.join(base_path, "checkpoints")
        if os.path.exists(dst_folder):
            os.rmdir(dst_folder)
        shutil.copytree(src_folder, dst_folder)

    def _copy_framework(self, base_path):
        src_folder = self._model.framework_dir
        dst_folder = os.path.join(base_path, "framework")
        if os.path.exists(dst_folder):
            os.rmdir(dst_folder)
        shutil.copytree(src_folder, dst_folder)

    def _model_file_path(self, base_path):
        return os.path.join(base_path, self.name + self._extension)

    def pack(self, chemprop_model):
        self._model = chemprop_model
        return self

    def load(self, path):
        model_file_path = self._model_file_path(path)
        chemprop_model = pickle.load(open(model_file_path, "rb"))
        chemprop_model.set_checkpoints_dir(
            os.path.join(os.path.dirname(model_file_path), "checkpoints")
        )
        chemprop_model.set_framework_dir(
            os.path.join(os.path.dirname(model_file_path), "framework")
        )
        return self.pack(chemprop_model)

    def get(self):
        return self._model

    def save(self, dst):
        self._copy_checkpoints(dst)
        self._copy_framework(dst)
        pickle.dump(self._model, open(self._model_file_path(dst), "wb"))


@artifacts([EToxArtifact("model")])
class Service(BentoService):
    @api(input=JsonInput(), batch=True)
    def run(self, input: List[JsonSerializable]):
        input = input[0]
        smiles_list = [inp["input"] for inp in input]
        output = self.artifacts.model.run(smiles_list)
        return [output]
