import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone 
from tkinter import *

root = Tk() 
num=StringVar()

def getnum():
	Output.delete("1.0", "end")
	global num
	if len(num.get())==10:
		number = phonenumbers.parse('+91'+num.get())
	else:
		number=phonenumbers.parse('+910000000000')
	phone= phonenumbers.is_valid_number(number)
	if phone==True:
		phone='Valid Number'
	else:
		phone='Invalid Number'
	country=geocoder.description_for_number(number,"en")
	sim=carrier.name_for_number(number,"en")
	timeZone = timezone.time_zones_for_number(number) 

  
	Output.place(x=250,y=900)
	Output.insert('1.0','1) '+str(phone)+'\n')
	Output.insert('2.0','2) '+str(country)+'\n')
	Output.insert('3.0','3) '+str(sim)+'\n')
	Output.insert(END,'4) '+str(timeZone))

w=root.winfo_screenwidth()
h=root.winfo_screenheight()

root.overrideredirect(True)
root.geometry(str(w)+"x"+str(h)+"+0+0")
root.config(bg='white')

label = Label(root,text=' Mobile Number Details ' ,bg='yellow',fg='red' ,font=('Arial',15,'bold','underline'))
label.place(x=100,y=100)

label1 = Label(root,text='Enter Mobile No:-' ,bg='white',fg='gray' ,font=('Arial',5,'bold'))
label1.place(x=220,y=410)
       
entry=Entry(root,textvariable=num,bd=10,bg="gray").place(x=220,y=450,height=100,width=700)

btn=Button(root,text="Get Details",font=('Arial',6,'bold'),bd=10,bg="orange",command=getnum).place(x=370,y=700,height=110,width=365)
 
Output = Text(root, height = 5, width = 25, bg= "yellow",fg='red')

root.mainloop()