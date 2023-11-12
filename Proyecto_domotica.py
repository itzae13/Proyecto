from tkinter import *
from tkinter import messagebox
import pymysql

def menu_principal():

    global home
    home=Tk()
    home.title('Smart Home')
    home.geometry('300x380')

    home.iconbitmap("Logo.ico")
    image=PhotoImage(file='Logo.gif')
    image=image.subsample(2,2)
    label=Label(image=image)
    label.pack()

    Label(text='Bienvenido a Smart Home',bg='navy',fg='white',width='300',height='3',font=('calibri',15)).pack()
    Label(text='').pack()

    Boton1=Button(text='Iniciar Sesión', height='3', width='30',command=iniciar_sesion).pack()
    Label(text='').pack()

    Boton2=Button(text='Registrarse', height='3', width='30',command=registrarse).pack()
    home.mainloop()

def iniciar_sesion():
    global Inicio
    Inicio = Toplevel(home)
    Inicio.geometry('400x280')
    Inicio.title('Iniciar Sesión')
    Inicio.iconbitmap("Logo.ico")

    Label(Inicio, text='Por favor ingrese\n usuario y contraseña', bg='navy',fg='white',width='300',height='3',font=('calibri',20)).pack()
    Label(Inicio,text='').pack()

    global usuario_verify
    global contrasena_verify

    usuario_verify=StringVar()
    contrasena_verify=StringVar()

    global usuario_entry
    global contrasena_entry

    Label(Inicio, text='Usuario').pack()
    usuario_entry = Entry(Inicio, textvariable=usuario_verify)
    usuario_entry.pack()
    Label(Inicio).pack()

    Label(Inicio, text='Contraseña').pack()
    contrasena_entry = Entry(Inicio,show="*", textvariable=contrasena_verify)
    contrasena_entry.pack()
    Label(Inicio).pack()
    
    Botonini=Button(Inicio,text='Iniciar Sesión',command=validacion_datos).pack()

def registrarse():

    global registro
    registro = Toplevel(home)
    registro.geometry('500x370')
    registro.title('Registrarse')
    registro.iconbitmap("Logo.ico")

    global usu_entry
    global contr_entry
    global clave

    usu_entry=StringVar()
    contr_entry=StringVar()
    clave=StringVar()

    Label(registro, text='Ingrese la clave de acceso,\n usuario y contraseña que desee', bg='navy',fg='white',width='300',height='3',font=('calibri',20)).pack()
    Label(registro,text='').pack()

    Label(registro, text='Clave de acceso proporcionada').pack()
    clave=Entry(registro)
    clave.pack()
    Button(registro,text='Verificar',command=clave_acceso).pack()
    Label(registro,text='').pack()

    Label(registro, text="Usuario").pack()
    usu_entry = Entry(registro)
    usu_entry.pack()
    Label(registro).pack()

    Label(registro, text="Contraseña").pack()
    contr_entry = Entry(registro,show="*")
    contr_entry.pack()
    Label(registro).pack()

    Button(registro,text='Registrar',command=b_datos).pack()

def b_datos():
    bd=pymysql.connect(
        host='localhost',
        user='root',
        passwd='',
        db='domotica'
        )
    
    fcursor=bd.cursor()
    sql="INSERT INTO login (Usuario, Contrasena) VALUES('{0}' , '{1}')".format(usu_entry.get(), contr_entry.get())

    try:
        fcursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message='Registro Exitoso',title='Aviso')
    except:
        bd.rollback()
        messagebox.showinfo(message='No registrado',title='Aviso')
    
    bd.close()

def validacion_datos():
    bd=pymysql.connect(
        host='localhost',
        user='root',
        passwd='',
        db='domotica'
        )
    
    fcursor=bd.cursor()
    fcursor.execute("SELECT Contrasena FROM login WHERE Usuario='"+usuario_verify.get()+"'and Contrasena='"+contrasena_verify.get()+"'")

    if fcursor.fetchall():
        messagebox.showinfo(title='Inicio de sesión correcto',message='Usuario y Contraseña correctos')
    
    else:
        messagebox.showinfo(title='Inicio de sesión Incorrecto',message='Usuario y Contraseña incorrectos')
    bd.close()

def clave_acceso():
    bd=pymysql.connect(
        host='localhost',
        user='root',
        passwd='',
        db='domotica'
        )
    
    fcursor=bd.cursor()
    fcursor.execute("SELECT codigo FROM clave_acceso WHERE codigo='"+clave.get()+"'")

    if fcursor.fetchall():
        messagebox.showinfo(title='Inicio de sesión correcto',message='Usuario y Contraseña correctos')
    
    else:
        messagebox.showinfo(title='Clave de acceso',message='Clave de acceso incorrecta,\nverifique la información del producto')
    bd.close()

menu_principal()   

