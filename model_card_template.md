# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This is a Census Income Classifier that predicts whether an individual's income is above or below $50K.

Model type: Random Forest.

Framework: scikit-learn.

Features used:
age, workclass, fnlgt, education, education-num, marital-status, occupation, relationship, race, sex, capital-gain, capital-loss, hours-per-week, native-country
## Intended Use
For educational and research purposes.

Can be used to analyze census data for income prediction.

Not intended for hiring, lending, or legal decisions (high stakes).
## Training Data
Dataset: UCI Adult Census dataset.
Training split: Data split into training and test sets in train_model.py
Features: age, workclass, education, education-num, marital-status, occupation, relationship, race, sex, capital-gain, capital-loss, hours-per-week, native-country.
## Evaluation Data
Split from the same dataset (train/test split in train_model.py).

Tested on unseen test data to compute precision, recall, F1-score.

Also evaluated on slices of the data by categorical features to detect potential biases
## Metrics
Overall model performance:

Precision: 0.7376

Recall: 0.6288

F1-score: 0.6789

Selected slice performance:

Feature	Category	Count	Precision	Recall	F1-score
workclass	Private	4597	0.7354	0.6254	0.6760
workclass	Self-emp-inc	222	0.7541	0.7797	0.7667
education	Bachelors	1096	0.7483	0.7757	0.7618
education	Masters	318	0.8389	0.8297	0.8343
marital-status	Married-civ-spouse	2977	0.7304	0.6808	0.7047
sex	Female	2158	0.7680	0.6082	0.6788
sex	Male	4355	0.7298	0.6432	0.6838

Note: Additional slices can be found in slice_output.txt.

## Ethical Considerations
Model may reflect biases in the dataset (gender, race, marital status, etc.).

Not suitable for decisions with real-world consequences without additional fairness checks.
## Caveats and Recommendations
The model is limited to the features provided.

Some categories in categorical features have very few samples, which can lead to unstable predictions.

Use caution if deploying in real-world scenarios.