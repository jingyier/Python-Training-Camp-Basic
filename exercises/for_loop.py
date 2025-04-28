"""
练习: for循环

描述：
计算从1到n的所有整数之和。

请补全下面的函数，使用for循环计算从1到n的所有整数之和。
"""

def sum_numbers():
    """
    计算从1到n的所有整数之和
    
    参数:
    - n: 正整数
    
    返回:
    - 从1到n的所有整数之和
    """
    # 请在下方编写代码
pass


def sum_numbers(n):
    """ 计算1到n的整数和

    Args:
        n: 非负整数

    Returns:
        int: 累加结果

    Raises:
        TypeError: 输入非整数时抛出
        ValueError: 输入负数时抛出
    """
    # 输入校验
    if not isinstance(n, int):
        raise TypeError("输入必须是整数")
    if n < 0:
        raise ValueError("输入必须是非负整数")

    total = 0
    for i in range(1, n + 1):
        total += i
    return total