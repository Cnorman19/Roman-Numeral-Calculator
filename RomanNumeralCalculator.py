import sys

x = sys.argv[1]
x = int(x)

RomanNumeral = []
	
def getRomanNumeral(x):

	if x <= 0 and not RomanNumeral or  x > 3999:

		print("This number can not be converted to a RomanNumeral!")

	elif x >= 1000:

		x -= 1000 

		RomanNumeral.append('M')

		getRomanNumeral(x)

	elif x >= 900:

		x -= 900

		RomanNumeral.append('CM')

		getRomanNumeral(x)

	elif x >= 500:

		x -= 500 

		RomanNumeral.append('D')

		getRomanNumeral(x)

	elif x >= 400:

		x -= 400

		RomanNumeral.append('CD')

		getRomanNumeral(x)

	elif x >= 100:

		x -= 100 

		RomanNumeral.append('C')

		getRomanNumeral(x)

	elif x >= 90:

		x -= 90

		RomanNumeral.append('XC')

		getRomanNumeral(x)

	elif x >= 50:

		x -= 50 

		RomanNumeral.append('L')

		getRomanNumeral(x)

	elif x >= 40:

		x -= 40

		RomanNumeral.append('XL')

		getRomanNumeral(x)

	elif x >= 10:

		x -=  10 

		RomanNumeral.append('X')

		getRomanNumeral(x)

	elif x >= 9:

		x-= 9

		RomanNumeral.append('IX')

		getRomanNumeral(x)

	elif x >= 5:

		x -= 5 

		RomanNumeral.append('V')

		getRomanNumeral(x)

		

	elif x >= 1:

		x -= 1

		RomanNumeral.append('I')

		getRomanNumeral(x)


	elif x == 0:

		print("Equivalent Roman Numeral: ", end = "")

		for i in RomanNumeral:

			print(i , end = "")


getRomanNumeral(x)

