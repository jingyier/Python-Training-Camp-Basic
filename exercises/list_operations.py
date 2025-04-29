"""
练习: 列表操作

描述：
实现对学生列表的添加、删除和修改操作。

请补全下面的函数，对学生列表进行各种操作。
"""

def student_list_operations(students, operation, *args):
    """
    对学生列表进行操作
    
    参数:
    - students: 学生列表
    - operation: 操作类型 ("add", "remove", "update")
    - args: 操作所需的额外参数
    
    返回:
    - 操作后的学生列表
    """
    # 请在下方编写代码
    pass


def student_list_operations(students, operation, *args):
    # 创建列表的副本以避免修改原列表
    modified_list = list(students)

    if operation == "add":
        # 添加学生（支持多参数添加）
        for name in args:
            modified_list.append(name)

    elif operation == "remove":
        # 删除学生（通过姓名删除，若存在）
        for name in args:
            if name in modified_list:
                modified_list.remove(name)

    elif operation == "update":
        # 更新学生信息（参数格式：旧名字，新名字）
        if len(args) != 2:
            raise ValueError("Update operation requires exactly 2 arguments: old_name and new_name")
        old_name, new_name = args
        if old_name in modified_list:
            index = modified_list.index(old_name)
            modified_list[index] = new_name

    else:
        raise ValueError("Invalid operation type. Supported: 'add', 'remove', 'update'")

    return modified_list