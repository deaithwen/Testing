print("Калькулятор версии: 0.4. Автор: Sultan")
print("Просмотреть историю обновлений - введи 'история'")
print("Список математических действий - введи 'действия' ")
print("P.S. Значения вводить только цифрами, максимум 3 действия, т.е. 4 числа!")

def convert():
	what1 = str.lower(input("Количество чисел, история, действия: "))
#2 числа
	if what1 == "действия":
		print("+, -, *, /, ** (степень)")

	elif what1 == "действие":
		print("+, -, *, /, ** (степень)")

	elif what1 == "история":
		print("v. 0.1: плюс и минус.")
		print("v. 0.2: деление и умножение.")
		print("v. 0.3: добавлена история версий и повторное использование калькулятора.")
		print("v. 0.4: добавлено введение в степень, исправлено деление на 0, немного изменен функционал.")

	elif what1 == "2":
		whaat1 = input("Что делаем ? ")
		a = int(input("Введи первое число: "))
		b = int(input("Введи второе число: "))
		if whaat1 == "+":
			z = a + b
			print("Результат:" + str(z))
		elif whaat1 == "-":
			z = a - b
			print("Результат:" + str(z))
		elif whaat1 == "*":
			z = a * b
			print("Результат:" + str(z))
		elif whaat1 == "/":
			if b == 0:
				while b == 0:
					b = int(input("На ноль делить нельзя, введи другое число: "))
					if b != 0:
						z = a / b   
			else:
				z=a/b
			print("Результат:" + str(z))


		elif whaat1 == "**":
			z = a ** b
			print("Результат:" + str(z))
		else:
			print("Выбрана неверная операция.")

#3 числа
	elif what1 == "3":
		whatact1 = input("Первое действие ? ")
		a2 = float(input("Введи первое число: "))
		b2 = float(input("Введи второе число: "))
	
		if whatact1 == "+":
			x = a2 + b2
		elif whatact1 == "-":
			x = a2 - b2
		elif whatact1 == "*":
			x = a2 * b2
		elif whatact1 == "/":
			if b2 == 0:
				while b2 == 0:
					b2 = int(input("На ноль делить нельзя, введи другое число: "))
					if b2 != 0:
						x = a2 / b2  
			else:
				x=a2/b2
		elif whatact1 == "**":
			x = a2 ** b2
		else:
			print("Выбрана неверная операция.")
		print("Результат первого действия:" + str(x))

		whatact2 = input("Второе действие ? ")
		c2 = float(input("Введи третье число: "))
		if whatact2 == "+":
			z = x + c2
		elif whatact2 == "-":
			z = x - c2
		elif whatact2 == "*":
			z = x * c2
		elif whatact2 == "/":
			if c2 == 0:
				while c2 == 0:
					c2 = int(input("На ноль делить нельзя, введи другое число: "))
					if c2 != 0:
						z = x / c2
			else:
				z=x/c2
		elif whatact2 == "**":
			z = x ** c2
		else:
			print("Выбрана неверная операция.")
		print("Результат:" + str(z))

#4 числа
	elif what1 == "4":
		whatactt1 = input("Первое действие ? ")
		a3 = float(input("Введи первое число: "))
		b3 = float(input("Введи второе число: "))
	
		if whatactt1 == "+":
			x1 = a3 + b3
		elif whatactt1 == "-":
			x1 = a3 - b3
		elif whatactt1 == "*":
			x1 = a3 * b3
		elif whatactt1 == "/":
			if b3 == 0:
				while b3 == 0:
					b3 = int(input("На ноль делить нельзя, введи другое число: "))
					if b3 != 0:
						x1 = a3 / b3
			else:
				x1=a3/b3
		elif whatactt1 == "**":
			x1 = a3 ** b3
		else:
			print("Выбрана неверная операция.")
		print("Результат первого действия:" + str(x1))

		whatactt2 = input("Второе действие ? ")
		c3 = float(input("Введи третье число: "))
		if whatactt2 == "+":
			x2 = x1 + c3
		elif whatactt2 == "-":
			x2 = x1 - c3
		elif whatactt2 == "*":
			x2 = x1 * c3
		elif whatactt2 == "/":
			if c3 == 0:
				while c3 == 0:
					c3 = int(input("На ноль делить нельзя, введи другое число: "))
					if c3 != 0:
						x2 = x1 / c3
			else:
				x2=x1/c3
		elif whatactt2 == "**":
			x2 = x1 ** c3
		else:
			print("Выбрана неверная операция.")
		print("Результат второго действия:" + str(x2))

		whatactt3 = input("Третье действие ? ")
		d3 = float(input("Введи четвёртое число: "))
		if whatactt3 == "+":
			z = x2 + d3
		elif whatactt3 == "-":
			z = x2 - d3
		elif whatactt3 == "*":
			z = x2 * d3
		elif whatactt3 == "/":
			if d3 == 0:
				while d3 == 0:
					d3 = int(input("На ноль делить нельзя, введи другое число: "))
					if d3 != 0:
						z = x2 / d3
			else:
				z=x2/d3
		elif whatactt3 == "**":
			z = x2 ** d3
		else:
			print("Выбрана неверная операция.")
		print("Результат:" + str(z))
#Конец 4 действия

	else:
		print("Введено неверное количество.")
convert()
while True:
    flag = str.lower(input("Продолжить ? [да/нет]: "))
    if flag == 'да':
        convert()
    elif flag == "нет":
    	break
    else:
        break
