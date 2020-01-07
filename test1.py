import asyncio
import requests
import copy
import time
class asyncRequests:
    def __init__(self):
        self._loop = asyncio.get_event_loop()

    async def s(self):
        done, pending = await asyncio.wait([self.fetch(i) for i in range(200)])
        # for item in done:
            # print(item.result())

    def work(self):
        start = time.clock()
        self._loop.run_until_complete(self.s())
        end = time.clock()
        print("cost time: ", end - start)

    async def fetch(self, s):
        # print("{}---------".format(s))
        url1 = 'https://api.bilibili.com/x/web-interface/newlist?callback=jqueryCallback_bili_982754966250929&rid=32&type=0&pn={}&ps=20&jsonp=jsonp&_=1578307922039'.format(s)

        headers = {
            'Referer':'https://www.bilibili.com/v/anime/finish/',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0',
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            'Connection': 'keep-alive'
        }    
        res1 = requests.get(url1, headers = headers)
        if res1.status_code != 200:
            return res1.status_code
        return res1.status_code

if __name__ == "__main__":
    asyncrequests = asyncRequests()
    asyncrequests.work()

