import pandas as pd
import numpy as np
import openpyxl





data=pd.read_excel('2023年下期期末成绩统计表.xlsx',sheet_name=1)

n=35  #人数
list=data['Unnamed: 2'][1:n+1]
for i in list:
    print(i,end=',')

