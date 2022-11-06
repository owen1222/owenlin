import streamlit as st
import requests

def getAllBookstore():
	url = 'https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M'
	headers = {"accept": "application/json"}
	response = requests.get(url, headers=headers)
	res=response.json()
	return res

def getCountyOption(items):
	optionList=[]# 創建一個空的 List 並命名為 optionList
	for item in items:
		name=item['cityname'][0:3]# 把 cityname 欄位中的縣市名稱擷取出來 並指定給變數 name
		if name not in optionList:
			optionList.append(name)
	return optionList
def app():
	bookstoreList = getAllBookstore()
	countyList = getCountyOption(bookstoreList)# 呼叫 getCountyOption 並將回傳值賦值給變數 countyOption
	# ['台北市', ....]
	st.header('特色書店地圖')
	st.metric('Total bookstore', len(bookstoreList))
	county = st.selectbox('請選擇縣市', ['A', 'B', 'C']) 
	# 將['A', 'B', 'C']替換成縣市選項 
	district = st.multiselect('請選擇區域', ['a', 'b', 'c', 'd'])

if __name__ == '__main__':
	app()
def getSpecificBookstore(items, county, districts):
	specificBookstoreList = []
	for item in items:
		name = item['cityName']
	# 如果 name 不是我們選取的 county 則跳過
	# hint: 用 if-else 判斷並用 continue 跳過
	return specificBookstoreList

