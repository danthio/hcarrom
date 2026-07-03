from PIL import Image,ImageTk,ImageDraw
import tkinter as tk
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
def load_im():
	global w,h
	global bg,bg2,circle
	global striker_im,black_im,white_im,red_im
	global striker_r,piece_r
	global quit,home
	global signature

	#striker_im


	im=Image.new("RGBA",(500,500),(0,0,0,0))
	draw=ImageDraw.Draw(im)

	draw.ellipse((16,16,500-16-1,500-16-1),fill=(255,255,0,255),outline=(0,0,0,255),width=32)

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

	bg=ImageTk.PhotoImage(im) 


	#darker layer
	im=Image.new("RGBA",(w,h+30),(0,0,0,200))
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
	root.geometry(f"{w}x{h}+{int((root.winfo_screenwidth()-w)/2)}+{50}")

	pos_intro2=[]

	st="intro2"

	can.delete("all")

	can.create_image(0,0,image=bg,anchor="nw")

	can.create_image(347,441,image=signature,anchor="c")
	can.create_image(0,0,image=bg2,anchor="nw")


	can.create_image(3,3,image=home,anchor="nw")

	x=200

	y=(h-90)/2

	im=draw_rounded_rect(w/2-x/2,y,w/2+x/2,y+30,15,(255,0,0),(255,0,0),255,255,1)
	intro2_im1=ImageTk.PhotoImage(im)

	can.create_image(w/2-x/2,y,image=intro2_im1,anchor="nw")

	can.create_text(w/2,y+15,text="2 Player",font=("FreeMono",13),fill="#000000",anchor="c")

	pos_intro2.append([w/2-x/2+15,y, w/2+x/2-15,y+30-1])


	y+=60


	im=draw_rounded_rect(w/2-x/2,y,w/2+x/2,y+30,15,(255,0,0),(255,0,0),255,255,1)
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

	can["height"]=h
	root.geometry(f"{w}x{h}+{int((root.winfo_screenwidth()-w)/2)}+{50}")
	pos_intro=[]

	st="intro"

	can.delete("all")

	can.create_image(0,0,image=bg,anchor="nw")

	can.create_image(347,441,image=signature,anchor="c")

	can.create_image(0,0,image=bg2,anchor="nw")

	x=200

	y=(h-90)/2

	im=draw_rounded_rect(w/2-x/2,y,w/2+x/2,y+30,15,(255,0,0),(255,0,0),255,255,1)
	intro_im1=ImageTk.PhotoImage(im)

	can.create_image(w/2-x/2,y,image=intro_im1,anchor="nw")

	can.create_text(w/2,y+15,text="Carrom",font=("FreeMono",13),fill="#000000",anchor="c")

	pos_intro.append([w/2-x/2+15,y, w/2+x/2-15,y+30-1])


	y+=60


	im=draw_rounded_rect(w/2-x/2,y,w/2+x/2,y+30,15,(255,0,0),(255,0,0),255,255,1)
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
arp0,arp1=[],[]
def draw_turn():
	global can,turn,turn0,turn1,turnx,turnv
	global pwhite,pwred,pblack,pbred
	global game_st,st
	global arp0,arp1
	global w,h

	try:
		
		if st=="main":	

			val=int(round(w/2-100+15,0))

			if turnx!=turn:

				turnx=turn
				turnv=0
				arp0=can.coords(turn0)
				arp1=can.coords(turn1)

			if turnv!=val:


				turnv+=1


				if turn==0:




					ar=[]
					con=0
					for v in arp0:

						if con==0:

							x=v-turnv
							ar.append(x)
						else:
							ar.append(v)


						if con==0:
							con=1
						elif con==1:
							con=0

					can.coords(turn0,ar)




					ar=[]
					con=0
					for v in arp1:

						if con==0:

							x=v-turnv
							ar.append(x)
						else:
							ar.append(v)


						if con==0:
							con=1
						elif con==1:
							con=0


					can.coords(turn1,ar)

					can.itemconfig(pwhite,fill="#ffffff")
					can.itemconfig(pwred,fill="#ffffff")
					can.itemconfig(pblack,fill="#000000")
					can.itemconfig(pbred,fill="#000000")




				elif turn==1:




					ar=[]
					con=0
					for v in arp0:

						if con==0:

							x=v+turnv
							ar.append(x)
						else:
							ar.append(v)


						if con==0:
							con=1
						elif con==1:
							con=0

					can.coords(turn0,ar)




					ar=[]
					con=0
					for v in arp1:

						if con==0:

							x=v+turnv
							ar.append(x)
						else:
							ar.append(v)


						if con==0:
							con=1
						elif con==1:
							con=0


					can.coords(turn1,ar)



					can.itemconfig(pwhite,fill="#000000")
					can.itemconfig(pwred,fill="#000000")
					can.itemconfig(pblack,fill="#ffffff")
					can.itemconfig(pbred,fill="#ffffff")



	except Exception as e:
		print(e)

	root.after(6,draw_turn)


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
	global turn,turn0,turn1,turnx,turnv,arp0,arp1
	global signature

	turn=1
	turnx=1
	turnv=0
	arp0,arp1=[],[]


	moves,moves_,_red_,_red2_=[],[],None,None


	can["height"]=h+30
	root.geometry(f"{w}x{h+30}+{int((root.winfo_screenwidth()-w)/2)}+{50}")

	st="main"

	can.delete("all")


	can.create_image(0,0,image=bg,anchor="nw")

	can.create_image(347,441,image=signature,anchor="c")

	can.create_image(w-3-25,3,image=quit,anchor="nw")



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

	turn1=can.create_polygon(0,h, w/2-100,h, w/2-100+15,h+30, 0,h+30, fill="#00ff00",outline="#00ff00")

	xx=w-(w/2+100-15)
	turn0=can.create_polygon(w/2+100+xx,h, w+xx,h, w+xx,h+30, w/2+100-15+xx,h+30,  fill="#00ff00",outline="#00ff00")

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


	#can.create_polygon(w/2-100,h, w/2+100,h, w/2+100-15,h+30, w/2-100+15,h+30,fill="#ff0000",outline="#ff0000")

	can.create_text(w/2,h+15,text=game, font=("FreeMono",13),fill="#ff0000")




p=0
#r=30
cx,cy=0,0
def draw_piece(x,y,r):
	global p
	global cx,cy

	cx,cy=x,y

	can.delete(p)

	p=can.create_oval(x-r,y-r, x+r,y+r,fill="#000000",outline="#ff0000")


def force_():

	global pieces
	global game_st
	global st

	if st=="main":

		if game_st==1:

			if not pieces["striker"]["initial_v"]+0.3>3:

				pieces["striker"]["initial_v"]+=0.3


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


	print(e.x,e.y)


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

		if 3<=e.x<=25+3:
				if 3<=e.y<=25+3:

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


		if w-3-25<=e.x<=w-3:
			if 3<=e.y<=3+25:

				quit_st=1

				draw_move_()

				quit_i[6]=can.create_image(0,0,image=bg2,anchor="nw")

				xx,yy=250,100

				x=(w-xx)/2
				y=(h-yy)/2


				im=draw_rounded_rect(x,y,x+xx,y+yy,15,(0,0,0),(255,0,0),180,255,1)
				quit_im=ImageTk.PhotoImage(im)

				quit_i[0]=can.create_image(x,y,image=quit_im,anchor="nw")

				quit_i[1]=can.create_text(x+xx/2,y+20, text="Quit Game?", font=("FreeMono",13),fill="#ff0000")

				quit_i[2]=can.create_line(x+1,y+yy-30, x+xx-1,y+yy-30,fill="#770000")

				quit_i[3]=can.create_line(x+xx/2,y+yy-30, x+xx/2,y+yy-1,fill="#770000")

				quit_i[4]=can.create_text(x+xx/4,y+yy-15,text="Yes",font=("FreeMono",13),fill="#ff0000")

				quit_i[5]=can.create_text(x+xx-xx/4,y+yy-15,text="No",font=("FreeMono",13),fill="#ff0000")

				quit_coord=[x,y+yy-30, x+xx,y+yy]

				return






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

			if r<=striker_r:
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




		if pieces[p_]["potted"]==1:
			continue


		if pieces[pc]["current_v"]<pieces[p_]["current_v"]:
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

				








			if pieces[p_]["move st"]==0:
				pieces[p_]["move st"]=1

				pieces[p_]["angle"]=aa
				pieces[p_]["initial_v"]=pieces[pc]["current_v"]
				pieces[p_]["current_v"]=0
				pieces[p_]["start_time"]=time.time()
			else:
				pieces[p_]["proj_ang"]=aa
				pieces[p_]["st"]=0
				pieces[p_]["initial_v"]=pieces[pc]["current_v"]
				pieces[p_]["current_v"]=0
				pieces[p_]["start_time"]=time.time()



			a1=pieces[pc]["angle"]


			x1,y1=pieces[pc]["coord"]
			x2,y2=pieces[p_]["coord"]

			a2=get_ang([x2,y2],[x1,y1])


			a3=a1+180



			a1=angle(a1)
			a2=angle(a2)
			a3=angle(a3)

			#print(a2,a1)

			_a1=angle(aa+90)
			_a2=angle(aa-90)




			ax=det_ang(angle(a1+180),_a1)
			ay=det_ang(angle(a1+180),_a2)




			#print(ax,ay)

			if ax>ay:
				aa2=_a1
			elif ay>ax:
				aa2=_a2
			else:
				aa2=aa+180
			aa2=angle(aa2)





			pieces[pc]["proj_ang"]=aa2
			pieces[pc]["angle"]=aa2
			pieces[pc]["st"]=0
			pieces[pc]["start_time"]=time.time()
			pieces[pc]["initial_v"]=pieces[pc]["current_v"]
			pieces[pc]["current_v"]=0
			#pieces[pc]["move st"]=1

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

							if r2>boundary[0]:





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

							if r2>boundary[0]:






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

							if r2>boundary[0]:






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

							if r2>boundary[0]:




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

	if st=="main":


		for i in dm_vs:

			can.delete(i)

		if quit_st==1 or go_st==1:
			return


		if con==0:

			cx,cy,x,y=dm_coord

			rr=100

			dm_vs[0]=can.create_line(cx,cy, x,y,fill="#ff0000")
			


			im=Image.new("RGBA",(501,501),(0,0,0,0))

			draw=ImageDraw.Draw(im)

			draw.ellipse((0,0, 500,500),fill=(0,0,0,0),outline=(255,0,0,255),width=2)
			im=im.resize((int(rr*2),int(rr*2)))
			dm_vs[5]=ImageTk.PhotoImage(im)
			dm_vs[2]=can.create_image(cx,cy,image=dm_vs[5])


			im=Image.new("RGBA",(501,501),(0,0,0,0))

			draw=ImageDraw.Draw(im)

			draw.ellipse((0,0, 500,500),fill=(0,0,0,0),outline=(255,0,0,255),width=30)


			im=im.resize((int(round(striker_r*2,0)),int(round(striker_r*2,0))))
			#im.show()
			dm_vs[6]=ImageTk.PhotoImage(im)
			dm_vs[1]=can.create_image(x,y,image=dm_vs[6])




			im=Image.new("RGBA",(501,501),(0,0,0,0))

			draw=ImageDraw.Draw(im)

			draw.ellipse((0,0, 500,500),fill=(255,0,0,128),outline=(255,0,0,128))

			sz=int(round(pieces["striker"]["initial_v"]*rr/3,0))

			


			if not sz==0:

				im=im.resize((sz*2,sz*2))

				dm_vs[3]=ImageTk.PhotoImage(im)

				dm_vs[4]=can.create_image(cx,cy,image=dm_vs[3])



			if not dm_piece_mv==[0,0,0,0]:



				x=100*math.sin(math.radians(dm_piece_mv[0]))+dm_piece_mv[1]
				y=100*math.cos(math.radians(dm_piece_mv[0]))+dm_piece_mv[2]


				x2=50*math.sin(math.radians(dm_piece_mv[-1]))+dm_piece_mv[1]
				y2=50*math.cos(math.radians(dm_piece_mv[-1]))+dm_piece_mv[2]


				dm_vs[4]=can.create_line(dm_piece_mv[1],dm_piece_mv[2], x,y,fill="#ff0000")
				dm_vs[7]=can.create_line(dm_piece_mv[1],dm_piece_mv[2], x2,y2,fill="#ff0000")

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



	boundary_=can.create_line(ar,fill="#ff0000")


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


	#print(r,coord)
	#print(r,cx,cy)

def get_pos(pc,cx,cy,r_,ang,con_mv,con):
	global boundary


	# colliding

	#if collusions(pc)==1:

	#	return 2

	#get_ang







	# border

	"""



	# 0,0	

	if con==0:

		for _r_ in range(600):


			x=_r_*math.sin(math.radians(ang))+cx
			y=_r_*math.cos(math.radians(ang))+cy

			

			if boundary[1][0]<=x<=boundary[1][0]+boundary[0]:
				if boundary[1][1]<=y<=boundary[1][1]+boundary[0]:

					con_mv=1
					break

	conx=0
	if con_mv==1:

			conx=1

	if conx==1:
		x=r_*math.sin(math.radians(ang))+cx
		y=r_*math.cos(math.radians(ang))+cy

		

		r2=math.sqrt((x-(boundary[1][0]+boundary[0]))**2+(y-(boundary[1][1]+boundary[0]))**2)

		if r2<=boundary[0]:

			game_st=0

			###

			return 1


		return [x,y,r_+1,ang,con_mv]

	#1,0

	if con==0:

		for _r_ in range(600):


			x=_r_*math.sin(math.radians(ang))+cx
			y=_r_*math.cos(math.radians(ang))+cy



			if boundary[1][2]-boundary[0]<=x<=boundary[1][2]:
				if boundary[1][1]<=y<=boundary[1][1]+boundary[0]:

					con_mv=2
					break


	conx=0
	if con_mv==2:

			conx=1


	if conx==1:
	

		x=r_*math.sin(math.radians(ang))+cx
		y=r_*math.cos(math.radians(ang))+cy

		r2=math.sqrt((x-(boundary[1][2]-boundary[0]))**2+(y-(boundary[1][1]+boundary[0]))**2)

		if r2<=boundary[0]:


			game_st=0

			###

			return 1


		return [x,y,r_+1,ang,con_mv]


	#1,1


	if con==0:

		for _r_ in range(600):


			x=_r_*math.sin(math.radians(ang))+cx
			y=_r_*math.cos(math.radians(ang))+cy


			if boundary[1][2]-boundary[0]<=x<=boundary[1][2]:
				if boundary[1][3]-boundary[0]<=y<=boundary[1][3]:

					con_mv=3
					break


	conx=0
	if con_mv==3:

			conx=1


	if conx==1:		




		x=r_*math.sin(math.radians(ang))+cx
		y=r_*math.cos(math.radians(ang))+cy



	


		r2=math.sqrt((x-(boundary[1][2]-boundary[0]))**2+(y-(boundary[1][3]-boundary[0]))**2)

		if r2<=boundary[0]:


			game_st=0

			###

			return 1



		return [x,y,r_+1,ang,con_mv]



	#0,1




	if con==0:

		for _r_ in range(600):


			x=_r_*math.sin(math.radians(ang))+cx
			y=_r_*math.cos(math.radians(ang))+cy


			if boundary[1][0]<=x<=boundary[1][0]+boundary[0]:
				if boundary[1][3]-boundary[0]<=y<=boundary[1][3]:

					con_mv=4
					break


	conx=0
	if con_mv==4:

			conx=1

	if conx==1:


		x=r_*math.sin(math.radians(ang))+cx
		y=r_*math.cos(math.radians(ang))+cy




		r2=math.sqrt((x-(boundary[1][0]+boundary[0]))**2+(y-(boundary[1][3]-boundary[0]))**2)

		if r2<=boundary[0]:


			game_st=0

			###

			return 1



		return [x,y,r_+1,ang,con_mv]

	"""






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


			r=math.sqrt((x-(boundary[1][0]+1))**2+(y-y)**2)

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

					con_mv=[5,_a_,_r_]

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



		r=math.sqrt((x-(boundary[1][0]+1))**2+(y-y)**2)


		if r_==con_mv[2]:
			if boundary[1][1]<=y<=boundary[1][3]:

				return 2

				#####



		return [x,y,r_+1,ang,con_mv]


	

	#right
	if con==0:


		for _r_ in range(600):



			x=_r_*math.sin(math.radians(ang))+cx
			y=_r_*math.cos(math.radians(ang))+cy



			r=math.sqrt((x-(boundary[1][2]-1))**2+(y-y)**2)

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





					con_mv=[6,_a_,_r_]

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


		r=math.sqrt((x-(boundary[1][2]-1))**2+(y-y)**2)

		if r_==con_mv[2]:

			if boundary[1][1]<=y<=boundary[1][3]:

				return 2

				#####


		return [x,y,r_+1,ang,con_mv]




	#up
	if con==0:


		for _r_ in range(600):



			x=_r_*math.sin(math.radians(ang))+cx
			y=_r_*math.cos(math.radians(ang))+cy



			r=math.sqrt(((x-x)**2+(y-(boundary[1][1]+1))**2))


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

					con_mv=[7,_a_,_r_]

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


		return [x,y,r_+1,ang,con_mv]




	#down
	if con==0:


		for _r_ in range(600):



			x=_r_*math.sin(math.radians(ang))+cx
			y=_r_*math.cos(math.radians(ang))+cy


			r=math.sqrt(((x-x)**2+(y-(boundary[1][3]-1))**2))


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



					con_mv=[8,_a_,_r_]

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



		return [x,y,r_+1,ang,con_mv]



def angle(a):

	try:

		if a>360:
			a=a-360
		elif a<0:
			a=360+a
		elif a==360:
			a=0

		return a

	except  Exception as e:
		#print("angle()",e)
		return a

def move_striker():
	global pieces
	global game_st,game_st2
	global st
	global turn

	

	if pieces["striker"]["potted"]==1:

		root.after(2,move_striker)
		return
	

	if st=="main":


		if pieces["striker"]["move st"]==1 and game_st==2:

			collusions("striker")

			

			if pieces["striker"]["st"]==0:

				

				try:

					#print(pieces["striker"]["proj_ang"])

					pieces["striker"]["coord_"]=pieces["striker"]["coord"]
					if pieces["striker"]["proj_ang"]!=None:
						pieces["striker"]["data"]=get_pos("striker",pieces["striker"]["coord"][0],pieces["striker"]["coord"][1],0,angle(pieces["striker"]["proj_ang"]),0,0)
						pieces["striker"]["angle"]=angle(pieces["striker"]["proj_ang"])
						pieces["striker"]["proj_ang"]=None
					else:

						pieces["striker"]["data"]=get_pos("striker",pieces["striker"]["coord"][0],pieces["striker"]["coord"][1],0,angle(pieces["striker"]["angle"]),0,0)
					
					#print(pieces["striker"]["data"])
					pieces["striker"]["coord"]=[pieces["striker"]["data"][0],pieces["striker"]["data"][1]]
					pieces["striker"]["angle"]=angle(pieces["striker"]["data"][3])

					draw_piece_("striker",1)

					pieces["striker"]["st"]=1

				except Exception as e:
					print("move_striker() 1",e)
			elif pieces["striker"]["st"]==1:
				game_st2=1

				pieces["striker"]["data"]=get_pos("striker",pieces["striker"]["coord_"][0],pieces["striker"]["coord_"][1],pieces["striker"]["data"][2],angle(pieces["striker"]["angle"]),pieces["striker"]["data"][4],1)
				

				if pieces["striker"]["data"]==1:

					pieces["striker"]["start_time"]=0
					pieces["striker"]["potted"]=1
					pieces["striker"]["coord"]=[-100,100]
					pieces["striker"]["speed"]=0
					pieces["striker"]["initial_v"]=0
					pieces["striker"]["current_v"]=0

					pieces["striker"]["proj_ang"]=None
					pieces["striker"]["move st"]=0

					#game_st=0
					pieces["striker"]["move st"]=0
					pieces["striker"]["st"]=0
					pieces["striker"]["initial_v"]=0
					pieces["striker"]["angle"]=0

					




					draw_piece_("striker" ,1)		

					root.after(200,move_striker)
					return


				elif pieces["striker"]["data"]==2:
					pieces["striker"]["st"]=0
					pieces["striker"]["angle"]=angle(pieces["striker"]["proj_ang"])
					draw_piece_("striker",1)	


				else:

					pieces["striker"]["angle"]=angle(pieces["striker"]["data"][3])
					pieces["striker"]["coord"]=[pieces["striker"]["data"][0],pieces["striker"]["data"][1]]


					pieces["striker"]["coord"]=[pieces["striker"]["data"][0],pieces["striker"]["data"][1]]
					

					

					try:


						if len(pieces["striker"]["data"][4])==3:



							pieces["striker"]["proj_ang"]=angle(pieces["striker"]["data"][4][1])

					except Exception as e:
						print("move_striker() 2",e)

					draw_piece_("striker" ,1)


				pieces["striker"]["current_v"]=pieces["striker"]["initial_v"]-0.05*9.8*(time.time()-pieces["striker"]["start_time"])

				if pieces["striker"]["current_v"]<0:



					pieces["striker"]["start_time"]=0

					pieces["striker"]["speed"]=0
					pieces["striker"]["initial_v"]=0
					pieces["striker"]["current_v"]=0
					pieces["striker"]["move st"]=0



					pieces["striker"]["proj_ang"]=None

					pieces["striker"]["angle"]=0

					pieces["striker"]["st"]=0
					pieces["striker"]["move st"]=0					
					#game_st=0
					pieces["striker"]["st"]=0
					pieces["striker"]["initial_v"]=0

					


					draw_piece_("striker" ,1)		

					root.after(2,move_striker)
					return
				else:

					pieces["striker"]["speed"]=int(round((1-pieces["striker"]["current_v"]/3)*10,0))

					if pieces["striker"]["speed"]<1:
						pieces["striker"]["speed"]=1

				


					#print(pieces["striker"]["speed"])


				

				root.after(pieces["striker"]["speed"],move_striker)
				return


			root.after(2,move_striker)
			return


					




		else:
			pieces["striker"]["st"]=0
			root.after(2,move_striker)
			return






		

	else:
		root.after(2,move_striker)
		return




def move_1_w():
	global pieces
	global game_st
	global st
	global turn
	global piece_r
	global moves

	if pieces["1 white"]["potted"]==1:

		root.after(2,move_1_w)
		return

	if st=="main":


		if pieces["1 white"]["move st"]==1:


			collusions("1 white")

			

			if pieces["1 white"]["st"]==0:

				

				try:

					#print(pieces["1 white"]["proj_ang"])

					pieces["1 white"]["coord_"]=pieces["1 white"]["coord"]
					if pieces["1 white"]["proj_ang"]!=None:
						pieces["1 white"]["data"]=get_pos("1 white",pieces["1 white"]["coord"][0],pieces["1 white"]["coord"][1],0,angle(pieces["1 white"]["proj_ang"]),0,0)
						
						pieces["1 white"]["angle"]=angle(pieces["1 white"]["proj_ang"])
						pieces["1 white"]["proj_ang"]=None
					else:

						pieces["1 white"]["data"]=get_pos("1 white",pieces["1 white"]["coord"][0],pieces["1 white"]["coord"][1],0,angle(pieces["1 white"]["angle"]),0,0)
					
					#print(pieces["1 white"]["data"])
					pieces["1 white"]["coord"]=[pieces["1 white"]["data"][0],pieces["1 white"]["data"][1]]
					pieces["1 white"]["angle"]=angle(pieces["1 white"]["data"][3])

					draw_piece_("1 white",1)


					pieces["1 white"]["st"]=1

				except Exception as e:
					print("1white",e)
			elif pieces["1 white"]["st"]==1:

				pieces["1 white"]["data"]=get_pos("1 white",pieces["1 white"]["coord_"][0],pieces["1 white"]["coord_"][1],pieces["1 white"]["data"][2],angle(pieces["1 white"]["angle"]),pieces["1 white"]["data"][4],1)


				if pieces["1 white"]["data"]==1:

					moves.append("1 white")

					pieces["1 white"]["potted"]=1

					pieces["1 white"]["start_time"]=0
					pieces["1 white"]["speed"]=0
					pieces["1 white"]["initial_v"]=0
					pieces["1 white"]["current_v"]=0

					pieces["1 white"]["proj_ang"]=None
					pieces["1 white"]["angle"]=0
					
					pieces["1 white"]["st"]=0
					pieces["1 white"]["initial_v"]=0

					pieces["1 white"]["move st"]=0

					

					pieces["1 white"]["coord"]=[-100,100]

					draw_piece_("1 white",1)		

					root.after(2,move_1_w)
					return


				elif pieces["1 white"]["data"]==2:
					pieces["1 white"]["st"]=0
					pieces["1 white"]["angle"]=angle(pieces["1 white"]["proj_ang"])
					draw_piece_("1 white",1)	


				else:

					pieces["1 white"]["angle"]=angle(pieces["1 white"]["data"][3])
					pieces["1 white"]["coord"]=[pieces["1 white"]["data"][0],pieces["1 white"]["data"][1]]


					pieces["1 white"]["coord"]=[pieces["1 white"]["data"][0],pieces["1 white"]["data"][1]]
					

					

					try:


						if len(pieces["1 white"]["data"][4])==3:



							pieces["1 white"]["proj_ang"]=angle(pieces["1 white"]["data"][4][1])

					except Exception as e:
						print("1white",e)

					draw_piece_("1 white",1)


				pieces["1 white"]["current_v"]=pieces["1 white"]["initial_v"]-0.05*9.8*(time.time()-pieces["1 white"]["start_time"])

				if pieces["1 white"]["current_v"]<0:



					pieces["1 white"]["start_time"]=0
					pieces["1 white"]["speed"]=0
					pieces["1 white"]["initial_v"]=0
					pieces["1 white"]["current_v"]=0



					pieces["1 white"]["proj_ang"]=None
					pieces["1 white"]["angle"]=0
					
					pieces["1 white"]["st"]=0
					pieces["1 white"]["initial_v"]=0

					pieces["1 white"]["move st"]=0

					

					draw_piece_("1 white",1)		

					root.after(2,move_1_w)
					return
				else:

					pieces["1 white"]["speed"]=int(round((1-pieces["1 white"]["current_v"]/3)*10,0))

					if pieces["1 white"]["speed"]<1:
						pieces["1 white"]["speed"]=1


					#print(pieces["1 white"]["speed"])

				

				root.after(pieces["1 white"]["speed"],move_1_w)
				return


			root.after(2,move_1_w)
			return


					




		else:
			pieces["1 white"]["st"]=0
			root.after(2,move_1_w)
			return


	else:
		root.after(2,move_1_w)
		return




def move_2_w():
	global pieces
	global game_st
	global st
	global turn
	global piece_r
	global moves

	if pieces["2 white"]["potted"]==1:

		root.after(2,move_2_w)
		return

	if st=="main":


		if pieces["2 white"]["move st"]==1:


			collusions("2 white")

			

			if pieces["2 white"]["st"]==0:

				

				try:

					#print(pieces["2 white"]["proj_ang"])

					pieces["2 white"]["coord_"]=pieces["2 white"]["coord"]
					if pieces["2 white"]["proj_ang"]!=None:
						pieces["2 white"]["data"]=get_pos("2 white",pieces["2 white"]["coord"][0],pieces["2 white"]["coord"][1],0,angle(pieces["2 white"]["proj_ang"]),0,0)
						
						pieces["2 white"]["angle"]=angle(pieces["2 white"]["proj_ang"])
						pieces["2 white"]["proj_ang"]=None
					else:

						pieces["2 white"]["data"]=get_pos("2 white",pieces["2 white"]["coord"][0],pieces["2 white"]["coord"][1],0,angle(pieces["2 white"]["angle"]),0,0)
					
					#print(pieces["2 white"]["data"])
					pieces["2 white"]["coord"]=[pieces["2 white"]["data"][0],pieces["2 white"]["data"][1]]
					pieces["2 white"]["angle"]=angle(pieces["2 white"]["data"][3])

					draw_piece_("2 white",1)


					pieces["2 white"]["st"]=1

				except Exception as e:
					print("2white",e)
			elif pieces["2 white"]["st"]==1:

				pieces["2 white"]["data"]=get_pos("2 white",pieces["2 white"]["coord_"][0],pieces["2 white"]["coord_"][1],pieces["2 white"]["data"][2],angle(pieces["2 white"]["angle"]),pieces["2 white"]["data"][4],1)


				if pieces["2 white"]["data"]==1:

					moves.append("2 white")

					pieces["2 white"]["potted"]=1

					pieces["2 white"]["start_time"]=0
					pieces["2 white"]["speed"]=0
					pieces["2 white"]["initial_v"]=0
					pieces["2 white"]["current_v"]=0

					pieces["2 white"]["proj_ang"]=None
					pieces["2 white"]["angle"]=0
					
					pieces["2 white"]["st"]=0
					pieces["2 white"]["initial_v"]=0

					pieces["2 white"]["move st"]=0

					

					pieces["2 white"]["coord"]=[-100,100]

					draw_piece_("2 white",1)		

					root.after(2,move_2_w)
					return


				elif pieces["2 white"]["data"]==2:
					pieces["2 white"]["st"]=0
					pieces["2 white"]["angle"]=angle(pieces["2 white"]["proj_ang"])
					draw_piece_("2 white",1)	


				else:

					pieces["2 white"]["angle"]=angle(pieces["2 white"]["data"][3])
					pieces["2 white"]["coord"]=[pieces["2 white"]["data"][0],pieces["2 white"]["data"][1]]


					pieces["2 white"]["coord"]=[pieces["2 white"]["data"][0],pieces["2 white"]["data"][1]]
					

					

					try:


						if len(pieces["2 white"]["data"][4])==3:



							pieces["2 white"]["proj_ang"]=angle(pieces["2 white"]["data"][4][1])

					except Exception as e:
						print("2white",e)

					draw_piece_("2 white",1)


				pieces["2 white"]["current_v"]=pieces["2 white"]["initial_v"]-0.05*9.8*(time.time()-pieces["2 white"]["start_time"])

				if pieces["2 white"]["current_v"]<0:



					pieces["2 white"]["start_time"]=0
					pieces["2 white"]["speed"]=0
					pieces["2 white"]["initial_v"]=0
					pieces["2 white"]["current_v"]=0



					pieces["2 white"]["proj_ang"]=None
					pieces["2 white"]["angle"]=0
					
					pieces["2 white"]["st"]=0
					pieces["2 white"]["initial_v"]=0

					pieces["2 white"]["move st"]=0

					

					draw_piece_("2 white",1)		

					root.after(2,move_2_w)
					return
				else:

					pieces["2 white"]["speed"]=int(round((1-pieces["2 white"]["current_v"]/3)*10,0))

					if pieces["2 white"]["speed"]<1:
						pieces["2 white"]["speed"]=1


					#print(pieces["2 white"]["speed"])

				

				root.after(pieces["2 white"]["speed"],move_2_w)
				return


			root.after(2,move_2_w)
			return


					




		else:
			pieces["2 white"]["st"]=0
			root.after(2,move_2_w)
			return


	else:
		root.after(2,move_2_w)
		return






def move_3_w():
	global pieces
	global game_st
	global st
	global turn
	global piece_r
	global moves

	if pieces["3 white"]["potted"]==1:

		root.after(2,move_3_w)
		return

	if st=="main":


		if pieces["3 white"]["move st"]==1:


			collusions("3 white")

			

			if pieces["3 white"]["st"]==0:

				

				try:

					#print(pieces["3 white"]["proj_ang"])

					pieces["3 white"]["coord_"]=pieces["3 white"]["coord"]
					if pieces["3 white"]["proj_ang"]!=None:
						pieces["3 white"]["data"]=get_pos("3 white",pieces["3 white"]["coord"][0],pieces["3 white"]["coord"][1],0,angle(pieces["3 white"]["proj_ang"]),0,0)
						
						pieces["3 white"]["angle"]=angle(pieces["3 white"]["proj_ang"])
						pieces["3 white"]["proj_ang"]=None
					else:

						pieces["3 white"]["data"]=get_pos("3 white",pieces["3 white"]["coord"][0],pieces["3 white"]["coord"][1],0,angle(pieces["3 white"]["angle"]),0,0)
					
					#print(pieces["3 white"]["data"])
					pieces["3 white"]["coord"]=[pieces["3 white"]["data"][0],pieces["3 white"]["data"][1]]
					pieces["3 white"]["angle"]=angle(pieces["3 white"]["data"][3])

					draw_piece_("3 white",1)


					pieces["3 white"]["st"]=1

				except Exception as e:
						print("3white",e)
			elif pieces["3 white"]["st"]==1:

				pieces["3 white"]["data"]=get_pos("3 white",pieces["3 white"]["coord_"][0],pieces["3 white"]["coord_"][1],pieces["3 white"]["data"][2],angle(pieces["3 white"]["angle"]),pieces["3 white"]["data"][4],1)


				if pieces["3 white"]["data"]==1:
					moves.append("3 white")

					pieces["3 white"]["potted"]=1

					pieces["3 white"]["start_time"]=0
					pieces["3 white"]["speed"]=0
					pieces["3 white"]["initial_v"]=0
					pieces["3 white"]["current_v"]=0

					pieces["3 white"]["proj_ang"]=None
					pieces["3 white"]["angle"]=0
					
					pieces["3 white"]["st"]=0
					pieces["3 white"]["initial_v"]=0

					pieces["3 white"]["move st"]=0

					

					pieces["3 white"]["coord"]=[-100,100]

					draw_piece_("3 white",1)		

					root.after(2,move_3_w)
					return


				elif pieces["3 white"]["data"]==2:
					pieces["3 white"]["st"]=0
					pieces["3 white"]["angle"]=angle(pieces["3 white"]["proj_ang"])
					draw_piece_("3 white",1)	


				else:

					pieces["3 white"]["angle"]=angle(pieces["3 white"]["data"][3])
					pieces["3 white"]["coord"]=[pieces["3 white"]["data"][0],pieces["3 white"]["data"][1]]


					pieces["3 white"]["coord"]=[pieces["3 white"]["data"][0],pieces["3 white"]["data"][1]]
					

					

					try:


						if len(pieces["3 white"]["data"][4])==3:



							pieces["3 white"]["proj_ang"]=angle(pieces["3 white"]["data"][4][1])

					except Exception as e:
						print("2white",e)

					draw_piece_("3 white",1)


				pieces["3 white"]["current_v"]=pieces["3 white"]["initial_v"]-0.05*9.8*(time.time()-pieces["3 white"]["start_time"])

				if pieces["3 white"]["current_v"]<0:



					pieces["3 white"]["start_time"]=0
					pieces["3 white"]["speed"]=0
					pieces["3 white"]["initial_v"]=0
					pieces["3 white"]["current_v"]=0



					pieces["3 white"]["proj_ang"]=None
					pieces["3 white"]["angle"]=0
					
					pieces["3 white"]["st"]=0
					pieces["3 white"]["initial_v"]=0

					pieces["3 white"]["move st"]=0

					

					draw_piece_("3 white",1)		

					root.after(2,move_3_w)
					return
				else:

					pieces["3 white"]["speed"]=int(round((1-pieces["3 white"]["current_v"]/3)*10,0))

					if pieces["3 white"]["speed"]<1:
						pieces["3 white"]["speed"]=1


					#print(pieces["3 white"]["speed"])

				

				root.after(pieces["3 white"]["speed"],move_3_w)
				return


			root.after(2,move_3_w)
			return


					




		else:
			pieces["3 white"]["st"]=0
			root.after(2,move_3_w)
			return


	else:
		root.after(2,move_3_w)
		return





def move_4_w():
	global pieces
	global game_st
	global st
	global turn
	global piece_r
	global moves

	if pieces["4 white"]["potted"]==1:

		root.after(2,move_4_w)
		return

	if st=="main":


		if pieces["4 white"]["move st"]==1:


			collusions("4 white")

			

			if pieces["4 white"]["st"]==0:

				

				try:

					#print(pieces["4 white"]["proj_ang"])

					pieces["4 white"]["coord_"]=pieces["4 white"]["coord"]
					if pieces["4 white"]["proj_ang"]!=None:
						pieces["4 white"]["data"]=get_pos("4 white",pieces["4 white"]["coord"][0],pieces["4 white"]["coord"][1],0,angle(pieces["4 white"]["proj_ang"]),0,0)
						
						pieces["4 white"]["angle"]=angle(pieces["4 white"]["proj_ang"])
						pieces["4 white"]["proj_ang"]=None
					else:

						pieces["4 white"]["data"]=get_pos("4 white",pieces["4 white"]["coord"][0],pieces["4 white"]["coord"][1],0,angle(pieces["4 white"]["angle"]),0,0)
					
					#print(pieces["4 white"]["data"])
					pieces["4 white"]["coord"]=[pieces["4 white"]["data"][0],pieces["4 white"]["data"][1]]
					pieces["4 white"]["angle"]=angle(pieces["4 white"]["data"][3])

					draw_piece_("4 white",1)


					pieces["4 white"]["st"]=1

				except Exception as e:
						print("4white",e)
			elif pieces["4 white"]["st"]==1:

				pieces["4 white"]["data"]=get_pos("4 white",pieces["4 white"]["coord_"][0],pieces["4 white"]["coord_"][1],pieces["4 white"]["data"][2],angle(pieces["4 white"]["angle"]),pieces["4 white"]["data"][4],1)


				if pieces["4 white"]["data"]==1:

					moves.append("4 white")

					pieces["4 white"]["potted"]=1

					pieces["4 white"]["start_time"]=0
					pieces["4 white"]["speed"]=0
					pieces["4 white"]["initial_v"]=0
					pieces["4 white"]["current_v"]=0

					pieces["4 white"]["proj_ang"]=None
					pieces["4 white"]["angle"]=0
					
					pieces["4 white"]["st"]=0
					pieces["4 white"]["initial_v"]=0

					pieces["4 white"]["move st"]=0

					

					pieces["4 white"]["coord"]=[-100,100]

					draw_piece_("4 white",1)		

					root.after(2,move_4_w)
					return


				elif pieces["4 white"]["data"]==2:
					pieces["4 white"]["st"]=0
					pieces["4 white"]["angle"]=angle(pieces["4 white"]["proj_ang"])
					draw_piece_("4 white",1)	


				else:

					pieces["4 white"]["angle"]=angle(pieces["4 white"]["data"][3])
					pieces["4 white"]["coord"]=[pieces["4 white"]["data"][0],pieces["4 white"]["data"][1]]


					pieces["4 white"]["coord"]=[pieces["4 white"]["data"][0],pieces["4 white"]["data"][1]]
					

					

					try:


						if len(pieces["4 white"]["data"][4])==3:



							pieces["4 white"]["proj_ang"]=angle(pieces["4 white"]["data"][4][1])

					except Exception as e:
						print("4white",e)

					draw_piece_("4 white",1)


				pieces["4 white"]["current_v"]=pieces["4 white"]["initial_v"]-0.05*9.8*(time.time()-pieces["4 white"]["start_time"])

				if pieces["4 white"]["current_v"]<0:



					pieces["4 white"]["start_time"]=0
					pieces["4 white"]["speed"]=0
					pieces["4 white"]["initial_v"]=0
					pieces["4 white"]["current_v"]=0



					pieces["4 white"]["proj_ang"]=None
					pieces["4 white"]["angle"]=0
					
					pieces["4 white"]["st"]=0
					pieces["4 white"]["initial_v"]=0

					pieces["4 white"]["move st"]=0

					

					draw_piece_("4 white",1)		

					root.after(2,move_4_w)
					return
				else:

					pieces["4 white"]["speed"]=int(round((1-pieces["4 white"]["current_v"]/3)*10,0))

					if pieces["4 white"]["speed"]<1:
						pieces["4 white"]["speed"]=1


					#print(pieces["4 white"]["speed"])

				

				root.after(pieces["4 white"]["speed"],move_4_w)
				return


			root.after(2,move_4_w)
			return


					




		else:
			pieces["4 white"]["st"]=0
			root.after(2,move_4_w)
			return


	else:
		root.after(2,move_4_w)
		return





def move_5_w():
	global pieces
	global game_st
	global st
	global turn
	global piece_r
	global moves

	if pieces["5 white"]["potted"]==1:

		root.after(2,move_5_w)
		return

	if st=="main":


		if pieces["5 white"]["move st"]==1:


			collusions("5 white")

			

			if pieces["5 white"]["st"]==0:

				

				try:

					#print(pieces["5 white"]["proj_ang"])

					pieces["5 white"]["coord_"]=pieces["5 white"]["coord"]
					if pieces["5 white"]["proj_ang"]!=None:
						pieces["5 white"]["data"]=get_pos("5 white",pieces["5 white"]["coord"][0],pieces["5 white"]["coord"][1],0,angle(pieces["5 white"]["proj_ang"]),0,0)
						
						pieces["5 white"]["angle"]=angle(pieces["5 white"]["proj_ang"])
						pieces["5 white"]["proj_ang"]=None
					else:

						pieces["5 white"]["data"]=get_pos("5 white",pieces["5 white"]["coord"][0],pieces["5 white"]["coord"][1],0,angle(pieces["5 white"]["angle"]),0,0)
					
					#print(pieces["5 white"]["data"])
					pieces["5 white"]["coord"]=[pieces["5 white"]["data"][0],pieces["5 white"]["data"][1]]
					pieces["5 white"]["angle"]=angle(pieces["5 white"]["data"][3])

					draw_piece_("5 white",1)


					pieces["5 white"]["st"]=1

				except Exception as e:
						print("5white",e)
			elif pieces["5 white"]["st"]==1:

				pieces["5 white"]["data"]=get_pos("5 white",pieces["5 white"]["coord_"][0],pieces["5 white"]["coord_"][1],pieces["5 white"]["data"][2],angle(pieces["5 white"]["angle"]),pieces["5 white"]["data"][4],1)


				if pieces["5 white"]["data"]==1:
					moves.append("5 white")

					pieces["5 white"]["potted"]=1

					pieces["5 white"]["start_time"]=0
					pieces["5 white"]["speed"]=0
					pieces["5 white"]["initial_v"]=0
					pieces["5 white"]["current_v"]=0

					pieces["5 white"]["proj_ang"]=None
					pieces["5 white"]["angle"]=0
					
					pieces["5 white"]["st"]=0
					pieces["5 white"]["initial_v"]=0

					pieces["5 white"]["move st"]=0

					

					pieces["5 white"]["coord"]=[-100,100]

					draw_piece_("5 white",1)		

					root.after(2,move_5_w)
					return


				elif pieces["5 white"]["data"]==2:
					pieces["5 white"]["st"]=0
					pieces["5 white"]["angle"]=angle(pieces["5 white"]["proj_ang"])
					draw_piece_("5 white",1)	


				else:

					pieces["5 white"]["angle"]=angle(pieces["5 white"]["data"][3])
					pieces["5 white"]["coord"]=[pieces["5 white"]["data"][0],pieces["5 white"]["data"][1]]


					pieces["5 white"]["coord"]=[pieces["5 white"]["data"][0],pieces["5 white"]["data"][1]]
					

					

					try:


						if len(pieces["5 white"]["data"][4])==3:



							pieces["5 white"]["proj_ang"]=angle(pieces["5 white"]["data"][4][1])

					except Exception as e:
						print("5white",e)

					draw_piece_("5 white",1)


				pieces["5 white"]["current_v"]=pieces["5 white"]["initial_v"]-0.05*9.8*(time.time()-pieces["5 white"]["start_time"])

				if pieces["5 white"]["current_v"]<0:



					pieces["5 white"]["start_time"]=0
					pieces["5 white"]["speed"]=0
					pieces["5 white"]["initial_v"]=0
					pieces["5 white"]["current_v"]=0



					pieces["5 white"]["proj_ang"]=None
					pieces["5 white"]["angle"]=0
					
					pieces["5 white"]["st"]=0
					pieces["5 white"]["initial_v"]=0

					pieces["5 white"]["move st"]=0

					

					draw_piece_("5 white",1)		

					root.after(2,move_5_w)
					return
				else:

					pieces["5 white"]["speed"]=int(round((1-pieces["5 white"]["current_v"]/3)*10,0))

					if pieces["5 white"]["speed"]<1:
						pieces["5 white"]["speed"]=1


					#print(pieces["5 white"]["speed"])

				

				root.after(pieces["5 white"]["speed"],move_5_w)
				return


			root.after(2,move_5_w)
			return


					




		else:
			pieces["5 white"]["st"]=0
			root.after(2,move_5_w)
			return


	else:
		root.after(2,move_5_w)
		return








def move_6_w():
	global pieces
	global game_st
	global st
	global turn
	global piece_r
	global moves

	if pieces["6 white"]["potted"]==1:

		root.after(2,move_6_w)
		return

	if st=="main":


		if pieces["6 white"]["move st"]==1:


			collusions("6 white")

			

			if pieces["6 white"]["st"]==0:

				

				try:

					#print(pieces["6 white"]["proj_ang"])

					pieces["6 white"]["coord_"]=pieces["6 white"]["coord"]
					if pieces["6 white"]["proj_ang"]!=None:
						pieces["6 white"]["data"]=get_pos("6 white",pieces["6 white"]["coord"][0],pieces["6 white"]["coord"][1],0,angle(pieces["6 white"]["proj_ang"]),0,0)
						
						pieces["6 white"]["angle"]=angle(pieces["6 white"]["proj_ang"])
						pieces["6 white"]["proj_ang"]=None
					else:

						pieces["6 white"]["data"]=get_pos("6 white",pieces["6 white"]["coord"][0],pieces["6 white"]["coord"][1],0,angle(pieces["6 white"]["angle"]),0,0)
					
					#print(pieces["6 white"]["data"])
					pieces["6 white"]["coord"]=[pieces["6 white"]["data"][0],pieces["6 white"]["data"][1]]
					pieces["6 white"]["angle"]=angle(pieces["6 white"]["data"][3])

					draw_piece_("6 white",1)


					pieces["6 white"]["st"]=1

				except Exception as e:
						print("6white",e)
			elif pieces["6 white"]["st"]==1:

				pieces["6 white"]["data"]=get_pos("6 white",pieces["6 white"]["coord_"][0],pieces["6 white"]["coord_"][1],pieces["6 white"]["data"][2],angle(pieces["6 white"]["angle"]),pieces["6 white"]["data"][4],1)


				if pieces["6 white"]["data"]==1:

					moves.append("6 white")

					pieces["6 white"]["potted"]=1

					pieces["6 white"]["start_time"]=0
					pieces["6 white"]["speed"]=0
					pieces["6 white"]["initial_v"]=0
					pieces["6 white"]["current_v"]=0

					pieces["6 white"]["proj_ang"]=None
					pieces["6 white"]["angle"]=0
					
					pieces["6 white"]["st"]=0
					pieces["6 white"]["initial_v"]=0

					pieces["6 white"]["move st"]=0

					

					pieces["6 white"]["coord"]=[-100,100]

					draw_piece_("6 white",1)		

					root.after(2,move_6_w)
					return


				elif pieces["6 white"]["data"]==2:
					pieces["6 white"]["st"]=0
					pieces["6 white"]["angle"]=angle(pieces["6 white"]["proj_ang"])
					draw_piece_("6 white",1)	


				else:

					pieces["6 white"]["angle"]=angle(pieces["6 white"]["data"][3])
					pieces["6 white"]["coord"]=[pieces["6 white"]["data"][0],pieces["6 white"]["data"][1]]


					pieces["6 white"]["coord"]=[pieces["6 white"]["data"][0],pieces["6 white"]["data"][1]]
					

					

					try:


						if len(pieces["6 white"]["data"][4])==3:



							pieces["6 white"]["proj_ang"]=angle(pieces["6 white"]["data"][4][1])

					except Exception as e:
						print("6white",e)

					draw_piece_("6 white",1)


				pieces["6 white"]["current_v"]=pieces["6 white"]["initial_v"]-0.05*9.8*(time.time()-pieces["6 white"]["start_time"])

				if pieces["6 white"]["current_v"]<0:



					pieces["6 white"]["start_time"]=0
					pieces["6 white"]["speed"]=0
					pieces["6 white"]["initial_v"]=0
					pieces["6 white"]["current_v"]=0



					pieces["6 white"]["proj_ang"]=None
					pieces["6 white"]["angle"]=0
					
					pieces["6 white"]["st"]=0
					pieces["6 white"]["initial_v"]=0

					pieces["6 white"]["move st"]=0

					

					draw_piece_("6 white",1)		

					root.after(2,move_6_w)
					return
				else:

					pieces["6 white"]["speed"]=int(round((1-pieces["6 white"]["current_v"]/3)*10,0))

					if pieces["6 white"]["speed"]<1:
						pieces["6 white"]["speed"]=1


					#print(pieces["6 white"]["speed"])

				

				root.after(pieces["6 white"]["speed"],move_6_w)
				return


			root.after(2,move_6_w)
			return


					




		else:
			pieces["6 white"]["st"]=0
			root.after(2,move_6_w)
			return


	else:
		root.after(2,move_6_w)
		return





def move_7_w():
	global pieces
	global game_st
	global st
	global turn
	global piece_r
	global moves

	if pieces["7 white"]["potted"]==1:

		root.after(2,move_7_w)
		return

	if st=="main":


		if pieces["7 white"]["move st"]==1:


			collusions("7 white")

			

			if pieces["7 white"]["st"]==0:

				

				try:

					#print(pieces["7 white"]["proj_ang"])

					pieces["7 white"]["coord_"]=pieces["7 white"]["coord"]
					if pieces["7 white"]["proj_ang"]!=None:
						pieces["7 white"]["data"]=get_pos("7 white",pieces["7 white"]["coord"][0],pieces["7 white"]["coord"][1],0,angle(pieces["7 white"]["proj_ang"]),0,0)
						
						pieces["7 white"]["angle"]=angle(pieces["7 white"]["proj_ang"])
						pieces["7 white"]["proj_ang"]=None
					else:

						pieces["7 white"]["data"]=get_pos("7 white",pieces["7 white"]["coord"][0],pieces["7 white"]["coord"][1],0,angle(pieces["7 white"]["angle"]),0,0)
					
					#print(pieces["7 white"]["data"])
					pieces["7 white"]["coord"]=[pieces["7 white"]["data"][0],pieces["7 white"]["data"][1]]
					pieces["7 white"]["angle"]=angle(pieces["7 white"]["data"][3])

					draw_piece_("7 white",1)


					pieces["7 white"]["st"]=1

				except Exception as e:
						print("7white",e)
			elif pieces["7 white"]["st"]==1:

				pieces["7 white"]["data"]=get_pos("7 white",pieces["7 white"]["coord_"][0],pieces["7 white"]["coord_"][1],pieces["7 white"]["data"][2],angle(pieces["7 white"]["angle"]),pieces["7 white"]["data"][4],1)


				if pieces["7 white"]["data"]==1:
					moves.append("7 white")

					pieces["7 white"]["potted"]=1

					pieces["7 white"]["start_time"]=0
					pieces["7 white"]["speed"]=0
					pieces["7 white"]["initial_v"]=0
					pieces["7 white"]["current_v"]=0

					pieces["7 white"]["proj_ang"]=None
					pieces["7 white"]["angle"]=0
					
					pieces["7 white"]["st"]=0
					pieces["7 white"]["initial_v"]=0

					pieces["7 white"]["move st"]=0

					

					pieces["7 white"]["coord"]=[-100,100]

					draw_piece_("7 white",1)		

					root.after(2,move_7_w)
					return


				elif pieces["7 white"]["data"]==2:
					pieces["7 white"]["st"]=0
					pieces["7 white"]["angle"]=angle(pieces["7 white"]["proj_ang"])
					draw_piece_("7 white",1)	


				else:

					pieces["7 white"]["angle"]=angle(pieces["7 white"]["data"][3])
					pieces["7 white"]["coord"]=[pieces["7 white"]["data"][0],pieces["7 white"]["data"][1]]


					pieces["7 white"]["coord"]=[pieces["7 white"]["data"][0],pieces["7 white"]["data"][1]]
					

					

					try:


						if len(pieces["7 white"]["data"][4])==3:



							pieces["7 white"]["proj_ang"]=angle(pieces["7 white"]["data"][4][1])

					except Exception as e:
						print("7white",e)

					draw_piece_("7 white",1)


				pieces["7 white"]["current_v"]=pieces["7 white"]["initial_v"]-0.05*9.8*(time.time()-pieces["7 white"]["start_time"])

				if pieces["7 white"]["current_v"]<0:



					pieces["7 white"]["start_time"]=0
					pieces["7 white"]["speed"]=0
					pieces["7 white"]["initial_v"]=0
					pieces["7 white"]["current_v"]=0



					pieces["7 white"]["proj_ang"]=None
					pieces["7 white"]["angle"]=0
					
					pieces["7 white"]["st"]=0
					pieces["7 white"]["initial_v"]=0

					pieces["7 white"]["move st"]=0

					

					draw_piece_("7 white",1)		

					root.after(2,move_7_w)
					return
				else:

					pieces["7 white"]["speed"]=int(round((1-pieces["7 white"]["current_v"]/3)*10,0))

					if pieces["7 white"]["speed"]<1:
						pieces["7 white"]["speed"]=1


					#print(pieces["7 white"]["speed"])

				

				root.after(pieces["7 white"]["speed"],move_7_w)
				return


			root.after(2,move_7_w)
			return


					




		else:
			pieces["7 white"]["st"]=0
			root.after(2,move_7_w)
			return


	else:
		root.after(2,move_7_w)
		return





def move_8_w():
	global pieces
	global game_st
	global st
	global turn
	global piece_r
	global moves

	if pieces["8 white"]["potted"]==1:

		root.after(2,move_8_w)
		return

	if st=="main":


		if pieces["8 white"]["move st"]==1:


			collusions("8 white")

			

			if pieces["8 white"]["st"]==0:

				

				try:

					#print(pieces["8 white"]["proj_ang"])

					pieces["8 white"]["coord_"]=pieces["8 white"]["coord"]
					if pieces["8 white"]["proj_ang"]!=None:
						pieces["8 white"]["data"]=get_pos("8 white",pieces["8 white"]["coord"][0],pieces["8 white"]["coord"][1],0,angle(pieces["8 white"]["proj_ang"]),0,0)
						
						pieces["8 white"]["angle"]=angle(pieces["8 white"]["proj_ang"])
						pieces["8 white"]["proj_ang"]=None
					else:

						pieces["8 white"]["data"]=get_pos("8 white",pieces["8 white"]["coord"][0],pieces["8 white"]["coord"][1],0,angle(pieces["8 white"]["angle"]),0,0)
					
					#print(pieces["8 white"]["data"])
					pieces["8 white"]["coord"]=[pieces["8 white"]["data"][0],pieces["8 white"]["data"][1]]
					pieces["8 white"]["angle"]=angle(pieces["8 white"]["data"][3])

					draw_piece_("8 white",1)


					pieces["8 white"]["st"]=1

				except Exception as e:
						print("8white",e)
			elif pieces["8 white"]["st"]==1:

				pieces["8 white"]["data"]=get_pos("8 white",pieces["8 white"]["coord_"][0],pieces["8 white"]["coord_"][1],pieces["8 white"]["data"][2],angle(pieces["8 white"]["angle"]),pieces["8 white"]["data"][4],1)


				if pieces["8 white"]["data"]==1:
					moves.append("8 white")

					pieces["8 white"]["potted"]=1

					pieces["8 white"]["start_time"]=0
					pieces["8 white"]["speed"]=0
					pieces["8 white"]["initial_v"]=0
					pieces["8 white"]["current_v"]=0

					pieces["8 white"]["proj_ang"]=None
					pieces["8 white"]["angle"]=0
					
					pieces["8 white"]["st"]=0
					pieces["8 white"]["initial_v"]=0

					pieces["8 white"]["move st"]=0

					

					pieces["8 white"]["coord"]=[-100,100]

					draw_piece_("8 white",1)		

					root.after(2,move_8_w)
					return


				elif pieces["8 white"]["data"]==2:
					pieces["8 white"]["st"]=0
					pieces["8 white"]["angle"]=angle(pieces["8 white"]["proj_ang"])
					draw_piece_("8 white",1)	


				else:

					pieces["8 white"]["angle"]=angle(pieces["8 white"]["data"][3])
					pieces["8 white"]["coord"]=[pieces["8 white"]["data"][0],pieces["8 white"]["data"][1]]


					pieces["8 white"]["coord"]=[pieces["8 white"]["data"][0],pieces["8 white"]["data"][1]]
					

					

					try:


						if len(pieces["8 white"]["data"][4])==3:



							pieces["8 white"]["proj_ang"]=angle(pieces["8 white"]["data"][4][1])

					except Exception as e:
						print("8white",e)

					draw_piece_("8 white",1)


				pieces["8 white"]["current_v"]=pieces["8 white"]["initial_v"]-0.05*9.8*(time.time()-pieces["8 white"]["start_time"])

				if pieces["8 white"]["current_v"]<0:



					pieces["8 white"]["start_time"]=0
					pieces["8 white"]["speed"]=0
					pieces["8 white"]["initial_v"]=0
					pieces["8 white"]["current_v"]=0



					pieces["8 white"]["proj_ang"]=None
					pieces["8 white"]["angle"]=0
					
					pieces["8 white"]["st"]=0
					pieces["8 white"]["initial_v"]=0

					pieces["8 white"]["move st"]=0

					

					draw_piece_("8 white",1)		

					root.after(2,move_8_w)
					return
				else:

					pieces["8 white"]["speed"]=int(round((1-pieces["8 white"]["current_v"]/3)*10,0))

					if pieces["8 white"]["speed"]<1:
						pieces["8 white"]["speed"]=1


					#print(pieces["8 white"]["speed"])

				

				root.after(pieces["8 white"]["speed"],move_8_w)
				return


			root.after(2,move_8_w)
			return


					




		else:
			pieces["8 white"]["st"]=0
			root.after(2,move_8_w)
			return


	else:
		root.after(2,move_8_w)
		return






def move_9_w():
	global pieces
	global game_st
	global st
	global turn
	global piece_r
	global moves

	if pieces["9 white"]["potted"]==1:

		root.after(2,move_9_w)
		return

	if st=="main":


		if pieces["9 white"]["move st"]==1:


			collusions("9 white")

			

			if pieces["9 white"]["st"]==0:

				

				try:

					#print(pieces["9 white"]["proj_ang"])

					pieces["9 white"]["coord_"]=pieces["9 white"]["coord"]
					if pieces["9 white"]["proj_ang"]!=None:
						pieces["9 white"]["data"]=get_pos("9 white",pieces["9 white"]["coord"][0],pieces["9 white"]["coord"][1],0,angle(pieces["9 white"]["proj_ang"]),0,0)
						
						pieces["9 white"]["angle"]=angle(pieces["9 white"]["proj_ang"])
						pieces["9 white"]["proj_ang"]=None
					else:

						pieces["9 white"]["data"]=get_pos("9 white",pieces["9 white"]["coord"][0],pieces["9 white"]["coord"][1],0,angle(pieces["9 white"]["angle"]),0,0)
					
					#print(pieces["9 white"]["data"])
					pieces["9 white"]["coord"]=[pieces["9 white"]["data"][0],pieces["9 white"]["data"][1]]
					pieces["9 white"]["angle"]=angle(pieces["9 white"]["data"][3])

					draw_piece_("9 white",1)


					pieces["9 white"]["st"]=1

				except Exception as e:
						print("9white",e)
			elif pieces["9 white"]["st"]==1:

				pieces["9 white"]["data"]=get_pos("9 white",pieces["9 white"]["coord_"][0],pieces["9 white"]["coord_"][1],pieces["9 white"]["data"][2],angle(pieces["9 white"]["angle"]),pieces["9 white"]["data"][4],1)


				if pieces["9 white"]["data"]==1:
					moves.append("9 white")

					pieces["9 white"]["potted"]=1

					pieces["9 white"]["start_time"]=0
					pieces["9 white"]["speed"]=0
					pieces["9 white"]["initial_v"]=0
					pieces["9 white"]["current_v"]=0

					pieces["9 white"]["proj_ang"]=None
					pieces["9 white"]["angle"]=0
					
					pieces["9 white"]["st"]=0
					pieces["9 white"]["initial_v"]=0

					pieces["9 white"]["move st"]=0

					

					pieces["9 white"]["coord"]=[-100,100]

					draw_piece_("9 white",1)		

					root.after(2,move_9_w)
					return


				elif pieces["9 white"]["data"]==2:
					pieces["9 white"]["st"]=0
					pieces["9 white"]["angle"]=angle(pieces["9 white"]["proj_ang"])
					draw_piece_("9 white",1)	


				else:

					pieces["9 white"]["angle"]=angle(pieces["9 white"]["data"][3])
					pieces["9 white"]["coord"]=[pieces["9 white"]["data"][0],pieces["9 white"]["data"][1]]


					pieces["9 white"]["coord"]=[pieces["9 white"]["data"][0],pieces["9 white"]["data"][1]]
					

					

					try:


						if len(pieces["9 white"]["data"][4])==3:



							pieces["9 white"]["proj_ang"]=angle(pieces["9 white"]["data"][4][1])

					except Exception as e:
						print("9white",e)

					draw_piece_("9 white",1)


				pieces["9 white"]["current_v"]=pieces["9 white"]["initial_v"]-0.05*9.8*(time.time()-pieces["9 white"]["start_time"])

				if pieces["9 white"]["current_v"]<0:



					pieces["9 white"]["start_time"]=0
					pieces["9 white"]["speed"]=0
					pieces["9 white"]["initial_v"]=0
					pieces["9 white"]["current_v"]=0



					pieces["9 white"]["proj_ang"]=None
					pieces["9 white"]["angle"]=0
					
					pieces["9 white"]["st"]=0
					pieces["9 white"]["initial_v"]=0

					pieces["9 white"]["move st"]=0

					

					draw_piece_("9 white",1)		

					root.after(2,move_9_w)
					return
				else:

					pieces["9 white"]["speed"]=int(round((1-pieces["9 white"]["current_v"]/3)*10,0))

					if pieces["9 white"]["speed"]<1:
						pieces["9 white"]["speed"]=1


					#print(pieces["9 white"]["speed"])

				

				root.after(pieces["9 white"]["speed"],move_9_w)
				return


			root.after(2,move_9_w)
			return


					




		else:
			pieces["9 white"]["st"]=0
			root.after(2,move_9_w)
			return


	else:
		root.after(2,move_9_w)
		return






def move_1_b():
    global pieces
    global game_st
    global st
    global turn
    global piece_r
    global moves

    if pieces["1 black"]["potted"]==1:

        root.after(2,move_1_b)
        return

    if st=="main":

        if pieces["1 black"]["move st"]==1:





            

            


            collusions("1 black")
            if pieces["1 black"]["st"]==0:
                

                try:

                    #print(pieces["1 black"]["proj_ang"])

                    pieces["1 black"]["coord_"]=pieces["1 black"]["coord"]
                    if pieces["1 black"]["proj_ang"]!=None:
                        pieces["1 black"]["data"]=get_pos("1 black",pieces["1 black"]["coord"][0],pieces["1 black"]["coord"][1],0,angle(pieces["1 black"]["proj_ang"]),0,0)
                        
                        pieces["1 black"]["angle"]=angle(pieces["1 black"]["proj_ang"])
                        pieces["1 black"]["proj_ang"]=None
                    else:

                        pieces["1 black"]["data"]=get_pos("1 black",pieces["1 black"]["coord"][0],pieces["1 black"]["coord"][1],0,angle(pieces["1 black"]["angle"]),0,0)
                    
                    #print(pieces["1 black"]["data"])
                    pieces["1 black"]["coord"]=[pieces["1 black"]["data"][0],pieces["1 black"]["data"][1]]
                    pieces["1 black"]["angle"]=angle(pieces["1 black"]["data"][3])

                    draw_piece_("1 black",1)


                    pieces["1 black"]["st"]=1

                except Exception as e:
                	print("1black",e)
            elif pieces["1 black"]["st"]==1:

                pieces["1 black"]["data"]=get_pos("1 black",pieces["1 black"]["coord_"][0],pieces["1 black"]["coord_"][1],pieces["1 black"]["data"][2],angle(pieces["1 black"]["angle"]),pieces["1 black"]["data"][4],1)

                

                if pieces["1 black"]["data"]==1:
                	

                    pieces["1 black"]["potted"]=1
                    moves.append("1 black")

                    pieces["1 black"]["start_time"]=0
                    pieces["1 black"]["speed"]=0
                    pieces["1 black"]["initial_v"]=0
                    pieces["1 black"]["current_v"]=0

                    pieces["1 black"]["proj_ang"]=None
                    pieces["1 black"]["angle"]=0
                    
                    pieces["1 black"]["st"]=0
                    pieces["1 black"]["initial_v"]=0

                    pieces["1 black"]["move st"]=0

                    

                    pieces["1 black"]["coord"]=[-100,100]

                    draw_piece_("1 black",1)        

                    root.after(2,move_1_b)
                    return


                elif pieces["1 black"]["data"]==2:
                    pieces["1 black"]["st"]=0
                    pieces["1 black"]["angle"]=angle(pieces["1 black"]["proj_ang"])
                    draw_piece_("1 black",1)    


                else:

                    pieces["1 black"]["angle"]=angle(pieces["1 black"]["data"][3])
                    pieces["1 black"]["coord"]=[pieces["1 black"]["data"][0],pieces["1 black"]["data"][1]]


                    pieces["1 black"]["coord"]=[pieces["1 black"]["data"][0],pieces["1 black"]["data"][1]]
                    

                    

                    try:


                        if len(pieces["1 black"]["data"][4])==3:



                            pieces["1 black"]["proj_ang"]=angle(pieces["1 black"]["data"][4][1])

                    except Exception as e:
                    	print("1black",e)


                    draw_piece_("1 black",1)


                pieces["1 black"]["current_v"]=pieces["1 black"]["initial_v"]-0.05*9.8*(time.time()-pieces["1 black"]["start_time"])
                #print("1 black"," - ",pieces["1 black"]["current_v"])

                if int(pieces["1 black"]["current_v"])<0:



                    pieces["1 black"]["start_time"]=0
                    pieces["1 black"]["speed"]=0
                    pieces["1 black"]["initial_v"]=0
                    pieces["1 black"]["current_v"]=0



                    pieces["1 black"]["proj_ang"]=None
                    pieces["1 black"]["angle"]=0
                    
                    pieces["1 black"]["st"]=0
                    pieces["1 black"]["move st"]=0

                    

                    draw_piece_("1 black",1)        

                    root.after(2,move_1_b)
                    return
                else:

                    pieces["1 black"]["speed"]=int(round((1-pieces["1 black"]["current_v"]/3)*10,0))

                    if pieces["1 black"]["speed"]<1:
                        pieces["1 black"]["speed"]=1

                




               

                root.after(pieces["1 black"]["speed"],move_1_b)
                return


            root.after(2,move_1_b)
            return


                    




        else:
            pieces["1 black"]["st"]=0
            root.after(2,move_1_b)
            return


    else:
        root.after(2,move_1_b)
        return





def move_2_b():
    global pieces
    global game_st
    global st
    global turn
    global piece_r
    global moves

    if pieces["2 black"]["potted"]==1:

        root.after(2,move_2_b)
        return

    if st=="main":

        if pieces["2 black"]["move st"]==1:





            

            


            collusions("2 black")
            if pieces["2 black"]["st"]==0:
                

                try:

                    #print(pieces["2 black"]["proj_ang"])

                    pieces["2 black"]["coord_"]=pieces["2 black"]["coord"]
                    if pieces["2 black"]["proj_ang"]!=None:
                        pieces["2 black"]["data"]=get_pos("2 black",pieces["2 black"]["coord"][0],pieces["2 black"]["coord"][1],0,angle(pieces["2 black"]["proj_ang"]),0,0)
                        
                        pieces["2 black"]["angle"]=angle(pieces["2 black"]["proj_ang"])
                        pieces["2 black"]["proj_ang"]=None
                    else:

                        pieces["2 black"]["data"]=get_pos("2 black",pieces["2 black"]["coord"][0],pieces["2 black"]["coord"][1],0,angle(pieces["2 black"]["angle"]),0,0)
                    
                    #print(pieces["2 black"]["data"])
                    pieces["2 black"]["coord"]=[pieces["2 black"]["data"][0],pieces["2 black"]["data"][1]]
                    pieces["2 black"]["angle"]=angle(pieces["2 black"]["data"][3])

                    draw_piece_("2 black",1)


                    pieces["2 black"]["st"]=1

                except Exception as e:
                    	print("2black",e)
            elif pieces["2 black"]["st"]==1:

                pieces["2 black"]["data"]=get_pos("2 black",pieces["2 black"]["coord_"][0],pieces["2 black"]["coord_"][1],pieces["2 black"]["data"][2],angle(pieces["2 black"]["angle"]),pieces["2 black"]["data"][4],1)

                

                if pieces["2 black"]["data"]==1:
                	

                    pieces["2 black"]["potted"]=1
                    moves.append("2 black")

                    pieces["2 black"]["start_time"]=0
                    pieces["2 black"]["speed"]=0
                    pieces["2 black"]["initial_v"]=0
                    pieces["2 black"]["current_v"]=0

                    pieces["2 black"]["proj_ang"]=None
                    pieces["2 black"]["angle"]=0
                    
                    pieces["2 black"]["st"]=0
                    pieces["2 black"]["initial_v"]=0

                    pieces["2 black"]["move st"]=0

                    

                    pieces["2 black"]["coord"]=[-100,100]

                    draw_piece_("2 black",1)        

                    root.after(2,move_2_b)
                    return


                elif pieces["2 black"]["data"]==2:
                    pieces["2 black"]["st"]=0
                    pieces["2 black"]["angle"]=angle(pieces["2 black"]["proj_ang"])
                    draw_piece_("2 black",1)    


                else:

                    pieces["2 black"]["angle"]=angle(pieces["2 black"]["data"][3])
                    pieces["2 black"]["coord"]=[pieces["2 black"]["data"][0],pieces["2 black"]["data"][1]]


                    pieces["2 black"]["coord"]=[pieces["2 black"]["data"][0],pieces["2 black"]["data"][1]]
                    

                    

                    try:


                        if len(pieces["2 black"]["data"][4])==3:



                            pieces["2 black"]["proj_ang"]=angle(pieces["2 black"]["data"][4][1])

                    except Exception as e:
                    	print("2black",e)

                    draw_piece_("2 black",1)


                pieces["2 black"]["current_v"]=pieces["2 black"]["initial_v"]-0.05*9.8*(time.time()-pieces["2 black"]["start_time"])
                #print("2 black"," - ",pieces["2 black"]["current_v"])

                if int(pieces["2 black"]["current_v"])<0:



                    pieces["2 black"]["start_time"]=0
                    pieces["2 black"]["speed"]=0
                    pieces["2 black"]["initial_v"]=0
                    pieces["2 black"]["current_v"]=0



                    pieces["2 black"]["proj_ang"]=None
                    pieces["2 black"]["angle"]=0
                    
                    pieces["2 black"]["st"]=0
                    pieces["2 black"]["move st"]=0

                    

                    draw_piece_("2 black",1)        

                    root.after(2,move_2_b)
                    return
                else:

                    pieces["2 black"]["speed"]=int(round((1-pieces["2 black"]["current_v"]/3)*10,0))

                    if pieces["2 black"]["speed"]<1:
                        pieces["2 black"]["speed"]=1

                




               

                root.after(pieces["2 black"]["speed"],move_2_b)
                return


            root.after(2,move_2_b)
            return


                    




        else:
            pieces["2 black"]["st"]=0
            root.after(2,move_2_b)
            return


    else:
        root.after(2,move_2_b)
        return





def move_3_b():
    global pieces
    global game_st
    global st
    global turn
    global piece_r
    global moves

    if pieces["3 black"]["potted"]==1:

        root.after(2,move_3_b)
        return

    if st=="main":

        if pieces["3 black"]["move st"]==1:





            

            


            collusions("3 black")
            if pieces["3 black"]["st"]==0:
                

                try:

                    #print(pieces["3 black"]["proj_ang"])

                    pieces["3 black"]["coord_"]=pieces["3 black"]["coord"]
                    if pieces["3 black"]["proj_ang"]!=None:
                        pieces["3 black"]["data"]=get_pos("3 black",pieces["3 black"]["coord"][0],pieces["3 black"]["coord"][1],0,angle(pieces["3 black"]["proj_ang"]),0,0)
                        
                        pieces["3 black"]["angle"]=angle(pieces["3 black"]["proj_ang"])
                        pieces["3 black"]["proj_ang"]=None
                    else:

                        pieces["3 black"]["data"]=get_pos("3 black",pieces["3 black"]["coord"][0],pieces["3 black"]["coord"][1],0,angle(pieces["3 black"]["angle"]),0,0)
                    
                    #print(pieces["3 black"]["data"])
                    pieces["3 black"]["coord"]=[pieces["3 black"]["data"][0],pieces["3 black"]["data"][1]]
                    pieces["3 black"]["angle"]=angle(pieces["3 black"]["data"][3])

                    draw_piece_("3 black",1)


                    pieces["3 black"]["st"]=1

                except Exception as e:
                    	print("3black",e)
            elif pieces["3 black"]["st"]==1:

                pieces["3 black"]["data"]=get_pos("3 black",pieces["3 black"]["coord_"][0],pieces["3 black"]["coord_"][1],pieces["3 black"]["data"][2],angle(pieces["3 black"]["angle"]),pieces["3 black"]["data"][4],1)

                

                if pieces["3 black"]["data"]==1:
                	

                    pieces["3 black"]["potted"]=1
                    moves.append("3 black")

                    pieces["3 black"]["start_time"]=0
                    pieces["3 black"]["speed"]=0
                    pieces["3 black"]["initial_v"]=0
                    pieces["3 black"]["current_v"]=0

                    pieces["3 black"]["proj_ang"]=None
                    pieces["3 black"]["angle"]=0
                    
                    pieces["3 black"]["st"]=0
                    pieces["3 black"]["initial_v"]=0

                    pieces["3 black"]["move st"]=0

                    

                    pieces["3 black"]["coord"]=[-100,100]

                    draw_piece_("3 black",1)        

                    root.after(2,move_3_b)
                    return


                elif pieces["3 black"]["data"]==2:
                    pieces["3 black"]["st"]=0
                    pieces["3 black"]["angle"]=angle(pieces["3 black"]["proj_ang"])
                    draw_piece_("3 black",1)    


                else:

                    pieces["3 black"]["angle"]=angle(pieces["3 black"]["data"][3])
                    pieces["3 black"]["coord"]=[pieces["3 black"]["data"][0],pieces["3 black"]["data"][1]]


                    pieces["3 black"]["coord"]=[pieces["3 black"]["data"][0],pieces["3 black"]["data"][1]]
                    

                    

                    try:


                        if len(pieces["3 black"]["data"][4])==3:



                            pieces["3 black"]["proj_ang"]=angle(pieces["3 black"]["data"][4][1])

                    except Exception as e:
                    	print("3black",e)

                    draw_piece_("3 black",1)


                pieces["3 black"]["current_v"]=pieces["3 black"]["initial_v"]-0.05*9.8*(time.time()-pieces["3 black"]["start_time"])
                #print("3 black"," - ",pieces["3 black"]["current_v"])

                if int(pieces["3 black"]["current_v"])<0:



                    pieces["3 black"]["start_time"]=0
                    pieces["3 black"]["speed"]=0
                    pieces["3 black"]["initial_v"]=0
                    pieces["3 black"]["current_v"]=0



                    pieces["3 black"]["proj_ang"]=None
                    pieces["3 black"]["angle"]=0
                    
                    pieces["3 black"]["st"]=0
                    pieces["3 black"]["move st"]=0

                    

                    draw_piece_("3 black",1)        

                    root.after(2,move_3_b)
                    return
                else:

                    pieces["3 black"]["speed"]=int(round((1-pieces["3 black"]["current_v"]/3)*10,0))

                    if pieces["3 black"]["speed"]<1:
                        pieces["3 black"]["speed"]=1

                




               

                root.after(pieces["3 black"]["speed"],move_3_b)
                return


            root.after(2,move_3_b)
            return


                    




        else:
            pieces["3 black"]["st"]=0
            root.after(2,move_3_b)
            return


    else:
        root.after(2,move_3_b)
        return




def move_4_b():
    global pieces
    global game_st
    global st
    global turn
    global piece_r
    global moves

    if pieces["4 black"]["potted"]==1:

        root.after(2,move_4_b)
        return

    if st=="main":

        if pieces["4 black"]["move st"]==1:





            

            


            collusions("4 black")
            if pieces["4 black"]["st"]==0:
                

                try:

                    #print(pieces["4 black"]["proj_ang"])

                    pieces["4 black"]["coord_"]=pieces["4 black"]["coord"]
                    if pieces["4 black"]["proj_ang"]!=None:
                        pieces["4 black"]["data"]=get_pos("4 black",pieces["4 black"]["coord"][0],pieces["4 black"]["coord"][1],0,angle(pieces["4 black"]["proj_ang"]),0,0)
                        
                        pieces["4 black"]["angle"]=angle(pieces["4 black"]["proj_ang"])
                        pieces["4 black"]["proj_ang"]=None
                    else:

                        pieces["4 black"]["data"]=get_pos("4 black",pieces["4 black"]["coord"][0],pieces["4 black"]["coord"][1],0,angle(pieces["4 black"]["angle"]),0,0)
                    
                    #print(pieces["4 black"]["data"])
                    pieces["4 black"]["coord"]=[pieces["4 black"]["data"][0],pieces["4 black"]["data"][1]]
                    pieces["4 black"]["angle"]=angle(pieces["4 black"]["data"][3])

                    draw_piece_("4 black",1)


                    pieces["4 black"]["st"]=1

                except Exception as e:
                    	print("4black",e)
            elif pieces["4 black"]["st"]==1:

                pieces["4 black"]["data"]=get_pos("4 black",pieces["4 black"]["coord_"][0],pieces["4 black"]["coord_"][1],pieces["4 black"]["data"][2],angle(pieces["4 black"]["angle"]),pieces["4 black"]["data"][4],1)

                

                if pieces["4 black"]["data"]==1:
                	

                    pieces["4 black"]["potted"]=1
                    moves.append("4 black")

                    pieces["4 black"]["start_time"]=0
                    pieces["4 black"]["speed"]=0
                    pieces["4 black"]["initial_v"]=0
                    pieces["4 black"]["current_v"]=0

                    pieces["4 black"]["proj_ang"]=None
                    pieces["4 black"]["angle"]=0
                    
                    pieces["4 black"]["st"]=0
                    pieces["4 black"]["initial_v"]=0

                    pieces["4 black"]["move st"]=0

                    

                    pieces["4 black"]["coord"]=[-100,100]

                    draw_piece_("4 black",1)        

                    root.after(2,move_4_b)
                    return


                elif pieces["4 black"]["data"]==2:
                    pieces["4 black"]["st"]=0
                    pieces["4 black"]["angle"]=angle(pieces["4 black"]["proj_ang"])
                    draw_piece_("4 black",1)    


                else:

                    pieces["4 black"]["angle"]=angle(pieces["4 black"]["data"][3])
                    pieces["4 black"]["coord"]=[pieces["4 black"]["data"][0],pieces["4 black"]["data"][1]]


                    pieces["4 black"]["coord"]=[pieces["4 black"]["data"][0],pieces["4 black"]["data"][1]]
                    

                    

                    try:


                        if len(pieces["4 black"]["data"][4])==3:



                            pieces["4 black"]["proj_ang"]=angle(pieces["4 black"]["data"][4][1])

                    except Exception as e:
                    	print("4black",e)

                    draw_piece_("4 black",1)


                pieces["4 black"]["current_v"]=pieces["4 black"]["initial_v"]-0.05*9.8*(time.time()-pieces["4 black"]["start_time"])
                #print("4 black"," - ",pieces["4 black"]["current_v"])

                if int(pieces["4 black"]["current_v"])<0:



                    pieces["4 black"]["start_time"]=0
                    pieces["4 black"]["speed"]=0
                    pieces["4 black"]["initial_v"]=0
                    pieces["4 black"]["current_v"]=0



                    pieces["4 black"]["proj_ang"]=None
                    pieces["4 black"]["angle"]=0
                    
                    pieces["4 black"]["st"]=0
                    pieces["4 black"]["move st"]=0

                    

                    draw_piece_("4 black",1)        

                    root.after(2,move_4_b)
                    return
                else:

                    pieces["4 black"]["speed"]=int(round((1-pieces["4 black"]["current_v"]/3)*10,0))

                    if pieces["4 black"]["speed"]<1:
                        pieces["4 black"]["speed"]=1

                




               

                root.after(pieces["4 black"]["speed"],move_4_b)
                return


            root.after(2,move_4_b)
            return


                    




        else:
            pieces["4 black"]["st"]=0
            root.after(2,move_4_b)
            return


    else:
        root.after(2,move_4_b)
        return






def move_5_b():
    global pieces
    global game_st
    global st
    global turn
    global piece_r
    global moves

    if pieces["5 black"]["potted"]==1:

        root.after(2,move_5_b)
        return

    if st=="main":

        if pieces["5 black"]["move st"]==1:





            

            


            collusions("5 black")
            if pieces["5 black"]["st"]==0:
                

                try:

                    #print(pieces["5 black"]["proj_ang"])

                    pieces["5 black"]["coord_"]=pieces["5 black"]["coord"]
                    if pieces["5 black"]["proj_ang"]!=None:
                        pieces["5 black"]["data"]=get_pos("5 black",pieces["5 black"]["coord"][0],pieces["5 black"]["coord"][1],0,angle(pieces["5 black"]["proj_ang"]),0,0)
                        
                        pieces["5 black"]["angle"]=angle(pieces["5 black"]["proj_ang"])
                        pieces["5 black"]["proj_ang"]=None
                    else:

                        pieces["5 black"]["data"]=get_pos("5 black",pieces["5 black"]["coord"][0],pieces["5 black"]["coord"][1],0,angle(pieces["5 black"]["angle"]),0,0)
                    
                    #print(pieces["5 black"]["data"])
                    pieces["5 black"]["coord"]=[pieces["5 black"]["data"][0],pieces["5 black"]["data"][1]]
                    pieces["5 black"]["angle"]=angle(pieces["5 black"]["data"][3])

                    draw_piece_("5 black",1)


                    pieces["5 black"]["st"]=1

                except Exception as e:
                    	print("5black",e)
            elif pieces["5 black"]["st"]==1:

                pieces["5 black"]["data"]=get_pos("5 black",pieces["5 black"]["coord_"][0],pieces["5 black"]["coord_"][1],pieces["5 black"]["data"][2],angle(pieces["5 black"]["angle"]),pieces["5 black"]["data"][4],1)

                

                if pieces["5 black"]["data"]==1:
                	

                    pieces["5 black"]["potted"]=1
                    moves.append("5 black")

                    pieces["5 black"]["start_time"]=0
                    pieces["5 black"]["speed"]=0
                    pieces["5 black"]["initial_v"]=0
                    pieces["5 black"]["current_v"]=0

                    pieces["5 black"]["proj_ang"]=None
                    pieces["5 black"]["angle"]=0
                    
                    pieces["5 black"]["st"]=0
                    pieces["5 black"]["initial_v"]=0

                    pieces["5 black"]["move st"]=0

                    

                    pieces["5 black"]["coord"]=[-100,100]

                    draw_piece_("5 black",1)        

                    root.after(2,move_5_b)
                    return


                elif pieces["5 black"]["data"]==2:
                    pieces["5 black"]["st"]=0
                    pieces["5 black"]["angle"]=angle(pieces["5 black"]["proj_ang"])
                    draw_piece_("5 black",1)    


                else:

                    pieces["5 black"]["angle"]=angle(pieces["5 black"]["data"][3])
                    pieces["5 black"]["coord"]=[pieces["5 black"]["data"][0],pieces["5 black"]["data"][1]]


                    pieces["5 black"]["coord"]=[pieces["5 black"]["data"][0],pieces["5 black"]["data"][1]]
                    

                    

                    try:


                        if len(pieces["5 black"]["data"][4])==3:



                            pieces["5 black"]["proj_ang"]=angle(pieces["5 black"]["data"][4][1])

                    except Exception as e:
                    	print("5black",e)

                    draw_piece_("5 black",1)


                pieces["5 black"]["current_v"]=pieces["5 black"]["initial_v"]-0.05*9.8*(time.time()-pieces["5 black"]["start_time"])
                #print("5 black"," - ",pieces["5 black"]["current_v"])

                if int(pieces["5 black"]["current_v"])<0:



                    pieces["5 black"]["start_time"]=0
                    pieces["5 black"]["speed"]=0
                    pieces["5 black"]["initial_v"]=0
                    pieces["5 black"]["current_v"]=0



                    pieces["5 black"]["proj_ang"]=None
                    pieces["5 black"]["angle"]=0
                    
                    pieces["5 black"]["st"]=0
                    pieces["5 black"]["move st"]=0

                    

                    draw_piece_("5 black",1)        

                    root.after(2,move_5_b)
                    return
                else:

                    pieces["5 black"]["speed"]=int(round((1-pieces["5 black"]["current_v"]/3)*10,0))

                    if pieces["5 black"]["speed"]<1:
                        pieces["5 black"]["speed"]=1

                




               

                root.after(pieces["5 black"]["speed"],move_5_b)
                return


            root.after(2,move_5_b)
            return


                    




        else:
            pieces["5 black"]["st"]=0
            root.after(2,move_5_b)
            return


    else:
        root.after(2,move_5_b)
        return





def move_6_b():
    global pieces
    global game_st
    global st
    global turn
    global piece_r
    global moves

    if pieces["6 black"]["potted"]==1:

        root.after(2,move_6_b)
        return

    if st=="main":

        if pieces["6 black"]["move st"]==1:





            

            


            collusions("6 black")
            if pieces["6 black"]["st"]==0:
                

                try:

                    #print(pieces["6 black"]["proj_ang"])

                    pieces["6 black"]["coord_"]=pieces["6 black"]["coord"]
                    if pieces["6 black"]["proj_ang"]!=None:
                        pieces["6 black"]["data"]=get_pos("6 black",pieces["6 black"]["coord"][0],pieces["6 black"]["coord"][1],0,angle(pieces["6 black"]["proj_ang"]),0,0)
                        
                        pieces["6 black"]["angle"]=angle(pieces["6 black"]["proj_ang"])
                        pieces["6 black"]["proj_ang"]=None
                    else:

                        pieces["6 black"]["data"]=get_pos("6 black",pieces["6 black"]["coord"][0],pieces["6 black"]["coord"][1],0,angle(pieces["6 black"]["angle"]),0,0)
                    
                    #print(pieces["6 black"]["data"])
                    pieces["6 black"]["coord"]=[pieces["6 black"]["data"][0],pieces["6 black"]["data"][1]]
                    pieces["6 black"]["angle"]=angle(pieces["6 black"]["data"][3])

                    draw_piece_("6 black",1)


                    pieces["6 black"]["st"]=1

                except Exception as e:
                    	print("6black",e)
            elif pieces["6 black"]["st"]==1:

                pieces["6 black"]["data"]=get_pos("6 black",pieces["6 black"]["coord_"][0],pieces["6 black"]["coord_"][1],pieces["6 black"]["data"][2],angle(pieces["6 black"]["angle"]),pieces["6 black"]["data"][4],1)

                

                if pieces["6 black"]["data"]==1:
                	

                    pieces["6 black"]["potted"]=1
                    moves.append("6 black")

                    pieces["6 black"]["start_time"]=0
                    pieces["6 black"]["speed"]=0
                    pieces["6 black"]["initial_v"]=0
                    pieces["6 black"]["current_v"]=0

                    pieces["6 black"]["proj_ang"]=None
                    pieces["6 black"]["angle"]=0
                    
                    pieces["6 black"]["st"]=0
                    pieces["6 black"]["initial_v"]=0

                    pieces["6 black"]["move st"]=0

                    

                    pieces["6 black"]["coord"]=[-100,100]

                    draw_piece_("6 black",1)        

                    root.after(2,move_6_b)
                    return


                elif pieces["6 black"]["data"]==2:
                    pieces["6 black"]["st"]=0
                    pieces["6 black"]["angle"]=angle(pieces["6 black"]["proj_ang"])
                    draw_piece_("6 black",1)    


                else:

                    pieces["6 black"]["angle"]=angle(pieces["6 black"]["data"][3])
                    pieces["6 black"]["coord"]=[pieces["6 black"]["data"][0],pieces["6 black"]["data"][1]]


                    pieces["6 black"]["coord"]=[pieces["6 black"]["data"][0],pieces["6 black"]["data"][1]]
                    

                    

                    try:


                        if len(pieces["6 black"]["data"][4])==3:



                            pieces["6 black"]["proj_ang"]=angle(pieces["6 black"]["data"][4][1])

                    except Exception as e:
                    	print("6black",e)

                    draw_piece_("6 black",1)


                pieces["6 black"]["current_v"]=pieces["6 black"]["initial_v"]-0.05*9.8*(time.time()-pieces["6 black"]["start_time"])
                #print("6 black"," - ",pieces["6 black"]["current_v"])

                if int(pieces["6 black"]["current_v"])<0:



                    pieces["6 black"]["start_time"]=0
                    pieces["6 black"]["speed"]=0
                    pieces["6 black"]["initial_v"]=0
                    pieces["6 black"]["current_v"]=0



                    pieces["6 black"]["proj_ang"]=None
                    pieces["6 black"]["angle"]=0
                    
                    pieces["6 black"]["st"]=0
                    pieces["6 black"]["move st"]=0

                    

                    draw_piece_("6 black",1)        

                    root.after(2,move_6_b)
                    return
                else:

                    pieces["6 black"]["speed"]=int(round((1-pieces["6 black"]["current_v"]/3)*10,0))

                    if pieces["6 black"]["speed"]<1:
                        pieces["6 black"]["speed"]=1

                




               

                root.after(pieces["6 black"]["speed"],move_6_b)
                return


            root.after(2,move_6_b)
            return


                    




        else:
            pieces["6 black"]["st"]=0
            root.after(2,move_6_b)
            return


    else:
        root.after(2,move_6_b)
        return






def move_7_b():
    global pieces
    global game_st
    global st
    global turn
    global piece_r
    global moves

    if pieces["7 black"]["potted"]==1:

        root.after(2,move_7_b)
        return

    if st=="main":

        if pieces["7 black"]["move st"]==1:





            

            


            collusions("7 black")
            if pieces["7 black"]["st"]==0:
                

                try:

                    #print(pieces["7 black"]["proj_ang"])

                    pieces["7 black"]["coord_"]=pieces["7 black"]["coord"]
                    if pieces["7 black"]["proj_ang"]!=None:
                        pieces["7 black"]["data"]=get_pos("7 black",pieces["7 black"]["coord"][0],pieces["7 black"]["coord"][1],0,angle(pieces["7 black"]["proj_ang"]),0,0)
                        
                        pieces["7 black"]["angle"]=angle(pieces["7 black"]["proj_ang"])
                        pieces["7 black"]["proj_ang"]=None
                    else:

                        pieces["7 black"]["data"]=get_pos("7 black",pieces["7 black"]["coord"][0],pieces["7 black"]["coord"][1],0,angle(pieces["7 black"]["angle"]),0,0)
                    
                    #print(pieces["7 black"]["data"])
                    pieces["7 black"]["coord"]=[pieces["7 black"]["data"][0],pieces["7 black"]["data"][1]]
                    pieces["7 black"]["angle"]=angle(pieces["7 black"]["data"][3])

                    draw_piece_("7 black",1)


                    pieces["7 black"]["st"]=1

                except Exception as e:
                    	print("7black",e)
            elif pieces["7 black"]["st"]==1:

                pieces["7 black"]["data"]=get_pos("7 black",pieces["7 black"]["coord_"][0],pieces["7 black"]["coord_"][1],pieces["7 black"]["data"][2],angle(pieces["7 black"]["angle"]),pieces["7 black"]["data"][4],1)

                

                if pieces["7 black"]["data"]==1:
                	

                    pieces["7 black"]["potted"]=1
                    moves.append("7 black")

                    pieces["7 black"]["start_time"]=0
                    pieces["7 black"]["speed"]=0
                    pieces["7 black"]["initial_v"]=0
                    pieces["7 black"]["current_v"]=0

                    pieces["7 black"]["proj_ang"]=None
                    pieces["7 black"]["angle"]=0
                    
                    pieces["7 black"]["st"]=0
                    pieces["7 black"]["initial_v"]=0

                    pieces["7 black"]["move st"]=0

                    

                    pieces["7 black"]["coord"]=[-100,100]

                    draw_piece_("7 black",1)        

                    root.after(2,move_7_b)
                    return


                elif pieces["7 black"]["data"]==2:
                    pieces["7 black"]["st"]=0
                    pieces["7 black"]["angle"]=angle(pieces["7 black"]["proj_ang"])
                    draw_piece_("7 black",1)    


                else:

                    pieces["7 black"]["angle"]=angle(pieces["7 black"]["data"][3])
                    pieces["7 black"]["coord"]=[pieces["7 black"]["data"][0],pieces["7 black"]["data"][1]]


                    pieces["7 black"]["coord"]=[pieces["7 black"]["data"][0],pieces["7 black"]["data"][1]]
                    

                    

                    try:


                        if len(pieces["7 black"]["data"][4])==3:



                            pieces["7 black"]["proj_ang"]=angle(pieces["7 black"]["data"][4][1])

                    except Exception as e:
                    	print("7black",e)

                    draw_piece_("7 black",1)


                pieces["7 black"]["current_v"]=pieces["7 black"]["initial_v"]-0.05*9.8*(time.time()-pieces["7 black"]["start_time"])
                #print("7 black"," - ",pieces["7 black"]["current_v"])

                if int(pieces["7 black"]["current_v"])<0:



                    pieces["7 black"]["start_time"]=0
                    pieces["7 black"]["speed"]=0
                    pieces["7 black"]["initial_v"]=0
                    pieces["7 black"]["current_v"]=0



                    pieces["7 black"]["proj_ang"]=None
                    pieces["7 black"]["angle"]=0
                    
                    pieces["7 black"]["st"]=0
                    pieces["7 black"]["move st"]=0

                    

                    draw_piece_("7 black",1)        

                    root.after(2,move_7_b)
                    return
                else:

                    pieces["7 black"]["speed"]=int(round((1-pieces["7 black"]["current_v"]/3)*10,0))

                    if pieces["7 black"]["speed"]<1:
                        pieces["7 black"]["speed"]=1

                




               

                root.after(pieces["7 black"]["speed"],move_7_b)
                return


            root.after(2,move_7_b)
            return


                    




        else:
            pieces["7 black"]["st"]=0
            root.after(2,move_7_b)
            return


    else:
        root.after(2,move_7_b)
        return




def move_8_b():
    global pieces
    global game_st
    global st
    global turn
    global piece_r
    global moves

    if pieces["8 black"]["potted"]==1:

        root.after(2,move_8_b)
        return

    if st=="main":

        if pieces["8 black"]["move st"]==1:





            

            


            collusions("8 black")
            if pieces["8 black"]["st"]==0:
                

                try:

                    #print(pieces["8 black"]["proj_ang"])

                    pieces["8 black"]["coord_"]=pieces["8 black"]["coord"]
                    if pieces["8 black"]["proj_ang"]!=None:
                        pieces["8 black"]["data"]=get_pos("8 black",pieces["8 black"]["coord"][0],pieces["8 black"]["coord"][1],0,angle(pieces["8 black"]["proj_ang"]),0,0)
                        
                        pieces["8 black"]["angle"]=angle(pieces["8 black"]["proj_ang"])
                        pieces["8 black"]["proj_ang"]=None
                    else:

                        pieces["8 black"]["data"]=get_pos("8 black",pieces["8 black"]["coord"][0],pieces["8 black"]["coord"][1],0,angle(pieces["8 black"]["angle"]),0,0)
                    
                    #print(pieces["8 black"]["data"])
                    pieces["8 black"]["coord"]=[pieces["8 black"]["data"][0],pieces["8 black"]["data"][1]]
                    pieces["8 black"]["angle"]=angle(pieces["8 black"]["data"][3])

                    draw_piece_("8 black",1)


                    pieces["8 black"]["st"]=1

                except Exception as e:
                    	print("8black",e)
            elif pieces["8 black"]["st"]==1:

                pieces["8 black"]["data"]=get_pos("8 black",pieces["8 black"]["coord_"][0],pieces["8 black"]["coord_"][1],pieces["8 black"]["data"][2],angle(pieces["8 black"]["angle"]),pieces["8 black"]["data"][4],1)

                

                if pieces["8 black"]["data"]==1:

                	

                    pieces["8 black"]["potted"]=1
                    moves.append("8 black")

                    pieces["8 black"]["start_time"]=0
                    pieces["8 black"]["speed"]=0
                    pieces["8 black"]["initial_v"]=0
                    pieces["8 black"]["current_v"]=0

                    pieces["8 black"]["proj_ang"]=None
                    pieces["8 black"]["angle"]=0
                    
                    pieces["8 black"]["st"]=0
                    pieces["8 black"]["initial_v"]=0

                    pieces["8 black"]["move st"]=0

                    

                    pieces["8 black"]["coord"]=[-100,100]

                    draw_piece_("8 black",1)        

                    root.after(2,move_8_b)
                    return


                elif pieces["8 black"]["data"]==2:
                    pieces["8 black"]["st"]=0
                    pieces["8 black"]["angle"]=angle(pieces["8 black"]["proj_ang"])
                    draw_piece_("8 black",1)    


                else:

                    pieces["8 black"]["angle"]=angle(pieces["8 black"]["data"][3])
                    pieces["8 black"]["coord"]=[pieces["8 black"]["data"][0],pieces["8 black"]["data"][1]]


                    pieces["8 black"]["coord"]=[pieces["8 black"]["data"][0],pieces["8 black"]["data"][1]]
                    

                    

                    try:


                        if len(pieces["8 black"]["data"][4])==3:



                            pieces["8 black"]["proj_ang"]=angle(pieces["8 black"]["data"][4][1])

                    except Exception as e:
                    	print("8black",e)

                    draw_piece_("8 black",1)


                pieces["8 black"]["current_v"]=pieces["8 black"]["initial_v"]-0.05*9.8*(time.time()-pieces["8 black"]["start_time"])
                #print("8 black"," - ",pieces["8 black"]["current_v"])

                if int(pieces["8 black"]["current_v"])<0:



                    pieces["8 black"]["start_time"]=0
                    pieces["8 black"]["speed"]=0
                    pieces["8 black"]["initial_v"]=0
                    pieces["8 black"]["current_v"]=0



                    pieces["8 black"]["proj_ang"]=None
                    pieces["8 black"]["angle"]=0
                    
                    pieces["8 black"]["st"]=0
                    pieces["8 black"]["move st"]=0

                    

                    draw_piece_("8 black",1)        

                    root.after(2,move_8_b)
                    return
                else:

                    pieces["8 black"]["speed"]=int(round((1-pieces["8 black"]["current_v"]/3)*10,0))

                    if pieces["8 black"]["speed"]<1:
                        pieces["8 black"]["speed"]=1

                




               

                root.after(pieces["8 black"]["speed"],move_8_b)
                return


            root.after(2,move_8_b)
            return


                    




        else:
            pieces["8 black"]["st"]=0
            root.after(2,move_8_b)
            return


    else:
        root.after(2,move_8_b)
        return





def move_9_b():
    global pieces
    global game_st
    global st
    global turn
    global piece_r
    global moves

    if pieces["9 black"]["potted"]==1:

        root.after(2,move_9_b)
        return

    if st=="main":

        if pieces["9 black"]["move st"]==1:





            

            


            collusions("9 black")
            if pieces["9 black"]["st"]==0:
                

                try:

                    #print(pieces["9 black"]["proj_ang"])

                    pieces["9 black"]["coord_"]=pieces["9 black"]["coord"]
                    if pieces["9 black"]["proj_ang"]!=None:
                        pieces["9 black"]["data"]=get_pos("9 black",pieces["9 black"]["coord"][0],pieces["9 black"]["coord"][1],0,angle(pieces["9 black"]["proj_ang"]),0,0)
                        
                        pieces["9 black"]["angle"]=angle(pieces["9 black"]["proj_ang"])
                        pieces["9 black"]["proj_ang"]=None
                    else:

                        pieces["9 black"]["data"]=get_pos("9 black",pieces["9 black"]["coord"][0],pieces["9 black"]["coord"][1],0,angle(pieces["9 black"]["angle"]),0,0)
                    
                    #print(pieces["9 black"]["data"])
                    pieces["9 black"]["coord"]=[pieces["9 black"]["data"][0],pieces["9 black"]["data"][1]]
                    pieces["9 black"]["angle"]=angle(pieces["9 black"]["data"][3])

                    draw_piece_("9 black",1)


                    pieces["9 black"]["st"]=1

                except Exception as e:
                    	print("9black",e)
            elif pieces["9 black"]["st"]==1:

                pieces["9 black"]["data"]=get_pos("9 black",pieces["9 black"]["coord_"][0],pieces["9 black"]["coord_"][1],pieces["9 black"]["data"][2],angle(pieces["9 black"]["angle"]),pieces["9 black"]["data"][4],1)

                

                if pieces["9 black"]["data"]==1:

                	

                    pieces["9 black"]["potted"]=1
                    moves.append("9 black")

                    pieces["9 black"]["start_time"]=0
                    pieces["9 black"]["speed"]=0
                    pieces["9 black"]["initial_v"]=0
                    pieces["9 black"]["current_v"]=0

                    pieces["9 black"]["proj_ang"]=None
                    pieces["9 black"]["angle"]=0
                    
                    pieces["9 black"]["st"]=0
                    pieces["9 black"]["initial_v"]=0

                    pieces["9 black"]["move st"]=0

                    

                    pieces["9 black"]["coord"]=[-100,100]

                    draw_piece_("9 black",1)        

                    root.after(2,move_9_b)
                    return


                elif pieces["9 black"]["data"]==2:
                    pieces["9 black"]["st"]=0
                    pieces["9 black"]["angle"]=angle(pieces["9 black"]["proj_ang"])
                    draw_piece_("9 black",1)    


                else:

                    pieces["9 black"]["angle"]=angle(pieces["9 black"]["data"][3])
                    pieces["9 black"]["coord"]=[pieces["9 black"]["data"][0],pieces["9 black"]["data"][1]]


                    pieces["9 black"]["coord"]=[pieces["9 black"]["data"][0],pieces["9 black"]["data"][1]]
                    

                    

                    try:


                        if len(pieces["9 black"]["data"][4])==3:



                            pieces["9 black"]["proj_ang"]=angle(pieces["9 black"]["data"][4][1])

                    except Exception as e:
                    	print("9black",e)

                    draw_piece_("9 black",1)


                pieces["9 black"]["current_v"]=pieces["9 black"]["initial_v"]-0.05*9.8*(time.time()-pieces["9 black"]["start_time"])
                #print("9 black"," - ",pieces["9 black"]["current_v"])

                if int(pieces["9 black"]["current_v"])<0:



                    pieces["9 black"]["start_time"]=0
                    pieces["9 black"]["speed"]=0
                    pieces["9 black"]["initial_v"]=0
                    pieces["9 black"]["current_v"]=0



                    pieces["9 black"]["proj_ang"]=None
                    pieces["9 black"]["angle"]=0
                    
                    pieces["9 black"]["st"]=0
                    pieces["9 black"]["move st"]=0

                    

                    draw_piece_("9 black",1)        

                    root.after(2,move_9_b)
                    return
                else:

                    pieces["9 black"]["speed"]=int(round((1-pieces["9 black"]["current_v"]/3)*10,0))

                    if pieces["9 black"]["speed"]<1:
                        pieces["9 black"]["speed"]=1

                




               

                root.after(pieces["9 black"]["speed"],move_9_b)
                return


            root.after(2,move_9_b)
            return


                    




        else:
            pieces["9 black"]["st"]=0
            root.after(2,move_9_b)
            return


    else:
        root.after(2,move_9_b)
        return









def move_red():
    global pieces
    global game_st
    global st
    global turn
    global piece_r
    global moves

    if pieces["red"]["potted"]==1:

        root.after(2,move_red)
        return

    if st=="main":

        if pieces["red"]["move st"]==1:





            

            


            collusions("red")
            if pieces["red"]["st"]==0:
                

                try:

                    #print(pieces["red"]["proj_ang"])

                    pieces["red"]["coord_"]=pieces["red"]["coord"]
                    if pieces["red"]["proj_ang"]!=None:
                        pieces["red"]["data"]=get_pos("red",pieces["red"]["coord"][0],pieces["red"]["coord"][1],0,angle(pieces["red"]["proj_ang"]),0,0)
                        
                        pieces["red"]["angle"]=angle(pieces["red"]["proj_ang"])
                        pieces["red"]["proj_ang"]=None
                    else:

                        pieces["red"]["data"]=get_pos("red",pieces["red"]["coord"][0],pieces["red"]["coord"][1],0,angle(pieces["red"]["angle"]),0,0)
                    
                    #print(pieces["red"]["data"])
                    pieces["red"]["coord"]=[pieces["red"]["data"][0],pieces["red"]["data"][1]]
                    pieces["red"]["angle"]=angle(pieces["red"]["data"][3])

                    draw_piece_("red",1)


                    pieces["red"]["st"]=1

                except Exception as e:
                    	print("red",e)
            elif pieces["red"]["st"]==1:

                pieces["red"]["data"]=get_pos("red",pieces["red"]["coord_"][0],pieces["red"]["coord_"][1],pieces["red"]["data"][2],angle(pieces["red"]["angle"]),pieces["red"]["data"][4],1)

                

                if pieces["red"]["data"]==1:
                	

                    pieces["red"]["potted"]=1
                    moves.append("red")

                    pieces["red"]["start_time"]=0
                    pieces["red"]["speed"]=0
                    pieces["red"]["initial_v"]=0
                    pieces["red"]["current_v"]=0

                    pieces["red"]["proj_ang"]=None
                    pieces["red"]["angle"]=0
                    
                    pieces["red"]["st"]=0
                    pieces["red"]["initial_v"]=0

                    pieces["red"]["move st"]=0

                    

                    pieces["red"]["coord"]=[-100,100]

                    draw_piece_("red",1)        

                    root.after(2,move_red)
                    return


                elif pieces["red"]["data"]==2:
                    pieces["red"]["st"]=0
                    pieces["red"]["angle"]=angle(pieces["red"]["proj_ang"])
                    draw_piece_("red",1)    


                else:

                    pieces["red"]["angle"]=angle(pieces["red"]["data"][3])
                    pieces["red"]["coord"]=[pieces["red"]["data"][0],pieces["red"]["data"][1]]


                    pieces["red"]["coord"]=[pieces["red"]["data"][0],pieces["red"]["data"][1]]
                    

                    

                    try:


                        if len(pieces["red"]["data"][4])==3:



                            pieces["red"]["proj_ang"]=angle(pieces["red"]["data"][4][1])

                    except Exception as e:
                    	print("red",e)

                    draw_piece_("red",1)


                pieces["red"]["current_v"]=pieces["red"]["initial_v"]-0.05*9.8*(time.time()-pieces["red"]["start_time"])
                #print("red"," - ",pieces["red"]["current_v"])

                if int(pieces["red"]["current_v"])<0:



                    pieces["red"]["start_time"]=0
                    pieces["red"]["speed"]=0
                    pieces["red"]["initial_v"]=0
                    pieces["red"]["current_v"]=0



                    pieces["red"]["proj_ang"]=None
                    pieces["red"]["angle"]=0
                    
                    pieces["red"]["st"]=0
                    pieces["red"]["move st"]=0

                    

                    draw_piece_("red",1)        

                    root.after(2,move_red)
                    return
                else:

                    pieces["red"]["speed"]=int(round((1-pieces["red"]["current_v"]/3)*10,0))

                    if pieces["red"]["speed"]<1:
                        pieces["red"]["speed"]=1

                




               

                root.after(pieces["red"]["speed"],move_red)
                return


            root.after(2,move_red)
            return


                    




        else:
            pieces["red"]["st"]=0
            root.after(2,move_red)
            return


    else:
        root.after(2,move_red)
        return





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


	#print(first_move)

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
go_i=[0,0,0,0,0,0,0]

def go(winner):
	global go_st,go_im,go_coord,go_st
	global bg2

	go_st=1

	draw_move_()

	go_i[6]=can.create_image(0,0,image=bg2,anchor="nw")

	xx,yy=250,100

	x=(w-xx)/2
	y=(h-yy)/2


	im=draw_rounded_rect(x,y,x+xx,y+yy,15,(0,0,0),(255,0,0),180,255,1)
	go_im=ImageTk.PhotoImage(im)

	go_i[0]=can.create_image(x,y,image=go_im,anchor="nw")

	go_i[1]=can.create_text(x+xx/2,y+20, text=f"{winner} wins!", font=("FreeMono",13),fill="#ff0000")

	go_i[2]=can.create_line(x+1,y+yy-30, x+xx-1,y+yy-30,fill="#770000")

	go_i[3]=can.create_line(x+xx/2,y+yy-30, x+xx/2,y+yy-1,fill="#770000")

	go_i[4]=can.create_text(x+xx/4,y+yy-15,text="Main Menu",font=("FreeMono",13),fill="#ff0000")

	go_i[5]=can.create_text(x+xx-xx/4,y+yy-15,text="Quit",font=("FreeMono",13),fill="#ff0000")

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
root.resizable(0,0)
root.title("HCarrom")
root.iconbitmap("data/icon.ico")


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

