#Diabetes Diagnosis using Data Mining and Machine Learning techniques

#Importing Modules 

import numpy as np
import pandas as pd
df=pd.read_csv('diabetes.csv')
df1=pd.read_csv('diabetes_dataset__2019.csv')
df





#Data Preprocessing Steps

DiabetesPedigreeFunction_res= []
for row1 in df['DiabetesPedigreeFunction']:
    if row1<0.5: DiabetesPedigreeFunction_res.append('no')
    elif row1>0.5: DiabetesPedigreeFunction_res.append('yes')
    else: DiabetesPedigreeFunction_res.append('normal')
df['DiabetesPedigreeFunction_res'] = DiabetesPedigreeFunction_res


Ages = []
for row in df['Age']:
    if row<40: Ages.append('less than 40')
    elif row >=40 and row<=49 : Ages.append('40-49')
    elif row >=50 and row<=59: Ages.append('50-59')
    elif row>=60:  Ages.append('60 or older')
    else: Ages.append('Not_Rated')
df['Ages'] = Ages


BP = []
for row1 in df['BloodPressure']:
    if row1<=72: BP.append('normal')
    else: BP.append('high')
df['BP'] = BP

#del pregnancies>3
df.drop(df[df['BloodPressure']==0].index, inplace = True)
df.drop(df[df['Pregnancies']>3].index, inplace = True)
df.drop(df[df['Outcome']>1].index, inplace = True)

df.drop(df[df['SkinThickness']==0].index, inplace = True)

#df.drop(df[df['Outcome']==0].index, inplace = True)
del df['Age']
df['BMI']=round(df['BMI'])
df['BMI'] = df['BMI'].astype(int)


df = df.rename(columns={"BMI":"BodyMassIndex"})





#Merge operations
def select_columns(df, column_names):
    new_frame = df.loc[:, column_names]
    return new_frame
#Age_BMI
age_BMI_col = ['Ages', 'BodyMassIndex']
Age_BMI = select_columns(df, age_BMI_col)
#Age_BP
Age_Bp_col = ['Ages', 'BloodPressure','BP']
Age_BP=select_columns(df, Age_Bp_col)
#Age_Preg
Age_preg_col = ['Ages', 'Pregnancies']
Age_preg=select_columns(df, Age_preg_col)

#Age_outcome
#Age_outcome= ['Ages', 'Outcome']
#Age_outcome_val=select_columns(df, Age_outcome)

#Age_cols
Age_cols= ['Ages', 'DiabetesPedigreeFunction','DiabetesPedigreeFunction_res','Glucose','SkinThickness','Insulin','Outcome']
Age_columns=select_columns(df, Age_cols)


print(Age_columns)
print(Age_BMI)
print(Age_BP)
print(Age_preg)
#print(Age_outcome_val)

df1





#Data Preprocessing Steps
df1['Diabetic']=df1['Diabetic'].str.strip()
df1.drop(df1[df1['Diabetic']=='nan'].index, inplace = True)
for c in df1['Diabetic']:
    if(c=='no'):
        df1['Diabetic'] = df1['Diabetic'].replace(['no'],'1')
    else:
        df1['Diabetic'] = df1['Diabetic'].replace(['yes'],'0')
print(df1)
df1.drop(df1[df1['BMI']=='nan'].index, inplace = True)
df1.drop(df1[df1['Gender']=='Male'].index, inplace = True)
del df1['Pdiabetes']
del df1['highBP']
df1['Pregancies'] = df1['Pregancies'].replace(np.nan, -1)
df1['Pregancies'] = df1['Pregancies'].astype(int)

df1.drop(df1[df1['Pregancies']==-1].index, inplace = True)
df4=pd.merge(df1,Age_preg, left_on=  ['Age','Pregancies'],
                   right_on= ['Ages','Pregnancies'], 
                   how = 'inner')
#df4.to_csv('C:\\Users\\swapn\\OneDrive\\Desktop\\datamine\\Age_preg_inner.csv')
df4
#print(df4.columns)
print(df4)
#print(Age_BMI['Ages'],Age_BMI['BMI']>10)

df5=pd.merge(df4,Age_BP, left_on=  ['Age','BPLevel'],
                   right_on= ['Ages','BP'], 
                   how = 'left')
df5=df5.drop_duplicates()

df6=pd.merge(df5,Age_BMI, left_on=  ['Age','BMI'],
                   right_on= ['Ages','BodyMassIndex'], 
                   how = 'left')
print(df6)
df7=pd.merge(df6,Age_columns, left_on=  ['Age','Family_Diabetes'],
                   right_on= ['Ages','DiabetesPedigreeFunction_res'], 
                   how = 'left')
df7=df7.drop_duplicates()
del df7['Ages_x']
del df7['Ages_y']
del df7['BodyMassIndex']
del df7['Pregnancies']
del df7['BP']
del df7['Outcome']
del df7['DiabetesPedigreeFunction_res']
print(df7)
df7.to_csv('Diab.csv')
