import json
import random
import requests
import time
import csv
import pandas as pd
import locale
from datetime import datetime
locale.setlocale(locale.LC_ALL, 'zh-CN.UTF-8')
from urllib.parse import urlparse, parse_qs

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

url = "https://mp.weixin.qq.com/cgi-bin/appmsg"
headers = {"Cookie": "pgv_pvid=8517027142; pac_uid=0_dec261772ef9a; iip=0; ua_id=c4vMN2zDoRHemvAiAAAAAGjhhvhtkIuaYyTdFQnezuo=; mm_lang=zh_CN; rewardsn=; wxtokenkey=777; uuid=193f870c6ce2620ba50755200a7b74de; rand_info=CAESIEHMqbKs+XowsIeEKfxYcWK2eRbERxDBDtvGP6n7rDKR; slave_bizuin=2393352212; data_bizuin=2393352212; bizuin=2393352212; data_ticket=PO+0EKMvc0MD3cEu4S8OZR8NlGiNib0FzELKOh9b90QcH+jEmqTYTx4C9hPCjapR; slave_sid=VlZCQUdsUDhna0xTMExzTmVqYVBoUFNIdjNSeFJ0amdQeXMyV2p6VDA0UTJjUjdDY3I2Q1pJQnBGWURtN05qaUM1dF9CT2pLY0FwZ2hrYmtuNDg2RkhZOVE2VnJKN2JWMWdwV1R2Q2Z2UTNxYzY4R3pWVmpjYnBEbkNZaTQxODE5S1RxSWU1RFNtRzZqanVw; slave_user=gh_78d1ecfc8245; xid=c7f93b6f809e67833ccdef63e90c2936", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",}
params = { "action": "list_ex", "begin": "0", "count": "5", "fakeid": "MzIxMTExODU1NA==", "type": "9", "token": "1749780661", "lang": "zh_CN", "f": "json", "ajax": "1"}
date, title, read, link = [], [], [], []   

for i in range(20, 40):
    params["begin"] = str(i*5)
    content_json = requests.get(url, headers=headers, params=params, verify=False).json()
    if content_json['base_resp']['ret'] == 200013:
        print("frequencey control, stop at {}".format(params["begin"]))
        break
    if len(content_json['app_msg_list']) == 0:
        print("all ariticle parsed")
        break
    for item in content_json["app_msg_list"]:
        date.append(datetime.fromtimestamp(item['create_time']).strftime("%m.%d(%a)"))
        title.append(item['title'])
        read.append(getReadInfo(item['link']))
        link.append(item['link'])
    print("job complete: i={}".format(str(i)))
    time.sleep(random.randint(5,10))

df = pd.DataFrame({"日期": date, "标题": title, "阅读量": read, "链接": link})
df.to_csv('output.csv', encoding='utf_8_sig')
print("exiting...")