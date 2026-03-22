from PIL import Image,ImageTk,ImageDraw
import tkinter as tk
import math


bg=0
def load_im():
	global w,h
	global bg



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


def main():
	global bg

	can.delete("all")


	can.create_image(0,0,image=bg,anchor="nw")

p=0
#r=30
cx,cy=0,0
def draw_piece(x,y,r):
	global p
	global cx,cy

	cx,cy=x,y

	can.delete(p)

	p=can.create_oval(x-r,y-r, x+r,y+r,fill="#000000",outline="#ff0000")

drag_st=0
game_st=0

def can_b1(e):
	global drag_st,game_st
	global striker_coord,striker_r

	if game_st==0:

		x,y=striker_coord

		r=math.sqrt((e.x-x)**2+(e.y-y)**2)

		if r<=striker_r:
			drag_st=1




def drag(e):
	global drag_st
	global striker_coord,striker_r,xrng
	global dm_vs

	if drag_st==1:

		x,y=striker_coord

		r=math.sqrt((e.x-x)**2+(e.y-y)**2)

		if r<=striker_r:
			if xrng[0]<=e.x<=xrng[1]:
				striker_coord[0]=e.x


				for i in dm_vs:

					can.delete(i)
				draw_striker()



def can_b1_release(e):
	global drag_st


	drag_st=0


dm_vs=[0,0]
def draw_move(e):
	global game_st,drag_st
	global striker_coord
	global dm_vs
	global boundary






	if drag_st==1:
		return

	try:

		cx,cy=striker_coord


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



			#0,0

			r_=0

			for _ in range(600):

				#print(r_)


				x=r_*math.sin(math.radians(ang))+cx
				y=r_*math.cos(math.radians(ang))+cy



				

				if boundary[1][0]<=x<=boundary[1][0]+boundary[0]:
					if boundary[1][1]<=y<=boundary[1][1]+boundary[0]:


						r2=math.sqrt((x-(boundary[1][0]+boundary[0]))**2+(y-(boundary[1][1]+boundary[0]))**2)

						if r2>boundary[0]:


							for i in dm_vs:

								can.delete(i)


							x+=striker_r
							y+=striker_r

							dm_vs[0]=can.create_line(cx,cy, x,y,fill="#ff0000")
							dm_vs[1]=can.create_oval(x-striker_r,y-striker_r, x+striker_r,y+striker_r ,outline="#ff0000")

							return

				
				r_+=1


			#1,0







			r_=0

			for _ in range(600):

				#print(r_)


				x=r_*math.sin(math.radians(ang))+cx
				y=r_*math.cos(math.radians(ang))+cy



				

				if boundary[1][2]-boundary[0]<=x<=boundary[1][2]:
					if boundary[1][1]<=y<=boundary[1][1]+boundary[0]:

						#print("ok")

						r2=math.sqrt((x-(boundary[1][2]-boundary[0]))**2+(y-(boundary[1][1]+boundary[0]))**2)

						if r2>boundary[0]:


							for i in dm_vs:

								can.delete(i)


							x-=striker_r
							y+=striker_r

							dm_vs[0]=can.create_line(cx,cy, x,y,fill="#ff0000")
							dm_vs[1]=can.create_oval(x-striker_r,y-striker_r, x+striker_r,y+striker_r ,outline="#ff0000")

							return

				
				r_+=1



			#1,1







			r_=0

			for _ in range(600):

				#print(r_)


				x=r_*math.sin(math.radians(ang))+cx
				y=r_*math.cos(math.radians(ang))+cy



				

				if boundary[1][2]-boundary[0]<=x<=boundary[1][2]:
					if boundary[1][3]-boundary[0]<=y<=boundary[1][3]:

						#print("ok")

						r2=math.sqrt((x-(boundary[1][2]-boundary[0]))**2+(y-(boundary[1][3]-boundary[0]))**2)

						if r2>boundary[0]:


							for i in dm_vs:

								can.delete(i)


							x-=striker_r
							y-=striker_r

							dm_vs[0]=can.create_line(cx,cy, x,y,fill="#ff0000")
							dm_vs[1]=can.create_oval(x-striker_r,y-striker_r, x+striker_r,y+striker_r ,outline="#ff0000")

							return

				
				r_+=1




			#0,1







			r_=0

			for _ in range(600):

				#print(r_)


				x=r_*math.sin(math.radians(ang))+cx
				y=r_*math.cos(math.radians(ang))+cy



				

				if boundary[1][0]<=x<=boundary[1][0]+boundary[0]:
					if boundary[1][3]-boundary[0]<=y<=boundary[1][3]:

						#print("ok")

						r2=math.sqrt((x-(boundary[1][0]+boundary[0]))**2+(y-(boundary[1][3]-boundary[0]))**2)

						if r2>boundary[0]:


							for i in dm_vs:

								can.delete(i)


							x+=striker_r
							y-=striker_r

							dm_vs[0]=can.create_line(cx,cy, x,y,fill="#ff0000")
							dm_vs[1]=can.create_oval(x-striker_r,y-striker_r, x+striker_r,y+striker_r ,outline="#ff0000")

							return

				
				r_+=1



			#left

			r_=0

			for _ in range(600):

				#print(r_)


				x=r_*math.sin(math.radians(ang))+cx
				y=r_*math.cos(math.radians(ang))+cy




				if x<boundary[1][0]:

					if boundary[1][1]<=y<=boundary[1][3]:



						for i in dm_vs:

							can.delete(i)


						x+=striker_r
						#y-=striker_r

						dm_vs[0]=can.create_line(cx,cy, x,y,fill="#ff0000")
						dm_vs[1]=can.create_oval(x-striker_r,y-striker_r, x+striker_r,y+striker_r ,outline="#ff0000")

						return

				r_+=1



			#right

			r_=0

			for _ in range(600):

				#print(r_)


				x=r_*math.sin(math.radians(ang))+cx
				y=r_*math.cos(math.radians(ang))+cy




				if x>boundary[1][2]:

					if boundary[1][1]<=y<=boundary[1][3]:



						for i in dm_vs:

							can.delete(i)


						x-=striker_r
						#y-=striker_r

						dm_vs[0]=can.create_line(cx,cy, x,y,fill="#ff0000")
						dm_vs[1]=can.create_oval(x-striker_r,y-striker_r, x+striker_r,y+striker_r ,outline="#ff0000")

						return

				r_+=1



			#up

			r_=0

			for _ in range(600):

				#print(r_)


				x=r_*math.sin(math.radians(ang))+cx
				y=r_*math.cos(math.radians(ang))+cy




				if y<boundary[1][1]:

					if boundary[1][0]<=x<=boundary[1][2]:



						for i in dm_vs:

							can.delete(i)


						y+=striker_r

						dm_vs[0]=can.create_line(cx,cy, x,y,fill="#ff0000")
						dm_vs[1]=can.create_oval(x-striker_r,y-striker_r, x+striker_r,y+striker_r ,outline="#ff0000")

						return

				r_+=1


			#down

			r_=0

			for _ in range(600):

				#print(r_)


				x=r_*math.sin(math.radians(ang))+cx
				y=r_*math.cos(math.radians(ang))+cy




				if y>boundary[1][3]:

					if boundary[1][0]<=x<=boundary[1][2]:



						for i in dm_vs:

							can.delete(i)


						y-=striker_r

						dm_vs[0]=can.create_line(cx,cy, x,y,fill="#ff0000")
						dm_vs[1]=can.create_oval(x-striker_r,y-striker_r, x+striker_r,y+striker_r ,outline="#ff0000")

						return

				r_+=1


		find_r(cx,cy,ang)





		

	except:
		pass

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
	

	#draw_piece(cx,cy-1,r)


	if bnd_st==0:

		coord[1]-=1

		draw_boundary()
	else:

		coord[1]+=1

		draw_boundary()


def down(e):
	global cx,cy
	global bnd_st
	#draw_piece(cx,cy+1,r)


	if bnd_st==0:

		coord[3]+=1

		draw_boundary()
	else:

		coord[3]-=1

		draw_boundary()

def right(e):
	global cx,cy
	global bnd_st

	#draw_piece(cx+1,cy,r)



	if bnd_st==0:

		coord[2]+=1

		draw_boundary()
	else:

		coord[2]-=1

		draw_boundary()
def left(e):
	global cx,cy
	global bnd_st

	#draw_piece(cx-1,cy,r)


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

		#draw_piece(cx,cy,r)

		draw_boundary()

	elif e.char=="a":

		if r-1<0:
			return

		r-=1

		#draw_piece(cx,cy,r)

		draw_boundary()

	elif e.char=="w":

		if bnd_st==1:
			bnd_st=0
		elif bnd_st==0:
			bnd_st=1
def can_b3(e):

	global r,cx,cy
	global coord


	print(r,coord)#r,cx,cy)
"""

striker=0
def draw_striker():
	global can
	global striker,striker_r,striker_coord

	x,y=striker_coord

	can.delete(striker)

	striker=can.create_oval(x-striker_r,y-striker_r, x+striker_r,y+striker_r,
		fill="#323232",outline="#ffffff")




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
#can.bind("<Button-3>",can_b3)

can.focus_set()


#500- 7,5
striker_r=7*w/500
piece_r=5*w/500


yv1,yv2=82,404

xrng=(102*w/500,383*w/500)



striker_coord=[xrng[0]+(xrng[1]-xrng[0])/2,yv2]

#coord=[w/2-100,h/2-100, w/2+100,h/2+100]

boundary=[22,[22*w/500,21*w/500,463*w/500,464*w/500]]

coord=boundary[1]

r=22

load_im()

root.geometry(f"{w}x{h}+{int((root.winfo_screenwidth()-w)/2)}+{50}")
main()

draw_boundary()
draw_striker()


root.mainloop()

