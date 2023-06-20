import argparse
import os
import sys
import csv
import pandas as pd

from rdkit import Chem
from rdkit import rdBase
from rdkit.Chem import AllChem

import numpy as np

from sascore import SAscore
from joblib import load

rdBase.DisableLog("rdApp.error")

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

CHECKPOINTS_BASEDIR = os.path.abspath(os.path.join(__file__,"../../checkpoints"))
CHECKPOINT_FILE = "etoxpred_best_model.joblib" 
modelfile = os.path.join(CHECKPOINTS_BASEDIR, CHECKPOINT_FILE) 

def myargs():
    parser = argparse.ArgumentParser()
    parser.add_argument("--datafile", required=True, help="training data filename")
    parser.add_argument(
        "--outputfile",
        required=False,
        default="./results.csv",
        help="output file to save the result",
    )
    args = parser.parse_args()
    return args


def load_data(smiles_list):            
    mols = [Chem.MolFromSmiles(x) for x in smiles_list] 
    X = []
    cnt = 0
    for mol in mols:
        if mol is None:
            print("Error encountered parsing SMILES {}".format(smiles_list[cnt]))
            continue
        mol = Chem.AddHs(mol)
        fp = AllChem.GetMorganFingerprintAsBitVect(mol, radius=2, nBits=1024)
        fp_string = fp.ToBitString()
        tmpX = np.array(list(fp_string), dtype=float)
        X.append(tmpX)
        cnt += 1
    X = np.array(X)
    return X, smiles_list


def predict(smiles_list):
    df = pd.DataFrame(columns=["smiles", "Tox-score", "SAscore"])
    # laod the data
    X, smiles_list = load_data(smiles_list)
    # load the saved model and make predictions
    print("...loading models")
    clf = load(modelfile)
    reg = SAscore()
    print("...starts prediction")
    for i in range(X.shape[0]):
        tox_score = clf.predict_proba(X[i, :].reshape((1, 1024)))[:, 1]
        sa_score = reg(smiles_list[i]) 
        df.at[i, "smiles"] = smiles_list[i]
        df.at[i, "Tox-score"] = tox_score[0]
        df.at[i, "SAscore"] = sa_score
    print("...prediction done!")
    # df.to_csv(output_file, index=False)
    output = df[['smiles','Tox-score','SAscore']].values.tolist()  
    print('returning output')
    print(output)
    return output
 
# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# run model
outputs = predict(smiles_list)

#check input and output have the same lenght
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

# write output in a .csv file
with open(output_file, "w") as f:
    print('saving output')
    writer = csv.writer(f)
    writer.writerow(['smiles', 'Tox-score', 'SAscore'])  # header
    for r in outputs:
        print(r)
        writer.writerow(r)
    print('saving output done')


