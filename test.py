import requests
import csv
import time
def asyncRequests(s):
    # print("{}------".format(s))
    # url1 = 'https://api.bilibili.com/x/web-interface/newlist?callback=jqueryCallback_bili_982754966250929&rid=32&type=0&pn=1&ps=20&jsonp=jsonp&_=1578307922039'
    url1 = 'https://api.bilibili.com/x/web-interface/newlist?callback=jqueryCallback_bili_982754966250929&rid=32&type=0&pn={}&ps=20&jsonp=jsonp&_=1578307922039'.format(s)

    headers = {
        'Referer':'https://www.bilibili.com/v/anime/finish/',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0',
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'Connection': 'keep-alive'
    }    
    res1 = requests.get(url1, headers = headers)
    print(res1.status_code)

if __name__ == "__main__":
    # url = 'https://www.bilibili.com/v/anime/finish/#/all/default/0/1/'
    # headers = {
    #     'Referer':'https://www.bilibili.com/v/anime/finish/',
    #     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0',
    #     'Accept-Encoding': 'gzip, deflate',
    #     'Accept': '*/*',
    #     'Connection': 'keep-alive'
    # }
    # session = requests.session()
    # session.headers = headers
    # response = session.get(url = url)
    # print(response.status_code)
    # print(session.cookies)
    # print(session.headers)
    # print('---'*10)
    # requests
    # url1 = 'https://api.bilibili.com/x/web-interface/newlist?callback=jqueryCallback_bili_982754966250929&rid=32&type=0&pn=1&ps=20&jsonp=jsonp&_=1578307922039'
    # res1 = requests.get(url1, headers = headers)
    # print(res1.status_code)
    # f = open("data1.txt", 'w')
    # f.write(res1.text)
    start = time.clock()
    for i in range(1,2):
        asyncRequests(i)
    end = time.clock()
    print("cost time: ", end - start)