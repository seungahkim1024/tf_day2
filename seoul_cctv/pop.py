import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile


ctx = '../data/'
xls = pd.read_excel(ctx+'population_in_Seoul.xls')
csv = pd.read_csv(ctx+'CCTV_in_Seoul.csv')

pop_data = xls
cctv_data = csv
print(pop_data.head())
print(cctv_data.head())