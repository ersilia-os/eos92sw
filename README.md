# Toxicity and synthetic accessibility prediction

The eToxPred tool has been developed to predict, on one hand, the synthetic accessibility (SA) score, or how easy it is to make the molecule in the laboratory, and, on the other hand, the toxicity (Tox) score, or the probability of the molecule of being toxic to humans. The authors trained and cross-validated both predictors on a large number of datasets, and demonstrated the method usefulness in building virtual custom libraries.

This model was incorporated on 2021-04-30.


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
- **Interpretation:** Higher scores indicate easier synthetic accessibility and higher toxicity, respectively

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
- **Image Size (Mb):** `1031.45`

**Computational Performance (seconds):**
- 10 inputs: `32.85`
- 100 inputs: `26.61`
- 10000 inputs: `575.43`

### References
- **Source Code**: [https://github.com/pulimeng/eToxPred](https://github.com/pulimeng/eToxPred)
- **Publication**: [https://bmcpharmacoltoxicol.biomedcentral.com/articles/10.1186/s40360-018-0282-6](https://bmcpharmacoltoxicol.biomedcentral.com/articles/10.1186/s40360-018-0282-6)
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
