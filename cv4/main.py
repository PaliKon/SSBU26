import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data_hf = pd.read_csv("heart_failure_clinical_records_dataset.csv")
print(data_hf.head())
#print(data_hf.tail())
print(data_hf.shape)
print(data_hf.columns)

print("\nchybajuce hodnoty: ")
print(data_hf.isna().sum())
print("\nduplicit: ")
print(data_hf.duplicated().sum())

#uloha 2
print(data_hf['sex'].value_counts())
print(data_hf.groupby(['sex', 'smoking']).size())

#uloha 3
print("Min vek: ", data_hf['age'].min())
print("Max vek: ", data_hf['age'].max())
print("Priemerny vek: ", data_hf['age'].mean())
print("Najcastejsi vek: ", data_hf['age'].mode())

#uloha4

data_hf['risk'] = data_hf.apply(
    lambda row: 'High' if row['age'] > 50 and row['serum_creatinine'] > 1.2 else 'low', axis=1)

print(data_hf['risk'].value_counts())

high_risk = data_hf[data_hf['risk'] == 'High']
plt.hist(high_risk['age'], bins='auto')
plt.title('High Risk by Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

najvek = high_risk['age'].mode()[0]
print("zaznamov v tejto kategorii: ",(high_risk['age'] == najvek).sum())

#uloha 5
corr = data_hf.corr(numeric_only =True)
print(corr)


plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', vmin=0, vmax=1)
plt.title("Correlation ")
plt.tight_layout()
plt.show()

