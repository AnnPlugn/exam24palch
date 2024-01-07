import inspect


def func(subfunc):
    signature = inspect.signature(subfunc)
    params_info = []
    for param in signature.parameters.values():
        if param.default is param.empty:
            default_info = "позиционный"
        else:
            default_info = "ключевой"
        param_type = param.annotation if param.annotation != inspect.Parameter.empty else "не указан"
        params_info.append((param.name, default_info, param_type))

    print(f"Имя функции: {subfunc.__name__}")
    for param_info in params_info:
        print(f"Параметр {param_info[0]}: {param_info[1]}, {param_info[2]}")


# Пример использования
def subfunc(a: int, b: float):
    pass


func(subfunc)