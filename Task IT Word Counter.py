def count_words():
    paragraph = input("Masukkan sebuah paragraf: ")
    
    words = paragraph.split()
    word_count = len(words)
    
    return f"Paragraf Itu Memiliki {word_count} Kata."

if __name__ == "__main__":
    print(count_words())