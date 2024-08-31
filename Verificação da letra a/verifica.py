def count_letter_a(s):
    return s.lower().count('a')

def main():
    string = input("Digite uma plavra: ")
    count = count_letter_a(string)
    print(f"A letra 'a' ocorre {count} vezes na palavra.")

if __name__ == "__main__":
    main()
