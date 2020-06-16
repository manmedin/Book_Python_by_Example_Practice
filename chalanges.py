
########IF STATEMENT#####

######challenges 015#######
# fav_col = input('Enter your favourite color: ')
# if fav_col.lower() == 'red':
# 	print('I lke red too')
# else :
# 	print("I don't like " + fav_col +', I prefer red' )

###example how to print multiply lines whithout use \n ##########
# mensaje = '''este es un 
# mensaje de varias lineas
# que sera tomado como ejemplo'''
# print (mensaje)

#########challenges 026########
#si tengo 'pen' sera'enpay' si tengo 'ana' sera 'anaway'
# base_word = ('OTHER')
# fir_let = base_word[0].lower() #get the first letter's word

# if fir_let=='a' or fir_let=='e' or fir_let=='i' or fir_let=='o' or fir_let=='u':
# 	print(base_word.lower() + 'way' ) 
# else :
# 	fir_let_v1 = base_word[0]
# 	word_v1 = base_word.strip(fir_let_v1).lower()
# 	print(word_v1 + fir_let + 'ay')

######practice math######
#import math
# print (round(3.578,2))
# print (math.sqrt(225))
# print (math.pi)
# print (7//2)
# print (7%2)
# print (int(7/2))

########challenges 027,028######
# number = float(input('Enter a number with many decimal digits: '))
# print (round(2*number,2))

########challenges 029######
# number = float(input('Enter a number greater than 500: '))
# if number < 500 :
# 	print ('You must enter a number greater than 500!!, please try again')
# else :
# 	print ('Square root of ' + str(number) + ' is '+ str(round(math.sqrt(number),2)))

########challenges 031######
# import math
# r = 4.
# cir_are = round(math.pi*r**2,3)
# print (cir_are)

########challenges 033######
# n1 = int(input('Enter the first number to divide: '))
# n2 = int(input('Enter the second number to divide: '))
# D = int(n1/n2)
# R = n1%n2
# print(str(n1) + ' divided by ' + str(n2) + ' is ' + str(D) + ' with ' + str(R) + ' remaining.' )

#######challenges 034 ########
# while True:
# 	print('\n-----------------AREA CALCULATION---------------')
# 	print('\t1) Square')
# 	print('\t2) Triangle')
# 	print('------------------------------------------------')
# 	select = int(input('Type 1 or 2 to choose the area to calculate: '))

# 	if select == 1:
# 		side = int(input('\tType the side of the square: '))
# 		areasq = side*side
# 		print ('\tTotal square area is: ' + str(areasq))
# 	elif select == 2: 
# 		base = int(input('\tType the base of the triangule: '))
# 		height = int(input('\tType the height of the triangule: '))
# 		areatr = base*height/2
# 		print ('\tTotal triangule area is: ' + str(areatr))
# 	else :
# 		print('ERROR: You enter an invalid option, please try again')

# 	salir = input('Do you want to calcuate other area again ? if so enter "y": ' )
# 	if salir != 'y':
# 		break

#######challenges 037,038########
# name = 'manuel'
# times = 4
# for t in range(0,times):
# 	for i in name:
# 		print (i)


#########challenges 039##########
# print('XXXXXXXXXX MULTIPLY TABLE XXXXXXXXXX')
# table = int(input('Type the table value that you want to see: '))

# for x in range(1,13):
# 	print(str(x) + ' x ' + str(table) + ' = ' + str(x*table))

#########challenges 040##########
# limit = 40
# limit2 = limit - 1
# for i in range(50,limit2,-1):
# 	print(i)

#########challenges 042##########
# total = 0
# for i in range(0,5):
# 	add = int(input('Type a number: '))
# 	ask = input('Do you want to add the previous number to the total (y/n)? : ')
# 	if ask == 'y':
# 		total = total + add
# print('\nThe suma of the total numbers previously entered is equal to: ' + str(total))

######## challenges 043##########
# direction = input('Which direction up/down (u/d) do you want to count: ')
# if direction != 'up' and direction != 'down' and direction != 'u' and direction != 'd':
# 	print ('You type a wrong value!')
# elif direction == 'up' or direction == 'u':
# 	top = int(input('\nType the top number to count: '))
# 	for i in range (1,top+1):
# 		print (i)
# elif direction == 'down' or direction == 'd':
# 	bottom = int(input('\nType the bottom number to count: '))
# 	for i in range (20,bottom-1,-1):
# 		print (i)

######## challenges 046##########
# value = 0
# while value <= 5:
# 	value = int(input('Enter a value: '))
# print ('lat value entered was: ' + str(value))

######## challenges 047##########
# n1 = input('Enter the first number to add: ')
# n2 = input('Enter the second number to add: ')
# ntotal = str(n1) + str(n2)
# more = 'y'
# while more == 'y':
# 	more = input('Do you want to add more numbers ? ("y/n"): ')
# 	if more == 'y':
# 		nx = input('Enter the number to add: ')
# 		ntotal = ntotal + nx
# 	else:
# 		more = 'n'	
# print(ntotal)

######## challenges 048 #########
# guest = input('What is your name; ')
# print(guest.title() + ' you has been invited')
# guests = 1
# more = 'y'
# while more == 'y':
# 	moreguest = input('Do you wnat to invite someone else? ("y/n")')
# 	if moreguest == 'y':
# 		guests = guests + 1
# 	else:
# 		more = 'n'
# print ('Are coming ' +guest.title() + ' with '+str(guests-1) + ' friends to your party')

######## challenges 049 #########
# compnum = 50
# attempt = 0
# num = int(input('Try to guest the hide number: '))
# while num != compnum:
# 	if num > compnum:
# 		num = int(input('too high...try again: '))
# 		attempt += 1
# 	elif num < compnum:
# 		num = int(input('too low...try again: '))
# 		attempt += 1
# attempt +=1
# print ('\nWell done, you took ' + str(attempt) + ' attempts')

######## challenges 051 #########
# mes1 = 'There are '
# mes2 = ' green bottles hanging on the wall, '
# mes3 = ' and if 1 green bottle should accidentally fall.'
# ans = 0

# for b in range (10,0,-1):
# 	print('\n')
# 	print(mes1 + str(b) + mes2 + mes3)
# 	ans = int(input('How many green bottles will be hanging on the wall?: '))
# 	while ans != b-1:
# 		ans = int(input('No, try again: '))
# 	print('There will be '+ str(b-1) + ' green bottles hanging on the wall')
# print ('\nThere are no more green bottles hanging on the wall!!!')


######Practice Random chapter#######
# import random
# num = random.random()
# print (num)
# num1 = random.randint(0,10) # generate a random number between 0 and even 10
# print (num1)
# num2 = random.randrange(0,11,2)
# print (num2)
# rancolor = random.choice(['red','blue','yellow'])
# print(rancolor)

######## challenges 054 #########
# import random
# machine = random.choice(['h','t'])
# guess = input('Choice "h/t": ')
# if guess == machine:
# 	print('You Win!! :-)')
# else :
# 	print('Bad Luck :-(')
# if machine == 'h':
# 	print('Computre has chosen Heads')
# else:
# 	print('Computer has chosen Tails')


######## challenges 055 #########
# import random
# mach = random.randint(1,5)
# print ('machine choose ' + str(mach))
# #for i in range(1,3):
# user = int(input('Enter a number between 1 to 5: '))
# if user == mach:
# 	print ('Well Done!!')
# elif user > mach:
# 	user2 = int(input('You are too high... try again: '))
# 	if user2 == mach:
# 		print('Correct!!')
# 	else:
# 	 	print('You lose :-(')
# else:
# 	user2 = int(input('You are too low... try again: '))
# 	if user2 == mach:
# 		print ('Correct!!')
# 	else:
# 	 	print('You lose :-(')

######## challenges 056, 057 #########
# import random
# ranum = random.randint(1,10)
# # print ('number of machine is: '+ str(ranum))
# cont = 'no'
# while cont == 'no':
# 	guess = int(input('Try to gueest the number between 1 to 10: '))
# 	if guess == ranum:
# 		cont = 'yes'
# 	elif guess > ranum:
# 		print ('too high')
# 	else:
# 		print('too low')

######## challenges 058 #########
# import random
# points = 0
# for i in range(1,6):
# 	num1 = random.randint(1,10)
# 	num2 = random.randint(1,10)
# 	if i == 1:
# 		oper_quiz1 =  num1 + num2
# 		oper1 = int(input(str(num1) + ' + ' + str(num2) + ' = ' ))
# 		if oper1 == oper_quiz1:
# 			points += 1
# 	elif i ==2:
# 		oper_quiz2 = num1*num2
# 		oper2 = int(input(str(num1) + ' * ' + str(num2) + ' = '))
# 		if oper2 == oper_quiz2:
# 			points += 1
# 	elif i ==3:
# 		oper_quiz3 = num1**num2
# 		oper3 = int(input(str(num1) + ' ** ' + str(num2) + ' = '))
# 		if oper3 == oper_quiz3:
# 			points += 1
# 	elif i ==4:
# 		oper_quiz4 = int(num1/num2)
# 		oper4 = int(input(str(num1) + ' / ' + str(num2) + ' = '))
# 		if oper4 == oper_quiz4:
# 			points += 1
# 	else :
# 		oper_quiz5 = num1%num2
# 		oper5 = int(input(str(num1) + ' % ' + str(num2) + ' = '))
# 		if oper5 == oper_quiz5:
# 			points += 1
# print ('You got answered '+ str(points) + ' correctly from 5 questions')

######## challenges 059 #########
# import random
# color = random.choice(['rojo','verde','azul',])
# eleccion = input('Escoje un color "rojo/verde/azul": ')
# acertaste = 'no'
# while acertaste == 'no':
# 	if color != eleccion:
# 		if color == 'rojo':
# 			eleccion = input('"El ROJO carmesi," decia una poema: ')
# 		elif color == 'verde':
# 			eleccion = input('Ese viejo VERDE no deja de mirarla: ')
# 		elif color == 'azul':
# 			eleccion = input('La ballena AZUL era enorme: ')
# 	else :
# 		acertaste = 'si'
# print('Bien Hecho!!')


#########Practice turtle############
# import turtle
# turtle.shape("turtle")
# for i in range (0,5):
# 	turtle.right(-72)
# 	turtle.forward(100)	
# turtle.exitonclick()

# import turtle
# for i in range (0,10):
# 	turtle.right(36)
# 	for i in range(0,5):
# 		turtle.forward(100)
# 		turtle.right(72)
# turtle.exitonclick()

# import turtle
# scr = turtle.Screen()
# scr.bgcolor('purple') #set background color of the screen
# turtle.color('yellow','red') #set color for line and for filling
# turtle.shape('turtle') 
# #turtle.hideturtle()
# turtle.begin_fill()  #---> start for filling final shape
# for i in range (0,6):
# 	turtle.pensize(1)
# 	turtle.right(60)
# 	turtle.pendown()
# 	turtle.forward(70)
# 	turtle.penup()
# 	turtle.forward(50)
# for i in range (0,6):
# 	turtle.pensize(1)
# 	turtle.left(60)
# 	turtle.pendown()
# 	turtle.forward(70)
# 	turtle.penup()
# 	turtle.forward(50)
# turtle.end_fill()    # ----> end for filling final shape
# scr.exitonclick()

######## challenges 060 #########
# import turtle
# for i in range(0,4):
# 	turtle.forward(200)
# 	turtle.right(90)
# turtle.exitonclick()

######## challenges 061 #########
# import turtle
# for i in range(0,3):
# 	turtle.forward(200)
# 	turtle.left(120)
# turtle.exitonclick()

######## challenges 062 #########
# import turtle
# for i in range(0,360):
# 	turtle.forward(3)
# 	turtle.left(1)
# turtle.exitonclick()

######## challenges 063 #########
# import turtle
# colors = ['red','yellow','purple']
# turtle.penup()
# for c in colors:
# 	turtle.color('black',c)
# 	turtle.begin_fill()
# 	for i in range (0,4):
# 		turtle.forward(30)
# 		turtle.right(90)
# 	turtle.end_fill()
# 	#turtle.penup()
# 	turtle.forward(50)

# turtle.exitonclick()

######## challenges 064 #########
# import turtle
# for i in range (0,5):
# 	turtle.forward(100)
# 	turtle.right(144)
# turtle.exitonclick()

######## challenges 065 #########
# import turtle
# #doing 1
# turtle.left(90)
# turtle.forward(100)
# #space
# turtle.penup()
# turtle.right(90)
# turtle.forward(40)
# turtle.pendown()
# #doing 2
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(50)
# turtle.right(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(100)
# #space
# turtle.penup()
# turtle.forward(40)
# turtle.pendown()
# #doing 3
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.penup()
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(40)
# turtle.pendown()
# turtle.forward(60)

# turtle.hideturtle()
# turtle.exitonclick()

######## challenges 066 #########
# import turtle
# import random
# for i in range(0,8):
# 	color = random.choice(['yellow','red','green','blue','pink','brown','purple'])
# 	turtle.color(color)
# 	turtle.right(45)
# 	turtle.forward(100)
# turtle.hideturtle()
# turtle.exitonclick()

######## challenges 067 #########
# import turtle
# for i in range (0,10):
# 	for i in range(0,8):
# 		turtle.forward(100)
# 		turtle.right(45)
# 	turtle.right(36)
# turtle.exitonclick()

######## challenges 068 #########
# import turtle
# import random
# lines = random.randint(10,15)
# angle = random.randint(40,120)
# lenght = random.randint(40,100)
# for i in range(0,lines):
# 	turtle.forward(lenght)
# 	turtle.right(angle)
# turtle.exitonclick()


#########practice reading and writing to a file########
# file = open('countries.txt','w')
# file.write('Italy\n')
# file.write('Germany\n')
# file.write('Spain\n')
# file.close()

# file = open('msisdn.txt','w')
# for i in range (5400000,5400020):
# 	file.write(str(i) + '\n')
# file.close()

# file = open('countries.txt','r')
# print (file.read())

# file = open('countries.txt','a')
# file.write('Peru')
# file.close()

##############challenges 106,107###########
# names = open('names.txt','w')
# names.write('Alvaro\n')
# names.write('Leandro\n')
# names.write('Nidia\n')
# names.write('Manuel\n')
# names.close()
# names = open('names.txt','r')
# print(names.read())

##############challenges 108##############
# names = open('names.txt','a')
# names.write('Kalebh\n')
# names.write('Sahir')
# names.close()
# names = open('names.txt','r')
# print(names.read())

##############challenges 109##############
# selection = int(input('1) Create a new file\n' 
# 	     '2) Display the file\n'
# 	     '3) Add a new item to the file\n'
# 	     'Make a selection 1, 2 or 3: '))

# while selection == 0 or selection >3:
# 	again = int(input("You didn't select 1, 2 or 3: "))
# 	if again > 0 and again < 4:
# 		selection = again
# print('\n')
# if selection == 1:
# 	file = open('Subject.txt','w')
# 	subject = input('Enter a school subject: ')
# 	file.write(subject.title() + '\n')
# 	file.close()
# elif selection == 2:
# 	file = open('Subject.txt','r')
# 	print('The content of the Subject.txt file is: ')
# 	print(file.read())
# else :
# 	file = open('Subject.txt','a')
# 	subject = input('Enter a new Subject: ')
# 	file.write(subject.title() + '\n')
# 	file.close()
# 	file = open('Subject.txt','r')
# 	print(file.read())

##############challenges 110 ##############
# file = open('names.txt','r')
# names = file.read()
# print (names)
# word_name =''
# delete_name = input('Enter a name to delete: ')

# for letter in names:
# 	if letter != '\n':
# 		word_name = word_name + letter
# 	elif letter == '\n':
# 		if word_name != delete_name.title():
# 			file = open('names2.txt','a')
# 			file.write(word_name + '\n')
# 			file.close()
# 		word_name = ''

# file = open('names2.txt','r')
# print(file.read())
# file.close()

##############challenges 110 v2##############
#file = open('names.txt','r')
#print(file.read())
#file.close()

# selected_name = input('Enter a name from the list: ')
# file = open('names.txt','r')
# for row in file:
 	# if row != selected_name:
 	# 	file = open('names3.txt','a')
 	# 	file.write(row + '\n')
# 	# 	file.close()
# file.close()

####################Practice Reading and Writing to a .csv file############
#import csv
# file = open('test3.txt','w')
# newRecord = 'Brian 73 Taurus\n'
# file.write(newRecord)
# file.close()
# file = open('names.txt','r')
# for letter in file:
#     print(letter)
# file.close()

# import csv
# file = open('test3.csv','r')
# reader = csv.reader(file)
# rows = list(reader)
# print(rows[2])

# import csv
# file = open('test3.csv','r')
# search = input('Enter the data you are searching for: ')
# #reader = csv.reader(file) #--> no veo necesaria esta linea para el proposito del codigo
# for row in file:
# 	if search.title() in str(row):
# 		print(row)
#####Crea una lista de un file csv################
# import csv
# file = list(csv.reader(open('Books.csv')))
# tmp=[]
# for row in file:
# 	tmp.append(row)
# print(tmp)
# for i in tmp:
# 	print (i)
# ############Crea un nuevo csv de un una lista #################
# file = open('newtest3.csv','a')# con 'a' o con 'w' el resultado en la linea 596 es el mismo
# x = 0
# for row in tmp:
# 	newrow = tmp[x][0] + ',' + tmp[x][1] + ',' + tmp[x][2] + '\n'
# 	file.write(newrow)
# 	x = x + 1
# file.close()

##############challenges 112##############
# import csv
# newTitle =  input('Enter a new title book: ')
# newTitle = newTitle.title()
# newAuthor = input('Who is the author of the previous book: ')
# bookYear = input ('In what year the book was written: ')
# newReg = newTitle + ',' + newAuthor + ',' + bookYear + '\n'

# file = open('Books.csv','a')
# file.write(newReg)
# file.close()
# file = open('Books.csv','r')
# for row in file:
# 	print(row)
# file.close()

##############challenges 113##############
# import csv
# repeat = int(input('How new many record do you want to add: '))
# file = open('Books.csv','a')
# for i in range (0,repeat):
# 	newTitle =  input('Enter a new title book: ')
# 	newAuthor = input('Who is the author of the previous book: ')
# 	bookYear = input ('In what year the book was written: ')
# 	newReg = newTitle + ',' + newAuthor + ',' + bookYear + '\n'
# 	file.write(newReg)
# file.close()

# authorView = input('Enter an author to look for: ')
# file = open('Books.csv','r')
# reader = csv.reader(file) # convierte cada linea del documento en una lista.
# authorexists = 0
# for i in reader: #itera entre cada linea lista 
# 	if authorView in i: #si el autor a buscar es un valor de la lista (de cada linea)
# 		print(i[0]) # imprime solo el valor 0 (autor) de cada linea lista.
# 		authorexists =1

# if authorexists == 0:
# 	print("There isn't any book for the author " + authorView)

##############challenges 114##############
# import csv
# file = csv.reader(open('Books.csv','r'))
# yearinit = int(input('Enter the start year: '))
# yearend = int(input('Enter the end year: '))
# print('\n')
# for linea in file:
# 	date = int(linea[2])
# 	if date >= yearinit and date <= yearend:
# 		print(linea[0]+ ' was wrote in ' + linea[2])

##############challenges 115##############
# import csv
# file = csv.reader(open('Books.csv','r'))
# cont = 1
# filenew = open('NewBook.csv','a')
# for row in file:
# 	filenew.write(str(cont) + ',' + row[0] + ',' + row[1] + ',' + row[2] + '\n')
# 	cont += 1
# filenew.close()

##############challenges 115 V2##############
# import csv
# file = open('Books.csv','r')
# x = 0
# for row in file:
# 	print ('ROW: ' + str(x) + ' - ' + row)
# 	x +=1
# file.close()

##############challenges 116##############
# import csv
# file = list(csv.reader(open('Books.csv','r')))
# cont = 0
# booklist = []
# for row in file:
# 	print(row)
# 	booklist.append(row)
# print('\n')
# rowtodelete = int(input('Enter the # row to delete (0-9): '))
# dataold = str(input('Enter the data to change: '))
# datanew = str(input('Enter the new data to set: '))
# cont1 = 0
# cont2 = 0
# filenew = open('NewBook.csv','w')

# for row in booklist:
# 	#Change any value of any row, is not necesary to know the #row or #colum 
# 	for data in row:
# 		if dataold == data:
# 			booklist[cont1][cont2] = datanew
# 		cont2 +=1
# 	cont2 = 0
# 	#Delete a row
# 	if rowtodelete != cont1:
# 		newrec = booklist[cont1][0] + ',' + booklist[cont1][1] + ',' + booklist[cont1][2] + '\n'
# 		filenew.write(newrec)
# 	cont1 += 1		
# filenew.close()

##############challenges 117##############
# import csv
# import random

# player = str(input('Player Name: '))
# points = 0
# cont = 0
# precsvlist = [player.title()]

# file = open('PlayerHistorial.csv','a')
# for i in range (0,3):
# 	num1 = random.randint(2,10)
# 	num2 = random.randint(8,20)
# 	quiz = num1 * num2
# 	strquiz = str(num1)+' x '+str(num2)
# 	precsvlist.append(strquiz)
# 	reply = int(input(str(num1) + ' x ' + str(num2) + ' = '))
# 	if reply == quiz:
# 		points += 1
# 	precsvlist.append(reply)
# 	cont +=1
# precsvlist.append(points)
# rowcsv = precsvlist[0]
# for element in range(1,len(precsvlist)):
# 	strelement = precsvlist[element]
# 	rowcsv = rowcsv + ',' + str(strelement)
# rowcsv = rowcsv + '\n'
# file.write(rowcsv)
# file.close()

# ##############Subprogram practices##############
# def get_name():
# 	user_name = input('Enter your name: ')
# 	return user_name

# def print_msg(name):
# 	print('Hellow ' + name.title() + '!!')

# def main():
# 	uname = get_name()
# 	print_msg(uname)

# main()

##############challenges 118##############
# def defnum ():
# 	num = int(input('Enter a number: '))
# 	return num

# def count(num):
# 	for i in range(1,num+1):
# 		print(i)

# def main():
# 	num = defnum()
# 	count(num)

# main()

##############challenges 119##############
# import random

# lownum = int(input('Choose the low number limit : '))
# highnum = int(input('Choose the high number limit: '))

# def randnumset():
# 	randnum = random.randint(lownum,highnum)
# 	return randnum

# def guessnum():
# 	print('I am thinkig of a number...')
# 	guess = int(input('Guess the number I am thinking: '))
# 	return guess

# def checkguess(randnum,guess):
# 	#if guess != randnum:
# 	while guess != randnum:
# 		if guess > randnum:
# 			newguess = int(input('Too high...try again: '))
# 			guess = newguess
# 		elif guess < randnum:
# 			newguess = int(input('Too low...try again: '))
# 			guess = newguess
# 		else:
# 			print('You Win!!')

# 	print ('You Win!!')
	
		
# def main():
# 	rand_num = randnumset()
# 	print('random: ' + str(rand_num)) #help to win the game, this line must be delete to chalange the player.
# 	guess_num = guessnum()
# 	checkguess(rand_num,guess_num)

# main()

##############challenges 120##############
# import random

# log = []
# print ('1) Addition')
# print ('2) Substraction')	
# execute = int(input('Enter 1 or 2: '))

# def addition():
# 	num1 = random.randint(5,20)
# 	num2 = random.randint(5,20)
# 	ansum=int(input('\n' + str(num1) + ' + ' + str(num2) + ' = '))
# 	log.append(ansum)
# 	log.append(num1 +num2)
# 	#print ('Your answer is ' + str(log[0]) + ' and the righ answer is ' + str(log[1]) )
# 	return log

# def subsctraction():
# 	num1 = random.randint(25,50)
# 	num2 = random.randint(1,25)
# 	ansub = int(input('\n' + str(num1) + ' - ' + str(num2) + ' = '))
# 	log.insert(0,ansub)
# 	log.insert(1,num1-num2)
# 	return log

# def checkanswer():
# 	if log[0] != log[1]:
# 		print('Incorrect, the answer is: ' + str(log[1]))
# 	else:
# 		print ('Your are right...Congratulations!!')

# def main():
# 	if execute == 1:
# 		addition()
# 		checkanswer()
# 	elif execute ==2:
# 		subsctraction()
# 		checkanswer()
# 	else:
# 		print ('Only type 1 or 2')

# main()		

##############challenges 121##############
# def show_list(list_name):
# 	print('\nThe list currently contains the next names: ')
# 	for name in list_name:
# 		print(name)

# def add_name(list_name):
# 	name_to_add = str(input('Type the new name to add: ')).title()
# 	list_name.append(name_to_add)

# def del_name(list_name):
# 	name_to_del = str(input('Type the name to delete from list: ')).title()
# 	list_name.remove(name_to_del)

# def change_name(list_name):
# 	name_to_change = str(input('Type the name of the list to change: '))
# 	new_name_to_list = str(input('Type the new name to add to the list: '))
# 	index_to_change = list_name.index(name_to_change.title())
# 	for name in list_name:
# 		if name == name_to_change.title():
# 			list_name[index_to_change] = new_name_to_list.title()

# def main():
# 	list_name = ['Manuel','Nidia','Alvaro','Leandro','Grima','Eloy','Sheyla']
# 	enable = True
# 	while enable == True:
# 		print('\n1) Add a name.' +
# 			'\n2) Change a name.' +
# 			'\n3) Delete a name.'+
# 			'\n4) View all the names.'
# 			'\n5) End the program.')
# 		selection = str(input('Select an option: '))
# 		if selection =='1':
# 			add_name(list_name)
# 		elif selection == '2':
# 			change_name(list_name)
# 		elif selection == '3':
# 			del_name(list_name)
# 		elif selection == '4':
# 			show_list(list_name)
# 		elif selection == '5':
# 			enable = False
# 		else :
# 			print('Enter only a valid option from 1 to 5')

# main()

##############Remember working with external files (csv)##############
#import csv
# externalcsv = 'ExternalFiles/Books.csv'
# with open(externalcsv) as externalfile:
# 	#se convierte cada linea a un string entero (sin modulo).
	# linesfile = externalfile.readlines()
	# for line in linesfile:
	# 	print (line.strip())

	#se convierten las lineas a listas en formato csv.
	#se debe usar el modulo csv (import csv).
	# reader = csv.reader(externalfile)
	# for line in reader:
	# 	print (line)

	#se convierten cada linea a un string entero (sin modulos)
	# for line in externalfile:
	# 	print (line.strip())

########################Challenge 122######################
# #import csv #--> it's not neccesary to import this module for this challenge.
# externalfile = 'ExternalFiles/Salaries.csv'

# def add_to_file():
# 	with open(externalfile,'a') as salariesfile:
# 		name = input('Enter the name: ')
# 		salary = input('Enter the salary: ')
# 		new_reg = name.title() + ',' + salary + '\n'
# 		salariesfile.write(new_reg)
		
# def view_records():
# 	print('\n')
# 	with open(externalfile) as salariesfile:
# 		for register in salariesfile:
# 			print(register.strip())

# def main():
# 	continues = True
# 	while continues:
# 		print('\n1) Add to file.'
# 			'\n2) View all records.'
# 			'\n3) Quit program.')
# 		select = int(input('Select one option: '))
# 		if select == 1:
# 			add_to_file()
# 		elif select == 2:
# 			view_records()
# 		elif select == 3:
# 			continues = False
# 		else :
# 			print('\nSelect a valid option.')

# main()

########################Challenge 123######################
# #import csv #--> it's not neccesary to import this module for this challenge.
# externalfile = 'ExternalFiles/Salaries.csv'

# def add_to_file():
# 	with open(externalfile,'a') as salariesfile:
# 		name = input('Enter the name: ')
# 		salary = input('Enter the salary: ')
# 		new_reg = name.title() + ',' + salary + '\n'
# 		salariesfile.write(new_reg)
		
# def view_records():
# 	print('\n')
# 	with open(externalfile) as salariesfile:
# 		for register in salariesfile:
# 			print(register.strip())

# def del_record():
# 	list_file =[]
# 	line_to_delete =int(input('\nEnter the line to delete (starting in 0): '))
# 	count = 0
# 	with open(externalfile) as salariefile:
# 		for register in salariefile:
# 			if line_to_delete != count:
# 				list_file.append(register)
# 			count +=1
# 	with open(externalfile,'w') as salariefile:
# 		for element in list_file:
# 			salariefile.write(element)

# def main():
# 	continues = True
# 	while continues:
# 		print('\n1) Add to file.'
# 			'\n2) View all records.'
# 			'\n3) Delete a record.'
# 			'\n4) Quit program.')
# 		select = int(input('Select one option: '))
# 		if select == 1:
# 			add_to_file()
# 		elif select == 2:
# 			view_records()
# 		elif select == 3:
# 			del_record()	
# 		elif select == 4:
# 			continues = False
# 		else :
# 			print('\nSelect a valid option.')

# main()

##############Tkinter GUI learning##############
# from tkinter import *
# def call():
# 	msg = Label(window, text = 'You pressed the button')
# 	msg.place(x = 30, y =20)
# 	button['bg'] = 'black'
# 	button['fg'] = 'yellow'

# window = Tk()
# window.title('Test Window')
# window.geometry('450x130')
# # label = Label(text = 'message text')
# # label.place(x = 40, y = 100) # sin esta linea el mensaje de la linea anterior no se muestra.
# button = Button(text = 'Press me', command = call)
# button.place(x =70, y = 50, width=70, height=20)
# window.mainloop()

# from tkinter import *
# window = Tk()
# window.title('Window Example')
# #window.geometry('400x400')
# #label = Label(text = 'Enter number: ')
# #label.place(x=100,y=100)
# entry_box = Entry(bd = 3,bg = 'white',justify = CENTER)
# entry_box.pack(side=LEFT)
# output_box = Message(text = 'Message test', width = 85, bg = 'black', fg = 'white', bd = 4, relief = GROOVE)
# output_box.pack(side=RIGHT)	
# window.mainloop()