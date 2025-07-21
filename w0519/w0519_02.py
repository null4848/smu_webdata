import pandas as pd

#  2차원 데이터 : DataFrame 여러개 컬럼, 여러개 index 구성
# 데이터 구성 : 딕셔너리에 리스트 타입으로 구성됨

data = {
   '이름' : ['강나래', '강태원', '강호림', '김수찬', '김재욱', '박동현', '박혜정', '승근열'],
   '학교' : ['구로고', '구로고', '구로고', '구로고', '구로고', '디지털고', '디지털고', '디지털고'],
   '키' : [197, 184, 168, 187, 188, 202, 188, 190],
   '국어' : [90, 40, 80, 40, 15, 80, 55, 100],
   '영어' : [85, 35, 75, 60, 20, 100, 65, 85],
   '수학' : [100, 50, 70, 70, 10, 95, 45, 90],
   '과학' : [95, 55, 80, 75, 35, 85, 40, 95],
   '사회' : [85, 25, 75, 80, 10, 80, 35, 95],
   'SW특기' : ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']
}

df = pd.DataFrame(data)
print(df.describe())
print(df.info())
print(df['키'].mean())
print(df['키'].sum())
print(df.values)
print(df.index)
print(df.columns)

# index 지정
temp = pd.Series(dta), index=['1월','2월','3월','4월','5월','6월','7월']
df.index.name = "지원번호"
print(df)

# index 삭제 : reset_index(), index정보가 column으로 변경
# drop option index 모두 삭제
# inpalce 옵션 : index가 삭제 된것을 바녕깢 시켜?줌
print(df.reset_index(drop=True, inplace=True))
print(df)

# 1차원 데이터 : Series 1개 컬럽, 여러개의 index 구성
temp = pd.Series([-20,-10,0,10,20]), index=['1월','2월','3월','4월','5월',]
print(temp['1월'])
# print(temp)
# print(temp.sum( ))

