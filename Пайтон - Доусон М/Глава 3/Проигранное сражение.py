print("Вашего героя окружила несметная армия троллей.")
print("Смрадными зелёными трупами врагов устланны все ближайшие окрестности")
print("Одинокий герой достаёт меч из ножен, готовясь к последней битве!\n")
heals = 10
trolls = 0
damage = 3
while heals > 0:
    trolls += 1
    heals -= damage
    print('Взмахнув мечём, ваш герой истребляет злобного тролля.',\
          "но сам получает повреждений на", damage, 'очков\n')
print(f"Ваш герой доблестно сражался и убил {trolls} троллей")
print("Но увы! Он пал на поле боя.")
if __name__ == "__main__":
    input("\n\nНажмите Enter чтобы выйти. ")