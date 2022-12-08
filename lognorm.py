#データ元
#https://ganjoho.jp/reg_stat/statistics/data/dl/index.html
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import lognorm
import math

def log_normal_distribution(i, mu, sigma):
  # 対数正規分布
  x = (1 / (np.sqrt(2 * np.pi) * sigma * i))
  y = (np.e ** (- ((math.log(i) - mu) ** 2) / (2 * sigma ** 2)))
  result = x * y

  return result

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
#平均値
mean=np.mean(male)
#分散値
var=np.var(male)
#対数平均
mu=np.log(mean/np.sqrt(1+var/(mean**2)))
#対数標準偏差
std=np.log(1+np.var(male)/(np.mean(male)**2))
sigma=np.sqrt(std)

# 対数正規分布を実行
n = [log_normal_distribution(i, mu, sigma) for i in year]
plt.plot(year, n)
plt.show()

plt.xlabel("Year", fontsize=20)  
plt.ylabel("Fatalities", fontsize=20) 
plt.bar(year, female, width=0.6)
plt.show()
#平均値
mean=np.mean(female)
#分散値
var=np.var(female)
#対数平均
mu=np.log(mean/np.sqrt(1+var/(mean**2)))
#対数標準偏差
std=np.log(1+np.var(female)/(np.mean(female)**2))
sigma=np.sqrt(std)

# 対数正規分布を実行
n = [log_normal_distribution(i, mu, sigma) for i in year]
plt.plot(year, n)
plt.show()

