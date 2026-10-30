def input_data(caption):
    try:
        return int(input(caption))
    except ValueError:
        print("Введено некорректное значение")
        return None

def output_data(caption, value):
    print(f"{caption}: {value}")