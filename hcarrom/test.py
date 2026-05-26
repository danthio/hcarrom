import tkinter as tk 
import math
import pyperclip

def pieces_coord():
	global pieces

	pieces=[]

	x,y=243,243

	pieces.append([x,y,"red"])



	cx,cy=x,y


	a_=180
	a=360/6
	col="black"
	r=5+1+5+1
	for i in range(6):

		x=r*math.sin(math.radians(a_))+cx
		y=r*math.cos(math.radians(a_))+cy


		pieces.append([x,y,col])


		if col=="black":
			col="white"
		elif col=="white":
			col="black"



		a_+=a




	a_=180
	a=360/12
	col="white"
	r=5+1+5+5+1+5+1
	for i in range(12):

		x=r*math.sin(math.radians(a_))+cx
		y=r*math.cos(math.radians(a_))+cy


		pieces.append([x,y,col])


		if col=="black":
			col="white"
		elif col=="white":
			col="black"



		a_+=a


	draw_pieces()


def draw_pieces():
	global pieces


	for i in pieces:

		x,y,col=i

		can.create_oval(x-5,y-5, x+5,y+5, fill=col)

val=""
def get_val(e):
	global pieces
	global val

	for i in pieces:

		x,y=i[:2]

		r=math.sqrt((x-e.x)**2+(y-e.y)**2)

		if r<=5:

			val=f"{x},{y}"

def b1(e):
	global val

	pyperclip.copy(val)


pieces=[]

root=tk.Tk()
root.geometry(f"{500}x{500}")

can=tk.Canvas(width=500,height=500,relief="flat",highlightthickness=0,border=0,bg="#00ffff")
can.place(in_=root,x=0,y=0)

can.bind("<Button-1>",b1)
can.bind("<Motion>",get_val)

pieces_coord()
root.mainloop()