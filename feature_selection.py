from feature_engineering import feature_engineering

def feature_selection():
    dataset = feature_engineering()
    # Drop the unnecesssary columns
    print(dataset.head())
    dataset.drop(["SEX","PREGNANT","COPD","ASTHMA","INMSUPR","OTHER_DISEASE","CARDIOVASCULAR","OBESITY","TOBACCO"], axis=1, inplace=True)
    print(dataset)
    dataset.to_csv('Covid-19_cleaned_dataset.csv')
    return dataset

feature_selection()



