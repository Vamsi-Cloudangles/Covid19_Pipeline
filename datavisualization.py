import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
from data_cleaning import data_cleaning
def data_visualization():
    dataset = data_cleaning()
    sns.histplot(dataset['USMER'])
    plt.show()
    sns.histplot(dataset['SEX'])
    plt.show()
    sns.histplot(dataset['PREGNANT'])
    plt.show()
    sns.histplot(dataset['PNEUMONIA'])
    plt.show()
    sns.histplot(dataset['DIABETES'])
    plt.show()
    sns.histplot(dataset['ASTHMA'])
    plt.show()
    sns.histplot(dataset['HIPERTENSION'])
    plt.show()
    sns.histplot(dataset['TOBACCO'])
    plt.show()
    # Count plots ...................
    sns.countplot(x='MEDICAL_UNIT',data=dataset)
    plt.show()
    sns.countplot(x='PATIENT_TYPE',data=dataset)
    plt.show()
    return dataset
data_visualization()