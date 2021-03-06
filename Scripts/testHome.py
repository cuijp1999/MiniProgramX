import logging
import utils
from Api.apiFactory import ApiFactory


class TestHomeApi:

    def test_home_api(self):
        """轮播图"""
        # 请求返回数据
        res = ApiFactory.get_home_api().banner_api()
        # 打印 请求地址 请求参数 请求响应数据
        logging.info(f"请求地址：{res.url}")
        logging.info(f"请求响应数据：{res.json()}")
        # 断言状态码
        utils.common_assert_code(res)
        # 断言id和name
        assert res.json().get("id") == 1 and res.json().get("name") == '首页置顶'
        # 断言items列表长度大于0
        assert len(res.json().get("items")) > 0

    def test_theme_api(self):
        """专题栏"""
        res = ApiFactory.get_home_api().theme_api()
        # 打印 请求地址 请求参数 请求响应数据
        logging.info(f"请求地址：{res.url}")
        logging.info(f"请求响应数据：{res.json()}")
        # 断言状态码
        utils.common_assert_code(res)
        # 断言3个id
        assert 'id":1' in res.text and 'id":2' in res.text and 'id":3' in res.text
        # 断言关键字段
        assert False not in [i in res.text for i in ["name", "description", "topic_img", "head_img"]]

    def test_recent_product_api(self):
        """最近新品"""
        res = ApiFactory.get_home_api().recent_product_api()
        # 打印 请求地址 请求参数 请求响应数据
        logging.info(f"请求地址：{res.url}")
        logging.info(f"请求响应数据：{res.json()}")
        # 断言状态码
        utils.common_assert_code(res)
        # 断言新品数量
        assert len(res.json()) > 0
        # 断言关键字段
        assert 'id' in res.text and 'name' in res.text and 'price' in res.text
