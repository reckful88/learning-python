#encoding: utf-8
import requests
r = requests.get("http://www.baidu.com")
r.headers		#http头部信息
r.status_code		#状态码
r.text			#返回数据
r.content		#返回数据

with open("baidu.html","wb") as f:
        f.write(r.content)
        f.flush()

