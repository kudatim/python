
import os
import psutil
import sys
print ('Первая ПРОГРАММА')
print ('Привет, программист Python!')
name = input ('Ваше имя: ')
print ("Привет,", name)
work = ''
while work != 'q':
	work = input ("Давай поработаем? (Y/N/q)")
	if work == 'Y':
		#pass
		print ("круто, я соскучился по работе")
		print ("Я могу вывести на экран следующее:")
		print (" [1] - список файлов в текущей папке")
		print (" [2] - информацию о системе")
		print (" [3] - список процессов")
		do = int(input ("Укажите вариант действия: "))
		
		if do == 1:
			print (os.listdir ())
		elif do == 2:
			print ("Количество процессоров: ", psutil.cpu_count())
			print ("Платформа: ", sys.platform)
			print ("Кодировка файловой системы: ", sys.getfilesystemencoding)
			print ("Текущая директория: ", os.getcwd())
			print ("Текущий пользователь: ", os.getlogin())
		elif do == 3:
			print (psutil.pids())
		else:
			pass
	elif work =='N':
		print ("Пока!")
	else:
		#print ("Нажмите Y или N")
		pass
number = str(input('Введите целое число от 0 до 100: '))
print (number)