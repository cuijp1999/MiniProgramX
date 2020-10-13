import logging

import app
import requests


class UserApi:
    def __init__(self):
        # 获取token
        self.get_token_url = app.base_url + "/token/user"
        # token验证
        self.token_verify_url = app.base_url + "/token/verify"
        # 用户地址
        self.uesr_addr_url = app.base_url + "/address"

    def get_token_api(self):
        """获取token"""
        logging.info("用户 - 获取token")

        data = {"code": app.code}
        logging.info(f"请求参数：{data}")
        return requests.post(self.get_token_url, json=data, headers=app.headers)

    def token_verify_api(self):
        """token验证"""
        logging.info("用户 - token验证")
        # 请求参数
        data = {"token": app.headers.get("token")}
        logging.info(f"请求参数：{data}")
        # 返回响应对象
        return requests.post(self.token_verify_url, json=data, headers=app.headers)

    def user_addr_url(self):
        """用户地址信息"""
        logging.info("用户 - 用户地址信息")
        return requests.get(self.uesr_addr_url, headers=app.headers)
