import app
from Api.apiFactory import ApiFactory

# # 调用轮播图
# print(f"轮播图：{ApiFactory.get_home_api().banner_api().json()}")
# # 调用主题
# print(f"主题：{ApiFactory.get_home_api().theme_api().json()}")
# # 调用最近新品
# print(f"最近新品：{ApiFactory.get_home_api().recent_product_api().json()}")

# 商品分类
# print(f"分类：{ApiFactory.get_product_api().product_classify_api().json()}")
# # 商品下分类
# print(f"分类下商品：{ApiFactory.get_product_api().classify_product_api(5).json()}")
# # 商品信息
# print(f"商品信息：{ApiFactory.get_product_api().product_detail_api(26).json()}")

# 调用用户获取token
# res = ApiFactory.get_user_api().get_token_api()
# print(f"返回值:{res.json()}")
# print(res.json())
# # 保存token
# app.headers["token"] = res.json().get("token")
# print(app.headers)
# print(f"测试token：{ApiFactory.get_user_api().token_verify_api().json()}")
# print(f"用户地址信息:{ApiFactory.get_user_api().user_addr_url().json()}")

print(f"查看订单：{ApiFactory.get_order_api().order_list_api().json()}")
print(f"创建订单：{ApiFactory.get_order_api().create_order_api(12,7).json()}")
print(f"查看订单：{ApiFactory.get_order_api().query_order_api(111).json()}")
