#!/usr/bin/python3
# _*_coding:utf-8 _*_

"""
Author: qinchangshuai(cs_qin@qq.com) 
Date: 2021/1/19 10:24 
"""
from http import cookiejar  # Python 2: import cookielib as cookiejar

import requests
from requests.adapters import HTTPAdapter


session = requests.Session()
# adapter = HTTPAdapter(pool_connections=100, pool_maxsize=100, max_retries=3)
adapter = HTTPAdapter(max_retries=3)
session.mount('http://', adapter)
session.mount('https://', adapter)
session.verify = False


class BlockAll(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False


session.cookies.set_policy(BlockAll())
