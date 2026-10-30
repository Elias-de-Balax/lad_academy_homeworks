def str_to_int(value):
    try:
        return int(value)
    except ValueError:
        print("Значение не является числом")
        return 0

def is_parity(value) -> bool:
    try:
        return bool(int(value) % 2 == 0)
    except ValueError:
        print("Значение не является числом")
        return False

