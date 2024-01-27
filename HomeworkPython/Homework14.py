
num_students = int(input("Введите количество студентов: "))


names = []
scores = []


for i in range(num_students):
    name = input(f"{i+1}-й студент: Введите имя и фамилию: ")
    score = int(input("Балл: "))
    names.append(name)
    scores.append(score)


average_score = sum(scores) / num_students


print("Средний балл:", average_score)


print("Студенты с баллом выше среднего:")
for i in range(num_students):
    if scores[i] > average_score:
        print(names[i])
