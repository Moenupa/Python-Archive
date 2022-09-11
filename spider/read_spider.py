from urllib.parse import urlparse, parse_qs
import requests
import time
import json

def getReadInfo(url):
    parsed_url = urlparse(url)
    url = "http://mp.weixin.qq.com/mp/getappmsgext"
    headers = {
        "Cookie": "appmsg_token=appmsg_token=1147_WqnwqZso1Fs%2BTdJmqU0YmA8l517ZpwWDhsC7awxXiVuVSQL-P858QiGkJDb42A5UB8QR9qdBAbb4RbIB; rewardsn=; wxtokenkey=777; wxuin=3354233167; devicetype=Windows10; version=620603c8; lang=zh_CN; pass_ticket=7rYvibkTGmTtjv+L0rRGc7x9EpDt0noa1HRgtUfWomEw8kCGUbonNOV3tx5w+/iO; wap_sid2=CM+Str8MEooBeV9ITUlDY2wyN3l4RW9Wd3RaSUp6X1E0OHNKeWcyVTR6eEJjZjVWdTFidWxoWDAwOVVUcVNONV9DN013UVZlR09yQWI0eHFGR1dQWjFiWXpOOFRjV21oSUx0aloyazJYSXlMZi1BZGFWRnZpWDFydmRzcjB4Q3VLTXIyZUJqY3UtLVNGZ1NBQUF+ML7R2o4GOA1AAQ==",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.884.400 QQBrowser/9.0.2524.400"
    }
    data = {
        "is_only_read": "1",
        "is_temp_url": "0",                
        "appmsg_type": "9",
    }
    params = {
        "__biz": parse_qs(parsed_url.query)['__biz'][0],
        "mid": parse_qs(parsed_url.query)['mid'][0],
        "sn": parse_qs(parsed_url.query)['sn'][0],
        "idx": parse_qs(parsed_url.query)['idx'][0],
        "key": "558d5594ce1b1a1019e0275c00b98b55c6d40baa32f4148b4c0e07e2e62b44d9bd423313548a91e75413a319dcf1c743544486d7064dfbd928f307d60025eb9a3908e688fff507f0fa1148638995b7cb46fb120a8cc5373060ba48696ddeb1bc238a603afcff247cc83a0cb8c3517646751703436f162df168ca0e8aef448352",
        "pass_ticket": "7rYvibkTGmTtjv+L0rRGc7x9EpDt0noa1HRgtUfWomEw8kCGUbonNOV3tx5w+/iO",
        "appmsg_token": "1147_WqnwqZso1Fs%2BTdJmqU0YmA8l517ZpwWDhsC7awxXiVuVSQL-P858QiGkJDb42A5UB8QR9qdBAbb4RbIB",
        "f": "json",
        "wxtokenkey": "777",
        "devicetype": "Windows&nbsp;10",
        "clientversion": "620603c8"
    }
    print(params)
    content = requests.get(url, headers=headers, data=data, params=params).json()
    try:
        return content["appmsgstat"]["read_num"]
    except KeyError:
        # fallback
        origin_url = "https://mp.weixin.qq.com/mp/getappmsgext?"
        appmsgext_url = origin_url + "__biz={}&mid={}&sn={}&idx={}&appmsg_token={}&x5=1".format(params['__biz'], params['mid'], params['sn'], params['idx'], params['appmsg_token'])
        content = requests.post(appmsgext_url, headers=headers, data=data).json()
    
    try:
        return content["appmsgstat"]["read_num"]
    except KeyError:
        return -1

print(getReadInfo("http://mp.weixin.qq.com/s?__biz=MzIxMTExODU1NA==&mid=2649907163&idx=1&sn=a68a43df49d5a678c4ff2a10bc903bcf&chksm=8f5ccf6eb82b46781dfa589d35b9a81017722bd9e6c3d66ddacef331383f552a75bb4e3913c3#rd"))
