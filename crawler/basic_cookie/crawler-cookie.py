#抓取ppt 八卦版網頁原始碼
import urllib.request as req

#這是主程序
def getData(url):

    request=req.Request(url, headers={
        #建立一個request物件附加headerd資訊
        "cookie":"over18=1",
        #因為他有18禁, 所以我們需要去追蹤他的cookie是哪一個 然後把他複製過來
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"

    #這個user-Agent 在chrome右鍵打開inspect上面的network刷新網頁，跑最多的點進去看到header最下面的就是user-agent
    })
    with req.urlopen(request) as respone:
        data=respone.read().decode("utf-8")
    # print(data)
    #解析資料取得文章標題

    import bs4
    root = bs4.BeautifulSoup(data, "html.parser")#讓beautifulspup協助握們做解析 html 格式文件
    # print(root.title.string)
    # titles=root.find("div",class_="title")
    # #尋找class等於title 的地方
    # print(titles.a.string)


    titles=root.find_all("div",class_="title")
    # print(titles)
    for title in titles:
        if title.a != None:#如果標題含有a標籤(沒有被刪除). 的印出來
            print(title.a.string)

    #抓取上一頁的連結
    nextLink = root.find("a", string = "‹ 上頁")#找到內文是‹ 上頁 的a標籤
    return nextLink["href"]



#抓取一個頁面的標題
pageURL = "https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
while count<100:
    #抓前100頁
    pageURL="https://www.ptt.cc"+getData(pageURL)
    count+=1
    # getData(pageURL)
