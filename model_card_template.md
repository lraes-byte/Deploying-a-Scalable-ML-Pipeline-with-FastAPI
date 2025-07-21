# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

This is a RandomForestClassifier model that that was trained using Census data. The main task is binary classification which was predicting whether someones income was > $50k or <= $50k per year based on certain characteristics of demographic and employment. The model uses scikit-learn and was terained in a reproducable Python environment. The pipeline uses one-hot encoding and label binarization

## Intended Use

The model is made for educational purposes and for exploration on census data in a tabluar style. It is not made fore real-world decision making and was just made for demonstrating a FastAPI and classification processes.

## Training Data

Using a cleaned version of the Census Income dataset. The features of the data set include age, education, workclass, marital status, relationship,  hours-per-week, and nartive-country. The data set was split 80/20 fpr training and test sets respectively. 

## Evaluation Data

The 20% test set was used to evaluate model performance. This included:
- Overall performance metrics
- Performance on slices of data

## Metrics
_Please include the metrics used and your model's performance on those metrics._

The following metrics were used to evaluate the model:
- Precision = 0.7419
- Recall = 0.6384
- F1-score = 0.6863
## Ethical Considerations

- This model was trained on demographic data which includes PII like sex and race.
- There could be potential biases in the source data.
- Some groups mau have less representation which can lead to skewed or unblanaced results

## Caveats and Recommendations

- The precision and recall vary significantly among the slices. 
- The dataset is also older and may not reflect current census data.
- Recommendation
    - try different models
    - tune model settings to improve accuracy
