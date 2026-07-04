from PIL import Image,ImageTk,ImageDraw
import tkinter as tk
from tkinter import font
import math
import time
import random

bg=0
circle=0
bg2=0

striker_im=0
black_im=0
white_im=0
red_im=0

home=0
quit=0
signature=0

turnh1,turnh2=0,0
def load_im():
	global w,h
	global bg,bg2,circle
	global striker_im,black_im,white_im,red_im
	global striker_r,piece_r
	global quit,home
	global signature
	global turnh1,turnh2

	#striker_im


	im=Image.new("RGBA",(500,500),(0,0,0,0))
	draw=ImageDraw.Draw(im)

	draw.ellipse((16,16,500-16-1,500-16-1),fill=(255,0,255,255),outline=(0,0,0,255),width=32)

	im=im.resize((int(round(striker_r*2,0)),int(round(striker_r*2,0))), Image.LANCZOS)

	striker_im=im

	#black_im

	im=Image.new("RGBA",(500,500),(0,0,0,0))
	draw=ImageDraw.Draw(im)

	draw.ellipse((16,16,500-16-1,500-16-1),fill=(0,0,0,255),outline=(255,255,255,255),width=32)

	im=im.resize((int(round(piece_r*2,0)),int(round(piece_r*2,0))), Image.LANCZOS)

	black_im=im


	#white_im


	im=Image.new("RGBA",(500,500),(0,0,0,0))
	draw=ImageDraw.Draw(im)

	draw.ellipse((16,16,500-16-1,500-16-1),fill=(255,255,255,255),outline=(0,0,0,255),width=32)

	im=im.resize((int(round(piece_r*2,0)),int(round(piece_r*2,0))), Image.LANCZOS)

	white_im=im


	#red_im


	im=Image.new("RGBA",(500,500),(0,0,0,0))
	draw=ImageDraw.Draw(im)

	draw.ellipse((16,16,500-16-1,500-16-1),fill=(255,0,0,255),outline=(0,0,0,255),width=32)

	im=im.resize((int(round(piece_r*2,0)),int(round(piece_r*2,0))), Image.LANCZOS)

	red_im=im






	im=Image.open("data/board.png")
	im=im.resize((w,h))


	x,y=im.size

	x1=0
	for x_ in range(x):

		col=im.getpixel((x_,int(y/2)))
		x1=x_
		if max(col)>20:
			x1-=1
			break


	x2=0
	for x_ in range(x):

		col=im.getpixel((x-x_-1,int(y/2)))

		x2=x-x_-1
		if max(col)>20:
			x2+=1
			break



	y1=0

	for y_ in range(y):

		col=im.getpixel((int(x/4),y_))



		y1=y_

		if max(col)>20:

			y1-=1
			break

	y2=0

	for y_ in range(y):

		col=im.getpixel((int(x/4),y-y_-1))



		y2=y-y_-1

		if max(col)>20:

			y1+=1
			break






	im=im.crop((x1,y1,x2,y2))

	w,h=im.size


	im_=Image.new("RGBA",(w,h),(0,0,0,0))

	im_.paste(im,(0,0))

	draw=ImageDraw.Draw(im_)


	rr=22


	ar=[(0,h-1),(0,h-1-rr)]

	a_=270

	for a in range(90):

		x=rr*math.sin(math.radians(a_))+rr
		y=rr*math.cos(math.radians(a_))+(h-1-rr)

		x=int(round(x,0))
		y=int(round(y,0))

		ar.append((x,y))



		a_+=1

	draw.polygon(ar,fill=(0,0,0,0),outline=(0,0,0,0))


	ar=[(w-1,h-1),(w-1,h-1-rr)]

	a_=90

	for a in range(90):

		x=rr*math.sin(math.radians(a_))+w-1-rr
		y=rr*math.cos(math.radians(a_))+h-1-rr

		x=int(round(x,0))
		y=int(round(y,0))

		ar.append((x,y))



		a_-=1


	draw.polygon(ar,fill=(0,0,0,0),outline=(0,0,0,0))

	#im_.show()


	bg=ImageTk.PhotoImage(im_) 


	#darker layer
	im=Image.new("RGBA",(w,h+30),(0,0,0,170))
	bg2=ImageTk.PhotoImage(im)

	#home

	im=Image.open("data/home.png")
	im=im.resize((25,25))

	home=ImageTk.PhotoImage(im)


	#quit
	im=Image.open("data/quit.png")
	im=im.resize((25,25))

	quit=ImageTk.PhotoImage(im)


	im=Image.open("data/signature.png")
	x,y=im.size

	y=50*y/x
	x=50

	im=im.resize((int(round(x,0)),int(round(y,0))))

	signature=ImageTk.PhotoImage(im)

	val=int(round(w/2,0))

	im=Image.new("RGBA",(val,30+22),(0,0,0,0))
	x,y=im.size
	draw=ImageDraw.Draw(im)

	for y_ in range(y):

		op=255
		for x_ in range(x):

			draw.line(((x_,0),(x_,y)), fill=(0,255,0,int(round(op,0))))



			op-=255/val


	#draw.polygon(((x-15,0),(x,0),(x,y)),fill=(0,0,0,0),outline=(0,0,0,0))

	#im.show()

	turnh1=ImageTk.PhotoImage(im)




	im=Image.new("RGBA",(val,30+22),(0,0,0,0))
	x,y=im.size
	draw=ImageDraw.Draw(im)

	for y_ in range(y):

		op=255
		_x=x
		for x_ in range(x):

			draw.line(((_x,0),(_x,y)), fill=(0,255,0,int(round(op,0))))

			_x-=1

			op-=255/val





	#draw.polygon(((0,0),(15,0),(0,y)),fill=(0,0,0,0),outline=(0,0,0,0))

	#im.show()

	turnh2=ImageTk.PhotoImage(im)








st=""


pos_intro2=[]

intro2_im1,intro2_im2=0,0,

def intro2():
	global bg,bg2
	global st
	global w,h
	global pos_intro2
	global intro2_im1,intro2_im2
	global home
	global w,h
	global signature

	can["height"]=h
	#root.geometry(f"{w}x{h}+{int((root.winfo_screenwidth()-w)/2)}+{50}")

	pos_intro2=[]

	st="intro2"

	can.delete("all")

	can.create_image(0,0,image=bg,anchor="nw")

	can.create_image(347+40,441,image=signature,anchor="c")
	can.create_image(0,0,image=bg2,anchor="nw")





	x=200
	y=(h-90)/2

	can.create_image(w/2+x/2-25,y-10-25,image=home,anchor="nw")

	#print(w/2+x/2-25,y-10-25)

	im=draw_rounded_rect(w/2-x/2,y,w/2+x/2,y+30,15,((255,0,255)),((255,0,255)),255,255,1)
	intro2_im1=ImageTk.PhotoImage(im)

	can.create_image(w/2-x/2,y,image=intro2_im1,anchor="nw")

	can.create_text(w/2,y+15,text="2 Player",font=("FreeMono",13),fill="#000000",anchor="c")

	pos_intro2.append([w/2-x/2+15,y, w/2+x/2-15,y+30-1])


	y+=60


	im=draw_rounded_rect(w/2-x/2,y,w/2+x/2,y+30,15,((255,0,255)),((255,0,255)),255,255,1)
	intro2_im2=ImageTk.PhotoImage(im)

	can.create_image(w/2-x/2,y,image=intro2_im2,anchor="nw")
	can.create_text(w/2,y+15,text="Play vs CPU",font=("FreeMono",13),fill="#000000",anchor="c")

	pos_intro2.append([w/2-x/2+15,y, w/2+x/2-15,y+30-1])

pos_intro=[]

intro_im1,intro_im2=0,0,
def intro():
	global bg,bg2
	global st
	global w,h
	global pos_intro
	global intro_im1,intro_im2
	global w,h
	global signature

	root.geometry(f"{w}x{h}")

	can["height"]=h

	pos_intro=[]

	st="intro"

	can.delete("all")

	can.create_image(0,0,image=bg,anchor="nw")

	can.create_image(347+40,441,image=signature,anchor="c")

	can.create_image(0,0,image=bg2,anchor="nw")

	x=200

	y=(h-90)/2

	im=draw_rounded_rect(w/2-x/2,y,w/2+x/2,y+30,15,((255,0,255)),((255,0,255)),255,255,1)
	intro_im1=ImageTk.PhotoImage(im)

	can.create_image(w/2-x/2,y,image=intro_im1,anchor="nw")

	can.create_text(w/2,y+15,text="Carrom",font=("FreeMono",13),fill="#000000",anchor="c")

	pos_intro.append([w/2-x/2+15,y, w/2+x/2-15,y+30-1])


	y+=60


	im=draw_rounded_rect(w/2-x/2,y,w/2+x/2,y+30,15,((255,0,255)),((255,0,255)),255,255,1)
	intro_im2=ImageTk.PhotoImage(im)

	can.create_image(w/2-x/2,y,image=intro_im2,anchor="nw")
	can.create_text(w/2,y+15,text="Disk Pool",font=("FreeMono",13),fill="#000000",anchor="c")

	pos_intro.append([w/2-x/2+15,y, w/2+x/2-15,y+30-1])


pwhite=0
pwred=0

pblack=0
pbred=0

TY,black_im_,red_im_=0,0,0

turnx=1
turnv=0

_turn0,_turn1=0,0

tcon=0
def draw_turn():
	global can,turn,turn0,turn1,turnx,turnv,_turn0,_turn1,tcon
	global pwhite,pwred,pblack,pbred
	global game_st,st
	global w,h




	try:
		
		if st=="main":	



			val=int(round(w/2,0))

			if turnx!=turn:

				tcon=1

				turnx=turn
				turnv=0

				_turn0=can.coords(turn0)[0]
				_turn1=can.coords(turn1)[0]


			if turnv!=val:

				if tcon==1:


					turnv+=1


					if turn==0:





						can.coords(turn0,_turn0-turnv,h-22)

						can.coords(turn1,_turn1-turnv,h-22)

						can.itemconfig(pwhite,fill="#ffffff")
						can.itemconfig(pwred,fill="#ffffff")
						can.itemconfig(pblack,fill="#000000")
						can.itemconfig(pbred,fill="#000000")




					elif turn==1:





						can.coords(turn0,_turn0+turnv,h-22)

						can.coords(turn1,_turn1+turnv,h-22)



						can.itemconfig(pwhite,fill="#000000")
						can.itemconfig(pwred,fill="#000000")
						can.itemconfig(pblack,fill="#ffffff")
						can.itemconfig(pbred,fill="#ffffff")
			else:
				tcon=0



	except Exception as e:
		print(e)

	root.after(1,draw_turn)


turn0,turn1=0,0
def main():
	global can
	global bg
	global st
	global pieces
	global striker_r,piece_r
	global gameb
	global quit
	global w,h
	global white_im,black_im,red_im, white_im_,black_im_,red_im_
	global pwhite,pwred,pblack,pbred
	global moves,moves_,_red_,_red2_
	global turn,turn0,turn1,turnx,turnv
	global signature

	global turnh1,turnh2

	turn=1
	turnx=1
	turnv=0


	moves,moves_,_red_,_red2_=[],[],None,None


	can["height"]=h+30
	x=root.geometry().split("+")[1]
	y=root.geometry().split("+")[2]
	root.geometry(f"{w}x{h+30}+{x}+{y}")

	st="main"

	can.delete("all")

	turn0=can.create_image(0,h-22,image=turnh1,anchor="nw")

	xx=w/2
	turn1=can.create_image(w/2+xx,h-22,image=turnh2,anchor="nw")


	can.create_image(0,0,image=bg,anchor="nw")

	can.create_image(347+40,441,image=signature,anchor="c")

	#can.create_image(w-3-25,3,image=quit,anchor="nw")



	pieces={"striker":{"coord":[0,0],
						"coord_":[0,0],
						"angle":0,
						"proj_ang":None,
						"st":0,
						"data":[],
						"initial_v":0,
						"current_v":0,
						"start_time":0,
						"speed":0,
						"move st":0,
						"im":0,
						"potted":0,

						},


		"1 white":{"coord":[243.0,220.0],
							"coord_":[0,0],
							"angle":0,
							"proj_ang":None,
							"st":0,
							"data":[],
							"initial_v":0,
							"current_v":0,
							"start_time":0,
							"speed":0,
							"potted":0,
							"move st":0,
							"im":0,
							},


		"2 white":{"coord":[253.39230484541326,237.0],
							"coord_":[0,0],
							"angle":0,
							"proj_ang":None,
							"st":0,
							"data":[],
							"initial_v":0,
							"current_v":0,
							"start_time":0,
							"speed":0,
							"potted":0,
							"move st":0,
							"im":0,
							},



		"3 white":{"coord":[262.9185842870421,231.50000000000003],
							"coord_":[0,0],
							"angle":0,
							"proj_ang":None,
							"st":0,
							"data":[],
							"initial_v":0,
							"current_v":0,
							"start_time":0,
							"speed":0,
							"potted":0,
							"move st":0,
							"im":0,
							},

		"4 white":{"coord":[262.9185842870421,254.5],
							"coord_":[0,0],
							"angle":0,
							"proj_ang":None,
							"st":0,
							"data":[],
							"initial_v":0,
							"current_v":0,
							"start_time":0,
							"speed":0,
							"potted":0,
							"move st":0,
							"im":0,
							},


		"5 white":{"coord":[243.0,255.0],
							"coord_":[0,0],
							"angle":0,
							"proj_ang":None,
							"st":0,
							"data":[],
							"initial_v":0,
							"current_v":0,
							"start_time":0,
							"speed":0,
							"potted":0,
							"move st":0,
							"im":0,
							},

		"6 white":{"coord":[243.0,266.0],
							"coord_":[0,0],
							"angle":0,
							"proj_ang":None,
							"st":0,
							"data":[],
							"initial_v":0,
							"current_v":0,
							"start_time":0,
							"speed":0,
							"potted":0,
							"move st":0,
							"im":0,
							},

		"7 white":{"coord":[223.08141571295792,254.5],
							"coord_":[0,0],
							"angle":0,
							"proj_ang":None,
							"st":0,
							"data":[],
							"initial_v":0,
							"current_v":0,
							"start_time":0,
							"speed":0,
							"potted":0,
							"move st":0,
							"im":0,
							},


		"8 white":{"coord":[223.08141571295792,231.5],
							"coord_":[0,0],
							"angle":0,
							"proj_ang":None,
							"st":0,
							"data":[],
							"initial_v":0,
							"current_v":0,
							"start_time":0,
							"speed":0,
							"potted":0,
							"move st":0,
							"im":0,
							},

		"9 white":{"coord":[232.60769515458674,237.0],
							"coord_":[0,0],
							"angle":0,
							"proj_ang":None,
							"st":0,
							"data":[],
							"initial_v":0,
							"current_v":0,
							"start_time":0,
							"speed":0,
							"potted":0,
							"move st":0,
							"im":0,
							},

		"1 black":{"coord":[243.0,231.0],
							"coord_":[0,0],
							"angle":0,
							"proj_ang":None,
							"st":0,
							"data":[],
							"initial_v":0,
							"current_v":0,
							"start_time":0,
							"speed":0,
							"potted":0,
							"move st":0,
							"im":0,
							},

		"2 black":{"coord":[254.5,223.0814157129579],
							"coord_":[0,0],
							"angle":0,
							"proj_ang":None,
							"st":0,
							"data":[],
							"initial_v":0,
							"current_v":0,
							"start_time":0,
							"speed":0,
							"potted":0,
							"move st":0,
							"im":0,
							},


		"3 black":{"coord":[253.39230484541326,249.0],
							"coord_":[0,0],
							"angle":0,
							"proj_ang":None,
							"st":0,
							"data":[],
							"initial_v":0,
							"current_v":0,
							"start_time":0,
							"speed":0,
							"potted":0,
							"move st":0,
							"im":0,
							},

		"4 black":{"coord":[266.0,243.0],
							"coord_":[0,0],
							"angle":0,
							"proj_ang":None,
							"st":0,
							"data":[],
							"initial_v":0,
							"current_v":0,
							"start_time":0,
							"speed":0,
							"potted":0,
							"move st":0,
							"im":0,
							},


		"5 black":{"coord":[254.5,262.9185842870421],
							"coord_":[0,0],
							"angle":0,
							"proj_ang":None,
							"st":0,
							"data":[],
							"initial_v":0,
							"current_v":0,
							"start_time":0,
							"speed":0,
							"potted":0,
							"move st":0,
							"im":0,
							},

		"6 black":{"coord":[231.5,262.9185842870421],
							"coord_":[0,0],
							"angle":0,
							"proj_ang":None,
							"st":0,
							"data":[],
							"initial_v":0,
							"current_v":0,
							"start_time":0,
							"speed":0,
							"potted":0,
							"move st":0,
							"im":0,
							},

		"7 black":{"coord":[232.60769515458674,249.0],
							"coord_":[0,0],
							"angle":0,
							"proj_ang":None,
							"st":0,
							"data":[],
							"initial_v":0,
							"current_v":0,
							"start_time":0,
							"speed":0,
							"potted":0,
							"move st":0,
							"im":0,
							},


		"8 black":{"coord":[220.0,243.0],
							"coord_":[0,0],
							"angle":0,
							"proj_ang":None,
							"st":0,
							"data":[],
							"initial_v":0,
							"current_v":0,
							"start_time":0,
							"speed":0,
							"potted":0,
							"move st":0,
							"im":0,
							},

		"9 black":{"coord":[231.5,223.08141571295792],
							"coord_":[0,0],
							"angle":0,
							"proj_ang":None,
							"st":0,
							"data":[],
							"initial_v":0,
							"current_v":0,
							"start_time":0,
							"speed":0,
							"potted":0,
							"move st":0,
							"im":0,
							},


		"red":{"coord":[243,243],
							"coord_":[0,0],
							"angle":0,
							"proj_ang":None,
							"st":0,
							"data":[],
							"initial_v":0,
							"current_v":0,
							"start_time":0,
							"speed":0,
							"potted":0,
							"move st":0,
							"im":0,
							},

			}






	yv1,yv2=82,404

	xrng=(102*w/500,383*w/500)


	if turn==0:
		pieces["striker"]["coord"]=[xrng[0]+(xrng[1]-xrng[0])/2,yv1]
	elif turn==1:
		pieces["striker"]["coord"]=[xrng[0]+(xrng[1]-xrng[0])/2,yv2]

	for i in pieces:


		if i=="striker":

			draw_piece_(i)

		else:


			pieces[i]["potted"]=0

			if game=="Disk Pool" and i=="red":
				pieces["red"]["potted"]=1
				pieces["red"]["coord"]=[-100,100]



			if pieces[i]["potted"]==1:
				continue


			draw_piece_(i)



	_turn0=can.coords(turn0)[0]
	_turn1=can.coords(turn1)[0]
	
	white_im_=ImageTk.PhotoImage(white_im)


	can.create_image(10,int(can["height"])-15,image=white_im_)

	pwhite=can.create_text(10+5+10,int(can["height"])-15,text="0",font=("FreeMono",13),fill="#ffffff")

	red_im_=ImageTk.PhotoImage(red_im)

	if game=="Carrom":

		


		can.create_image(10+15+15+5,int(can["height"])-15,image=red_im_)

		pwred=can.create_text(10+5+10+15+15+5,int(can["height"])-15,text="0",font=("FreeMono",13),fill="#ffffff")



	if game=="Carrom":



		black_im_=ImageTk.PhotoImage(black_im)


		can.create_image(w-(10+5+10+15+15+5),int(can["height"])-15,image=black_im_)

		pblack=can.create_text(w-(10+5+10+15+15+5)+(5+10),int(can["height"])-15,text="0",font=("FreeMono",13),fill="#ffffff")

		can.create_image(w-(10+5+10+15+15+5)+(15+15+5),int(can["height"])-15,image=red_im_)

		pbred=can.create_text(w-(10+5+10+15+15+5)+(5+10+15+15+5),int(can["height"])-15,text="0",font=("FreeMono",13),fill="#ffffff")


	else:


		black_im_=ImageTk.PhotoImage(black_im)


		can.create_image(w-(10+5+10+5),int(can["height"])-15,image=black_im_)

		pblack=can.create_text(w-(10+5+10+5)+(5+10),int(can["height"])-15,text="0",font=("FreeMono",13),fill="#ffffff")


	#can.create_polygon(w/2-100,h, w/2+100,h, w/2+100-15,h+30, w/2-100+15,h+30,fill="#ff00ff",outline="#ff00ff")

	#can.create_text(w/2,h+15,text=game, font=("FreeMono",13),fill="#ff00ff")




p=0
#r=30
cx,cy=0,0
def draw_piece(x,y,r):
	global p
	global cx,cy

	cx,cy=x,y

	can.delete(p)

	p=can.create_oval(x-r,y-r, x+r,y+r,fill="#000000",outline="#ff00ff")


def force_():

	global pieces
	global game_st,reset_st
	global st

	if st=="main":

		if reset_st==1:
			root.after(100,force_)
			return


		if game_st==1:

			if not pieces["striker"]["initial_v"]+0.5>5:

				pieces["striker"]["initial_v"]+=0.5
				pieces["striker"]["current_v"]=pieces["striker"]["initial_v"]


				draw_move_()
		elif game_st==2:


			draw_move_(1)



	root.after(100,force_)

drag_st=0
game_st=0
game=""

quit_im=0
quit_st=0
quit_coord=[]
quit_i=[0,0,0,0,0,0,0]
def can_b1(e):
	global st
	global drag_st,game_st
	global pieces
	global pos_intro,pos_intro2
	global game
	global dm_vs
	global quit_im,quit_st,quit_coord,quit_i
	global go_st,go_coord


	#print(e.x,e.y)


	#global r


	#draw_piece(e.x,e.x,r)


	if st=="intro":

		#Carrom
		
		cx,cy=pos_intro[0][0],pos_intro[0][1]+15

		r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

		if r<=15:

			game="Carrom"

			intro2()

			return


		cx,cy=pos_intro[0][2],pos_intro[0][1]+15

		r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

		if r<=15:
			game="Carrom"

			intro2()

			return

		if pos_intro[0][0]<=e.x<=pos_intro[0][2]:

			if pos_intro[0][1]<=e.y<=pos_intro[0][3]:

				game="Carrom"
				

				intro2()

				return



		#Disk Pool



		cx,cy=pos_intro[1][0],pos_intro[1][1]+15

		r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

		if r<=15:

			game="Disk Pool"

			intro2()

			return


		cx,cy=pos_intro[1][2],pos_intro[1][1]+15

		r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

		if r<=15:

			game="Disk Pool"

			intro2()

			return

		if pos_intro[1][0]<=e.x<=pos_intro[1][2]:

			if pos_intro[1][1]<=e.y<=pos_intro[1][3]:
				
				game="Disk Pool"

				intro2()


				return

	elif st=="intro2":

		#home

		if 317.5<=e.x<=317.5+25:
				if 162.5<=e.y<=162.5+25:

					intro()
					return
		#2 player
		
		cx,cy=pos_intro2[0][0],pos_intro2[0][1]+15

		r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

		if r<=15:


			main()

			return


		cx,cy=pos_intro2[0][2],pos_intro2[0][1]+15

		r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

		if r<=15:

			main()

			return

		if pos_intro2[0][0]<=e.x<=pos_intro2[0][2]:

			if pos_intro2[0][1]<=e.y<=pos_intro2[0][3]:

				

				main()

				return



		#play vs cpu



		cx,cy=pos_intro2[1][0],pos_intro2[1][1]+15

		r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

		if r<=15:

			

			return


		cx,cy=pos_intro2[1][2],pos_intro2[1][1]+15

		r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

		if r<=15:


			return

		if pos_intro2[1][0]<=e.x<=pos_intro2[1][2]:

			if pos_intro2[1][1]<=e.y<=pos_intro2[1][3]:
				


				return

	elif st=="main":

		if go_st==1:


			x1,y1,x2,y2=go_coord

			if x1<=e.x<=x1+15:
				if y2-15<=e.y<=y2:

					cx,cy=x1+15,y2-15

					r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

					if r<=15:

						for i in go_i:

							can.delete(i)

						intro()
						go_st=0
						return


			if x1<=e.x<=x1+(x2-x1)/2:
				if y1<=e.y<=y2-15:

					for i in go_i:

						can.delete(i)

					intro()
					go_st=0
					return

			if x1+15<=e.x<=x1+(x2-x1)/2:
				if y1<=e.y<=y2:

					for i in go_i:

						can.delete(i)

					intro()
					go_st=0
					return


			if x2-15<=e.x<=x2:
				if y2-15<=e.y<=y2:

					cx,cy=x2-15,y2-15

					r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

					if r<=15:

						root.destroy()

						return






			if x1+(x2-x1)/2<=e.x<=x2:
				if y1<=e.y<=y2-15:

					root.destroy()

					return

			if x1+(x2-x1)/2<=e.x<=x2-15:
				if y1<=e.y<=y2:

					root.destroy()

					return



			return



		if quit_st==1:




			x1,y1,x2,y2=quit_coord

			if x1<=e.x<=x1+15:
				if y2-15<=e.y<=y2:

					cx,cy=x1+15,y2-15

					r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

					if r<=15:

						for i in quit_i:

							can.delete(i)

						intro()
						quit_st=0
						return


			if x1<=e.x<=x1+(x2-x1)/2:
				if y1<=e.y<=y2-15:

					for i in quit_i:

						can.delete(i)

					intro()
					quit_st=0
					return


			if x1+15<=e.x<=x1+(x2-x1)/2:
				if y1<=e.y<=y2:

					for i in quit_i:

						can.delete(i)

					intro()
					quit_st=0
					return


			if x2-15<=e.x<=x2:
				if y2-15<=e.y<=y2:

					cx,cy=x2-15,y2-15

					r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

					if r<=15:

						quit_st=0

						for i in quit_i:

							can.delete(i)

						draw_move_()

						return


			if x1+(x2-x1)/2<=e.x<=x2:
				if y1<=e.y<=y2-15:

					quit_st=0

					for i in quit_i:

						can.delete(i)

					draw_move_()

					return


			if x1+(x2-x1)/2<=e.x<=x2-15:
				if y1<=e.y<=y2:

					quit_st=0

					for i in quit_i:

						can.delete(i)

					draw_move_()

					return



			return

		"""


		if w-3-25<=e.x<=w-3:
			if 3<=e.y<=3+25:

				quit_st=1

				draw_move_()

				quit_i[6]=can.create_image(0,0,image=bg2,anchor="nw")

				xx,yy=250,100

				x=(w-xx)/2
				y=(h-yy)/2


				im=draw_rounded_rect(x,y,x+xx,y+yy,15,(0,0,0),((255,0,255)),140,255,1)
				quit_im=ImageTk.PhotoImage(im)

				quit_i[0]=can.create_image(x,y,image=quit_im,anchor="nw")

				quit_i[1]=can.create_text(x+xx/2,y+20, text="Quit Game?", font=("FreeMono",13),fill="#ff00ff")

				quit_i[2]=can.create_line(x+1,y+yy-30, x+xx-1,y+yy-30,fill="#770077")

				quit_i[3]=can.create_line(x+xx/2,y+yy-30, x+xx/2,y+yy-1,fill="#770077")

				quit_i[4]=can.create_text(x+xx/4,y+yy-15,text="Yes",font=("FreeMono",13),fill="#ff00ff")

				quit_i[5]=can.create_text(x+xx-xx/4,y+yy-15,text="No",font=("FreeMono",13),fill="#ff00ff")

				quit_coord=[x,y+yy-30, x+xx,y+yy]

				return
		"""






		if game_st==0:

			x,y=pieces["striker"]["coord"]

			r=math.sqrt((e.x-x)**2+(e.y-y)**2)

			if r<=striker_r:
				drag_st=1
				return

			else:


				if turn==0:

					if 102<=e.x<=383:
						if 82-10.36<=e.y<=82+10.36:
							pieces["striker"]["coord"][0]=e.x


							for i in dm_vs:

								can.delete(i)
							draw_piece_("striker",1)
							


							return


					cx,cy=102,82

					r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

					if r<=10.36:
						pieces["striker"]["coord"][0]=xrng[0]

						for i in dm_vs:

							can.delete(i)

						draw_piece_("striker",1)
						return

					cx,cy=383,82

					r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

					if r<=10.36:
						pieces["striker"]["coord"][0]=xrng[1]



						for i in dm_vs:

							can.delete(i)

						draw_piece_("striker",1)
						return



				elif turn==1:

					if 102<=e.x<=383:
						if 404-10.36<=e.y<=404+10.36:
							pieces["striker"]["coord"][0]=e.x



							for i in dm_vs:

								can.delete(i)
							draw_piece_("striker",1)

							return


					cx,cy=102,404

					r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

					if r<=10.36:
						pieces["striker"]["coord"][0]=xrng[0]


						for i in dm_vs:

							can.delete(i)

						draw_piece_("striker",1)
						return

					cx,cy=383,404

					r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

					if r<=10.36:
						pieces["striker"]["coord"][0]=xrng[1]


						for i in dm_vs:

							can.delete(i)

						draw_piece_("striker",1)
						return





		if game_st==0:
			game_st=1














def drag(e):
	global drag_st
	global pieces
	global dm_vs
	global st

	if st=="main":

		if drag_st==1:

			x,y=pieces["striker"]["coord"]

			r=math.sqrt((e.x-x)**2+(e.y-y)**2)

			#if r<=striker_r:
			if xrng[0]<=e.x<=xrng[1]:
				pieces["striker"]["coord"][0]=e.x


				for i in dm_vs:

					can.delete(i)
				draw_piece_("striker",1)



def can_b1_release(e):
	global drag_st,game_st
	global st
	global reset_st
	global pieces
	global dm_vs
	global force


	if st=="main":

		if reset_st==1:

			reset_st=0
			game_st=0
			pieces["striker"]["initial_v"]=0


			for i in dm_vs:

				can.delete(i)
			return




		drag_st=0



		if game_st==1:
			game_st=2
			pieces["striker"]["potted"]=0
			pieces["striker"]["start_time"]=time.time()
			pieces["striker"]["move st"]=1

def det_ang(a_1,a_2):

	a_1=int(a_1)
	a_2=int(a_2)

	_a1_=a_2
	_a2_=a_2


	acx=0

	for a in range(360):


		if _a1_==a_1:

			break


		_a1_-=1

		acx+=1

		if _a1_==-1:

			_a1_=359



	acy=0


	for a in range(360):




		if _a2_==a_1:

			break

		_a2_+=1

		acy+=1

		if _a2_==361:

			_a2_=1


	#print(acx,acy)

	if acx<=acy:
		return acx
	elif acy<acx:
		return acy




def collusions(pc):
	global pieces
	global striker_r,piece_r
	global first_move
	global ccc


	if pieces[pc]["current_v"]==0:
		return


	ar=[]

	for p_ in pieces:

		if p_ ==pc:
			continue


		x1,y1=pieces[pc]["coord"]
		x2,y2=pieces[p_]["coord"]

		r=math.sqrt((x1-x2)**2+(y1-y2)**2)

		ar.append([p_,r])

	ar=sorted(ar,key=lambda x:x[1])

	for i in ar:

		p_=i[0]

		if p_ ==pc:
			continue



		if pieces[pc]["current_v"]<pieces[p_]["current_v"]:
			continue


		if pieces[p_]["potted"]==1:
			continue


		if pc=="striker":
			r1=striker_r
		else:
			r1=piece_r




		if p_=="striker":
			r2=striker_r
		else:
			r2=piece_r

			


		x1,y1=pieces[pc]["coord"]
		x2,y2=pieces[p_]["coord"]

		



		r=math.sqrt((x1-x2)**2+(y1-y2)**2)

		if r<=r1+r2:


			if pc=="striker":
				first_move.append(p_)


			aa=angle(get_ang([x1,y1],[x2,y2])+180)

			a1=angle(pieces[pc]["angle"])

			_a1=angle(aa+90)
			_a2=angle(aa-90)

			ax=det_ang(angle(a1+180),_a1)
			ay=det_ang(angle(a1+180),_a2)

			#print(ax,ay)

			con=0
			if ax>ay:
				aa2=angle(_a1)
			elif ay>ax:
				aa2=angle(_a2)
			else:
				aa2=angle(aa+180)
				con=1



			if con==1:

				v_p_=pieces[pc]["current_v"]
				v_pc=0
			else:
				glancing_ang = abs((aa - pieces[pc]["angle"] + 180) % 360 - 180)

				#print(glancing_ang)

				#p_
				v_p_=pieces[pc]["current_v"]*math.cos(math.radians(glancing_ang))

				#pc

				v_pc=pieces[pc]["current_v"]*math.sin(math.radians(glancing_ang))



			"""

			if v_p_==0:
				pieces[pc]["move st"]=0

			else:
			"""

			pieces[p_]["proj_ang"]=aa
			pieces[p_]["start_time"]=time.time()
			pieces[p_]["initial_v"]=v_p_
			pieces[p_]["current_v"]=0
			pieces[p_]["st"]=0
			pieces[p_]["move st"]=1


			#print(pieces[pc]["initial_v"],pieces[pc]["current_v"])

			"""
			if v_pc==0:
				pieces[pc]["move st"]=0
			else:

			"""


			pieces[pc]["proj_ang"]=aa2
			pieces[pc]["start_time"]=time.time()
			pieces[pc]["initial_v"]=v_pc
			pieces[pc]["current_v"]=0
			pieces[pc]["st"]=0
			pieces[pc]["move st"]=1






			return 1

def get_ang(p1,p2):

	x1,y1=p1
	x2,y2=p2

	if x1>=x2:

		if y1<=y2:

			o=x1-x2
			a=y2-y1

			ang=math.degrees(math.atan(o/a))

			ang=180-ang


		else:


			o=x1-x2
			a=y1-y2


			ang=math.degrees(math.atan(o/a))



	else:


		if y1<=y2:

			o=x2-x1
			a=y2-y1

			ang=math.degrees(math.atan(o/a))

			ang=180+ang


		else:


			o=x2-x1
			a=y1-y2


			ang=math.degrees(math.atan(o/a))

			ang=360-ang

	return ang

def draw_move(e):
	global game_st,drag_st
	global pieces
	global dm_vs
	global boundary
	global st



	if st=="main":









		if drag_st==1:
			return

		if game_st==2:
			return

		try:

			cx,cy=pieces["striker"]["coord"]


			if e.x>=cx:

				if e.y>=cy:

					a=e.x-cx
					o=e.y-cy

					if a==0:
						a=0.00001
					ang=math.degrees(math.atan(o/a))

					ang=90-ang

				else:

					a=cy-e.y
					o=e.x-cx

					if a==0:
						a=0.00001

					ang=math.degrees(math.atan(o/a))

					ang=90-ang

					ang+=90


			else:



				if e.y>=cy:

					a=cx-e.x
					o=e.y-cy


					if a==0:
						a=0.00001

					ang=math.degrees(math.atan(o/a))

					ang+=270



				else:

					a=cx-e.x
					o=cy-e.y

					if a==0:
						a=0.00001



					ang=math.degrees(math.atan(o/a))

					ang=90-ang

					ang+=180






			def find_r(cx,cy,ang):
				global boundary
				global striker_r
				global dm_vs
				global can
				global dm_coord
				global pieces,striker_r,piece_r
				global dm_piece_mv
				global turn

				#collusions

				pieces_ar=[]
				ar2=[]

				for p in pieces:




					if p!="striker":

						if pieces[p]["potted"]==1:
							continue

						x,y=pieces[p]["coord"]
						r=math.sqrt((cx-x)**2+(cy-y)**2)

						pieces_ar.append([p,r])
						ar2.append(y)


				pieces_ar=sorted(pieces_ar,key=lambda x:x[1],reverse=False)



				con=0

				ar=[]

				

				for p in pieces_ar:

					x_,y_=pieces[p[0]]["coord"]

					r_=0

					for _ in range(600):



						x=r_*math.sin(math.radians(ang))+cx
						y=r_*math.cos(math.radians(ang))+cy


						r=math.sqrt((x-x_)**2+(y-y_)**2)



						if r<striker_r+piece_r:

							con=1

							a=angle(get_ang([x,y],[x_,y_])+180)


							ax=det_ang(angle(pieces["striker"]["angle"]+180),angle(a+90))
							ay=det_ang(angle(pieces["striker"]["angle"]+180),angle(a-90))




							#print(ax,ay)

							if ax>ay:
								aa2=angle(a+90)
							elif ay>ax:
								aa2=angle(a-90)
							else:
								aa2=angle(a+180)


							ar=[p[0],x,y,x_,y_,a,angle(aa2)]

							break

						r_+=1


					if con==1:
						break

				


				

				if con==1:

					a_=ar[-2]


					dm_coord=[cx,cy,ar[1],ar[2]]


					dm_piece_mv=[a_,ar[1],ar[2],ar[-1]]




					draw_move_()

					return



							







				#0,0

				r_=0

				for _ in range(600):



					x=r_*math.sin(math.radians(ang))+cx
					y=r_*math.cos(math.radians(ang))+cy



					x2=(r_+striker_r)*math.sin(math.radians(ang))+cx
					y2=(r_+striker_r)*math.cos(math.radians(ang))+cy
					

					if boundary[1][0]<=x2<=boundary[1][0]+boundary[0]:
						if boundary[1][1]<=y2<=boundary[1][1]+boundary[0]:


							r2=math.sqrt((x2-(boundary[1][0]+boundary[0]))**2+(y2-(boundary[1][1]+boundary[0]))**2)

							r2=int(round(r2,0))
							b=int(round(boundary[0],0))

							if r2>=boundary[0]:

								x=(r_-1)*math.sin(math.radians(ang))+cx
								y=(r_-1)*math.cos(math.radians(ang))+cy



								dm_coord=[cx,cy,x,y]
								draw_move_()

								return

					
					r_+=1


				#1,0







				r_=0

				for _ in range(600):



					x=r_*math.sin(math.radians(ang))+cx
					y=r_*math.cos(math.radians(ang))+cy

					x2=(r_+striker_r)*math.sin(math.radians(ang))+cx
					y2=(r_+striker_r)*math.cos(math.radians(ang))+cy

					

					if boundary[1][2]-boundary[0]<=x2<=boundary[1][2]:
						if boundary[1][1]<=y2<=boundary[1][1]+boundary[0]:


							r2=math.sqrt((x2-(boundary[1][2]-boundary[0]))**2+(y2-(boundary[1][1]+boundary[0]))**2)

							r2=int(round(r2,0))
							b=int(round(boundary[0],0))

							if r2>=boundary[0]:



								x=(r_-1)*math.sin(math.radians(ang))+cx
								y=(r_-1)*math.cos(math.radians(ang))+cy





								dm_coord=[cx,cy,x,y]
								draw_move_()

								return

					
					r_+=1



				#1,1







				r_=0

				for _ in range(600):



					x=r_*math.sin(math.radians(ang))+cx
					y=r_*math.cos(math.radians(ang))+cy

					x2=(r_+striker_r)*math.sin(math.radians(ang))+cx
					y2=(r_+striker_r)*math.cos(math.radians(ang))+cy


					

					if boundary[1][2]-boundary[0]<=x2<=boundary[1][2]:
						if boundary[1][3]-boundary[0]<=y2<=boundary[1][3]:


							r2=math.sqrt((x2-(boundary[1][2]-boundary[0]))**2+(y2-(boundary[1][3]-boundary[0]))**2)

							r2=int(round(r2,0))
							b=int(round(boundary[0],0))

							if r2>=boundary[0]:


								x=(r_-1)*math.sin(math.radians(ang))+cx
								y=(r_-1)*math.cos(math.radians(ang))+cy





								dm_coord=[cx,cy,x,y]
								draw_move_()

								return

					
					r_+=1




				#0,1







				r_=0

				for _ in range(600):



					x=r_*math.sin(math.radians(ang))+cx
					y=r_*math.cos(math.radians(ang))+cy

					x2=(r_+striker_r)*math.sin(math.radians(ang))+cx
					y2=(r_+striker_r)*math.cos(math.radians(ang))+cy

					

					if boundary[1][0]<=x2<=boundary[1][0]+boundary[0]:
						if boundary[1][3]-boundary[0]<=y2<=boundary[1][3]:


							r2=math.sqrt((x2-(boundary[1][0]+boundary[0]))**2+(y2-(boundary[1][3]-boundary[0]))**2)

							r2=int(round(r2,0))
							b=int(round(boundary[0],0))

							if r2>=boundary[0]:



								x=(r_-1)*math.sin(math.radians(ang))+cx
								y=(r_-1)*math.cos(math.radians(ang))+cy


								dm_coord=[cx,cy,x,y]
								draw_move_()

								return

					
					r_+=1



				#left

				r_=0

				for _ in range(600):



					x=r_*math.sin(math.radians(ang))+cx
					y=r_*math.cos(math.radians(ang))+cy

					x2=(striker_r+1)*math.sin(math.radians(270))+x
					y2=(striker_r+1)*math.cos(math.radians(270))+y



					if x2<=boundary[1][0]:

						if boundary[1][1]<=y2<=boundary[1][3]:




							dm_coord=[cx,cy,x,y]
							draw_move_()

							return

					r_+=1



				#right

				r_=0

				for _ in range(600):



					x=r_*math.sin(math.radians(ang))+cx
					y=r_*math.cos(math.radians(ang))+cy

					x2=(striker_r+1)*math.sin(math.radians(90))+x
					y2=(striker_r+1)*math.cos(math.radians(90))+y



					if x2>=boundary[1][2]:

						if boundary[1][1]<=y2<=boundary[1][3]:






							dm_coord=[cx,cy,x,y]
							draw_move_()

							return

					r_+=1



				#up

				r_=0

				for _ in range(600):



					x=r_*math.sin(math.radians(ang))+cx
					y=r_*math.cos(math.radians(ang))+cy


					x2=(striker_r+1)*math.sin(math.radians(180))+x
					y2=(striker_r+1)*math.cos(math.radians(180))+y


					if y2<=boundary[1][1]:

						if boundary[1][0]<=x2<=boundary[1][2]:






							dm_coord=[cx,cy,x,y]
							draw_move_()

							return

					r_+=1


				#down

				r_=0

				for _ in range(600):



					x=r_*math.sin(math.radians(ang))+cx
					y=r_*math.cos(math.radians(ang))+cy

					x2=(striker_r+1)*math.sin(math.radians(0))+x
					y2=(striker_r+1)*math.cos(math.radians(0))+y


					if y2>=boundary[1][3]:

						if boundary[1][0]<=x2<=boundary[1][2]:






							dm_coord=[cx,cy,x,y]
							draw_move_()

							return

					r_+=1


			find_r(cx,cy,ang)

			pieces["striker"]["angle"]=ang





			

		except Exception as e:
			print("draw_move()",e)


dm_coord=[0,0,0,0]
dm_vs=[0,0,0,0,0,0,0,0]
dm_piece_mv=[0,0,0]
def draw_move_(con=0):
	global can
	global striker_r
	global pieces
	global dm_vs,dm_coord
	global st
	global dm_piece_mv
	global quit_st,go_st
	global tcon
	global reset_st

	if st=="main":


		for i in dm_vs:

			can.delete(i)

		if tcon==1 or con==2:
			return



		if quit_st==1 or go_st==1:
			return


		if con==0:

			cx,cy,x,y=dm_coord

			rr=100

			dm_vs[0]=can.create_line(cx,cy, x,y,fill="#ff00ff",dash=(1, 3))
			


			im=Image.new("RGBA",(501,501),(0,0,0,0))

			draw=ImageDraw.Draw(im)

			draw.ellipse((0,0, 500,500),fill=(0,0,0,0),outline=(255,0,255,255),width=2)
			im=im.resize((int(rr*2),int(rr*2)))
			dm_vs[5]=ImageTk.PhotoImage(im)
			dm_vs[2]=can.create_image(cx,cy,image=dm_vs[5])


			im=Image.new("RGBA",(501,501),(0,0,0,0))

			draw=ImageDraw.Draw(im)

			draw.ellipse((0,0, 500,500),fill=(0,0,0,0),outline=(255,0,255,255),width=30)


			im=im.resize((int(round(striker_r*2,0)),int(round(striker_r*2,0))))
			#im.show()
			dm_vs[6]=ImageTk.PhotoImage(im)
			dm_vs[1]=can.create_image(x,y,image=dm_vs[6])



			im_=Image.new("RGBA",(201,201),(0,0,0,0))
			draw_=ImageDraw.Draw(im_)

			im=Image.new("RGBA",(501,501),(0,0,0,0))

			draw=ImageDraw.Draw(im)

			draw.ellipse((0,0, 500,500),fill=(255,0,255,80),outline=(255,0,255,80))



			if reset_st==1:
				sz=0
			else:
				sz=int(round(pieces["striker"]["initial_v"]*rr/5,0))


			
			


			if not sz==0:

				im=im.resize((sz*2,sz*2))


				im_.paste(im,(int(round(100-sz,0)),int(round(100-sz,0))))

				draw_.ellipse(( int(round(100-(striker_r+2),0)),int(round(100-(striker_r+2),0)), int(round(100+(striker_r+2)-1,0)),int(round(100+(striker_r+2)-1,0)) ),fill=(0,0,0,0),outline=(0,0,0,0))






				dm_vs[3]=ImageTk.PhotoImage(im_)

				dm_vs[4]=can.create_image(cx,cy,image=dm_vs[3])



			if not dm_piece_mv==[0,0,0,0]:



				x=100*math.sin(math.radians(dm_piece_mv[0]))+dm_piece_mv[1]
				y=100*math.cos(math.radians(dm_piece_mv[0]))+dm_piece_mv[2]


				x2=50*math.sin(math.radians(dm_piece_mv[-1]))+dm_piece_mv[1]
				y2=50*math.cos(math.radians(dm_piece_mv[-1]))+dm_piece_mv[2]


				dm_vs[4]=can.create_line(dm_piece_mv[1],dm_piece_mv[2], x,y,fill="#ff00ff")
				dm_vs[7]=can.create_line(dm_piece_mv[1],dm_piece_mv[2], x2,y2,fill="#ff00ff")

			dm_piece_mv=[0,0,0,0]





boundary_=0
def draw_boundary():
	global can,boundary_
	global r,coord

	can.delete(boundary_)




	ar=[]

	cx,cy=coord[0]+r,coord[1]+r

	a_=180
	for a in range(90):

		x=r*math.sin(math.radians(a_))+cx
		y=r*math.cos(math.radians(a_))+cy

		ar.append(round(x,0))
		ar.append(round(y,0))

		a_+=1


	cx,cy=coord[0]+r,coord[3]-r


	a_=270
	for a in range(90):

		x=r*math.sin(math.radians(a_))+cx
		y=r*math.cos(math.radians(a_))+cy

		ar.append(round(x,0))
		ar.append(round(y,0))
		
		a_+=1


	cx,cy=coord[2]-r,coord[3]-r
	a_=0
	for a in range(90):

		x=r*math.sin(math.radians(a_))+cx
		y=r*math.cos(math.radians(a_))+cy

		ar.append(round(x,0))
		ar.append(round(y,0))
		
		a_+=1


	cx,cy=coord[2]-r,coord[1]+r

	a_=90
	for a in range(90):

		x=r*math.sin(math.radians(a_))+cx
		y=r*math.cos(math.radians(a_))+cy

		ar.append(round(x,0))
		ar.append(round(y,0))
		
		a_+=1


	ar.append(ar[0])
	ar.append(ar[1])



	boundary_=can.create_line(ar,fill="#ff00ff")


"""
bnd_st=0



def up(e):
	global cx,cy
	global coord
	global bnd_st
	

	draw_piece(cx,cy-1,r)


	


	if bnd_st==0:

		coord[1]-=1

		draw_boundary()
	else:

		coord[1]+=1

		draw_boundary()



def down(e):
	global cx,cy
	global bnd_st
	draw_piece(cx,cy+1,r)


	


	if bnd_st==0:

		coord[3]+=1

		draw_boundary()
	else:

		coord[3]-=1

		draw_boundary()

	

def right(e):
	global cx,cy
	global bnd_st

	draw_piece(cx+1,cy,r)


	



	if bnd_st==0:

		coord[2]+=1

		draw_boundary()
	else:

		coord[2]-=1

		draw_boundary()

	
def left(e):
	global cx,cy
	global bnd_st

	draw_piece(cx-1,cy,r)


	


	if bnd_st==0:

		coord[0]-=1

		draw_boundary()
	else:

		coord[0]+=1

		draw_boundary()

	

def char(e):
	global r,cx,cy
	global bnd_st

	if e.char=="q":



		r+=1

		draw_piece(cx,cy,r)

		#draw_boundary()

	elif e.char=="a":

		if r-1<0:
			return

		r-=1

		draw_piece(cx,cy,r)

		#draw_boundary()

	elif e.char=="w":

		if bnd_st==1:
			bnd_st=0
		elif bnd_st==0:
			bnd_st=1
"""

reset_st=0
def can_b3(e):

	global r,cx,cy
	global coord

	global reset_st,pieces

	reset_st=1
	pieces["striker"]["initial_v"]=0

	draw_move_(2)


	#print(r,coord)
	#print(r,cx,cy)

def get_pos(pc,cx,cy,r_,ang,con_mv,con):
	global boundary

	ang=angle(ang)





	def check_if_potted(x,y):
		global boundary



		r2=math.sqrt((x-40)**2+(y-39)**2)

		if r2<=16:

			

			return 1


		r2=math.sqrt((x-446)**2+(y-39)**2)

		if r2<=16:

			

			return 1

		r2=math.sqrt((x-40)**2+(y-447)**2)

		if r2<=16:

			

			return 1

		r2=math.sqrt((x-446)**2+(y-447)**2)

		if r2<=16:

			

			return 1


		return 0
	



	





	#left
	if con==0:

		
		for _r_ in range(600):




			x=_r_*math.sin(math.radians(ang))+cx
			y=_r_*math.cos(math.radians(ang))+cy


			r=math.sqrt((x-(boundary[1][0]))**2+(y-y)**2)

			if r<=striker_r:
				if boundary[1][1]<=y<=boundary[1][3]:

					#print(5)
					if ang==270:
						_a_=90

					else:

						if cy<=y:

							o=cx-x
							a=y-cy


							if o<0:
								o=-o
							if a<0:
								a=-a


							if a==0:
								a=0.0001
								

							_a_=math.degrees(math.atan(o/a))

						else:

							o=cx-x
							a=cy-y


							if o<0:
								o=-o
							if a<0:
								a=-a


							if a==0:
								a=0.0001
								


							_a_=180-math.degrees(math.atan(o/a))





					#print(_a_)

					con_mv=[5,angle(_a_),_r_]

					break





	conx=0

	try:
		if con_mv[0]==5:

				conx=1
	except:
		pass
	if conx==1:



		x=r_*math.sin(math.radians(ang))+cx
		y=r_*math.cos(math.radians(ang))+cy


		if check_if_potted(x,y)==1:

			return 1



		r=math.sqrt((x-(boundary[1][0]))**2+(y-y)**2)


		if r_==con_mv[2]:
			if boundary[1][1]<=y<=boundary[1][3]:

				return 2

				#####



		return [x,y,r_+1,angle(ang),con_mv]


	

	#right
	if con==0:


		for _r_ in range(600):



			x=_r_*math.sin(math.radians(ang))+cx
			y=_r_*math.cos(math.radians(ang))+cy



			r=math.sqrt((x-(boundary[1][2]))**2+(y-y)**2)

			if r<=striker_r:

				if boundary[1][1]<=y<=boundary[1][3]:


					#print(6)



					if ang==90:

						_a_=270

					else:

						if cy<=y:					

							o=x-cx
							a=y-cy


							if o<0:
								o=-o
							if a<0:
								a=-a


							if a==0:
								a=0.0001
								
							_a_=360-math.degrees(math.atan(o/a))
						else:


							o=x-cx
							a=cy-y


							if o<0:
								o=-o
							if a<0:
								a=-a


							if a==0:
								a=0.0001

							_a_=180+math.degrees(math.atan(o/a))





					con_mv=[6,angle(_a_),_r_]

					break

	conx=0
	try:

		
		if con_mv[0]==6:

				conx=1
	except:
		pass

	if conx==1:


		x=r_*math.sin(math.radians(ang))+cx
		y=r_*math.cos(math.radians(ang))+cy



		if check_if_potted(x,y)==1:

			return 1


		#print(r_)


		r=math.sqrt((x-(boundary[1][2]))**2+(y-y)**2)

		if r_==con_mv[2]:

			if boundary[1][1]<=y<=boundary[1][3]:

				return 2

				#####


		return [x,y,r_+1,angle(ang),con_mv]




	#up
	if con==0:


		for _r_ in range(600):



			x=_r_*math.sin(math.radians(ang))+cx
			y=_r_*math.cos(math.radians(ang))+cy



			r=math.sqrt(((x-x)**2+(y-(boundary[1][1]))**2))


			if r<=striker_r:
				#print(_r_)
				if boundary[1][0]<=x<=boundary[1][2]:

					#print(7)

					if cx<=x:

						o=cy-y
						a=x-cx


						if o<0:
							o=-o
						if a<0:
							a=-a

						if a==0:
							a=0.0001

						_a_=90-math.degrees(math.atan(o/a))
					else:


						o=cy-y
						a=cx-x


						if o<0:
							o=-o
						if a<0:
							a=-a

						if a==0:
							a=0.0001

						_a_=270+math.degrees(math.atan(o/a))

					con_mv=[7,angle(_a_),_r_]

					break
	conx=0
	try:
		
		if con_mv[0]==7:

				conx=1
	except:
		pass
	if conx==1:


		x=r_*math.sin(math.radians(ang))+cx
		y=r_*math.cos(math.radians(ang))+cy


		if check_if_potted(x,y)==1:

			return 1



		if r_==con_mv[2]:
			if boundary[1][0]<=x<=boundary[1][2]:

				return 2

				#####


		return [x,y,r_+1,angle(ang),con_mv]




	#down
	if con==0:


		for _r_ in range(600):



			x=_r_*math.sin(math.radians(ang))+cx
			y=_r_*math.cos(math.radians(ang))+cy


			r=math.sqrt(((x-x)**2+(y-(boundary[1][3]))**2))


			if r<=striker_r:
				if boundary[1][0]<=x<=boundary[1][2]:

					#print(8,_r_)

					if cx<=x:

						o=y-cy
						a=x-cx

						if o<0:
							o=-o
						if a<0:
							a=-a

						if a==0:
							a=0.0001


						_a_=90+math.degrees(math.atan(o/a))

					else:

						o=y-cy
						a=cx-x

						if o<0:
							o=-o
						if a<0:
							a=-a


						if a==0:
							a=0.0001


						_a_=270-math.degrees(math.atan(o/a))



					con_mv=[8,angle(_a_),_r_]

					break


	conx=0

	try:
		if con_mv[0]==8:

				conx=1
	except:
		pass

	if conx==1:


		x=r_*math.sin(math.radians(ang))+cx
		y=r_*math.cos(math.radians(ang))+cy


		if check_if_potted(x,y)==1:

			return 1




		if r_==con_mv[2]:
			if boundary[1][0]<=x<=boundary[1][2]:

				return 2

				#####



		return [x,y,r_+1,angle(ang),con_mv]



def angle(a):

	try:

		a_=360


		if a>a_:
			a=a-a_
		elif a<0:
			a=a_+a
		elif a==a_:
			a=0

		return a

	except  Exception as e:
		print("angle()",e)
		return a


def move_pieces(p):

	global pieces
	global game_st,game_st2
	global st
	global turn

	

	if pieces[p]["potted"]==1:

		return 2
	

	if st=="main":


		if pieces[p]["move st"]==1 and game_st==2:

			collusions(p)

			

			if pieces[p]["st"]==0:

				

				try:

					#print(pieces[p]["proj_ang"])

					pieces[p]["coord_"]=pieces[p]["coord"]
					if pieces[p]["proj_ang"]!=None:
						pieces[p]["data"]=get_pos(p,pieces[p]["coord"][0],pieces[p]["coord"][1],0,angle(pieces[p]["proj_ang"]),0,0)

					else:

						pieces[p]["data"]=get_pos(p,pieces[p]["coord"][0],pieces[p]["coord"][1],0,angle(pieces[p]["angle"]),0,0)
					
					pieces[p]["proj_ang"]=None					
					pieces[p]["angle"]=angle(pieces[p]["data"][3])
					pieces[p]["coord"]=[pieces[p]["data"][0],pieces[p]["data"][1]]

					draw_piece_(p,1)

					pieces[p]["st"]=1

				except Exception as e:
					print(p," 1",e)
			elif pieces[p]["st"]==1:
				game_st2=1

				pieces[p]["data"]=get_pos(p,pieces[p]["coord_"][0],pieces[p]["coord_"][1],pieces[p]["data"][2],angle(pieces[p]["angle"]),pieces[p]["data"][4],1)
				

				if pieces[p]["data"]==1:

					if not p=="striker":

						moves.append(p)

					pieces[p]["start_time"]=0
					pieces[p]["potted"]=1
					pieces[p]["coord"]=[-100,100]
					pieces[p]["speed"]=0
					pieces[p]["initial_v"]=0
					pieces[p]["current_v"]=0

					pieces[p]["proj_ang"]=None
					pieces[p]["move st"]=0

					#game_st=0
					pieces[p]["move st"]=0
					pieces[p]["st"]=0
					pieces[p]["initial_v"]=0
					pieces[p]["angle"]=0

					




					draw_piece_(p ,1)		

					return 200


				elif pieces[p]["data"]==2:
					pieces[p]["st"]=0
					draw_piece_(p,1)	

					return 2


				else:

					pieces[p]["angle"]=angle(pieces[p]["data"][3])
					pieces[p]["coord"]=[pieces[p]["data"][0],pieces[p]["data"][1]]


					try:


						if len(pieces[p]["data"][4])==3:



							pieces[p]["proj_ang"]=angle(pieces[p]["data"][4][1])

					except Exception as e:
						print("move_striker() 2",e)

					draw_piece_(p ,1)


				pieces[p]["current_v"]=pieces[p]["initial_v"]-0.05*9.8*(time.time()-pieces[p]["start_time"])

				if pieces[p]["current_v"]<0:



					pieces[p]["start_time"]=0

					pieces[p]["speed"]=0
					pieces[p]["initial_v"]=0
					pieces[p]["current_v"]=0
					pieces[p]["move st"]=0



					pieces[p]["proj_ang"]=None

					pieces[p]["angle"]=0

					pieces[p]["st"]=0
					pieces[p]["move st"]=0					
					#game_st=0
					pieces[p]["st"]=0
					pieces[p]["initial_v"]=0

					


					draw_piece_(p ,1)		

					return 2
				else:

					#int(round(pieces[p]["initial_v"]-pieces[p]["current_v"],0))

					pieces[p]["speed"]=int(round((1-pieces[p]["current_v"]/5)*10,0))

					if pieces[p]["speed"]<1:
						pieces[p]["speed"]=1

				


					#print(pieces[p]["speed"])


				

				return pieces[p]["speed"]


			return 2


					




		else:
			pieces[p]["st"]=0
			return 2






		

	else:
		return 2


def move_striker():

	root.after(move_pieces("striker"),move_striker)





def move_1_w():
	root.after(move_pieces("1 white"),move_1_w)



def move_2_w():
	root.after(move_pieces("2 white"),move_2_w)





def move_3_w():
	root.after(move_pieces("3 white"),move_3_w)





def move_4_w():
	root.after(move_pieces("4 white"),move_4_w)





def move_5_w():
	root.after(move_pieces("5 white"),move_5_w)







def move_6_w():
	root.after(move_pieces("6 white"),move_6_w)





def move_7_w():
	root.after(move_pieces("7 white"),move_7_w)





def move_8_w():
	root.after(move_pieces("8 white"),move_8_w)


def move_9_w():
	root.after(move_pieces("9 white"),move_9_w)





def move_1_b():
    root.after(move_pieces("1 black"),move_1_b)





def move_2_b():
    root.after(move_pieces("2 black"),move_2_b)





def move_3_b():
    root.after(move_pieces("3 black"),move_3_b)



def move_4_b():
    root.after(move_pieces("4 black"),move_4_b)


def move_5_b():
    root.after(move_pieces("5 black"),move_5_b)




def move_6_b():
    root.after(move_pieces("6 black"),move_6_b)

def move_7_b():
    root.after(move_pieces("7 black"),move_7_b)


def move_8_b():
    root.after(move_pieces("8 black"),move_8_b)





def move_9_b():
    root.after(move_pieces("9 black"),move_9_b)




def move_red():
    root.after(move_pieces("red"),move_red)


_pieces_={}

def draw_piece_(p,con=0):
	global can
	global pieces,_pieces_
	global striker_im,red_im,white_im,black_im


	x,y=pieces[p]["coord"]

	def get_index(p):
		global pieces,_pieces_

		


		ar=[]

		for i in pieces:

			ar.append(i)


		try:

			v=ar.index(p)

			return _pieces_[p]

		except:

			c=100


			ar=[]

			for i in _pieces_:

				ar.append(_pieces_[i])

			if len(ar)>0:

				c=max(ar)+1

			return c





			




	if p=="striker":

		im=striker_im
	elif p=="red":
		im=red_im
	elif p.split(" ")[-1]=="white":
		im=white_im
	elif p.split(" ")[-1]=="black":
		im=black_im


	if con==0:

		
		_pieces_[p]=get_index(p)

		can.delete(_pieces_[p])



		pieces[p]["im"]=ImageTk.PhotoImage(im)

		_pieces_[p]=can.create_image(x,y,image=pieces[p]["im"],anchor="c")
	elif con==1:

		can.coords(_pieces_[p],x,y)

def draw_rounded_rect(x1,y1,x2,y2,r,col1,col2,op1,op2,width):

	w_=int(round((x2-x1)*4,0))
	h_=int(round((y2-y1)*4,0))

	im=Image.new("RGBA",(w_,h_),(0,0,0,0))
	draw=ImageDraw.Draw(im)

	r_=r*4


	ar=[]


	cx,cy=r_,r_

	a_=180

	for a in range(90):
		x=int(round(r_*math.sin(math.radians(a_))+cx,0))
		y=int(round(r_*math.cos(math.radians(a_))+cy,0))

		ar.append((x,y))

		a_+=1




	cx,cy=r_,h_-r_-1

	a_=270

	for a in range(90):
		x=int(round(r_*math.sin(math.radians(a_))+cx,0))
		y=int(round(r_*math.cos(math.radians(a_))+cy,0))

		ar.append((x,y))

		a_+=1





	cx,cy=w_-r_-1,h_-r_-1

	a_=0

	for a in range(90):
		x=int(round(r_*math.sin(math.radians(a_))+cx,0))
		y=int(round(r_*math.cos(math.radians(a_))+cy,0))

		ar.append((x,y))

		a_+=1



	cx,cy=w_-r_-1,r_

	a_=90

	for a in range(90):
		x=int(round(r_*math.sin(math.radians(a_))+cx,0))
		y=int(round(r_*math.cos(math.radians(a_))+cy,0))

		ar.append((x,y))

		a_+=1

	draw.polygon(ar,fill=(*col1,op1),outline=(*col2,op2),width=int(width*4))

	im=im.resize((int(x2-x1),int(y2-y1)))

	return im

moves=[]
_red_,_red2_=None,None
def validate_moves():
	global pieces
	global moves
	global game
	global game_st
	global turn
	global striker_r,piece_r
	global first_move
	global moves_
	global _red_,_red2_


	def reposition(p):

		def check_pos(x,y):
			global pieces,striker_r,piece_r

			con=0

			for i in pieces:

				if i=="striker":
					r=striker_r
				else:
					r=piece_r

				x2,y2=pieces[i]["coord"]

				r_=math.sqrt((x-x2)**2+(y-y2)**2)

				if r_<r+piece_r:

					con=1
					break

			if con==0:
				return [x,y]
			else:
				return -1

		cx,cy=243,243

		v=check_pos(cx,cy)


		if not v==-1:
			return v


		a=360/6
		a_=180

		r=piece_r*2+4

		for _ in range(6):

			x=r*math.sin(math.radians(a_))+cx
			y=r*math.cos(math.radians(a_))+cy


			v=check_pos(x,y)

			if not v==-1:
				return v

			a_-=a



		a=360/12
		a_=180

		r=piece_r*4+8

		for _ in range(6):

			x=r*math.sin(math.radians(a_))+cx
			y=r*math.cos(math.radians(a_))+cy


			v=check_pos(x,y)

			if not v==-1:
				return v

			a_-=a



		a=360/24
		a_=180

		r=piece_r*6+12

		for _ in range(6):

			x=r*math.sin(math.radians(a_))+cx
			y=r*math.cos(math.radians(a_))+cy


			v=check_pos(x,y)

			if not v==-1:
				return v

			a_-=a


	def cancel_0():

		global game
		global pieces
		global _red2_,_red_
		global moves,moves_


		con=1


		if game=="Carrom":





			if pieces["red"]["potted"]==1 and _red_==None and _red2_==0:




				try:

					v=moves_[-2].index("red")




					_red_=None
					_red2_=None
					pieces["red"]["coord"]=reposition("red")
					pieces["red"]["potted"]=0

					draw_piece_("red",1)									

				except:
					pass










		for i in moves:

			if i.split(" ")[-1]=="black":


				pieces[i]["coord"]=reposition(i)
				pieces[i]["potted"]=0

				#print(pieces[i]["coord"])

				draw_piece_(i,1)


		if game=="Carrom":

			try:
				v=moves.index("red")
				_red_,_red2_=None,None

				pieces["red"]["coord"]=reposition("red")
				pieces["red"]["potted"]=0

				draw_piece_("red",1)
			except:
				pass

		return 1


	def cancel_1():
		global game
		global pieces
		global _red2_,_red_
		global moves,moves_


		con=1




		if game=="Carrom":




			if pieces["red"]["potted"]==1 and _red_==None and _red2_==1:




				try:

					v=moves_[-2].index("red")

					_red_=None
					_red2_=None
					pieces["red"]["coord"]=reposition("red")
					pieces["red"]["potted"]=0

					draw_piece_("red",1)									

				except:
					pass







		for i in moves:

			if i.split(" ")[-1]=="white":


				pieces[i]["coord"]=reposition(i)
				pieces[i]["potted"]=0

				#print(pieces[i]["coord"])

				draw_piece_(i,1)

		if game=="Carrom":

			try:

				v=moves.index("red")

				_red_,_red2_=None,None

				pieces["red"]["coord"]=reposition("red")
				pieces["red"]["potted"]=0

				draw_piece_("red",1)
			except:
				pass

		return 1



	#####

	if turn==1:

		if pieces["striker"]["potted"]==1:
			con=cancel_1()



		elif len(first_move)>0:

			if first_move[0].split(" ")[-1]=="white" or first_move[0]=="red":

				if len(moves)>0:
					
					if moves[0].split(" ")[-1]=="white" or moves[0]=="red":

						con=0


						if game=="Carrom":
							if _red_==None:

								try:
									v=moves.index("red")



									_red2_=1
									con_=0
									for m in moves:

										if m.split(" ")[-1]=="white":
											con_=1

									if con_==1:
										_red_=1




									return con




								except:
									pass


							if _red_==None:



								if pieces["red"]["potted"]==1:

									try:

										v=moves_[-2].index("red")



										if _red2_==1:


											con_=0

											for m in moves:

												if m.split(" ")[-1]=="white":

													
													con_=1

											if con_==1:
												_red_=1

									except:
										pass





					else:
						con=cancel_1()
				else:

					con=cancel_1()
			else:

				con=cancel_1()
		else:
			con=cancel_1()
	elif turn==0:


		if pieces["striker"]["potted"]==1:
			con=cancel_0()


		elif len(first_move)>0:
			if first_move[0].split(" ")[-1]=="black" or first_move[0]=="red":

				if len(moves)>0:

					if moves[0].split(" ")[-1]=="black" or moves[0]=="red":

						con=0


						if game=="Carrom":
							if _red_==None:

								try:
									v=moves.index("red")



									_red2_=0
									con_=0
									for m in moves:

										if m.split(" ")[-1]=="black":
											con_=1

									if con_==1:
										_red_=0




									return con




								except:
									pass


							if _red_==None:



								if pieces["red"]["potted"]==1:

									try:

										v=moves_[-2].index("red")


										if _red2_==0:


											con_=0

											for m in moves:

												if m.split(" ")[-1]=="black":

													
													con_=1

											if con_==1:
												_red_=0

									except:
										pass





					else:
						con=cancel_0()
				else:
					con=cancel_0()
			else:

				con=cancel_0()
		else:
			con=cancel_0()


	return con



	#print(moves)


game_st2=0

go_im=0
go_st=0
go_coord=[]
go_i=[0,0,0,0,0,0,0,0]

def go(winner):
	global go_st,go_im,go_coord,go_st
	global bg2
	global white_im_,black_im_

	go_st=1

	draw_move_()

	go_i[6]=can.create_image(0,0,image=bg2,anchor="nw")

	xx,yy=250,100

	x=(w-xx)/2
	y=(h-yy)/2


	im=draw_rounded_rect(x,y,x+xx,y+yy,15,(0,0,0),((255,0,255)),140,255,1)
	go_im=ImageTk.PhotoImage(im)

	go_i[0]=can.create_image(x,y,image=go_im,anchor="nw")

	txt=f"{winner} wins!"

	f=font.Font(family="FreeMono",size=13)

	x_=x+xx/2-f.measure(txt)/2-15

	if winner=="White":

		go_i[7]=can.create_image(x_,y+20,image=white_im_,anchor="c")
	elif winner=="Black":
		go_i[7]=can.create_image(x_,y+20,image=black_im_,anchor="c")



	go_i[1]=can.create_text(x+xx/2,y+20, text=f"{winner} wins!", font=("FreeMono",13),fill="#ff00ff")

	go_i[2]=can.create_line(x+1,y+yy-30, x+xx-1,y+yy-30,fill="#770077")

	go_i[3]=can.create_line(x+xx/2,y+yy-30, x+xx/2,y+yy-1,fill="#770077")

	go_i[4]=can.create_text(x+xx/4,y+yy-15,text="Main Menu",font=("FreeMono",13),fill="#ff00ff")

	go_i[5]=can.create_text(x+xx-xx/4,y+yy-15,text="Quit",font=("FreeMono",13),fill="#ff00ff")

	go_coord=[x,y+yy-30, x+xx,y+yy]

moves_=[]
first_move=[]
def check_game():

	global can
	global pieces,game_st,turn,xrng,yv2,striker_r
	global game_st,game_st2
	global force
	global pwhite,pwred,pblack,pbred
	global moves,moves_
	global first_move
	global turn
	global _red2_

	if game_st2==1:

		

		w,b,r=0,0,None
		for p in pieces:

			if p!="striker":

				if pieces[p]["potted"]==1:

					if p.split(" ")[-1]=="white":
						w+=1
					elif p.split(" ")[-1]=="black":
						b+=1

		can.itemconfig(pwhite,text=str(w))
		can.itemconfig(pblack,text=str(b))



		#print(_red2_)
		if pieces["red"]["potted"]==1:



			if _red2_==None:
				can.itemconfig(pwred,text=str(0))
				can.itemconfig(pbred,text=str(0))

			elif _red2_==1:
				can.itemconfig(pwred,text=str(1))
			elif _red2_==0:
				can.itemconfig(pbred,text=str(1))

		#print(pieces["red"]["potted"])



		con=0
		for p in pieces:

			if pieces[p]["initial_v"]!=0:
				con=1
				break


		if con==0:


			con_=1


			moves_.append(moves)

			#print(moves_)


			#if len(moves)>0:
			con_=validate_moves()



			w,b=0,0
			for p in pieces:

				if p!="striker":

					if pieces[p]["potted"]==1:

						if p.split(" ")[-1]=="white":
							w+=1
						elif p.split(" ")[-1]=="black":
							b+=1

			can.itemconfig(pwhite,text=str(w))
			can.itemconfig(pblack,text=str(b))



			if pieces["red"]["potted"]==1:

				if _red2_==None:
					can.itemconfig(pwred,text=str(0))
					can.itemconfig(pbred,text=str(0))

				elif _red2_==1:
					can.itemconfig(pwred,text=str(1))
				elif _red2_==0:
					can.itemconfig(pbred,text=str(1))
			else:

				can.itemconfig(pwred,text=str(0))
				can.itemconfig(pbred,text=str(0))



			pieces["striker"]["potted"]=0

			moves=[]
			first_move=[]
			game_st=0

			game_st2=0
			force=0
			

			if con_==1:


				if turn==0:
					turn=1
					pieces["striker"]["coord"]=[xrng[0]+(xrng[1]-xrng[0])/2,yv2]
				elif turn==1:
					turn=0				
					pieces["striker"]["coord"]=[xrng[0]+(xrng[1]-xrng[0])/2,yv1]

				draw_piece_("striker",1)	

			else:


				if turn==0:
					pieces["striker"]["coord"]=[xrng[0]+(xrng[1]-xrng[0])/2,yv1]
					
				elif turn==1:
					pieces["striker"]["coord"]=[xrng[0]+(xrng[1]-xrng[0])/2,yv2]

				draw_piece_("striker",1)



			#check if game is finished



			w,b=0,0
			for p in pieces:

				if p!="striker":

					if pieces[p]["potted"]==1:

						if p=="red":
							pass
						elif p.split(" ")[-1]=="white":
							w+=1
						elif p.split(" ")[-1]=="black":
							b+=1



			if w==9:

				winner="White"
				if game=="Carrom":

					if pieces["red"]["potted"]==0:
						winner="Black"

				go(winner)

			elif b==9:

				winner="Black"

				if game=="Carrom":

					if pieces["red"]["potted"]==0:
						winner="White"

				go(winner)


				

			






	root.after(2,check_game)


pieces={"striker":{"coord":[0,0],
					"coord_":[0,0],
					"angle":0,
					"proj_ang":None,
					"st":0,
					"data":[],
					"initial_v":0,
					"current_v":0,
					"start_time":0,
					"speed":0,
					"move st":0,
					"im":0,
					"potted":0,

					},


	"1 white":{"coord":[243.0,220.0],
						"coord_":[0,0],
						"angle":0,
						"proj_ang":None,
						"st":0,
						"data":[],
						"initial_v":0,
						"current_v":0,
						"start_time":0,
						"speed":0,
						"potted":0,
						"move st":0,
						"im":0,
						},


	"2 white":{"coord":[253.39230484541326,237.0],
						"coord_":[0,0],
						"angle":0,
						"proj_ang":None,
						"st":0,
						"data":[],
						"initial_v":0,
						"current_v":0,
						"start_time":0,
						"speed":0,
						"potted":0,
						"move st":0,
						"im":0,
						},



	"3 white":{"coord":[262.9185842870421,231.50000000000003],
						"coord_":[0,0],
						"angle":0,
						"proj_ang":None,
						"st":0,
						"data":[],
						"initial_v":0,
						"current_v":0,
						"start_time":0,
						"speed":0,
						"potted":0,
						"move st":0,
						"im":0,
						},

	"4 white":{"coord":[262.9185842870421,254.5],
						"coord_":[0,0],
						"angle":0,
						"proj_ang":None,
						"st":0,
						"data":[],
						"initial_v":0,
						"current_v":0,
						"start_time":0,
						"speed":0,
						"potted":0,
						"move st":0,
						"im":0,
						},


	"5 white":{"coord":[243.0,255.0],
						"coord_":[0,0],
						"angle":0,
						"proj_ang":None,
						"st":0,
						"data":[],
						"initial_v":0,
						"current_v":0,
						"start_time":0,
						"speed":0,
						"potted":0,
						"move st":0,
						"im":0,
						},

	"6 white":{"coord":[243.0,266.0],
						"coord_":[0,0],
						"angle":0,
						"proj_ang":None,
						"st":0,
						"data":[],
						"initial_v":0,
						"current_v":0,
						"start_time":0,
						"speed":0,
						"potted":0,
						"move st":0,
						"im":0,
						},

	"7 white":{"coord":[223.08141571295792,254.5],
						"coord_":[0,0],
						"angle":0,
						"proj_ang":None,
						"st":0,
						"data":[],
						"initial_v":0,
						"current_v":0,
						"start_time":0,
						"speed":0,
						"potted":0,
						"move st":0,
						"im":0,
						},


	"8 white":{"coord":[223.08141571295792,231.5],
						"coord_":[0,0],
						"angle":0,
						"proj_ang":None,
						"st":0,
						"data":[],
						"initial_v":0,
						"current_v":0,
						"start_time":0,
						"speed":0,
						"potted":0,
						"move st":0,
						"im":0,
						},

	"9 white":{"coord":[232.60769515458674,237.0],
						"coord_":[0,0],
						"angle":0,
						"proj_ang":None,
						"st":0,
						"data":[],
						"initial_v":0,
						"current_v":0,
						"start_time":0,
						"speed":0,
						"potted":0,
						"move st":0,
						"im":0,
						},

	"1 black":{"coord":[243.0,231.0],
						"coord_":[0,0],
						"angle":0,
						"proj_ang":None,
						"st":0,
						"data":[],
						"initial_v":0,
						"current_v":0,
						"start_time":0,
						"speed":0,
						"potted":0,
						"move st":0,
						"im":0,
						},

	"2 black":{"coord":[254.5,223.0814157129579],
						"coord_":[0,0],
						"angle":0,
						"proj_ang":None,
						"st":0,
						"data":[],
						"initial_v":0,
						"current_v":0,
						"start_time":0,
						"speed":0,
						"potted":0,
						"move st":0,
						"im":0,
						},


	"3 black":{"coord":[253.39230484541326,249.0],
						"coord_":[0,0],
						"angle":0,
						"proj_ang":None,
						"st":0,
						"data":[],
						"initial_v":0,
						"current_v":0,
						"start_time":0,
						"speed":0,
						"potted":0,
						"move st":0,
						"im":0,
						},

	"4 black":{"coord":[266.0,243.0],
						"coord_":[0,0],
						"angle":0,
						"proj_ang":None,
						"st":0,
						"data":[],
						"initial_v":0,
						"current_v":0,
						"start_time":0,
						"speed":0,
						"potted":0,
						"move st":0,
						"im":0,
						},


	"5 black":{"coord":[254.5,262.9185842870421],
						"coord_":[0,0],
						"angle":0,
						"proj_ang":None,
						"st":0,
						"data":[],
						"initial_v":0,
						"current_v":0,
						"start_time":0,
						"speed":0,
						"potted":0,
						"move st":0,
						"im":0,
						},

	"6 black":{"coord":[231.5,262.9185842870421],
						"coord_":[0,0],
						"angle":0,
						"proj_ang":None,
						"st":0,
						"data":[],
						"initial_v":0,
						"current_v":0,
						"start_time":0,
						"speed":0,
						"potted":0,
						"move st":0,
						"im":0,
						},

	"7 black":{"coord":[232.60769515458674,249.0],
						"coord_":[0,0],
						"angle":0,
						"proj_ang":None,
						"st":0,
						"data":[],
						"initial_v":0,
						"current_v":0,
						"start_time":0,
						"speed":0,
						"potted":0,
						"move st":0,
						"im":0,
						},


	"8 black":{"coord":[220.0,243.0],
						"coord_":[0,0],
						"angle":0,
						"proj_ang":None,
						"st":0,
						"data":[],
						"initial_v":0,
						"current_v":0,
						"start_time":0,
						"speed":0,
						"potted":0,
						"move st":0,
						"im":0,
						},

	"9 black":{"coord":[231.5,223.08141571295792],
						"coord_":[0,0],
						"angle":0,
						"proj_ang":None,
						"st":0,
						"data":[],
						"initial_v":0,
						"current_v":0,
						"start_time":0,
						"speed":0,
						"potted":0,
						"move st":0,
						"im":0,
						},


	"red":{"coord":[243,243],
						"coord_":[0,0],
						"angle":0,
						"proj_ang":None,
						"st":0,
						"data":[],
						"initial_v":0,
						"current_v":0,
						"start_time":0,
						"speed":0,
						"potted":0,
						"move st":0,
						"im":0,
						},

		}





w,h=500,500
root=tk.Tk()
root.geometry(f"{w}x{h}+{int((root.winfo_screenwidth()-w)/2)}+{50}")
root.resizable(0,0)
root.title("HCarrom")
root.iconbitmap("data/icon.ico")

def esc(e):
	global quit_st,quit_im,quit_i,quit_coord
	global bg2
	global st

	if st=="main":

		if quit_st==1:
			return




		quit_st=1

		draw_move_()

		quit_i[6]=can.create_image(0,0,image=bg2,anchor="nw")

		xx,yy=250,100

		x=(w-xx)/2
		y=(h-yy)/2


		im=draw_rounded_rect(x,y,x+xx,y+yy,15,(0,0,0),((255,0,255)),140,255,1)
		quit_im=ImageTk.PhotoImage(im)

		quit_i[0]=can.create_image(x,y,image=quit_im,anchor="nw")

		quit_i[1]=can.create_text(x+xx/2,y+20, text="Quit Game?", font=("FreeMono",13),fill="#ff00ff")

		quit_i[2]=can.create_line(x+1,y+yy-30, x+xx-1,y+yy-30,fill="#770077")

		quit_i[3]=can.create_line(x+xx/2,y+yy-30, x+xx/2,y+yy-1,fill="#770077")

		quit_i[4]=can.create_text(x+xx/4,y+yy-15,text="Yes",font=("FreeMono",13),fill="#ff00ff")

		quit_i[5]=can.create_text(x+xx-xx/4,y+yy-15,text="No",font=("FreeMono",13),fill="#ff00ff")

		quit_coord=[x,y+yy-30, x+xx,y+yy]


can=tk.Canvas(width=w,height=h,bg="#000000",relief="flat",highlightthickness=0,border=0)
can.place(in_=root,x=0,y=0)

can.bind("<Button-1>",can_b1)
can.bind("<B1-Motion>",drag)
can.bind("<ButtonRelease-1>",can_b1_release)
can.bind("<Motion>",draw_move)
#can.bind("<Up>",up)
#can.bind("<Down>",down)
#can.bind("<Right>",right)
#can.bind("<Left>",left)
#can.bind("<KeyPress>",char)
can.bind("<Button-3>",can_b3)
can.bind("<Escape>",esc)

can.focus_set()


#500- 7,5
striker_r=7*w/500
piece_r=5*w/500


turn=1

yv1,yv2=82,404

xrng=(102*w/500,383*w/500)


if turn==0:
	pieces["striker"]["coord"]=[xrng[0]+(xrng[1]-xrng[0])/2,yv1]
elif turn==1:
	pieces["striker"]["coord"]=[xrng[0]+(xrng[1]-xrng[0])/2,yv2]

#coord=[w/2-100,h/2-100, w/2+100,h/2+100]

boundary=[22,[22*w/500,21*w/500,463*w/500,464*w/500]]

coord=boundary[1]

r=22

max_v0=20 # N
pieces["striker"]["initial_v"]=0

load_im()

root.geometry(f"{w}x{h}+{int((root.winfo_screenwidth()-w)/2)}+{50}")
#main()
intro()
#draw_boundary()

force_()

move_striker()


move_1_w()
move_2_w()
move_3_w()
move_4_w()
move_5_w()
move_6_w()
move_7_w()
move_8_w()
move_9_w()



move_1_b()
move_2_b()
move_3_b()
move_4_b()
move_5_b()
move_6_b()
move_7_b()
move_8_b()
move_9_b()

move_red()

draw_turn()


def update():

	root.after(1,update)
update()

check_game()
root.mainloop()

