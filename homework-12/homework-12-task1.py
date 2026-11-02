"""
Защищённый калькулятор. Напишите программу, которая запрашивает два числа и выводит их сумму, разность, произведение и
частное. Оберните вычисления в try/except так, чтобы: при делении на ноль (ZeroDivisionError) программа не «падала», а
выводила «Деление на ноль невозможно»; при невалидном вводе (ValueError) — просила ввести число заново. Используйте else
для вывода результата и finally для сообщения «Вычисления завершены».
"""

while True:
    try:
        a, b = int(input("Введите первое число: ")), int(input("Введите второе число: "))

        res_sum = a + b
        res_diff = a - b
        res_mult = a * b
        res_div = a / b
    except ValueError:
        print("Неверно задано число.")
        continue
    except ZeroDivisionError:
        print("Деление на ноль невозможно.")
        continue
    else:
        print(f"Сумма: {res_sum}\nРазность: {res_diff}\nПроизведение: {res_mult}\nЧастное: {res_div}")
        break
    finally:
        print("Вычисления завершены.\n")


