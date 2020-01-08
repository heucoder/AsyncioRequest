import asyncio
from aiohttp import ClientSession
import time

async def fetch(url):
    headers = {
        'Referer':'https://www.bilibili.com/v/anime/finish/',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0',
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'Connection': 'keep-alive'
    } 
    async with ClientSession() as session:
        async with session.get(url=url, headers = headers) as response:
            print(response.status)
            text = await response.text()
            # print(text)
if __name__ == "__main__":
    url1 = 'https://api.bilibili.com/x/web-interface/newlist?callback=jqueryCallback_bili_982754966250929&rid=32&type=0&pn={}&ps=20&jsonp=jsonp&_=1578307922039'
    url = url1.format(1)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch(url))
    
    # tasks = [fetch(url1.format(i)) for i in range(1,201)]
    # loop = asyncio.get_event_loop()
    # start_time = time.clock()
    # loop.run_until_complete(asyncio.wait(tasks))
    # end_time = time.clock()
    # print(end_time - start_time)