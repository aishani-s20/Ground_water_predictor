import numpy as np
import pandas as pd
import joblib

df=pd.read_csv("DWLR_Dataset_2023.csv")

for i in ['Dissolved_Oxygen_mg_L']:
    df[i].fillna(df[i].median(),inplace=True)

def wisker(col):
    q1,q3=np.percentile(col,[25,75])
    iqr=q3-q1
    lw=q1-1.5*iqr
    uw=q3+1.5*iqr
    return lw,uw


for i in ['pH','Rainfall_mm']:
    lw,uw=wisker(df[i])
    df[i]=np.where(df[i]<lw,lw,df[i])
    df[i]=np.where(df[i]>uw,uw,df[i])

df_x=df.drop('Water_Level_m',axis=1)
df_y=df['Water_Level_m']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.2, random_state=42)


from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
joblib.dump(model, 'water_level_model.joblib')