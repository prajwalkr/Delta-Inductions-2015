from Tkinter import *
import tkMessageBox
from random import randint

main = Tk()
main.title('Play!')
main.geometry("249x170")
app = Frame(main)
app.grid()

def init():
	for i in range(1,9):
		row = randint(0,2)
		while True:
			if a[row][0] == '' or a[row][1] == '' or a[row][2] == '':
				break
			row = randint(0,2)
		col = randint(0,2)
		while a[row][col] != '':
			col = randint(0,2)
		if a[row][col] == '':
			a[row][col] += str(i)
	for i in range(3):
		for j in range(3):
			if a[i][j] == '':
				a[i][j] = 'T'
				return

def program():
	global a 
	a = [['','',''],['','',''],['','','']]
	init()
	return display()

def check():
	p = 1
	for i in range(3):
		for j in range(3):
			if i == 2 and j == 2:
				if a[i][j] != 'T':
					return False
			elif a[i][j] != str(p):
				return False
			p += 1
	return True

def findT():
	for i in range(3):
		for j in range(3):
			if a[i][j] == 'T':
				return i,j

def leftKey(event):
	x,y = findT()
	if y == 0:
		return
	t = a[x][y-1]
	a[x][y-1] = 'T'
	a[x][y] = t
	display()
	if check() == True:
		tkMessageBox.showinfo('Game over!','Well done! :D')
		exit(0)

def rightKey(event):
	x,y = findT()
	if y == 2:
		return
	t = a[x][y+1]
	a[x][y+1] = 'T'
	a[x][y] = t
	display()
	if check() == True:
		tkMessageBox.showinfo('Game over!','Well done! :D')
		exit(0)

def upKey(event):
	x,y = findT()
	if x == 0:
		return
	t = a[x-1][y]
	a[x-1][y] = 'T'
	a[x][y] = t
	display()
	if check() == True:
		tkMessageBox.showinfo('Game over!','Well done! :D')
		exit(0)

def downKey(event):
	x,y = findT()
	if x == 2:
		return
	t = a[x+1][y]
	a[x+1][y] = 'T'
	a[x][y] = t
	display()
	if check() == True:
		tkMessageBox.showinfo('Game over!','Well done! :D')
		exit(0)

def display():
	text.delete('0.0',END)
	printtext = '\n\n\t'
	for i in range(3):
		for j in range(3):
			printtext += a[i][j] + '\t'
		printtext += '\n\t'
	text.insert(0.0,printtext)

text = Text(width = 30,height = 10,wrap = WORD)
text.grid(row = 0,column = 0, sticky = W)
program()
main.bind('<Left>', leftKey)
main.bind('<Right>', rightKey)
main.bind('<Up>', upKey)
main.bind('<Down>', downKey)

main.mainloop()
