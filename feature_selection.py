from feature_engineering import feature_engineering
import pandas as pd
def feature_selection():
    dataset = feature_engineering()
    # Drop the unnecesssary columns
    print(dataset.head())
    dataset.drop(["SEX","PREGNANT","COPD","ASTHMA","INMSUPR","OTHER_DISEASE","CARDIOVASCULAR","OBESITY","TOBACCO"], axis=1, inplace=True)
    print(dataset)
    dataset.to_csv("Covid-19_cleaned_dataset.csv")
    return dataset

print(feature_selection())
feature_selection()
