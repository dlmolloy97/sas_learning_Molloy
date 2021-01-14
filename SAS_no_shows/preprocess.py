import pandas as pd
df=pd.read_csv('KaggleV2-May-2016.csv')
#Citation: https://note.nkmk.me/en/python-pandas-sample/
df = df.sample(frac = 1) 
newdf=df.sample(frac=0.90)
newdf.to_csv('cleaned_appt_data.csv')