import logging

from Api.apiFactory import ApiFactory
import app
import utils
import pytest


@pytest.mark.run(order=0)
class TestUserApi:
    def test_get_token(self):
        """获取token"""
        res = ApiFactory.get_user_api().get_token_api()
        # 打印 请求地址 请求参数 请求响应数据
        logging.info(f"请求地址：{res.url}")
        logging.info(f"请求响应数据：{res.json()}")
        # 断言状态码
        utils.common_assert_code(res)
        # 断言token存在
        assert len(res.json().get("token")) > 0
        print(res.json())
        # 保存token
        app.headers["token"] = res.json().get("token")
        print(f"app.headers={app.headers}")

    def test_verify_token(self):
        res = ApiFactory.get_user_api().token_verify_api()
        # 打印 请求地址 请求参数 请求响应数据
        logging.info(f"请求地址：{res.url}")
        logging.info(f"请求响应数据：{res.json()}")
        # 断言状态码
        utils.common_assert_code(res)
        # 断言有效
        assert res.json().get("isValid")

    def test_user_addr(self):
        res = ApiFactory.get_user_api().user_addr_url()
        # 打印 请求地址 请求参数 请求响应数据
        logging.info(f"请求地址：{res.url}")
        logging.info(f"请求响应数据：{res.json()}")
        # 断言状态码
        utils.common_assert_code(res)
        assert False not in [i in res.text for i in ["大王", "13888888888", "上海市", "浦东新区", "111号"]]
