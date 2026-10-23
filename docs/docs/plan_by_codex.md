# Four-Week Student Dropout Competition Plan

## Project goal

Build a model that predicts whether a student will **drop out**, remain **enrolled**, or **graduate** using the UCI *Predict Students' Dropout and Academic Success* dataset.

The dataset contains 4,424 students and 36 features. It includes both enrollment-time information and academic performance from the first and second semesters.

Before modeling, decide which prediction scenario the competition expects:

- **Early prediction:** use only information available at enrollment or early in the first semester.
- **Maximum predictive performance:** allow first- and second-semester academic variables.

Maintain both feature sets. Semester-performance features may be very predictive, but they could be data leakage if the intended use case is early intervention.

## Week 1: Understand and validate the data

### Deliverables

- Download and preserve the original dataset in `data/raw/`.
- Create a reproducible data-loading and preprocessing script.
- Document every feature and when it becomes available.
- Confirm the following:
    - Target distribution and class imbalance
    - Duplicate rows
    - Invalid or unusual values
    - Feature data types
    - Integer-coded categorical variables
    - Missing values
    - Correlated or redundant features
- Produce an initial EDA report containing:
    - Class counts
    - Dropout rate by course, age, gender, tuition status, attendance, and prior education
    - Grade and academic-performance distributions
    - Missingness and outlier checks
- Establish stratified cross-validation or a fixed stratified validation split.
- Add basic tests for data loading, expected columns, target values, and row counts.

Do not rely on Pearson correlation alone. Many variables are categorical codes, so use group-level target rates, mutual information, permutation importance, and model-based importance as well.

The current project is still mostly a scaffold: `competitions/dataset.py`, `competitions/features.py`, and `competitions/modeling/train.py` are placeholders. The existing `tests/test_data.py` also contains an intentionally failing test and should be replaced with useful data checks.

## Week 2: Establish strong baselines

Train simple models before tuning complex ones:

- Majority-class baseline
- Stratified dummy baseline
- Multinomial logistic regression
- Random forest or ExtraTrees
- HistGradientBoostingClassifier
- XGBoost, LightGBM, or CatBoost if permitted by the competition

Use a scikit-learn pipeline so encoding, scaling, and feature selection happen inside cross-validation. Do not preprocess the complete dataset before splitting.

Track the competition's official metric as the primary measure. Also report:

- Macro F1
- Per-class precision and recall
- Balanced accuracy
- Confusion matrix
- Log loss, if probability predictions are evaluated

Do not optimize accuracy alone because the dataset has imbalanced classes.

## Week 3: Improve the model systematically

Run controlled experiments and record each result in an experiment table.

| Experiment | Features | Model | Cross-validation metric | Per-class results | Notes |
| --- | --- | --- | ---: | --- | --- |
|  |  |  |  |  |  |

Test the following:

- Enrollment-only features versus semester-performance features
- Class weights and decision thresholds
- One-hot encoding versus native categorical handling
- Age groups and other clearly justified derived features
- Academic performance averages
- Change between first- and second-semester performance
- Credit approval or enrollment ratios
- Tuition and payment-risk indicators
- Repeated stratified cross-validation for stability

Check performance by course, gender, age group, and attendance mode. Use permutation importance or SHAP to understand which variables drive predictions.

Only add external variables if the competition permits them and the variables will be available at prediction time.

## Week 4: Finalize, stress-test, and submit

- Select the model using cross-validation results rather than one lucky split.
- Retrain the selected model on all available training data.
- Run a final data-leakage audit.
- Validate prediction labels, probabilities, row counts, and submission format.
- Submit a working baseline before the final day.
- Run the complete workflow from a clean environment to verify reproducibility.
- Prepare a short report covering:
    - Problem definition
    - Data cleaning
    - Feature availability and leakage decisions
    - Validation strategy
    - Model comparison
    - Final model and results
    - Limitations and fairness considerations

After the final model is selected, make only controlled changes so that improvements can be attributed to specific experiments.

## Team responsibilities

- **Data and EDA:** cleaning, feature dictionary, distributions, and visualizations
- **Modeling:** baselines, cross-validation, hyperparameter tuning, and calibration
- **Validation:** leakage checks, class imbalance, subgroup performance, and reproducibility
- **Documentation and submission:** experiment log, report, citations, and submission formatting

## Important decisions

1. Confirm the competition metric before optimizing anything.
2. Keep early-prediction and post-semester feature sets separate.
3. Use stratified cross-validation.
4. Track dropout recall as well as macro-level metrics.
5. Log every experiment and preserve the validation folds.
6. Establish a working baseline during Week 1.

## Repository setup notes

The project is based on a Cookiecutter Data Science scaffold. Implement the workflow in the existing modules instead of keeping logic only in notebooks:

- `competitions/dataset.py`: load, validate, and prepare raw data
- `competitions/features.py`: create reproducible feature sets
- `competitions/modeling/train.py`: train and evaluate models
- `competitions/modeling/predict.py`: generate predictions and submissions
- `reports/figures/`: store generated plots
- `models/`: store trained models and evaluation summaries

Also review the Python version constraint in `pyproject.toml`. The current `~=3.1.0` constraint appears unintended for a modern Python environment and should be aligned with the version used by the team.