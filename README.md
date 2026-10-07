# Toxicity and synthetic accessibility prediction

Pairs a toxicity estimate with a synthetic accessibility estimate so a candidate can be triaged for safety and for ease of synthesis in one pass, which the authors used to assemble custom virtual screening libraries. eToxPred predicts toxicity with extremely randomized trees over 1024-bit Morgan fingerprints, trained on 1515 FDA-approved drugs against 3035 hazardous chemicals from TOXNET, reaching an AUC of 0.82. The released code computes accessibility with the Ertl and Schuffenhauer fragment score, exponentially rescaled, so here higher values mean easier synthesis.

This model was incorporated on 2021-04-30.Last packaged on 2025-10-08.

## Information
### Identifiers
- **Ersilia Identifier:** `eos92sw`
- **Slug:** `etoxpred`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `ADMET`
- **Target Organism:** `Homo sapiens`
- **Tags:** `Toxicity`, `Synthetic accessibility`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `2`
- **Output Consistency:** `Fixed`
- **Interpretation:** Probability of being toxic, above 0.58 by the authors' cut-off, with higher accessibility values meaning easier synthesis.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| tox_score | float | high | Predicted toxicity score |
| sa_score | float | high | Synthetic accessibility score |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos92sw](https://hub.docker.com/r/ersiliaos/eos92sw)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos92sw.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos92sw.zip)

### Resource Consumption
- **Model Size (Mb):** `59`
- **Environment Size (Mb):** `944`
- **Image Size (Mb):** `1069.58`

**Computational Performance (seconds):**
- 10 inputs: `28.43`
- 100 inputs: `19.72`
- 10000 inputs: `154.69`

### References
- **Source Code**: [https://github.com/pulimeng/eToxPred](https://github.com/pulimeng/eToxPred)
- **Publication**: [https://doi.org/10.1186/s40360-018-0282-6](https://doi.org/10.1186/s40360-018-0282-6)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2019`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [GPL-3.0-only](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos92sw
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos92sw
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
