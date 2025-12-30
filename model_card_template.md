# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This is a Census Income Classifier that predicts whether an individual's income is above or below $50K.

Model type: Random Forest (or whatever you used in train_model.py).

Framework: scikit-learn.
## Intended Use
For educational and research purposes.

Can be used to analyze census data for income prediction.

Not intended for hiring, lending, or legal decisions (high stakes).
## Training Data
UCI Adult Census dataset.

Features: age, workclass, education, education-num, marital-status, occupation, relationship, race, sex, capital-gain, capital-loss, hours-per-week, native-country.
## Evaluation Data
Split from the same dataset (train/test split in train_model.py).

Tested on unseen test data to compute precision, recall, F1-score.
## Metrics
Overall model performance:

Precision: ~0.73

Recall: ~0.63

F1-score: ~0.68

Slice metrics:

workclass: Private → Precision: 0.7354, Recall: 0.6254, F1: 0.6760

education: Bachelors → Precision: 0.7483, Recall: 0.7757, F1: 0.7618

## Ethical Considerations
Model may reflect biases in the dataset (gender, race, marital status, etc.).

Not suitable for decisions with real-world consequences without additional fairness checks.
## Caveats and Recommendations
The model is limited to the features provided.

Some categories in categorical features have very few samples, which can lead to unstable predictions.

Use caution if deploying in real-world scenarios.