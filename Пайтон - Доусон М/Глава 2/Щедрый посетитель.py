print("Эта программа расчитывает количество чаевых в зависимости от суммы!")
print("Выдаёт два результата - шедро отсыпая чаевых и тоже щедро, но поменьше!\n")
try:
    prise = int(input('Введите оплачивемый счёт: '))
except:
    print("Произошла ошибка попробуйте ещё раз")
else:
    print("\nЩедрые чаевые" )
    print('20%: ', prise + prise * 0.20)
    print("Поменьше")
    print("15%: ", prise + prise * 0.15)

if __name__ == "__main__":
    input("\n\nНажмите Enter чтобы выйти. ")
