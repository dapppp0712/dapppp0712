def file_writer_reader():
    user_input = input("Masukkan Teks Untuk Disimpan: ")
    
    filename = "user_input.txt"
    try:
        with open(filename, 'w') as file:
            file.write(user_input)
        print(f"Berhasil Save ke {filename}")
        
        with open(filename, 'r') as file:
            content = file.read()
        
        print("Isi file:")
        print(content)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    file_writer_reader()