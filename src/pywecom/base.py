# -*- coding: utf-8 -*-
# @Time        : 2022/6/17 5:41 PM
# @File        : base.py
# @Description : None
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> Mail      : liu_zhao_feng_alex@163.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import json
import os

import requests

from src.pywecom.exception import WeComException

WECOM_API_ROOT_URL = os.environ.get("WECOM_API_ROOT_URL", "https://qyapi.weixin.qq.com/cgi-bin")


def get_access_token(corp_id, app_secret) -> (str, int):
    """
    获取access_token
    :param corp_id: 企业ID
    :param app_secret: 应用密钥
    :return: (access_token, expires_in)
        - access_token: 获取到的凭证，最长为512字节
        - expires_in: 凭证的有效时间（秒），通常为7200
    """
    url = f"{WECOM_API_ROOT_URL}/gettoken?corpid={corp_id}&corpsecret={app_secret}"
    data = json.loads(requests.get(url).content)
    if int(data["errcode"]) == 0:
        return data["access_token"], int(data["expires_in"])
    else:
        raise WeComException(data["errcode"], data["errmsg"])


class WeChatWorkSDK:
    """
    企业微信SDK基本类
    """
    API_ROOT_URL = WECOM_API_ROOT_URL

    def __init__(self, corp_id, app_secret):
        """
        :param corp_id:
        :param app_secret:
        """
        self.corp_id = corp_id
        self.app_secret = app_secret
        self._access_token = None

    @property
    def access_token(self):
        """
        获取access_token
        详细说明：https://developer.work.weixin.qq.com/document/path/91039
        :return access_token: str
        """
        # 新创建的实例或者access_token过期，请求access_token并缓存
        if self._access_token is None:
            access_token, expires_in = get_access_token(corp_id=self.corp_id, app_secret=self.app_secret)
            self._access_token = access_token
        return self._access_token


if __name__ == '__main__':
    wecom = WeChatWorkSDK(corp_id="ww612ee73b2518642a", app_secret="ZF8rE4-ifH2TgVBmz1AqAKgFua0rkMof98phK4PCcho")
    print(wecom.access_token)
