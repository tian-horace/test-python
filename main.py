def generate_2d_array():
    return [[i + j for j in range(1, 6)] for i in range(1, 11)]


# 测试函数
def test_generate_2d_array():
    array = generate_2d_array()
    for row in array:
        print(row)


# 调用测试函数
test_generate_2d_array()
