# Модуль 6: Викторина "Знаменитые люди"
# Правильные ответы:
# А.С. Пушкин - 1799
# Л.Н. Толстой - 1828
# Ф.М. Достоевский - 1821
# М.В. Ломоносов - 1711
# Ю.А. Гагарин - 1934

def play_quiz():
    # Словарь с вопросами и правильными ответами
    famous_people = {
        "А.С. Пушкин": 1799,
        "Л.Н. Толстой": 1828,
        "Ф.М. Достоевский": 1821,
        "М.В. Ломоносов": 1711,
        "Ю.А. Гагарин": 1934
    }
    
    correct_answers = 0
    total_questions = len(famous_people)
    
    print("Викторина 'Знаменитые люди'")
    print("Ответьте на вопросы о годах рождения известных личностей:\n")
    
    # Задаем вопросы
    for person, correct_year in famous_people.items():
        user_answer = int(input(f"Введите год рождения {person}: "))
        
        if user_answer == correct_year:
            correct_answers += 1
            print("Правильно!\n")
        else:
            print(f"Неправильно. Правильный ответ: {correct_year}\n")
    
    # Вычисляем проценты
    wrong_answers = total_questions - correct_answers
    correct_percent = (correct_answers * 100) / total_questions
    wrong_percent = (wrong_answers * 100) / total_questions
    
    # Выводим результаты
    print("=" * 40)
    print("РЕЗУЛЬТАТЫ:")
    print(f"Правильных ответов: {correct_answers}")
    print(f"Ошибочных ответов: {wrong_answers}")
    print(f"Процент правильных ответов: {correct_percent:.1f}%")
    print(f"Процент неправильных ответов: {wrong_percent:.1f}%")
    print("=" * 40)
    
    # Спрашиваем о повторной игре
    play_again = input("\nХотите сыграть еще раз? (да/нет): ").lower()
    return play_again == 'да' or play_again == 'yes' or play_again == 'y'

# Основная программа
print("Добро пожаловать в викторину!")

while True:
    if not play_quiz():
        print("Спасибо за игру! До свидания!")
        break
    print("\n" + "=" * 40 + "\n")