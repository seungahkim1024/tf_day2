import pandas as pd
import numpy as np

ctx = '../data/'
df_pop = pd.read_excel(ctx+'population_in_Seoul.xls'
                    , encoding='UTF-8'
                    , header=2
                    , usecols='B,D,G,J,N') # excel 파일에서 해당 컬럼의 data만 가지고 와라!
df_cctv = pd.read_csv(ctx+'CCTV_in_Seoul.csv')


df_cctv_col = df_cctv.columns
df_pop_col = df_pop.columns

"""
df_cctv_col
구별    소계  2013년도 이전  2014년  2015년  2016년

df_pop_col
구별         인구수        한국인       외국인        고령자
"""

df_cctv.rename(columns={df_cctv.columns[0]:'구별'},inplace=True)
# inplace=True 실제 변수의 내용을 바꿔라


df_pop.rename(columns={df_pop.columns[0]:'구별'
                         , df_pop.columns[1]:'인구수'
                         , df_pop.columns[2]:'한국인'
                         , df_pop.columns[3]:'외국인'
                         , df_pop.columns[4]:'고령자'}
                , inplace=True)

# df = pd.DataFrame(df_cctv)

df_cctv.sort_values(by="소계", ascending=True)  #소계 기준 오름차순 정렬
df_pop.drop([0], inplace=True) #0번행 삭제
df_pop['구별'].unique() #구별기준 중복제거
df_pop[df_pop['구별'].isnull()] #null 체크
df_pop.drop([26],inplace=True) #인구수 기준 오름차순 정렬
df_pop['외국인비율'] = (df_pop['외국인'] / df_pop['인구수']) * 100
df_pop['고령자비율'] = (df_pop['고령자'] / df_pop['인구수']) * 100
df_cctv.drop(['2013년도 이전', '2014년', '2015년', '2016년'],1,inplace=True) #년도별 열 삭제


df_cctv_pop = pd.merge(df_cctv, df_pop, on='구별')

"""
r이 -1.0과 -0.7 사이이면, 강한 음적 선형관계,
r이 -0.7과 -0.3 사이이면, 뚜렷한 음적 선형관계,
r이 -0.3과 -0.1 사이이면, 약한 음적 선형관계,
r이 -0.1과 +0.1 사이이면, 거의 무시될 수 있는 선형관계,
r이 +0.1과 +0.3 사이이면, 약한 양적 선형관계,
r이 +0.3과 +0.7 사이이면, 뚜렷한 양적 선형관계,
r이 +0.7과 +1.0 사이이면, 강한 양적 선형관계
"""
# np.corrcoef()

df_cctv_pop.set_index('구별', inplace=True)

cor1 = np.corrcoef(df_cctv_pop['고령자비율'], df_cctv_pop['소계'])
cor2 = np.corrcoef(df_cctv_pop['외국인비율'], df_cctv_pop['소계'])

#("고령자비율 상관계수 {}, 외국인비율 상관계수 {}"
#     .format(cor1, cor2))

df_cctv_pop.to_csv(ctx+'cctv_pop.csv')