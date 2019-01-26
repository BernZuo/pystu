# _*_ coding:utf-8 _*_
# @Time     :17:46
# @Author   :zwl
# @Email    :
# @File     :Study.py
# @Software :PyCharm
import pandas
csv_data = pandas.read_csv('FKLL005-getFlowIn3MonthsAvgLabel.csv',header=None)
#print(csv_data[4])
csv_data[4] = csv_data[4].astype(str)
csv_data[4] = csv_data[4].apply(lambda x:x.replace(x,'A') if 'aa' in x else x)
print(csv_data)
csv_data.to_csv('a.csv',index=False,header=False)

