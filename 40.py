def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Пример использования:
file_name = "example.txt"
read_file(file_name)