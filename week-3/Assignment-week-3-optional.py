from urllib import response
import urllib.request as req
import bs4 #To analyze the data in html format
def WebData(url):
    #建立request物件 附加request headers資訊, to make our code acts as a normal user.
    request=req.Request(url, headers={
        "user-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    
    root=bs4.BeautifulSoup(data, "html.parser") # Let beautifulsoup to help us analyze html format data
    titles=root.find_all("div", class_="title") # find div with class="title"
    PrevUrl=root.find('a', string="‹ 上頁")
    # print(PrevUrl)
    return titles, PrevUrl["href"]



#Analyze source code data to get article title

url="https://www.ptt.cc/bbs/movie/index.html"
countG=0
countN=0
countB=0
Good={}
Normal={}
Bad={}
for i in range(10):
    titles, PrevUrl=WebData(url)
    # print(titles.a.string)
    
    for title in titles:
        if title.a != None:# print title if title contains a tag
            if "[好雷]" in title.a.string:
                title.a.string.replace('Re:','')
                Good[countG]=title.a.string
                countG+=1
            elif "[普雷]" in title.a.string:
                title.a.string.replace('Re:','')
                Normal[countN]=title.a.string
                countN+=1
            elif "[負雷]" in title.a.string:
                title.a.string=title.a.string.replace('Re: ','')
                # print(title.a.string)
                Bad[countB]=title.a.string
                countB+=1
    
    url="https://www.ptt.cc"+PrevUrl
    # print("page:", i)

with open("movie.txt", mode="w",encoding="utf-8") as file:
    for i in range(len(Good)):
        file.write(Good[i]+'\n')
    for i in range(len(Normal)):
        file.write(Normal[i]+'\n')
    for i in range(len(Bad)):
        file.write(Bad[i]+'\n')

