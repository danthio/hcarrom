from PIL import Image,ImageTk,ImageDraw
import tkinter as tk
import math
import time
import random

bg=0
circle=0
bg2=0
def load_im():
	global w,h
	global bg,bg2,circle



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

	im=Image.new("RGBA",(500,500),(0,0,0,0))
	draw=ImageDraw.Draw(im)

	draw.ellipse((0,0,500,500),fill=(255,0,0,255),outline=(255,0,0,255))

	im=im.resize((30,30))

	circle=ImageTk.PhotoImage(im)

	im=Image.new("RGBA",(w,h),(0,0,0,160))
	bg2=ImageTk.PhotoImage(im)


st=""
pos_intro=[]
def intro():
	global bg2,circle
	global st
	global w,h
	global pos_intro

	pos_intro=[]

	st="intro"

	can.delete("all")

	can.create_image(0,0,image=bg,anchor="nw")

	can.create_image(0,0,image=bg2,anchor="nw")

	x=200

	y=(h-90)/2

	can.create_image(w/2-x/2,y,image=circle,anchor="nw")
	can.create_image(w/2+x/2-30,y,image=circle,anchor="nw")

	can.create_rectangle(w/2-x/2+15,y, w/2+x/2-15,y+30-1,fill="#ff0000",outline="#ff0000")

	can.create_text(w/2,y+15,text="Carrom",font=("FreeMono",13),fill="#000000",anchor="c")

	pos_intro.append([w/2-x/2+15,y, w/2+x/2-15,y+30-1])


	y+=60


	can.create_image(w/2-x/2,y,image=circle,anchor="nw")
	can.create_image(w/2+x/2-30,y,image=circle,anchor="nw")

	can.create_rectangle(w/2-x/2+15,y, w/2+x/2-15,y+30-1,fill="#ff0000",outline="#ff0000")

	can.create_text(w/2,y+15,text="Disk Pool",font=("FreeMono",13),fill="#000000",anchor="c")

	pos_intro.append([w/2-x/2+15,y, w/2+x/2-15,y+30-1])

def main():
	global bg
	global st
	global pieces
	global striker_r,piece_r

	st="main"

	can.delete("all")


	can.create_image(0,0,image=bg,anchor="nw")

	for i in pieces:

		if i=="striker":

			draw_piece_(striker_r,i,"#323232","#ffffff")

		else:

			if i.split(" ")[-1]=="white":
				col1="#ffffff"
				col2="#000000"

			elif i.split(" ")[-1]=="black":
				col1="#000000"
				col2="#ffffff"
			draw_piece_(piece_r,i,col1,col2)




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
def can_b1(e):
	global st
	global drag_st,game_st
	global pieces
	global pos_intro
	global game
	global dm_vs

	#global r


	#draw_piece(e.x,e.x,r)


	if st=="intro":

		#carrom
		
		cx,cy=pos_intro[0][0],pos_intro[0][1]+15

		r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

		if r<=15:

			game="carrom"

			main()

			return


		cx,cy=pos_intro[0][2],pos_intro[0][1]+15

		r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

		if r<=15:
			game="carrom"

			main()

			return

		if pos_intro[0][0]<=e.x<=pos_intro[0][2]:

			if pos_intro[0][1]<=e.y<=pos_intro[0][3]:

				game="carrom"
				

				main()

				return



		#disk pool



		cx,cy=pos_intro[1][0],pos_intro[1][1]+15

		r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

		if r<=15:

			game="disk pool"

			main()

			return


		cx,cy=pos_intro[1][2],pos_intro[1][1]+15

		r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

		if r<=15:

			game="disk pool"

			main()

			return

		if pos_intro[1][0]<=e.x<=pos_intro[1][2]:

			if pos_intro[1][1]<=e.y<=pos_intro[1][3]:
				
				game="disk pool"

				main()


				return



	elif st=="main":



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
							draw_piece_(striker_r,"striker","#323232","#ffffff",1)
							


							return


					cx,cy=102,82

					r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

					if r<=10.36:
						pieces["striker"]["coord"][0]=xrng[0]

						for i in dm_vs:

							can.delete(i)

						draw_piece_(striker_r,"striker","#323232","#ffffff",1)
						return

					cx,cy=383,82

					r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

					if r<=10.36:
						pieces["striker"]["coord"][0]=xrng[1]



						for i in dm_vs:

							can.delete(i)

						draw_piece_(striker_r,"striker","#323232","#ffffff",1)
						return



				elif turn==1:

					if 102<=e.x<=383:
						if 404-10.36<=e.y<=404+10.36:
							pieces["striker"]["coord"][0]=e.x



							for i in dm_vs:

								can.delete(i)
							draw_piece_(striker_r,"striker","#323232","#ffffff",1)

							return


					cx,cy=102,404

					r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

					if r<=10.36:
						pieces["striker"]["coord"][0]=xrng[0]


						for i in dm_vs:

							can.delete(i)

						draw_piece_(striker_r,"striker","#323232","#ffffff",1)
						return

					cx,cy=383,404

					r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

					if r<=10.36:
						pieces["striker"]["coord"][0]=xrng[1]


						for i in dm_vs:

							can.delete(i)

						draw_piece_(striker_r,"striker","#323232","#ffffff",1)
						return





		if game_st==0:
			game_st=1


	print(st)












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
					draw_piece_(striker_r,"striker","#323232","#ffffff",1)



def can_b1_release(e):
	global drag_st,game_st
	global st
	global reset_st
	global pieces
	global dm_vs


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
			pieces["striker"]["start_time"]=time.time()



def collusions(pc):
	global pieces
	global striker_r,piece_r


	if pieces[pc]["current_v"]==0:
		return

	for p_ in pieces:

		if p_ ==pc:
			continue




		x1,y1=pieces[pc]["coord"]

		if pc=="striker":

			rr=striker_r
		else:
			rr=piece_r

		x1=(rr)*math.sin(math.radians(pieces[pc]["angle"]))+x1
		y1=(rr)*math.cos(math.radians(pieces[pc]["angle"]))+y1

		x2,y2=pieces[p_]["coord"]

		_r=math.sqrt((x2-x1)**2+(y2-y1)**2)

		if p_=="striker":

			rr=striker_r
		else:
			rr=piece_r

		#print(_r,rr)

		if int(_r-1)<=rr+3:
			#print("ok",_r-1)
			
			a=get_ang([x1,y1],[x2,y2])





			if pieces[p_]["move st"]==0:
				pieces[p_]["move st"]=1

				pieces[p_]["angle"]=a+180
				pieces[p_]["initial_v"]=pieces[pc]["current_v"]
				pieces[p_]["current_v"]=0
				pieces[p_]["start_time"]=time.time()
			else:
				pieces[p_]["proj_ang"]=a+180
				pieces[p_]["st"]=0
				pieces[p_]["initial_v"]=pieces[pc]["current_v"]
				pieces[p_]["current_v"]=0
				pieces[p_]["start_time"]=time.time()






			pieces[pc]["proj_ang"]=a
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

					ang=math.degrees(math.atan(o/a))

					ang=90-ang

					#print(ang)
				else:

					a=cy-e.y
					o=e.x-cx


					ang=math.degrees(math.atan(o/a))

					ang=90-ang

					ang+=90

					#print(ang)

			else:



				if e.y>=cy:

					a=cx-e.x
					o=e.y-cy

					ang=math.degrees(math.atan(o/a))

					ang+=270

					#print(ang)



				else:

					a=cx-e.x
					o=cy-e.y


					ang=math.degrees(math.atan(o/a))

					ang=90-ang

					ang+=180




					#print(ang)


			def find_r(cx,cy,ang):
				global boundary
				global striker_r
				global dm_vs
				global can
				global dm_coord
				global pieces,striker_r,piece_r
				global dm_piece_mv

				#collusions




				r_=0

				for _ in range(600):

					#print(r_)


					x=r_*math.sin(math.radians(ang))+cx
					y=r_*math.cos(math.radians(ang))+cy


					x2=(r_+striker_r+1)*math.sin(math.radians(ang))+cx
					y2=(r_+striker_r+1)*math.cos(math.radians(ang))+cy

					for p in pieces:

						xx,yy=pieces[p]["coord"]

						if p=="striker":
							_r=striker_r
						else:
							_r=piece_r

						rr=math.sqrt((xx-x2)**2+(yy-y2)**2)

						if rr<=_r:

							dm_coord=[cx,cy,x,y]

							a=get_ang([x2,y2],[xx,yy])+180

							

							dm_piece_mv=[a,xx,yy]




							draw_move_()

							return



					

					r_+=1






				#0,0

				r_=0

				for _ in range(600):

					#print(r_)


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

					#print(r_)


					x=r_*math.sin(math.radians(ang))+cx
					y=r_*math.cos(math.radians(ang))+cy

					x2=(r_+striker_r)*math.sin(math.radians(ang))+cx
					y2=(r_+striker_r)*math.cos(math.radians(ang))+cy

					

					if boundary[1][2]-boundary[0]<=x2<=boundary[1][2]:
						if boundary[1][1]<=y2<=boundary[1][1]+boundary[0]:

							#print("ok")

							r2=math.sqrt((x2-(boundary[1][2]-boundary[0]))**2+(y2-(boundary[1][1]+boundary[0]))**2)

							if r2>boundary[0]:






								dm_coord=[cx,cy,x,y]
								draw_move_()

								return

					
					r_+=1



				#1,1







				r_=0

				for _ in range(600):

					#print(r_)


					x=r_*math.sin(math.radians(ang))+cx
					y=r_*math.cos(math.radians(ang))+cy

					x2=(r_+striker_r)*math.sin(math.radians(ang))+cx
					y2=(r_+striker_r)*math.cos(math.radians(ang))+cy


					

					if boundary[1][2]-boundary[0]<=x2<=boundary[1][2]:
						if boundary[1][3]-boundary[0]<=y2<=boundary[1][3]:

							#print("ok")

							r2=math.sqrt((x2-(boundary[1][2]-boundary[0]))**2+(y2-(boundary[1][3]-boundary[0]))**2)

							if r2>boundary[0]:






								dm_coord=[cx,cy,x,y]
								draw_move_()

								return

					
					r_+=1




				#0,1







				r_=0

				for _ in range(600):

					#print(r_)


					x=r_*math.sin(math.radians(ang))+cx
					y=r_*math.cos(math.radians(ang))+cy

					x2=(r_+striker_r)*math.sin(math.radians(ang))+cx
					y2=(r_+striker_r)*math.cos(math.radians(ang))+cy

					

					if boundary[1][0]<=x2<=boundary[1][0]+boundary[0]:
						if boundary[1][3]-boundary[0]<=y2<=boundary[1][3]:

							#print("ok")

							r2=math.sqrt((x2-(boundary[1][0]+boundary[0]))**2+(y2-(boundary[1][3]-boundary[0]))**2)

							if r2>boundary[0]:




								dm_coord=[cx,cy,x,y]
								draw_move_()

								return

					
					r_+=1



				#left

				r_=0

				for _ in range(600):

					#print(r_)


					x=r_*math.sin(math.radians(ang))+cx
					y=r_*math.cos(math.radians(ang))+cy

					x2=(striker_r+1)*math.sin(math.radians(270))+x
					y2=(striker_r+1)*math.cos(math.radians(270))+y



					if x2<boundary[1][0]:

						if boundary[1][1]<=y2<=boundary[1][3]:




							dm_coord=[cx,cy,x,y]
							draw_move_()

							return

					r_+=1



				#right

				r_=0

				for _ in range(600):

					#print(r_)


					x=r_*math.sin(math.radians(ang))+cx
					y=r_*math.cos(math.radians(ang))+cy

					x2=(striker_r+1)*math.sin(math.radians(90))+x
					y2=(striker_r+1)*math.cos(math.radians(90))+y



					if x2>boundary[1][2]:

						if boundary[1][1]<=y2<=boundary[1][3]:






							dm_coord=[cx,cy,x,y]
							draw_move_()

							return

					r_+=1



				#up

				r_=0

				for _ in range(600):

					#print(r_)


					x=r_*math.sin(math.radians(ang))+cx
					y=r_*math.cos(math.radians(ang))+cy


					x2=(striker_r+1)*math.sin(math.radians(180))+x
					y2=(striker_r+1)*math.cos(math.radians(180))+y


					if y2<boundary[1][1]:

						if boundary[1][0]<=x2<=boundary[1][2]:






							dm_coord=[cx,cy,x,y]
							draw_move_()

							return

					r_+=1


				#down

				r_=0

				for _ in range(600):

					#print(r_)


					x=r_*math.sin(math.radians(ang))+cx
					y=r_*math.cos(math.radians(ang))+cy

					x2=(striker_r+1)*math.sin(math.radians(0))+x
					y2=(striker_r+1)*math.cos(math.radians(0))+y


					if y2>boundary[1][3]:

						if boundary[1][0]<=x2<=boundary[1][2]:






							dm_coord=[cx,cy,x,y]
							draw_move_()

							return

					r_+=1


			find_r(cx,cy,ang)

			pieces["striker"]["angle"]=ang





			

		except:
			pass


dm_coord=[0,0,0,0]
dm_vs=[0,0,0,0,0,0]
dm_piece_mv=[0,0,0]
def draw_move_(con=0):
	global can
	global striker_r
	global pieces
	global dm_vs,dm_coord
	global st
	global dm_piece_mv

	if st=="main":


		for i in dm_vs:

			can.delete(i)


		if con==0:

			cx,cy,x,y=dm_coord

			rr=100

			dm_vs[0]=can.create_line(cx,cy, x,y,fill="#ff0000")
			dm_vs[1]=can.create_oval(x-striker_r,y-striker_r, x+striker_r,y+striker_r ,outline="#ff0000")
			dm_vs[2]=can.create_oval(cx-rr,cy-rr, cx+rr,cy+rr ,outline="#ff0000")

			im=Image.new("RGBA",(500,500),(0,0,0,0))

			draw=ImageDraw.Draw(im)

			draw.ellipse((0,0, 500,500),fill=(255,0,0,128),outline=(255,0,0,128))

			sz=int(round(pieces["striker"]["initial_v"]*rr/3,0))

			


			if not sz==0:

				im=im.resize((sz*2,sz*2))

				dm_vs[3]=ImageTk.PhotoImage(im)

				dm_vs[4]=can.create_image(cx,cy,image=dm_vs[3])



			if not dm_piece_mv==[0,0,0]:



				x=50*math.sin(math.radians(dm_piece_mv[0]))+dm_piece_mv[1]
				y=50*math.cos(math.radians(dm_piece_mv[0]))+dm_piece_mv[2]


				dm_vs[4]=can.create_line(dm_piece_mv[1],dm_piece_mv[2], x,y,fill="#ff0000")


			dm_piece_mv=[0,0,0]





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

	if collusions(pc)==1:

		return 2

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


					if cy<=y:

						o=cx-x
						a=y-cy


						if o<0:
							o=-o
						if a<0:
							a=-a


						_a_=math.degrees(math.atan(o/a))

					else:

						o=cx-x
						a=cy-y


						if o<0:
							o=-o
						if a<0:
							a=-a


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

					if cy<=y:					

						o=x-cx
						a=y-cy


						if o<0:
							o=-o
						if a<0:
							a=-a


						_a_=360-math.degrees(math.atan(o/a))
					else:


						o=x-cx
						a=cy-y


						if o<0:
							o=-o
						if a<0:
							a=-a


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


						_a_=90-math.degrees(math.atan(o/a))
					else:


						o=cy-y
						a=cx-x


						if o<0:
							o=-o
						if a<0:
							a=-a


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


						_a_=90+math.degrees(math.atan(o/a))

					else:

						o=y-cy
						a=cx-x

						if o<0:
							o=-o
						if a<0:
							a=-a


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




def move_striker():
	global pieces
	global game_st
	global st
	global turn

	if st=="main":


		if game_st==2:

			

			if pieces["striker"]["st"]==0:

				

				try:

					#print(pieces["striker"]["proj_ang"])

					pieces["striker"]["coord_"]=pieces["striker"]["coord"]
					if pieces["striker"]["proj_ang"]!=None:
						pieces["striker"]["data"]=get_pos("striker",pieces["striker"]["coord"][0],pieces["striker"]["coord"][1],0,pieces["striker"]["proj_ang"],0,0)
						pieces["striker"]["proj_ang"]=None
						pieces["striker"]["angle"]=pieces["striker"]["proj_ang"]
					else:

						pieces["striker"]["data"]=get_pos("striker",pieces["striker"]["coord"][0],pieces["striker"]["coord"][1],0,pieces["striker"]["angle"],0,0)
					
					#print(pieces["striker"]["data"])
					pieces["striker"]["coord"]=[pieces["striker"]["data"][0],pieces["striker"]["data"][1]]
					pieces["striker"]["angle"]=pieces["striker"]["data"][3]

					draw_piece_(striker_r,"striker","#323232","#ffffff",1)

					pieces["striker"]["st"]=1

				except:
					print(pieces["striker"]["data"],"error")
			elif pieces["striker"]["st"]==1:

				pieces["striker"]["data"]=get_pos("striker",pieces["striker"]["coord_"][0],pieces["striker"]["coord_"][1],pieces["striker"]["data"][2],pieces["striker"]["angle"],pieces["striker"]["data"][4],1)
				

				if pieces["striker"]["data"]==1:

					pieces["striker"]["start_time"]=0
					pieces["striker"]["speed"]=0
					pieces["striker"]["initial_v"]=0
					pieces["striker"]["current_v"]=0

					pieces["striker"]["proj_ang"]=None
					game_st=0
					pieces["striker"]["move st"]=0
					pieces["striker"]["st"]=0
					pieces["striker"]["initial_v"]=0
					pieces["striker"]["angle"]=0

					
					if turn==0:
						turn=1
						pieces["striker"]["coord"]=[xrng[0]+(xrng[1]-xrng[0])/2,yv2]
					elif turn==1:
						turn=0				
						pieces["striker"]["coord"]=[xrng[0]+(xrng[1]-xrng[0])/2,yv1]



					draw_piece_(striker_r,"striker","#323232","#ffffff",1)		

					root.after(100,move_striker)
					return


				elif pieces["striker"]["data"]==2:
					pieces["striker"]["st"]=0
					pieces["striker"]["angle"]=pieces["striker"]["proj_ang"]
					draw_piece_(striker_r,"striker","#323232","#ffffff",1)	


				else:

					pieces["striker"]["angle"]=pieces["striker"]["data"][3]
					pieces["striker"]["coord"]=[pieces["striker"]["data"][0],pieces["striker"]["data"][1]]


					pieces["striker"]["coord"]=[pieces["striker"]["data"][0],pieces["striker"]["data"][1]]
					

					

					try:


						if len(pieces["striker"]["data"][4])==3:



							pieces["striker"]["proj_ang"]=pieces["striker"]["data"][4][1]

					except:
						pass

					draw_piece_(striker_r,"striker","#323232","#ffffff",1)


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
					game_st=0
					pieces["striker"]["st"]=0
					pieces["striker"]["initial_v"]=0

					
					if turn==0:
						turn=1
						pieces["striker"]["coord"]=[xrng[0]+(xrng[1]-xrng[0])/2,yv2]
					elif turn==1:
						turn=0				
						pieces["striker"]["coord"]=[xrng[0]+(xrng[1]-xrng[0])/2,yv1]



					draw_piece_(striker_r,"striker","#323232","#ffffff",1)		

					root.after(1,move_striker)
					return
				else:

					pieces["striker"]["speed"]=int(round((1-pieces["striker"]["current_v"]/3)*10,0))

					if pieces["striker"]["speed"]<2:
						pieces["striker"]["speed"]=2

				


					#print(pieces["striker"]["speed"])


				

				root.after(pieces["striker"]["speed"],move_striker)
				return


			root.after(1,move_striker)
			return


					




		else:
			pieces["striker"]["st"]=0
			root.after(1,move_striker)
			return






		

	else:
		root.after(1,move_striker)
		return




def move_1_w():
	global pieces
	global game_st
	global st
	global turn
	global piece_r

	if pieces["1 white"]["potted"]==1:

		root.after(1,move_1_w)
		return

	if st=="main":


		if pieces["1 white"]["move st"]==1:

			

			if pieces["1 white"]["st"]==0:

				

				try:

					#print(pieces["1 white"]["proj_ang"])

					pieces["1 white"]["coord_"]=pieces["1 white"]["coord"]
					if pieces["1 white"]["proj_ang"]!=None:
						pieces["1 white"]["data"]=get_pos("1 white",pieces["1 white"]["coord"][0],pieces["1 white"]["coord"][1],0,pieces["1 white"]["proj_ang"],0,0)
						pieces["1 white"]["proj_ang"]=None
						pieces["1 white"]["angle"]=pieces["1 white"]["proj_ang"]
					else:

						pieces["1 white"]["data"]=get_pos("1 white",pieces["1 white"]["coord"][0],pieces["1 white"]["coord"][1],0,pieces["1 white"]["angle"],0,0)
					
					#print(pieces["1 white"]["data"])
					pieces["1 white"]["coord"]=[pieces["1 white"]["data"][0],pieces["1 white"]["data"][1]]
					pieces["1 white"]["angle"]=pieces["1 white"]["data"][3]

					draw_piece_(piece_r,"1 white","#ffffff","#000000",1)


					pieces["1 white"]["st"]=1

				except:
					print(pieces["1 white"]["data"],"error")
			elif pieces["1 white"]["st"]==1:

				pieces["1 white"]["data"]=get_pos("1 white",pieces["1 white"]["coord_"][0],pieces["1 white"]["coord_"][1],pieces["1 white"]["data"][2],pieces["1 white"]["angle"],pieces["1 white"]["data"][4],1)


				if pieces["1 white"]["data"]==1:

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

					draw_piece_(piece_r,"1 white","#ffffff","#000000",1)		

					root.after(1,move_1_w)
					return


				elif pieces["1 white"]["data"]==2:
					pieces["1 white"]["st"]=0
					pieces["1 white"]["angle"]=pieces["1 white"]["proj_ang"]
					draw_piece_(piece_r,"1 white","#ffffff","#000000",1)	


				else:

					pieces["1 white"]["angle"]=pieces["1 white"]["data"][3]
					pieces["1 white"]["coord"]=[pieces["1 white"]["data"][0],pieces["1 white"]["data"][1]]


					pieces["1 white"]["coord"]=[pieces["1 white"]["data"][0],pieces["1 white"]["data"][1]]
					

					

					try:


						if len(pieces["1 white"]["data"][4])==3:



							pieces["1 white"]["proj_ang"]=pieces["1 white"]["data"][4][1]

					except:
						pass

					draw_piece_(piece_r,"1 white","#ffffff","#000000",1)


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

					

					draw_piece_(piece_r,"1 white","#ffffff","#000000",1)		

					root.after(1,move_1_w)
					return
				else:

					pieces["1 white"]["speed"]=int(round((1-pieces["1 white"]["current_v"]/3)*10,0))

					if pieces["1 white"]["speed"]<2:
						pieces["1 white"]["speed"]=2


					#print(pieces["1 white"]["speed"])

				

				root.after(pieces["1 white"]["speed"],move_1_w)
				return


			root.after(1,move_1_w)
			return


					




		else:
			pieces["1 white"]["st"]=0
			root.after(1,move_1_w)
			return


	else:
		root.after(1,move_1_w)
		return


def move_1_b():
    global pieces
    global game_st
    global st
    global turn
    global piece_r

    if pieces["1 black"]["potted"]==1:

        root.after(1,move_1_b)
        return

    if st=="main":

        if pieces["1 black"]["move st"]==1:

            

            
            if pieces["1 black"]["st"]==0:

                

                try:

                    #print(pieces["1 black"]["proj_ang"])

                    pieces["1 black"]["coord_"]=pieces["1 black"]["coord"]
                    if pieces["1 black"]["proj_ang"]!=None:
                        pieces["1 black"]["data"]=get_pos("1 black",pieces["1 black"]["coord"][0],pieces["1 black"]["coord"][1],0,pieces["1 black"]["proj_ang"],0,0)
                        pieces["1 black"]["proj_ang"]=None
                        pieces["1 black"]["angle"]=pieces["1 black"]["proj_ang"]
                    else:

                        pieces["1 black"]["data"]=get_pos("1 black",pieces["1 black"]["coord"][0],pieces["1 black"]["coord"][1],0,pieces["1 black"]["angle"],0,0)
                    
                    #print(pieces["1 black"]["data"])
                    pieces["1 black"]["coord"]=[pieces["1 black"]["data"][0],pieces["1 black"]["data"][1]]
                    pieces["1 black"]["angle"]=pieces["1 black"]["data"][3]

                    draw_piece_(piece_r,"1 black","#000000","#ffffff",1)


                    pieces["1 black"]["st"]=1

                except:
                    print(pieces["1 black"]["data"],"error")
            elif pieces["1 black"]["st"]==1:

                pieces["1 black"]["data"]=get_pos("1 black",pieces["1 black"]["coord_"][0],pieces["1 black"]["coord_"][1],pieces["1 black"]["data"][2],pieces["1 black"]["angle"],pieces["1 black"]["data"][4],1)

                

                if pieces["1 black"]["data"]==1:

                    pieces["1 black"]["potted"]=1

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

                    draw_piece_(piece_r,"1 black","#000000","#ffffff",1)        

                    root.after(1,move_1_b)
                    return


                elif pieces["1 black"]["data"]==2:
                    pieces["1 black"]["st"]=0
                    pieces["1 black"]["angle"]=pieces["1 black"]["proj_ang"]
                    draw_piece_(piece_r,"1 black","#000000","#ffffff",1)    


                else:

                    pieces["1 black"]["angle"]=pieces["1 black"]["data"][3]
                    pieces["1 black"]["coord"]=[pieces["1 black"]["data"][0],pieces["1 black"]["data"][1]]


                    pieces["1 black"]["coord"]=[pieces["1 black"]["data"][0],pieces["1 black"]["data"][1]]
                    

                    

                    try:


                        if len(pieces["1 black"]["data"][4])==3:



                            pieces["1 black"]["proj_ang"]=pieces["1 black"]["data"][4][1]

                    except:
                        pass

                    draw_piece_(piece_r,"1 black","#000000","#ffffff",1)


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

                    

                    draw_piece_(piece_r,"1 black","#000000","#ffffff",1)        

                    root.after(1,move_1_b)
                    return
                else:

                    pieces["1 black"]["speed"]=int(round((1-pieces["1 black"]["current_v"]/3)*10,0))

                    if pieces["1 black"]["speed"]<2:
                        pieces["1 black"]["speed"]=2

                




               

                root.after(pieces["1 black"]["speed"],move_1_b)
                return


            root.after(1,move_1_b)
            return


                    




        else:
            pieces["1 black"]["st"]=0
            root.after(1,move_1_b)
            return


    else:
        root.after(1,move_1_b)
        return

_pieces_={}

def draw_piece_(r,p,col1,col2,con=0):
	global can
	global pieces,_pieces_

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





			





	if con==0:

		
		_pieces_[p]=get_index(p)

		can.delete(_pieces_[p])

		_pieces_[p]=can.create_oval(x-r,y-r, x+r,y+r,
			fill=col1,outline=col2)
	elif con==1:

		can.coords(_pieces_[p],x-r,y-r, x+r,y+r)







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

					},


	"1 white":{"coord":[150,150],
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
						},


	"1 black":{"coord":[150,250],
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
						},

		}

print(pieces["striker"])


w,h=500,500
root=tk.Tk()


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
move_1_b()

def update():

	root.after(1,update)
update()
root.mainloop()

