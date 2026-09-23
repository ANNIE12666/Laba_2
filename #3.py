def check_leap_year():
    try:
        year = int(input("Введите год: "))
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"{year} год — ВИСОКОСНЫЙ.")
        else:
            print(f"{year} год — НЕ високосный.")
    except ValueError:
        print("Ошибка: введите целое число.")

if __name__ == "__main__":
    check_leap_year()

