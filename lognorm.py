#データ元
#https://ganjoho.jp/reg_stat/statistics/data/dl/index.html
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

input = pd.read_csv('./cancer.csv',header=None)
#がん死亡者数[年度、男性の死亡者数、女性の死亡者数]
cancers=input.values
#年度
year=[]
#男性の死亡者数
male=[]
#女性の死亡者数
female=[]

for i in range(len(cancers)):
    year.append(cancers[i][0])
    male.append(cancers[i][1])
    female.append(cancers[i][2])

plt.xlabel("Year", fontsize=20)  
plt.ylabel("Fatalities", fontsize=20) 
plt.bar(year, male, width=0.6)
plt.show()
