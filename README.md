# Toxicity and synthetic accessibility prediction

## Model Identifiers
* Slug: etoxpred
* Ersilia ID: eos92sw
* Tags: toxicity, synthesis, ADMET 

## Model Description
This model predicts, on one hand, the synthetic accessibility (SA) score, or how easy it is to make the molecule in the laboratory, and, on the other hand, the toxicity (Tox) score, or the probability of the molecule of being toxic to humans.
* Input: SMILES
* Output: Score	(Higher scores indicate easier synthetic accessibility and higher toxicity, respectively)
* Model type: Regression
* Mode of Training: Pretrained
* Training data: 93,460 compounds	(https://github.com/pulimeng/eToxPred/blob/master/training_set.smi)
* Experimentally validated: No

## Source code
This model has been published by Pu, L., Naderi, M., Liu, T. et al. eToxPred: a machine learning-based approach to estimate the toxicity of drug candidates. BMC Pharmacol Toxicol 20, 2 (2019). DOI:https://doi.org/10.1186/s40360-018-0282-6
* Code: https://github.com/pulimeng/eToxPred
* Checkpoints: https://github.com/pulimeng/eToxPred/blob/master/stale/SAScore/sa_dbn.py

## License
The GPL-v3 license applies to all parts of the repository. This repository uses the externally maintained library "eToxPred", located at `/model`.
