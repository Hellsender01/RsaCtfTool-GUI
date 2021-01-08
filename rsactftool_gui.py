#!/usr/bin/python3
from tkinter import *
import tkinter.messagebox as tmsg
from webbrowser import open as open_web
from subprocess import getoutput
from tkinter.filedialog import asksaveasfilename,askopenfilename

def read_output(command):
	run = getoutput(command)
	text.insert(END, f"{run}\n")


def runattack():
	statusvar.set("Attacking...")
	sbar.update()
	argu = {"n" : nvalue.get(), "p" : pvalue.get() , "q" : qvalue.get() , "e" : evalue.get() , "key" : keyvalue.get(), "password" : passwordvalue.get() , "uncipher" : unciphervalue.get() , "attack" : box.get(ACTIVE) , "timeout" : slider.get() , "private" : privatevalue.get() , "verbosity" : verbosityvalue.get()}
	command = "/opt/rsactftool/rsactftool"
	for key,value in argu.items():
		if value:
			if key == "private":
				command += " --private"
			elif key in ["n","p","q","e"]:
				command += f" -{key} {value}"
			else:
				command += f" --{key} {value}"
	text.configure(state=NORMAL)
	text.delete("1.0", "end")
	text.insert(END, f"{command}\n\n")
	text.update()

	read_output(command)
	text.configure(state=DISABLED)
	text.bind("<1>", lambda event: text.focus_set())
	statusvar.set("Done")

def saveas():
	try:
		file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
		write = open(file,"w")
		write.write(text.get(1.0,END))
		write.close()
		statusvar.set("Done")
	except:
		statusvar.set("Ready")

def openfile():
	try:
		file = askopenfilename()
		read = open(file,"r")
		content = read.read()
		read.close()
		data_list = content.split("\n")
		for data in data_list:
			single_list = (data.split("="))
			if single_list[0].lower() == "n":
				nvalue.set(single_list[1])
			elif single_list[0].lower() == "e":
				evalue.set(single_list[1])
			elif single_list[0].lower() == "c":
				unciphervalue.set(single_list[1])
			elif single_list[0].lower() == "p":
				pvalue.set(single_list[1])
			elif single_list[0].lower() == "q":
				qvalue.set(single_list[1])
			elif single_list[0].lower() == "key":
				keyvalue.set(single_list[1])
			elif single_list[0].lower() == "password":
				passwordvalue.set(single_list[1])
			elif single_list[0].lower() == "attack":
				if single_list[1].lower() in attacks:
					index = attacks.index(single_list[1].lower())
					box.activate(index)
			elif single_list[0].lower() == "verbose":
				if single_list[1].lower() == "yes":
					verbosityvalue.set("INFO")
			elif single_list[0].lower() == "private_key":
				if single_list[1].lower() == "yes":
					privatevalue.set("yes")
			elif single_list[0].lower() == "timeout":
				try:
					slider.set(single_list[1])
				except:
					pass
			else:
				continue

	except:
		 statusvar.set("Ready")

def sage():
	open_web("https://www.sagemath.org/download.html")
	statusvar.set("Done")

def about_rsactftool():
	open_web("https://github.com/Ganapati/RsaCtfTool#RsaCtfTool")
	statusvar.set("Done")

def about_rsactftool_gui():
	open_web("https://github.com/Hellsender01/RsaCtfTool-GUI#RsaCtfTool-GUI")
	statusvar.set("Done")

def about_author():
	open_web("https://github.com/Hellsender01")
	statusvar.set("Done")
def help():
	open_web("https://github.com/Hellsender01/RsaCtfTool-GUI#Test")
	statusvar.set("Done")
# Creating Intial Style
root = Tk()

root.geometry(f"700x700")
root.title("RsaCtfTool-GUI")
root.maxsize(650,700)
root.resizable(0,0)
root.configure(background='grey')
try:
	img = PhotoImage(file='favicon.png')
	root.tk.call('wm','iconphoto',root._w, img)
except:
	pass

f = Frame(root,bg='#12232E')
f.pack(fill=BOTH)

f1 = Frame(f,bg='#12232E')
f1.grid(row=0,column=0)

Label(f1,text="N = ",bg='#12232E',font='Helvetica 14 bold').grid(row=1,column=0,pady=10)
Label(f1,text="P = ",bg='#12232E',font='Helvetica 14 bold').grid(row=2,column=0,pady=10)
Label(f1,text="Q = ",bg='#12232E',font='Helvetica 14 bold').grid(row=3,column=0,pady=10)
Label(f1,text="E = ",bg='#12232E',font='Helvetica 14 bold').grid(row=4,column=0,pady=10)
Label(f1,text="Key = ",bg='#12232E',font='Helvetica 14 bold').grid(row=5,column=0,pady=10)
Label(f1,text="Password = ",bg='#12232E',font='Helvetica 14 bold').grid(row=6,column=0,pady=10)
Label(f1,text="Cipher = ",bg='#12232E',font='Helvetica 14 bold').grid(row=7,column=0,pady=10)


verbosityvalue = StringVar()
verbosityvalue.set("")
unciphervalue = StringVar()
privatevalue = StringVar()
privatevalue.set("")
nvalue = StringVar()
pvalue = StringVar()
qvalue = StringVar()
evalue = StringVar()
keyvalue = StringVar()
passwordvalue = StringVar()
attackvalue = StringVar()


Entry(f1,textvariable=nvalue,bg="grey").grid(row=1,column=3)
Entry(f1,textvariable=pvalue,bg="grey").grid(row=2,column=3)
Entry(f1,textvariable=qvalue,bg="grey").grid(row=3,column=3)
Entry(f1,textvariable=evalue,bg="grey").grid(row=4,column=3)
Entry(f1,textvariable=keyvalue,bg="grey").grid(row=5,column=3)
Entry(f1,textvariable=passwordvalue,bg="grey").grid(row=6,column=3)
Entry(f1,textvariable=unciphervalue,bg="grey").grid(row=7,column=3)

f3 = Frame(f,bg='#12232E')
f3.grid(row=2)
Label(f3,text="Display Private Key ",bg='#12232E',font='Helvetica 14 bold').grid(row=0,column=1,pady=10)
Radiobutton(f3,text="yes",variable=privatevalue,value="yes",bg='#12232E',highlightthickness = 0, bd = 0).grid(row=0,column=2)
Radiobutton(f3,text="no",variable=privatevalue,value="",bg='#12232E',highlightthickness = 0, bd = 0).grid(row=0,column=3)
Label(f3,text="Enable Verbosity ",anchor="w",bg='#12232E',font='Helvetica 14 bold').grid(row=1,column=1,pady=10)
Radiobutton(f3,text="yes",variable=verbosityvalue,value="INFO",bg='#12232E',highlightthickness = 0, bd = 0).grid(row=1,column=2)
Radiobutton(f3,text="no",variable=verbosityvalue,value="",bg='#12232E',highlightthickness = 0, bd = 0).grid(row=1,column=3)

f4 = Frame(f,bg='#12232E')
f4.grid(row=0,column=1)
Label(f4,text="Attacks",bg='#12232E',font='Helvetica 14 bold').pack(pady=(20,0))
box = Listbox(f4,bg="grey")
box.pack(padx=100,pady=(1,20))
box.select_set(0)
attacks = ["all","pollard_p_1","londahl","boneh_durfee","smallfraction","pastctfprimes","siqs","binary_polinomial_factoring","smallq","pollard_rho","partial_q","noveltyprimes","wiener","cube_root","ecm","qicheng","mersenne_primes","comfact_cn","roca","fermat","factordb","ecm2","euler","same_n_huge_e","commonfactors","hastads"]
for valu in attacks:
	box.insert(END,valu)
Label(f4,text="Set Timeout For Attack",bg='#12232E',font='Helvetica 14 bold').pack(pady=(10,0))
slider = Scale(f4,from_=0,to=180,orient=HORIZONTAL,tickinterval=30,length=230,bg='#12232E', troughcolor="grey",borderwidth=2,highlightthickness = 0, bd = 0)
slider.set(60)
slider.pack()

f2 = Frame(f,bg='#12232E')
f2.grid(row=3,column=1,sticky="w")
Button(f2,text="Start Attack",command=runattack,bg="grey").pack(pady=(10))

f5 = Frame(root)
f5.pack(fill=BOTH)
scrollbar = Scrollbar(f5)
scrollbar.pack(side=RIGHT,fill=Y)
text= Text(f5,height=10,yscrollcommand = scrollbar.set)
text.pack(fill=X)
scrollbar.config(command=text.yview)


f6 = Frame(root)
f6.pack()
statusvar = StringVar()
statusvar.set("Ready")

sbar = Label(root,textvariable=statusvar,relief=SUNKEN,anchor="w")
sbar.pack(fill=BOTH)

mainmenu = Menu(root)

m1 = Menu(mainmenu,tearoff=0)
m1.add_command(label="Save Output",command=saveas)
m1.add_command(label="Open File",command=openfile)
m1.add_separator()
m1.add_command(label="Exit",command=root.destroy)
mainmenu.add_cascade(label="File",menu=m1)

m2 = Menu(mainmenu,tearoff=0)
m2.add_command(label="Download Sage",command=sage)
mainmenu.add_cascade(label="Sage",menu=m2)

m3 = Menu(mainmenu,tearoff=0)
m3.add_command(label="About RsaCtfTool",command=about_rsactftool)
m3.add_command(label="About RsaCtfTool-GUI",command=about_rsactftool_gui)
m3.add_command(label="About Author",command=about_author)
mainmenu.add_cascade(label="About",menu=m3)

m4 = Menu(mainmenu,tearoff=0)
m4.add_command(label="Help",command=help)
mainmenu.add_cascade(label="Help",menu=m4)

root.configure(menu=mainmenu)

root.mainloop()
