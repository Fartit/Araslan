

month = ["Январе", "Феврале", "Марте"]
total_sales = [52000.00, 51000.00, 48000.00]
prod_cost = [46800.00, 45900.00, 43200.00]

for m, s, c in zip(month, total_sales, prod_cost):
    profit = s - c
    print("Чистая прибыль в", m, "=", profit, "Топкоинов")
