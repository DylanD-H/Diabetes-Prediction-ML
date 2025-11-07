import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('./Diabetes Classification.csv', index_col=0)
df['Gender'] = df['Gender'].str.upper()

df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)
df_full_train = df_full_train.reset_index(drop=True)
y_train = df_full_train.Diagnosis.values
del df_full_train['Diagnosis']

dv = DictVectorizer()
train_dict = df_full_train.to_dict(orient='records')
X_train = dv.fit_transform(train_dict)

model = RandomForestClassifier(random_state=1, max_depth=20, max_features='sqrt', min_samples_split=10, n_estimators=300)
model.fit(X_train, y_train)

with open('RandomForestClassifier.bin', 'wb') as f_out:
    pickle.dump((dv,model), f_out)