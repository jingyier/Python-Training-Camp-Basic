"""
练习: 字典操作

描述：
实现对学生成绩字典的添加、删除、修改和查询操作。

请补全下面的函数，对学生成绩字典进行各种操作。
"""

def student_dict_operations(students_dict, operation, *args):
    """
    对学生字典进行操作
    
    参数:
    - students_dict: 学生字典 {姓名: 成绩}
    - operation: 操作类型 ("add", "remove", "update", "get")
    - args: 操作所需的额外参数
    
    返回:
    - 根据操作返回不同结果
    """
    # 请在下方编写代码
    pass
def student_dict_operations(students_dict, operation, *args):
    if operation not in ('add', 'remove', 'update', 'get'):
        raise ValueError(f"Invalid operation: {operation}")

    if operation == 'add':
        if len(args) != 2:
            raise ValueError("Add operation requires two arguments: name and score")
        name, score = args
        if name in students_dict:
            raise KeyError(f"Student {name} already exists")
        students_dict[name] = score
        return students_dict
    elif operation == 'remove':
        if len(args) != 1:
            raise ValueError("Remove operation requires one argument: name")
        name = args[0]
        if name not in students_dict:
            raise KeyError(f"Student {name} does not exist")
        del students_dict[name]
        return students_dict
    elif operation == 'update':
        if len(args) != 2:
            raise ValueError("Update operation requires two arguments: name and new score")
        name, new_score = args
        if name not in students_dict:
            raise KeyError(f"Student {name} does not exist")
        students_dict[name] = new_score
        return students_dict
    elif operation == 'get':
        if len(args) != 1:
            raise ValueError("Get operation requires one argument: name")
        name = args[0]
        return students_dict.get(name)