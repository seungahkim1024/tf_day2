import pandas as pd

import googlemaps

ctx = '../data/'
df_crime = pd.read_csv(ctx+'crime_in_Seoul.csv', encoding='euc-kr')


gmaps_key = "AIzaSyAZr9gM_9zi96H6PyWM53T2HoinWLBY_9o"
gmaps = googlemaps.Client(key=gmaps_key)
"""
['관서명', '살인 발생', '살인 검거', '강도 발생', '강도 검거', '강간 발생', 
'강간 검거', '절도 발생', '절도 검거', '폭력 발생', '폭력 검거']
"""
#print(gmaps.geocode('길음뉴타운', language='ko'))

station_name = []
for name in df_crime['관서명']:
    station_name.append('서울'+str(name[:-1])+'경찰서') # -1은 all의 의미를 갖는다.


station_addr = []
station_lat = [] # 위도
station_lng = [] # 경도
for name in station_name:
    tmp = gmaps.geocode(name, language='ko')
    station_addr.append(tmp[0].get('formatted_address'))
    tmp_loc = tmp[0].get('geometry')
    station_lat.append(tmp_loc['location']['lat'])
    station_lng.append(tmp_loc['location']['lng'])
    #print(name+'----->' + tmp[0].get('formatted_address'))
station_name
station_lat
station_lng
gu_names = []
for name in station_addr:
    tmp = name.split()
    tmp_gu = [gu for gu in tmp if gu[-1] == '구'][0]
    gu_names.append(tmp_gu)

# print(len(df_crime['관서명']))
df_crime['구별'] = gu_names
# print(df_crime) #31개의 관서명 존재

# 금천경찰서는 관악구 위치에 있어서 금천서를 찾아서 금천구라고 수동 작업

df_crime.loc[df_crime['관서명']=='금천서', ['구별']] = '금천구'

df_crime.to_csv(ctx+'crime_police.csv', sep=',', encoding='UTF-8')
