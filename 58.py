
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        raise NameError("404. File (filename) not found")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


try:
    file_name = "ex.txt"
    read_file(file_name)
except NameError as e:
    print(e)