def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            return content

    except FileNotFoundError:
        print("Файлът не съществува.")
        raise

    except PermissionError:
        print("Нямате права за достъп до файла.")
        raise

    except OSError as error:
        print("Грешка при работа с файла:", error)
        raise