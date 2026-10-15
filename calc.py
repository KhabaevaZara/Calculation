def calc():
    print("Простой калькулятор")
    print("Операции: +, -, *, /")
    
    try:
        a = float(input("Введите 1 число: "))
        op = input("Введите операцию (+, -, *, /): ").strip()
        b = float(input("Введите 2 число: "))
        
        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            if b == 0:
                print("Ошибка: деление на ноль!")
                return
            result = a / b
        else:
            print("Неизвестная операция")
            return
        
        print(f"Результат: {a} {op} {b} = {result}")
    
    except ValueError:
        print("Ошибка: введите корректное число!")


if __name__ == "__main__":
    calc()