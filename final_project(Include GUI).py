from tkinter import *
from tkinter import ttk
import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

from matplotlib.figure import Figure
from tkinter import ttk
import matplotlib.pyplot as plt

import matplotlib.animation as animation

from matplotlib import style

import numpy as np

style.use("ggplot")

LARGE_FONT=("Verdana",30)
MEDIUM_FONT=("Verdana",12)

class OS_Project(tk.Tk):

    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        tk.Tk.wm_title(self,"Disk Scheduling Algorithm")
        container=tk.Frame(self)
        container.pack(side="top",fill="both",expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames={}

        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive, PageSix):

            frame=F(container,self)

            self.frames[F]=frame

            frame.grid(row=0,column=0,sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self,cont):
        frame=self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        self.controller=controller
        tk.Frame.__init__(self,parent)

        self.label=tk.Label(self,text="Disk Scheduling Algorithm",font=LARGE_FONT)
        self.label.place(y=40,x=415)

        self.label=tk.Label(self,text="Number of I/O Requests:",font=MEDIUM_FONT)
        self.label.place(y=150,x=400)

        self.nr=tk.Entry(self,bd=4,width=50)
        self.nr.place(x=670,y=150)

        self.label=tk.Label(self,text="First value of I/O Requests:",font=MEDIUM_FONT)
        self.label.place(y=250,x=400)

        self.fr=tk.Entry(self,bd=4,width=50)
        self.fr.place(x=670,y=250)

        self.label=tk.Label(self,text="All the values of I/O Requests:",font=MEDIUM_FONT)
        self.label.place(y=350,x=400)

        self.ar=tk.Entry(self,bd=4,width=50)
        self.ar.place(x=670,y=350)

        self.label=tk.Label(self,text="Starting value of I/O Requests:",font=MEDIUM_FONT)
        self.label.place(y=450,x=400)

        self.sr=tk.Entry(self,bd=4,width=50)
        self.sr.place(x=670,y=450)

        self.label=tk.Label(self,text="Ending value of I/O Requests:",font=MEDIUM_FONT)
        self.label.place(y=550,x=400)

        self.er=tk.Entry(self,bd=4,width=50)
        self.er.place(x=670,y=550)

    

            
        button1 = ttk.Button(self, text="FCFS", command=lambda: self.Page_one_values())
        button1.grid(column=0, row=0,padx=75,pady=650)

        button2 = ttk.Button(self, text="SSTF", command=lambda: self.Page_two_values())
        button2.grid(column=1, row=0,padx=75,pady=650)

        button3 = ttk.Button(self, text="SCAN", command=lambda: self.Page_three_values())
        button3.grid(column=2, row=0,padx=75,pady=650)
        
        button4 = ttk.Button(self, text="C_SCAN", command=lambda: self.Page_four_values())
        button4.grid(column=3, row=0,padx=75,pady=650)

        button5 = ttk.Button(self, text="LOOK", command=lambda: self.Page_five_values())
        button5.grid(column=4, row=0,padx=75,pady=650)

        button6 = ttk.Button(self, text="C_LOOK", command=lambda: self.Page_six_values())
        button6.grid(column=5, row=0,padx=75,pady=650)

    def Page_one_values(self):
        self.controller.NR=self.nr.get()
        self.controller.FR=self.fr.get()
        self.controller.AR=self.ar.get()
        self.controller.SR=self.sr.get()
        self.controller.ER=self.er.get()
        self.controller.frames[PageOne].FCFS()
        self.controller.show_frame(PageOne)
        

    def Page_two_values(self):
        self.controller.NR=self.nr.get()
        self.controller.FR=self.fr.get()
        self.controller.AR=self.ar.get()
        self.controller.SR=self.sr.get()
        self.controller.ER=self.er.get()
        self.controller.frames[PageTwo].SSTF()
        self.controller.show_frame(PageTwo)

        

    def Page_three_values(self):
        self.controller.NR=self.nr.get()
        self.controller.FR=self.fr.get()
        self.controller.AR=self.ar.get()
        self.controller.SR=self.sr.get()
        self.controller.ER=self.er.get()
        self.controller.show_frame(PageThree)
        self.controller.frames[PageThree].SCAN()

    def Page_four_values(self):
        self.controller.NR=self.nr.get()
        self.controller.FR=self.fr.get()
        self.controller.AR=self.ar.get()
        self.controller.SR=self.sr.get()
        self.controller.ER=self.er.get()
        self.controller.show_frame(PageFour)
        self.controller.frames[PageFour].C_SCAN()

    def Page_five_values(self):
        self.controller.NR=self.nr.get()
        self.controller.FR=self.fr.get()
        self.controller.AR=self.ar.get()
        self.controller.SR=self.sr.get()
        self.controller.ER=self.er.get()
        self.controller.show_frame(PageFive)
        self.controller.frames[PageFive].LOOK()

    def Page_six_values(self):
        self.controller.NR=self.nr.get()
        self.controller.FR=self.fr.get()
        self.controller.AR=self.ar.get()
        self.controller.SR=self.sr.get()
        self.controller.ER=self.er.get()
        self.controller.show_frame(PageSix)
        self.controller.frames[PageSix].C_LOOK()

    
class PageOne(tk.Frame):
    #def __init__(self, parent, controller):
    def page_two(self):
        self.controller.frames[PageTwo].SSTF()
        self.controller.show_frame(PageTwo)
    def FCFS(self):
        for i in self.winfo_children():
            i.destroy()
        label=tk.Label(self,text="First Come First Serve",font=LARGE_FONT)
        label.pack(pady=20,padx=10)
        self.button1 = ttk.Button(self, text="Start Page", command=lambda: self.controller.show_frame(StartPage))
        self.button1.place(x=1050,y=600)

        self.button2 = ttk.Button(self, text="SSTF", command=lambda: self.page_two())
        self.button2.place(x=850,y=600)
       
        seek_count = 0
        label=tk.Label(self,text="Seek Sequence is:",font=MEDIUM_FONT)
        label.place(y=150,x=900)
        data=self.controller.AR
        head=int(self.controller.FR)
        size=int(self.controller.NR)
        d=[]
        d = list(map(int,data.split(' ')))
        n = len(d)
        distance, cur_seek = 0, 0 
        x=[]
        x.append(head)
        temp=200
        for i in range(size): 
            cur_seek = d[i]
            distance = abs(cur_seek - head) 
            seek_count += distance 
            head = cur_seek
        for i in range(size): 
            label=tk.Label(self,text= "Seeked number " + str(i+1) + " is: " + str(d[i]),font=MEDIUM_FONT)
            label.place(y=temp,x=900)
            temp+=30
            x.append(d[i])

        label=tk.Label(self,text="Total number of seek operations of FCFS is : ",font=MEDIUM_FONT)
        label.place(y=100,x=800)
        label=tk.Label(self,text=seek_count,font=MEDIUM_FONT)
        label.place(y=100,x=1200)
        y=[]
        for i in range(size+1):
            y.append(i+1)
        label=tk.Label(self,text="The values of list x is: ",font=MEDIUM_FONT)
        label.place(y=450,x=800)
        label=tk.Label(self,text=x,font=MEDIUM_FONT)
        label.place(y=450,x=1000)
        label=tk.Label(self,text="The values of list y is: ",font=MEDIUM_FONT)
        label.place(y=500,x=800)
        label=tk.Label(self,text=y,font=MEDIUM_FONT)
        label.place(y=500,x=1000)
        f = Figure(figsize=(7,7) , dpi=100)
        a = f.add_subplot(111)
        a.plot(x,y)
        self.canvas = FigureCanvasTkAgg(f, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

        self.toolbar = NavigationToolbar2Tk(self.canvas, self)
        self.toolbar.update()
        self.canvas._tkcanvas.pack(side=tk.LEFT, fill=tk.BOTH)

        avg_seek_time = seek_count/n

        label=tk.Label(self,text="Average seek time by all the I/O processes is : " + str(avg_seek_time),font=MEDIUM_FONT)
        label.place(y=550,x=800)
        
        
        
        self.canvas.draw()

    def __init__(self, parent, controller):
        self.controller=controller
        tk.Frame.__init__(self, parent)
        
        
        
class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        self.controller=controller
        tk.Frame.__init__(self, parent)
        

    def Page_one_values(self):
        self.controller.show_frame(PageOne)
        self.controller.frames[PageOne].FCFS()


    def Page_three_values(self):
        self.controller.show_frame(PageThree)
        self.controller.frames[PageThree].SCAN()

    def calculateDifference(self,arra, head, diff): 
        for i in range(len(diff)): 
            diff[i][0] = abs(arra[i] - head)
        
    def findMin(self,diff):  
        index = -1
        minimum = 999999999
        for i in range(len(diff)): 
            if (not diff[i][1] and 
                    minimum > diff[i][0]): 
                minimum = diff[i][0] 
                index = i 
        return index  
      
    def SSTF(self):
        for i in self.winfo_children():
            i.destroy()
        label=tk.Label(self,text="Second Seek Time First",font=LARGE_FONT)
        label.pack(pady=40,padx=10)

        self.button1 = ttk.Button(self, text="FCFS-1", command=lambda: self.Page_one_values())
        self.button1.place(x=1015,y=600)

        self.button2 = ttk.Button(self, text="SCAN-3", command=lambda: self.Page_three_values())
        self.button2.place(x=1200,y=600)

        self.button3 = ttk.Button(self, text="Start Page", command=lambda: self.controller.show_frame(StartPage))
        self.button3.place(x=800,y=600)

        f = Figure(figsize=(6,6) , dpi=100)
        a = f.add_subplot(111)
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.LEFT, fill=tk.BOTH)

        head=int(self.controller.FR)
        data=self.controller.AR
        d=[]
        d = list(map(int,data.split(' ')))
        
        if (len(d) == 0):
            return
        x=[]
        l = len(d)
        diff = [0] * l
        for i in range(l):
            diff[i] = [0, 0]   
            seek_count = 0
            seek_sequence = [0] * (l + 1)       
        for i in range(l):
            seek_sequence[i] = head
            self.calculateDifference(d, head, diff)
            index = self.findMin(diff)  
            diff[index][1] = True  
            seek_count += diff[index][0]
            head = d[index]  
            seek_sequence[len(seek_sequence) - 1] = head

        label=tk.Label(self,text="Total number of seek operations of SSTF is : ",font=MEDIUM_FONT)
        label.place(y=100,x=800)

        label=tk.Label(self,text=seek_count,font=MEDIUM_FONT)
        label.place(y=100,x=1200)
        
        label=tk.Label(self,text="Seek Sequence is:",font=MEDIUM_FONT)
        label.place(y=150,x=900)
        temp=200
        for i in range(l + 1):
            label=tk.Label(self,text= "Seeked number " + str(i+1) + " is: " + str(seek_sequence[i]),font=MEDIUM_FONT)
            label.place(y=temp,x=800)
            temp+=30
            x.append(seek_sequence[i])
        y=[]
        for i in range(l+1):
            y.append(i+1)
        label=tk.Label(self,text="The values of list X is: ",font=MEDIUM_FONT)
        label.place(y=500,x=700)
        label=tk.Label(self,text=x,font=MEDIUM_FONT)
        label.place(y=500,x=900)
        label=tk.Label(self,text="The values of list Y is: ",font=MEDIUM_FONT)
        label.place(y=550,x=700)
        label=tk.Label(self,text=y,font=MEDIUM_FONT)
        label.place(y=550,x=900)
        
        
        a.plot(x,y)

        
            
class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        

    def Page_four_values(self):
        self.controller.frames[PageFour].C_SCAN()
        self.controller.show_frame(PageFour)
        

    def Page_two_values(self):
        self.controller.frames[PageTwo].SSTF()
        self.controller.show_frame(PageTwo)

    def SCAN(self):
        for i in self.winfo_children():
            i.destroy()
        label=tk.Label(self,text="SCAN Algorithm",font=LARGE_FONT)
        label.pack(pady=40,padx=10)

        self.button1 = ttk.Button(self, text="SSTF-2", command=lambda: self.Page_two_values())
        self.button1.place(x=1015,y=600)

        self.button2 = ttk.Button(self, text="C_SCAN-4", command=lambda: self.Page_four_values())
        self.button2.place(x=1200,y=600)

        self.button3 = ttk.Button(self, text="Start Page", command=lambda: self.controller.show_frame(StartPage))
        self.button3.place(x=800,y=600)
        data = self.controller.AR
        d=[]
        d = list(map(int,data.split(' ')))
        head = int(self.controller.FR)
        pos = head
        n = len(d)
        start = int(self.controller.SR)
        time=0
        end = int(self.controller.ER)
        end1 = end
        count,cl,cr=0,0,0
        x=[]
        x.append(head)
        seek_sequence = [0] * len(d)
        for i in d:
            if i>=head:
                cr+=1
            else:
                cl+=1
        if cr > cl:
            for i in range(pos,end+1):
                if i in d:
                    time+=abs(pos-i)
                    pos=i
                    seek_sequence[count] = i
                    count += 1
                    d.remove(i)      
            time+=abs(pos-end)
            pos=end                              
            for i in range(end,start-1,-1):
                if i in d:
                    time+=abs(pos-i)
                    pos=i
                    seek_sequence[count] = i
                    count += 1
                    d.remove(i)        
            label=tk.Label(self,text="Total number of seek operations of SCAN is : ",font=MEDIUM_FONT)
            label.place(y=100,x=800)

            label=tk.Label(self,text = time,font=MEDIUM_FONT)
            label.place(y=100,x=1200)

            label=tk.Label(self,text="Seek Sequence is:",font=MEDIUM_FONT)
            label.place(y=150,x=900)
            temp=200
            cou=1
            for i in range(len(seek_sequence)):
                if seek_sequence[i] <= head and cou==1:
                    label=tk.Label(self,text= "Seeked number " + str(i+1) + " is: " + str(seek_sequence[i]),font=MEDIUM_FONT)
                    label.place(y=temp,x=900)
                    temp+=30
                    x.append(end1)
                    x.append(seek_sequence[i])
                    cou+=1
                else:
                    label=tk.Label(self,text= "Seeked number " + str(i+1) + " is: " + str(seek_sequence[i]),font=MEDIUM_FONT)
                    label.place(y=temp,x=900)
                    temp+=30
                    x.append(seek_sequence[i])
            y=[]
            for i in range(len(seek_sequence)+2):
                y.append(i+1)
            label=tk.Label(self,text="The values of list X is: ",font=MEDIUM_FONT)
            label.place(y=450,x=750)
            label=tk.Label(self,text=x,font=MEDIUM_FONT)
            label.place(y=450,x=950)
            label=tk.Label(self,text="The values of list Y is: ",font=MEDIUM_FONT)
            label.place(y=500,x=750)
            label=tk.Label(self,text=y,font=MEDIUM_FONT)
            label.place(y=500,x=950)
            
            f = Figure(figsize=(7,7) , dpi=100)
            a = f.add_subplot(111)
            a.plot(x,y)

            canvas = FigureCanvasTkAgg(f, self)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

            toolbar = NavigationToolbar2Tk(canvas, self)
            toolbar.update()
            canvas._tkcanvas.pack(side=tk.LEFT, fill=tk.BOTH)
            
            avg_seek_time = time/n

            label=tk.Label(self,text="Average seek time by all the I/O processes is : " + str(avg_seek_time),font=MEDIUM_FONT)
            label.place(y=550,x=750)

        else:
            for i in range(pos,start-1,-1):
                if i in d:
                    time+=abs(pos-i)
                    pos=i
                    seek_sequence[count] = i
                    count += 1
                    d.remove(i)
            time+=abs(pos-start)
            pos=start                        
            for i in range(start,end+1,+1):
                if i in d:
                    time+=abs(pos-i)
                    pos=i
                    seek_sequence[count] = i
                    count += 1
                    d.remove(i)

            label=tk.Label(self,text="Total number of seek operations of C_SCAN is : ",font=MEDIUM_FONT)
            label.place(y=100,x=800)

            label=tk.Label(self,text=time,font=MEDIUM_FONT)
            label.place(y=100,x=1200)

            label=tk.Label(self,text="Seek Sequence is:",font=MEDIUM_FONT)
            label.place(y=150,x=900)
            temp=200
            cou=1
            for i in range(len(seek_sequence)):
                if seek_sequence[i] > head and cou==1:
                    label=tk.Label(self,text= "Seeked number " + str(i+1) + " is: " + str(seek_sequence[i]),font=MEDIUM_FONT)
                    label.place(y=temp,x=900)
                    temp+=30
                    x.append(start)
                    x.append(seek_sequence[i])
                    cou+=1
                else:
                    label=tk.Label(self,text= "Seeked number " + str(i+1) + " is: " + str(seek_sequence[i]),font=MEDIUM_FONT)
                    label.place(y=temp,x=900)
                    temp+=30
                    x.append(seek_sequence[i])

            y=[]
            for i in range(len(seek_sequence)+2):
                y.append(i+1)
            label=tk.Label(self,text="The values of list X is: ",font=MEDIUM_FONT)
            label.place(y=450,x=700)
            label=tk.Label(self,text=x,font=MEDIUM_FONT)
            label.place(y=450,x=900)
            label=tk.Label(self,text="The values of list Y is: ",font=MEDIUM_FONT)
            label.place(y=500,x=700)
            label=tk.Label(self,text=y,font=MEDIUM_FONT)
            label.place(y=500,x=900)
            
            f = Figure(figsize=(7,7) , dpi=100)
            a = f.add_subplot(111)
            a.plot(x,y)

            canvas = FigureCanvasTkAgg(f, self)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

            toolbar = NavigationToolbar2Tk(canvas, self)
            toolbar.update()
            canvas._tkcanvas.pack(side=tk.LEFT, fill=tk.BOTH)
            
        
            avg_seek_time = time/n

            label=tk.Label(self,text="Average seek time by all the I/O processes is : " + str(avg_seek_time),font=MEDIUM_FONT)
            label.place(y=550,x=750)

class PageFour(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        

    def Page_five_values(self):
        self.controller.frames[PageFive].LOOK()
        self.controller.show_frame(PageFive)
        

    def Page_three_values(self):
        self.controller.frames[PageThree].SCAN()
        self.controller.show_frame(PageThree)
        
        
    def C_SCAN(self):
        for i in self.winfo_children():
            i.destroy()
        label=tk.Label(self,text="Circular SCAN Algorithm",font=LARGE_FONT)
        label.pack(pady=40,padx=10)

        self.button1 = ttk.Button(self, text="SCAN-3", command=lambda: self.Page_three_values())
        self.button1.place(x=1015,y=600)

        self.button2 = ttk.Button(self, text="LOOK-5", command=lambda: self.Page_five_values())
        self.button2.place(x=1200,y=600)

        self.button3 = ttk.Button(self, text="Start Page", command=lambda: self.controller.show_frame(StartPage))
        self.button3.place(x=800,y=600)
        data = self.controller.AR
        d=[]
        d = list(map(int,data.split(' ')))
        head = int(self.controller.FR)
        n = len(d)
        pos = head
        start = int(self.controller.SR)
        time=0
        end = int(self.controller.ER)
        end1 = end
        count,cl,cr=0,0,0
        x=[]
        x.append(head)
        seek_sequence = [0] * len(d)
        for i in d:
            if i>=head:
                cr+=1
            else:
                cl+=1
        if cr > cl:            
            for i in range(pos,end+1):
                if i in d:
                    time+=abs(pos-i)
                    pos=i
                    seek_sequence[count] = i
                    count += 1
                    d.remove(i)
            time+=abs(pos-end)
            pos=end
            temp,ans=0,0
            for i in range(start,head+1):
                if i in d:
                    temp += 1
                    time+=abs(pos-i)
                    pos=i
                    seek_sequence[count] = i
                    count += 1
                    d.remove(i)
                    if temp == 1:
                        ans = i
            time += (ans*2)

            label=tk.Label(self,text="Total number of seek operations of C_SCAN is : ",font=MEDIUM_FONT)
            label.place(y=100,x=800)

            label=tk.Label(self,text = time,font=MEDIUM_FONT)
            label.place(y=100,x=1200)

            label=tk.Label(self,text="Seek Sequence is:",font=MEDIUM_FONT)
            label.place(y=150,x=900)
            temp=200
            cou=1
            for i in range(len(seek_sequence)):
                if seek_sequence[i] <= head and cou==1:
                    label=tk.Label(self,text= "Seeked number " + str(i+1) + " is: " + str(seek_sequence[i]),font=MEDIUM_FONT)
                    label.place(y=temp,x=900)
                    temp+=30
                    x.append(end1)
                    x.append(start)
                    x.append(seek_sequence[i])
                    cou+=1
                else:
                    label=tk.Label(self,text= "Seeked number " + str(i+1) + " is: " + str(seek_sequence[i]),font=MEDIUM_FONT)
                    label.place(y=temp,x=900)
                    temp+=30
                    x.append(seek_sequence[i])
                    
            y=[]
            for i in range(len(seek_sequence)+3):
                y.append(i+1)
            label=tk.Label(self,text="The values of list X is: ",font=MEDIUM_FONT)
            label.place(y=450,x=700)
            label=tk.Label(self,text=x,font=MEDIUM_FONT)
            label.place(y=450,x=900)
            label=tk.Label(self,text="The values of list Y is: ",font=MEDIUM_FONT)
            label.place(y=500,x=700)
            label=tk.Label(self,text=y,font=MEDIUM_FONT)
            label.place(y=500,x=900)
                
            f = Figure(figsize=(7,7) , dpi=100)
            a = f.add_subplot(111)
            a.plot(x,y)

            canvas = FigureCanvasTkAgg(f, self)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

            toolbar = NavigationToolbar2Tk(canvas, self)
            toolbar.update()
            canvas._tkcanvas.pack(side=tk.LEFT, fill=tk.BOTH)
            
            avg_seek_time = time/n

            label=tk.Label(self,text="Average seek time by all the I/O processes is : " + str(avg_seek_time),font=MEDIUM_FONT)
            label.place(y=550,x=750)

        else:
            tmep=0
            for i in range(pos,start-1,-1):
                if i in d:
                    time+=abs(pos-i)
                    pos=i
                    seek_sequence[count] = i
                    count += 1
                    temp=i
                    d.remove(i)
            time+=abs(pos-end)
            pos=end
            time += (temp*2)
            for i in range(end,head,-1):
                if i in d:
                    time+=abs(pos-i)
                    pos=i
                    seek_sequence[count] = i
                    count += 1
                    d.remove(i)

            label=tk.Label(self,text="Total number of seek operations of C_SCAN is : ",font=MEDIUM_FONT)
            label.place(y=100,x=800)

            label=tk.Label(self,text= time,font=MEDIUM_FONT)
            label.place(y=100,x=1200)

            label=tk.Label(self,text="Seek Sequence is:",font=MEDIUM_FONT)
            label.place(y=150,x=900)
            temp=200
            cou=1
            for i in range(len(seek_sequence)):
                print(seek_sequence[i])
                if seek_sequence[i] > head and cou==1:
                    label=tk.Label(self,text= "Seeked number " + str(i+1) + " is: " + str(seek_sequence[i]),font=MEDIUM_FONT)
                    label.place(y=temp,x=900)
                    temp+=30
                    x.append(start)
                    x.append(end1)
                    x.append(seek_sequence[i])
                    cou+=1
                    
                else:
                    label=tk.Label(self,text= "Seeked number " + str(i+1) + " is: " + str(seek_sequence[i]),font=MEDIUM_FONT)
                    label.place(y=temp,x=900)
                    temp+=30
                    x.append(seek_sequence[i])

            y=[]
            for i in range(len(seek_sequence)+3):
                y.append(i+1)
            label=tk.Label(self,text="The values of list X is: ",font=MEDIUM_FONT)
            label.place(y=450,x=800)
            label=tk.Label(self,text=x,font=MEDIUM_FONT)
            label.place(y=450,x=1000)
            label=tk.Label(self,text="The values of list Y is: ",font=MEDIUM_FONT)
            label.place(y=500,x=800)
            label=tk.Label(self,text=y,font=MEDIUM_FONT)
            label.place(y=500,x=1000)

            f = Figure(figsize=(7,7) , dpi=100)
            a = f.add_subplot(111)
            a.plot(x,y)

            canvas = FigureCanvasTkAgg(f, self)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

            toolbar = NavigationToolbar2Tk(canvas, self)
            toolbar.update()
            canvas._tkcanvas.pack(side=tk.LEFT, fill=tk.BOTH)
            
            avg_seek_time = time/n

            label=tk.Label(self,text="Average seek time by all the I/O processes is : " + str(avg_seek_time),font=MEDIUM_FONT)
            label.place(y=550,x=750)
            
class PageFive(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        

    def Page_four_values(self):
        self.controller.frames[PageFour].C_SCAN()
        self.controller.show_frame(PageFour)
        

    def Page_six_values(self):
        self.controller.frames[PageSix].C_LOOK()
        self.controller.show_frame(PageSix)
        

    def LOOK(self):
        for i in self.winfo_children():
            i.destroy()
        label=tk.Label(self,text="LOOK Algorihtm",font=LARGE_FONT)
        label.pack(pady=40,padx=10)

        self.button1 = ttk.Button(self, text="C_SCAN-4", command=lambda: self.Page_four_values())
        self.button1.place(x=1015,y=600)

        self.button2 = ttk.Button(self, text="C_LOOK-6", command=lambda: self.Page_six_values())
        self.button2.place(x=1200,y=600)

        self.button3 = ttk.Button(self, text="Start Page", command=lambda: self.controller.show_frame(StartPage))
        self.button3.place(x=800,y=600)
        data = self.controller.AR
        d=[]
        d = list(map(int,data.split(' ')))
        head = int(self.controller.FR)
        n = len(d)
        pos = head
        start = int(self.controller.SR)
        time=0
        end = int(self.controller.ER)
        end1 = end
        count,cl,cr=0,0,0
        x=[]
        x.append(head)
        seek_sequence = [0] * len(d)

        for i in d:
            if i>=head:
                cr+=1
            else:
                cl+=1
        if cr > cl:
            for i in range(pos,end+1):
                if i in d:
                    time+=abs(pos-i)
                    pos=i
                    seek_sequence[count] = i
                    count += 1
                    d.remove(i)      
            #time+=abs(pos-end)
            pos=end                               
            for i in range(end,start-1,-1):
                if i in d:
                    time+=abs(pos-i)
                    pos=i
                    seek_sequence[count] = i
                    count += 1
                    d.remove(i)
            label=tk.Label(self,text="Total number of seek operations of LOOK is : ",font=MEDIUM_FONT)
            label.place(y=100,x=800)

            label=tk.Label(self,text= time,font=MEDIUM_FONT)
            label.place(y=100,x=1200)

            label=tk.Label(self,text="Seek Sequence is:",font=MEDIUM_FONT)
            label.place(y=150,x=900)
            temp=200
            cou=1
            for i in range(len(seek_sequence)):
                label=tk.Label(self,text= "Seeked number " + str(i+1) + " is: " + str(seek_sequence[i]),font=MEDIUM_FONT)
                label.place(y=temp,x=900)
                x.append(seek_sequence[i])
                temp += 30

            y=[]
            for i in range(len(seek_sequence)+1):
                y.append(i+1)
            label=tk.Label(self,text="The values of list X is: ",font=MEDIUM_FONT)
            label.place(y=450,x=800)
            label=tk.Label(self,text=x,font=MEDIUM_FONT)
            label.place(y=450,x=1000)
            label=tk.Label(self,text="The values of list Y is: ",font=MEDIUM_FONT)
            label.place(y=500,x=800)
            label=tk.Label(self,text=y,font=MEDIUM_FONT)
            label.place(y=500,x=1000)
            
            f = Figure(figsize=(6,6) , dpi=100)
            a = f.add_subplot(111)
            a.plot(x,y)

            canvas = FigureCanvasTkAgg(f, self)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

            toolbar = NavigationToolbar2Tk(canvas, self)
            toolbar.update()
            canvas._tkcanvas.pack(side=tk.LEFT, fill=tk.BOTH)
    
            avg_seek_time = time/n

            label=tk.Label(self,text="Average seek time by all the I/O processes is : " + str(avg_seek_time),font=MEDIUM_FONT)
            label.place(y=550,x=750)

        else:
            for i in range(pos,start-1,-1):
                if i in d:
                    time+=abs(pos-i)
                    pos=i
                    seek_sequence[count] = i
                    count += 1
                    d.remove(i)
            #time+=abs(pos-start)
            pos=start
                                    
            for i in range(start,end+1,+1):
                if i in d:
                    time+=abs(pos-i)
                    pos=i
                    seek_sequence[count] = i
                    count += 1
                    d.remove(i)
            label=tk.Label(self,text="Total number of seek operations of LOOK is : ",font=MEDIUM_FONT)
            label.place(y=100,x=800)

            label=tk.Label(self,text=time,font=MEDIUM_FONT)
            label.place(y=100,x=1200)

            label=tk.Label(self,text="Seek Sequence is:",font=MEDIUM_FONT)
            label.place(y=150,x=900)
            temp=200
            cou=1
            for i in range(len(seek_sequence)):
                label=tk.Label(self,text= "Seeked number " + str(i+1) + " is: " + str(seek_sequence[i]),font=MEDIUM_FONT)
                label.place(y=temp,x=900)
                x.append(seek_sequence[i])
                temp += 30

            y=[]
            for i in range(len(seek_sequence)+1):
                y.append(i+1)
            label=tk.Label(self,text="The values of list X is: ",font=MEDIUM_FONT)
            label.place(y=450,x=700)
            label=tk.Label(self,text=x,font=MEDIUM_FONT)
            label.place(y=450,x=900)
            label=tk.Label(self,text="The values of list Y is: ",font=MEDIUM_FONT)
            label.place(y=500,x=700)
            label=tk.Label(self,text=y,font=MEDIUM_FONT)
            label.place(y=500,x=900)
            
            f = Figure(figsize=(6,6) , dpi=100)
            a = f.add_subplot(111)
            a.plot(x,y)

            canvas = FigureCanvasTkAgg(f, self)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

            toolbar = NavigationToolbar2Tk(canvas, self)
            toolbar.update()
            canvas._tkcanvas.pack(side=tk.LEFT, fill=tk.BOTH)
    
            avg_seek_time = time/n

            label=tk.Label(self,text="Average seek time by all the I/O processes is : " + str(avg_seek_time),font=MEDIUM_FONT)
            label.place(y=550,x=750)

class PageSix(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        

    def Page_five_values(self):
        self.controller.frames[PageFive].LOOK()
        self.controller.show_frame(PageFive)
        

    def C_LOOK(self):
        for i in self.winfo_children():
            i.destroy()
        label=tk.Label(self,text="Circular LOOK Algorithm",font=LARGE_FONT)
        label.pack(pady=40,padx=10)

        self.button1 = ttk.Button(self, text="Start Page", command=lambda: self.controller.show_frame(StartPage))
        self.button1.place(x=1050,y=600)

        self.button2 = ttk.Button(self, text="LOOK-5", command=lambda: self.Page_five_values())
        self.button2.place(x=850,y=600)
        data = self.controller.AR
        d=[]
        d = list(map(int,data.split(' ')))
        head = int(self.controller.FR)
        n = len(d)
        pos = head
        start = int(self.controller.SR)
        time=0
        end = int(self.controller.ER)
        end1 = end
        count,cl,cr=0,0,0
        x=[]
        x.append(head)
        seek_sequence = [0] * len(d)
       
        for i in d:
            if i>=head:
                cr+=1
            else:
                cl+=1
        if cr > cl:            
            for i in range(pos,end+1):
                if i in d:
                    time+=abs(pos-i)
                    pos=i
                    seek_sequence[count] = i
                    count += 1
                    d.remove(i)
            #time+=abs(pos-end)
            pos=end
            for i in range(start,head+1):
                if i in d:
                    time+=abs(pos-i)
                    pos=i
                    seek_sequence[count] = i
                    count += 1
                    d.remove(i)
            label=tk.Label(self,text="Total number of seek operations of C_LOOK is : ",font=MEDIUM_FONT)
            label.place(y=100,x=800)

            label=tk.Label(self,text=time,font=MEDIUM_FONT)
            label.place(y=100,x=1200)

            label=tk.Label(self,text="Seek Sequence is:",font=MEDIUM_FONT)
            label.place(y=150,x=900)
            temp=200
            cou=1
            for i in range(len(seek_sequence)):
                label=tk.Label(self,text= "Seeked number " + str(i+1) + " is: " + str(seek_sequence[i]),font=MEDIUM_FONT)
                label.place(y=temp,x=800)
                x.append(seek_sequence[i])
                temp += 30
            y=[]
            for i in range(len(seek_sequence)+1):
                y.append(i+1)
            label=tk.Label(self,text="The values of list X is: ",font=MEDIUM_FONT)
            label.place(y=450,x=700)
            label=tk.Label(self,text=x,font=MEDIUM_FONT)
            label.place(y=450,x=900)
            label=tk.Label(self,text="The values of list Y is: ",font=MEDIUM_FONT)
            label.place(y=500,x=700)
            label=tk.Label(self,text=y,font=MEDIUM_FONT)
            label.place(y=500,x=900)
            
            f = Figure(figsize=(7,7) , dpi=100)
            a = f.add_subplot(111)
            a.plot(x,y)

            canvas = FigureCanvasTkAgg(f, self)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

            toolbar = NavigationToolbar2Tk(canvas, self)
            toolbar.update()
            canvas._tkcanvas.pack(side=tk.LEFT, fill=tk.BOTH)
            
            avg_seek_time = time/n

            label=tk.Label(self,text="Average seek time by all the I/O processes is : " + str(avg_seek_time),font=MEDIUM_FONT)
            label.place(y=550,x=750)

        else:
            for i in range(pos,start-1,-1):
                if i in d:
                    time+=abs(pos-i)
                    pos=i
                    seek_sequence[count] = i
                    count += 1
                    d.remove(i)
            #time+=abs(pos-end)
            pos=end

            for i in range(end,head,-1):
                if i in d:
                    time+=abs(pos-i)
                    pos=i
                    seek_sequence[count] = i
                    count += 1
                    d.remove(i)
            label=tk.Label(self,text="Total number of seek operations of FCFS is : ",font=MEDIUM_FONT)
            label.place(y=100,x=800)

            label=tk.Label(self,text= time,font=MEDIUM_FONT)
            label.place(y=100,x=1200)
            
            label=tk.Label(self,text="Seek Sequence is:",font=MEDIUM_FONT)
            label.place(y=150,x=900)
            temp=200
            cou=1
            for i in range(len(seek_sequence)):
                label=tk.Label(self,text= "Seeked number " + str(i+1) + " is: " + str(seek_sequence[i]),font=MEDIUM_FONT)
                label.place(y=temp,x=800)
                temp+=30
                x.append(seek_sequence[i])

            y=[]
            for i in range(len(seek_sequence)+1):
                y.append(i+1)
            label=tk.Label(self,text="The values of list X is: ",font=MEDIUM_FONT)
            label.place(y=450,x=700)
            label=tk.Label(self,text=x,font=MEDIUM_FONT)
            label.place(y=450,x=900)
            label=tk.Label(self,text="The values of list Y is: ",font=MEDIUM_FONT)
            label.place(y=500,x=700)
            label=tk.Label(self,text=y,font=MEDIUM_FONT)
            label.place(y=500,x=900)
            
            f = Figure(figsize=(6,6) , dpi=100)
            a = f.add_subplot(111)
            a.plot(x,y)

            canvas = FigureCanvasTkAgg(f, self)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

            toolbar = NavigationToolbar2Tk(canvas, self)
            toolbar.update()
            canvas._tkcanvas.pack(side=tk.LEFT, fill=tk.BOTH)
            
            avg_seek_time = time/n

            label=tk.Label(self,text="Average seek time by all the I/O processes is : " + str(avg_seek_time),font=MEDIUM_FONT)
            label.place(y=550,x=750)

ob= OS_Project()
ob.mainloop()
