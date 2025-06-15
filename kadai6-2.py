import requests

#エンドポイント
endpoint='https://www.jma.go.jp/bosai/forecast/data/forecast/'

# パラメータ
area='120000'

#リクエスト用のurlを作成
url = endpoint+area+'.json' 

# 作成したurlを使いAPIにリクエストを送る
response = requests.get(url).json()

# 天気情報の表示
for i, dt in enumerate(response[0]["timeSeries"][0]["timeDefines"]):
    print(dt + "：" + response[0]["timeSeries"][0]["areas"][0]["weathers"][i])