def common_assert_code(res, code=200):
    """通用断言"""
    assert res.status_code == code
