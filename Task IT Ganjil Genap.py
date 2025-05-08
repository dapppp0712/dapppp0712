def even_odd_detector():
    try:
        number = int(input("Masukkan Angka: "))
        
        if number % 2 == 0:
            result = "Genap"
        else:
            result = "Ganjil"
        
        return f"Angka {number} Adalah Angka {result}."
    except ValueError:
        return "Error: Masukan Angka Yang Valid."

if __name__ == "__main__":
    print(even_odd_detector())