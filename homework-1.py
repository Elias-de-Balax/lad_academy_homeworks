height = 1.8
love_number = 7
is_python = True

name = input("Как вас зовут? ")

try:
    if "" == name.strip():
        raise ValueError()

    age = int(input("Сколько вам лет? "))

    print(f"\nПривет, {name}! В следующем году вам будет {age + 1}.")
    print(f"\nКалькулятор лет в днях: {age * 365} дней.")

    print(f"\nФакты о себе:"
          f"\n\tВозраст: {age} лет"
          f"\n\tРост: {height} м"
          f"\n\tЛюбимое число: {love_number}"
          f"\n\tЛюблю Python: {is_python}")

    print(f"\nТипы данных:"
          f"\n\t {type(age)}"
          f"\n\t {type(height)}"
          f"\n\t {type(love_number)}"
          f"\n\t {type(is_python)}")
except ValueError:
    print("Вы ввели неверное значение.")
