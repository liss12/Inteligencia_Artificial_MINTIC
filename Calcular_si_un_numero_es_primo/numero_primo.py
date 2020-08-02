# -*- coding: utf-8 -*-

def run():
  number = int(input('Digita un numero: '))
  result = isPrimeNumber(number)
  if result == True:
    print('El numero ES primo')
  else:
    print('El numero NO es primo')


def isPrimeNumber(number):
	if number < 2:
		return False
	elif number == 2:	
		return True
	elif number > 2 and number % 2 == 0:
		return False
	else:
		for i in range(3, number):
			if number % i == 0:
				return False
	return True

if __name__ == "__main__":
  run()
