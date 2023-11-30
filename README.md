# Toxicity and synthetic accessibility prediction

The eToxPred tool has been developed to predict, on one hand, the synthetic accessibility (SA) score, or how easy it is to make the molecule in the laboratory, and, on the other hand, the toxicity (Tox) score, or the probability of the molecule of being toxic to humans. The authors trained and cross-validated both predictors on a large number of datasets, and demonstrated the method usefulness in building virtual custom libraries.

## Identifiers

* EOS model ID: `eos92sw`
* Slug: `etoxpred`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Regression`
* Output: `Score`
* Output Type: `Float`
* Output Shape: `Single`
* Interpretation: Higher scores indicate easier synthetic accessibility and higher toxicity, respectively

## References

* [Publication](https://bmcpharmacoltoxicol.biomedcentral.com/articles/10.1186/s40360-018-0282-6)
* [Source Code](https://github.com/pulimeng/eToxPred)
* Ersilia contributor: [miquelduranfrigola](https://github.com/miquelduranfrigola)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos92sw)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos92sw.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos92sw) (AMD64)

## Citation

If you use this model, please cite the [original authors](https://bmcpharmacoltoxicol.biomedcentral.com/articles/10.1186/s40360-018-0282-6) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a GPL-3.0 license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!