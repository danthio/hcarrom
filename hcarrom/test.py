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
root.resizable((0,0))

can=tk.Canvas(width=500,height=500,relief="flat",highlightthickness=0,border=0,bg="#00ffff")
can.place(in_=root,x=0,y=0)

can.bind("<Button-1>",b1)
can.bind("<Motion>",get_val)


pieces_coord()
root.mainloop()















def move_red():
    global pieces
    global game_st
    global st
    global turn
    global piece_r

    if pieces["red"]["potted"]==1:

        root.after(1,move_red)
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
                        pieces["red"]["proj_ang"]=None
                        pieces["red"]["angle"]=angle(pieces["red"]["proj_ang"])
                    else:

                        pieces["red"]["data"]=get_pos("red",pieces["red"]["coord"][0],pieces["red"]["coord"][1],0,angle(pieces["red"]["angle"]),0,0)
                    
                    #print(pieces["red"]["data"])
                    pieces["red"]["coord"]=[pieces["red"]["data"][0],pieces["red"]["data"][1]]
                    pieces["red"]["angle"]=angle(pieces["red"]["data"][3])

                    draw_piece_("red",1)


                    pieces["red"]["st"]=1

                except:
                    print(pieces["red"]["data"],"error")
            elif pieces["red"]["st"]==1:

                pieces["red"]["data"]=get_pos("red",pieces["red"]["coord_"][0],pieces["red"]["coord_"][1],pieces["red"]["data"][2],angle(pieces["red"]["angle"]),pieces["red"]["data"][4],1)

                

                if pieces["red"]["data"]==1:

                    pieces["red"]["potted"]=1

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

                    root.after(1,move_red)
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

                    except:
                        pass

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

                    root.after(1,move_red)
                    return
                else:

                    pieces["red"]["speed"]=int(round((1-pieces["red"]["current_v"]/3)*10,0))

                    if pieces["red"]["speed"]<1:
                        pieces["red"]["speed"]=1

                




               

                root.after(pieces["red"]["speed"],move_red)
                return


            root.after(1,move_red)
            return


                    




        else:
            pieces["red"]["st"]=0
            root.after(1,move_red)
            return


    else:
        root.after(1,move_red)
        return
