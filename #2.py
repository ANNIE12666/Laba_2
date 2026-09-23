def distance_converter():
    to_meters = {"км": 1000.0, "м": 1.0, "см": 0.01, "мм": 0.001, "mi": 1609.344, "yd": 0.9144}
    source = input("Исходная единица (км, м, см, мм, mi, yd): ").strip().lower()
    target = input("Целевая единица (км, м, см, мм, mi, yd): ").strip().lower()
    if source not in to_meters or target not in to_meters:
        print("Ошибка: Неподдерживаемая единица.")
        return
    try:
        value = float(input(f"Введите значение в {source}: "))
        result = value * to_meters[source] / to_meters[target]
        print(f"Результат: {value} {source} = {result:.4f} {target}")
    except ValueError:
        print("Ошибка: Некорректный ввод.")

if __name__ == "__main__":
    distance_converter()
