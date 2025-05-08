def calculator():
    num1 = float(input("Masukkan Angka Pertama: "))
    num2 = float(input("Masukkan Angka Kedua: "))
    operator = input("Masukkan Tanda (+, -, *, /): ")
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Pembagian Dengan 0"
        result = num1 / num2
    else:
        return "Error: Tanda Tidak Valid"
    
    return f"Hasil: {result}"

if __name__ == "__main__":
    print(calculator())