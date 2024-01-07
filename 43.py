def file_withsymb(f):
    con = read_file(f)
    summa = 0
    for i, strok in enumerate(con):
        if '!' in strok:
            summa += strok.count('!')
            print(i, strok)
    print(summa)


def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.readlines()
            return content
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


name = "data43.csv"
file_withsymb(name)
