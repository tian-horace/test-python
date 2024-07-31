def generate_2d_array():
    return [[i + j for j in range(1, 6)] for i in range(1, 11)]


# 测试函数
def test_generate_2d_array:
    array = generate_2d_array()
    # 遍历array中的每一行
    for row in array:
        # 使用字符串的join()方法和列表推导式，生成格式化的字符串
        formatted_row = ' '.join(['{:<5}'.format(item) for item in row])
        print(formatted_row)


# 调用测试函数
test_generate_2d_array()
