'''Metode Newton'''

import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
import tkinter

def start(Event):
    mulai()
    
def mulai():
    global masukan
    masukan = e.get()
    newton()
#    e.delete(0, tkinter.END)
#    tebak_x.delete(0, tkinter.END)
#    toleransi.delete(0, tkinter.END)
def mulai_akar():
    global masukan
    masukan = e.get()
    newton_akar()
    
def newton():
    global masukan, jend2, f
    
#    jendela2.grid_forget()
#    jendela2 = tkinter.Frame(window)
#    jendela2.grid(row=0,column=1)
#    f_simbol = (1/2)*(x**2)-sym.sin(x)
    jend2.pack_forget()
    jend2 = tkinter.Frame(window_baru)
    jend2.pack()
    
    x = sym.symbols('x')
    f_simbol = masukan
    f = sym.lambdify([x],f_simbol)
    
    dfdx_simbol = sym.diff(f_simbol,x)
    dfdx2_simbol = sym.diff(f_simbol,x,2)
    
    dfdx = sym.lambdify([x],dfdx_simbol)
    dfdx2 = sym.lambdify([x],dfdx2_simbol)
    
    i = 0
    n = 1
    a = 0
    x = float(tebak_x.get())
    tol = float(toleransi.get())
    label2_1 = tkinter.Label(jend2,text="                                       Diperoleh :                                       ",font="TNR 16 bold",bg="white",fg='black')
    label2_1.pack()
    space2_1 = tkinter.Label(jend2,text="------------------------------------------------------------------------------------------\n",
                                 font="Candana 12",bg='white')
    space2_1.pack()
    while abs(x-a)>tol:
        
        a = x
        x = x-dfdx(x)/dfdx2(x)
#        print("p"+str(n)+"= ",x)
        label2_i = tkinter.Label(jend2,text=("                                          p{0} = {1}                                            ".format(n,x)),
                                 font="Candana 12",bg='white')
        label2_i.pack()
        space_i = tkinter.Label(jend2,text="                                                                                                                    ",
                                 font="Candana 12",bg='white')
        space_i.pack()
        i+=1
        n+=1
    akar = tkinter.Label(jend2, text="                                  Titik nilai minimum nya adalah {0}                                  ".format(x),font="Candana 12",bg='lightblue')
    akar.pack()
    nilai_akar = tkinter.Label(jend2, text="                                  f(x) = {0}                                  ".format(f(x)),font="Candana 12",bg='lightblue')
    nilai_akar.pack()
    plt.clf()
    
    return f(0)

def newton_akar():
    global masukan, jend2, f
    
#    jendela2.grid_forget()
#    jendela2 = tkinter.Frame(window)
#    jendela2.grid(row=0,column=1)
#    f_simbol = (1/2)*(x**2)-sym.sin(x)
    jend2.pack_forget()
    jend2 = tkinter.Frame(window_baru)
    jend2.pack()
#    canvas = tkinter.Canvas(jend2)
    sb = tkinter.Scrollbar(jend2, orient = 'vertical')
    sb.pack(side=tkinter.RIGHT,fill='y')
#    canvas.pack()
    
    x = sym.symbols('x')
    f_simbol = masukan
    f = sym.lambdify([x],f_simbol)
    
    dfdx_simbol = sym.diff(f_simbol,x)
    dfdx = sym.lambdify([x],dfdx_simbol)
    
    i = 0
    n = 1
    a = 0
    x = float(tebak_x.get())
    tol = float(toleransi.get())
    label2_1 = tkinter.Label(jend2,text="                                       Diperoleh :                                       ",font="TNR 16 bold",bg="white",fg='black')
    label2_1.pack()
    space2_1 = tkinter.Label(jend2,text="------------------------------------------------------------------------------------------\n",
                                 font="Candana 12",bg='white')
    space2_1.pack()
    while abs(x-a)>tol:
        
        a = x
        x = x-f(x)/dfdx(x)
#        print("p"+str(n)+"= ",x)
        label2_i = tkinter.Label(jend2,text=("                                          p{0} = {1}                                            ".format(n,x)),
                                 font="Candana 12",bg='white')
        label2_i.pack()
        space_i = tkinter.Label(jend2,text="                                                                                                                    ",
                                 font="Candana 12",bg='white')
        space_i.pack()
        i+=1
        n+=1
    akar = tkinter.Label(jend2, text="                                  Akarnya adalah {0}                                  ".format(x),font="Candana 12",bg='lightblue')
    akar.pack()
    nilai_akar = tkinter.Label(jend2, text="                                  f(x) = {0}                                  ".format(f(x)),font="Candana 12",bg='lightblue')
    nilai_akar.pack()
    plt.clf()

    
def plots():
    global masukan
    x = sym.symbols('x')
    f_simbol = masukan
    f = sym.lambdify([x],f_simbol)
    
    x1 = np.arange(-4,4,0.01)
    y1 = []
    
    for i in x1:
        y1.append(f(i))
        
    plt.plot(x1,y1)
    plt.title("Grafik Fungsi $f(x)$")
    plt.legend(['$f(x)$'],loc='best')
    plt.axis([min(x1),max(x1),min(y1),max(y1)])
    plt.xlabel('sumbu x')
    plt.ylabel('sumbu y')
    plt.grid()
 
    plt.show()
    

'''Menu'''
def buatMenu():
    menubar = tkinter.Menu(window)
    menusize = tkinter.Menu(window, tearoff=False)
    menusize.add_command(label="Info", command= info)
    menusize.add_separator()
    menusize.add_command(label="Help", command= bantuan)
    menubar.add_cascade(label="Menu", menu=menusize)
    menubar.add_command(label="Keluar", command= keluar)
    window.config(menu=menubar)
 
def bantuan():
    tkinter.messagebox.showinfo("Metode Newton",'Masukan tebakan, fungsi, dan toleransi')
    
def keluar():
    answer=tkinter.messagebox.askquestion("Keluar","Apakah anda ingin keluar beneran?",icon='question')
    if answer=='yes':
        window.destroy()
        window_baru.destroy()
    else :
        tkinter.messagebox.showinfo("NOTIF","Selamat datang kembali",icon='info')
         
def info():
    tkinter.messagebox.showinfo("Creator","Steven & Tassya",icon='info')         
         


#print(np.sin(0.5))
#print(newton(f,fprime,1000,0.001))

window = tkinter.Tk()
window.title("Metode Newton")
window_baru = tkinter.Tk()
window_baru.title("Hasil Iterasi")

window.geometry("580x280")
window_baru.geometry("500x500")
window.bind('<Return>', start)
window_baru.configure(bg="white", relief="groove",bd='30')

jendela1=tkinter.Frame(window)
jendela1.configure(background="lightblue",relief="groove",bd='25')
jendela1.grid(row=0,column=0)
jend2=tkinter.Frame(window_baru)
jend2.pack()
#jendela2 = tkinter.Frame(window)
#jendela2.grid(row=0,column=1)



label22 = tkinter.Label(jend2,text="HASIL",font="Arial 18 bold italic",bg="white",fg='black')
label22.pack()

label1 = tkinter.Label(jendela1,text="-- Metode Newton --",font="Courier 18 bold underline",bg="lightblue",fg='black')
label1.grid(row=0,column=1)
space1 = tkinter.Label(jendela1,text="\n",bg="lightblue",fg='white')
space1.grid(row=1,column=0)

teks_1 = tkinter.Label(jendela1,text="Tebak x",font="Candana 12",bg="lightblue",fg='black')
teks_1.grid(row=2,column=0)
teks_2 = tkinter.Label(jendela1,text="Fungsi f(x)",font="Candana 12",bg="lightblue",fg='black')
teks_2.grid(row=2,column=1)
teks_3 = tkinter.Label(jendela1,text="Toleransi",font="Candana 12",bg="lightblue",fg='black')
teks_3.grid(row=2,column=2)


tebak_x = tkinter.Entry(jendela1,bg="lightgray")
tebak_x.grid(row=3,column=0)
e = tkinter.Entry(jendela1,bg="lightgray")
e.focus_set()
e.grid(row=3,column=1)
toleransi = tkinter.Entry(jendela1,bg="lightgray")
toleransi.grid(row=3,column=2)

space2 = tkinter.Label(jendela1,text="---\n",bg="lightblue",fg='white')
space2.grid(row=4,column=2)

tombol_mulai = tkinter.Button(jendela1,text="TITIK MINIMUM",font="System 12 bold",bg="white",relief="groove",
                      command=mulai,height=2,width=15)
tombol_mulai.grid(row=5,column=0)
tombol_mulai2 = tkinter.Button(jendela1,text="AKAR",font="System 12 bold",bg="white",relief="groove",
                      command=mulai_akar,height=2,width=15)
tombol_mulai2.grid(row=5,column=2)
space3 = tkinter.Label(jendela1,text="-------\n",bg="lightblue",fg='white')
space3.grid(row=6,column=0)

tombol_refresh = tkinter.Button(jendela1,text="PLOT",font="System 12 bold",bg="white",relief="groove",
                      command=plots,height=2,width=10)
tombol_refresh.grid(row=5,column=1)

buatMenu()
window.mainloop()
window_baru.mainloop()
