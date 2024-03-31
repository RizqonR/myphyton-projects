import pandas as pd
import numpy as np
file='epl-goalScorer(20-21).csv'
isifile=pd.read_csv(file)
isifile.head
print(isifile.dtypes)

import pandas as pd
import numpy as np
file='epl-goalScorer(20-21).csv'
isifile=pd.read_csv(file)
df_noid=isifile.iloc[:,2:]
df_noid
df_noid.groupby('team_title').mean()
df_noid.groupby('team_title').mean().sort_values(by='goals',ascending='true')
df1=df_noid.groupby('team_title')['goals'].mean()
df1.sort_index()
df2=df1.sort_values(ascending=False)
df2.head()

q1=df_noid['goals'].quantile(0.25)
q3=df_noid['goals'].quantile(0.75)
iqr=q3-q1
iqr
df_noid['goals']

iso=(df_noid['goals']<q1-1.5*iqr)|(df_noid['goals']>q3+1.5*iqr)
iseo=(df_noid['goals']<q1-3*iqr)|(df_noid['goals']<q3+3*iqr)
df1=df_noid[['player_name','goals']].assign(is_outlier=iso,is_extreme_outlier=iseo)
df1.loc[df1['is_outlier'] | df1['is_extreme_outlier']]
