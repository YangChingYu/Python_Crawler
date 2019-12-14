import urllib.request as req
url = "https://www.ptt.cc/bbs/movie/index.html"
request=req.Request(url, headers={
    #建立一個request物件附加headerd資訊

    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"
#這個user-Agent 在chrome右鍵打開inspect上面的network刷新網頁，跑最多的點進去看到header最下面的就是user-agent
})
with req.urlopen(request) as respone:
    data=respone.read().decode("utf-8")
print(data)
#解析資料取得文章標題

import bs4
root = bs4.BeautifulSoup(data, "html.parser")#讓beautifulspup協助握們做解析 html 格式文件
print(root.title.string)
titles=root.find("div",class_="title")
#尋找class等於title 的地方
print(titles.a.string)


titles=root.find_all("div",class_="title")
print(titles)
for title in titles:
    if title.a != None:#如果標題含有a標籤(沒有被刪除). 的印出來
        print(title.a.string)