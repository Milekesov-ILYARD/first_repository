name = input('Привет. Как тебя зовут? ')
age = 0
weight = 0
counter = 0
try:
    age = int(input("Сколько тебе лет? "))
    weight = int(input("Хорошо, и последний вопрос. Сколько в тебе киллограмм? "))
except:
    print('Данные введены не корректно, попробуйте ещё раз')
else:
    counter = 1

print("\nЕсл бы поэт Каммингс адресовал тебе письмо он сделал бы это так: ", name.lower())
print("А если это был рехнувшийся Каммингс, то так: ", name.upper())

called = name * 6
print('\nЕсли бы ребёнок решил привлеч твоё внимание: ')
print("Он произнёс бы твоё имя так: ")
print(called)

seconds = age * 365 * 24 * 60 * 60
print('\nТвой нынешний возраст свыше:', seconds, "секунд. ")

moon_weight = weight / 6
sun_weight = weight * 27.1
print('\nЗнаете ли вы, что на Луне вы весили бы всего', moon_weight, "кг?")
print('А вот находясь на Солнце вы бы весели', sun_weight, "кг. (Но, увы, это продолжилось бы недолго...)")
if __name__ == "__main__":
    input("\n\nНажмите Enter чтобы выйти. ")