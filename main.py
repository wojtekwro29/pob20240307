import calculator
def calculate(a, b, operation):
    match operation:
        case 1:
            return calculator.add(a,b)
        case 2:
            return calculator.substract(a,b)
        case 3:
            return calculator.multiply(a,b)
        case 4:
            if b==0:
                return "Nie można dzielic przez 0"
            else:
                return calculator.divide(a,b)



if __name__ == '__main__':
    while(True):
        operation = int(input("Wybór opcji:\n1.dodawanie\n2.odejmowanie\n3.mnożenie\n4.dzielenie\n5.wyjscie\n"))
        if operation not in range(1,6):
            print("Zły wybór")
        elif operation==5:
            print("Wychodzenie...")
            exit(0)
        else:
            a = float(input("Podaj a:"))
            b = float(input("Podaj b:"))
            print(calculate(a, b, operation))