def calculations(a, b, x, y, z, n):
    # Сумма двух чисел
    sum_result = a + b
    
    # Среднее арифметическое трёх чисел
    average_result = (x + y + z) / 3
    
    # Квадрат числа
    square_result = n ** 2
    
    # Возвращаем результаты в виде словаря
    return {
        "sum": sum_result,
        "average": average_result,
        "square": square_result
    }

# Вызов функции
results = calculations(10, 5, 4, 8, 12, 7)

# Формируем текст для файла
output_text = (
    f"Сумма двух чисел (10 + 5): {results['sum']}\n"
    f"Среднее арифметическое трёх чисел (4, 8, 12): {results['average']}\n"
    f"Квадрат числа 7: {results['square']}\n"
)

# Записываем результат в отдельный файл
with open("result.txt", "w", encoding="utf-8") as f:
    f.write(output_text)

print("Результаты сохранены в result.txt")
