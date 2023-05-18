
from tkinter import *

root = Tk()
root.title('Calculator')
root.config(bg='gray11')
root.resizable(True,False)
input1_string = StringVar()

input1 = Entry(root, width=45, borderwidth=5)
input1.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
	string = input1.get()
	input1.delete(0, END)
	input1.insert(0, str(string)+str(number))

def button_clear():
	input1.delete(0, END)

def button_add():
	user_number = input1.get()
	global saved_number		
	global symbol
	symbol = 'add'
	saved_number = int(user_number)
	input1.delete(0, END)

def button_subtract():
	user_number = input1.get()
	global saved_number		
	global symbol
	symbol = 'subtract'
	saved_number = int(user_number)
	input1.delete(0, END)	

def button_divide():
	user_number = input1.get()
	global saved_number		
	global symbol
	symbol = 'divide'
	saved_number = int(user_number)
	input1.delete(0, END)	

def button_multiply():
	user_number = input1.get()
	global saved_number		
	global symbol
	symbol = 'multiply'
	saved_number = int(user_number)
	input1.delete(0, END)	

def button_equal():
	summa = input1.get()
	input1.delete(0, END)
	if symbol == 'add':
		input1.insert(0, saved_number + int(summa))
	if symbol == 'subtract':
		input1.insert(0, saved_number - int(summa))
	if symbol == 'divide':
		input1.insert(0, saved_number / int(summa))
	if symbol == 'multiply':
		input1.insert(0, saved_number * int(summa))

font_value = ('Calibari',9)		

button_1 = 		Button(root, text='1', padx=40, pady=20, font=font_value, bg='gray11', fg='DarkOrange1', borderwidth=3, command=lambda: button_click(1))
button_2 = 		Button(root, text='2', padx=40, pady=20, font=font_value, bg='gray11', fg='DarkOrange1', borderwidth=3, command=lambda: button_click(2))
button_3 =		Button(root, text='3', padx=40, pady=20, font=font_value, bg='gray11', fg='DarkOrange1', borderwidth=3,	command=lambda: button_click(3))
button_4 = 		Button(root, text='4', padx=40, pady=20, font=font_value, bg='gray11', fg='DarkOrange1', borderwidth=3, command=lambda: button_click(4))
button_5 = 		Button(root, text='5', padx=40, pady=20, font=font_value, bg='gray11', fg='DarkOrange1', borderwidth=3, command=lambda: button_click(5))
button_6 = 		Button(root, text='6', padx=40, pady=20, font=font_value, bg='gray11', fg='DarkOrange1', borderwidth=3, command=lambda: button_click(6))
button_7 = 		Button(root, text='7', padx=40, pady=20, font=font_value, bg='gray11', fg='DarkOrange1', borderwidth=3, command=lambda: button_click(7))
button_8 = 		Button(root, text='8', padx=40, pady=20, font=font_value, bg='gray11', fg='DarkOrange1', borderwidth=3, command=lambda: button_click(8))
button_9 = 		Button(root, text='9', padx=40, pady=20, font=font_value, bg='gray11', fg='DarkOrange1', borderwidth=3, command=lambda: button_click(9))
button_0 =		Button(root, text='0', padx=40, pady=20, font=font_value, bg='gray11', fg='DarkOrange1', borderwidth=3, command=lambda: button_click(0))

button_add = 		Button(root, text='+', padx=40, pady=20, font=font_value, bg='gray11', fg='DarkOrange1', borderwidth=3, command=button_add)
button_subtract = 	Button(root, text='-', padx=41, pady=20, font=font_value, bg='gray11', fg='DarkOrange1', borderwidth=3, command=button_subtract)
button_divide = 	Button(root, text='/', padx=40, pady=20, font=font_value, bg='gray11', fg='DarkOrange1', borderwidth=3, command=button_divide)
button_multiply = 	Button(root, text='*', padx=40, pady=20, font=font_value, bg='gray11', fg='DarkOrange1', borderwidth=3,	command=button_multiply)
button_equal = 		Button(root, text='=', padx=91, pady=20, font=font_value, bg='Orange', fg='white',       borderwidth=3, command=button_equal)
button_clear = 		Button(root, text='Clear', padx=80, pady=20, font=font_value, bg='Orange', fg='white', 	 borderwidth=3, command=button_clear)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=4, column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)
button_7.grid(row=5, column=0)
button_8.grid(row=5, column=1)
button_9.grid(row=5, column=2)
button_0.grid(row=6, column=0)

button_add.grid(row=6, column=1)
button_subtract.grid(row=6, column=2)
button_divide.grid(row=7, column=0)
button_clear.grid(row=7, column=1, columnspan=2)
button_multiply.grid(row=8, column=0)
button_equal.grid(row=8, column=1, columnspan=2)

root.mainloop()
