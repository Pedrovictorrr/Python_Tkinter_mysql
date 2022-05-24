# -*- coding: cp1252 -*-
from turtle import onclick
import mysql.connector
from setuptools import Command

conexao = mysql.connector.connect(
                 host = 'localhost',
                 user = 'root',
                 passwd=''
                 )

cursor = conexao.cursor()
cursor.execute('show databases')

for x in cursor:
  cursor
cursor.execute('use tela_login')



#CRIAR TABELAS DE USUARIOS
#cursor.execute('create table usuario(cod int primary key auto_increment,\nnome varchar(40),Usuario varchar(40), senha varchar(40),email varchar(255))')
#cursor.execute('create table adm(cod int primary key auto_increment,\nnome varchar(40),Usuario varchar(40), senha varchar(40),email varchar(255))')


from tkinter import *

def login1():
    login = Tk()
    def __init__():
        pass
    def cadastro():
        login.destroy()
        cadastrar = Tk()

#===================== Cadastrar no banco de dados        
        def cadastrar1():
            flag2 = 0
            email = str(e_email.get())
            lista1=(email,)
            cursor.execute("select email from usuario")
            result2 = cursor.fetchall()
            for i in result2:
                print(i)
                if i == lista1:
                    print("Email em uso")
                    flag2 = 1
                


            usuario = str(e_usuario.get())
            lista2=(usuario,)
            cursor.execute("select Usuario from usuario")
            result3 = cursor.fetchall()
            for i in result3:
                print(i)
                if i == lista2:
                    print("Usuario ja esta em uso")
                    flag2 = 2
            
            nome = str(e_nome.get())
            senha = str(e_senha.get())
            senha2 = str(e_senha2.get())
            L_Nome = nome
            L_Email = email
            L_Usuario = usuario
            L_Senha1 = senha
            L_Senha2 = senha2
            print ("Nome: ", L_Nome)
            print ("email: ", L_Email)
            print ("Usuario: ", L_Usuario)
            print ("Senha: ", L_Senha1)
            print ("Senha Confirmada:",L_Senha2)
            def login3():
                sucesso.destroy()
                login1()
            if L_Senha1 == L_Senha2 and flag2 == 0:  
                cadastrar.destroy()
                sucesso = Tk()
                text = Label(text="Cadastro realizado com sucesso")
                text.place(x=15, y=25)
                sql1="insert into usuario(nome,Usuario,email,senha) values (%s,%s,%s,%s)"
                val = [(nome,usuario,email,senha)]
                cursor.executemany(sql1,val)
                conexao.commit()
                print(cursor.rowcount,'registro(s) inseridos')
                login2 = Button(text="Logar",command=login3)
                login2.place(x=15,y=50)
                sucesso.geometry("200x100")
                sucesso.mainloop()  
            elif L_Senha1 == L_Senha2 and flag2 == 1:
                erro = Label(text="Falha ao criar conta!")
                erro.place(x=15,y=210)
                erro2 = Label(text="Email ja em uso!")
                erro2.place(x=15,y=230)
            elif L_Senha1 == L_Senha2 and flag2 == 2:
                erro = Label(text="Falha ao criar conta!")
                erro.place(x=15,y=210)
                erro2 = Label(text="Usuario ja em uso!")
                erro2.place(x=15,y=230)
            elif L_Senha1 != L_Senha2:
                erro = Label(text="Falha ao criar conta!")
                erro.place(x=15,y=210)
                erro2 = Label(text="Senhas nao se coincidem!")
                erro2.place(x=15,y=230)


        

#========================================== Tela de cadastro:

        titulo1 = Label(text='Cadastro')
        titulo1.place(x=130, y=10)

        e_nome = Entry(width=25)
        e_nome.place(x=130, y=50)
        Info1 = Label(text='Nome:')
        Info1.place(x=10, y=50)

        e_email = Entry(width=25)
        e_email.place(x=130, y=75)
        Info2 = Label(text='Email:')
        Info2.place(x=10, y=75)

        e_usuario = Entry(width=25)
        e_usuario.place(x=130, y=100)
        Info3 = Label(text='Usuario:')
        Info3.place(x=10, y=100)

        e_senha = Entry(width=25,show="*")
        e_senha.place(x=130, y=125)
        Info4 = Label(text='Senha:')
        Info4.place(x=10, y=125)

        e_senha2 = Entry(width=25,show="*")
        e_senha2.place(x=130, y=150)
        Info5 = Label(text='Confirmar senha:')
        Info5.place(x=10, y=150)

        cadastro = Button(width='39', text='Cadastrar', command=cadastrar1)
        cadastro.place(x=15, y=175)
        cadastrar.geometry('300x260')
        cadastrar.mainloop()

    def esqueci():
        user=Tk()
        user.title("Esqueci minha senha:")
        Label(user,text="Informe o email cadastrado:").grid(pady=5,column=0,row=1)
        Entry(user, width=40).grid(pady=5,column=1,row=1)
        Button(user,text="Enviar",width=50).grid(pady=3,padx=10,columnspan=2,column=0,row=2)
        user.mainloop()
        
    
#============================= tela de login
    def entrar1():
        flag =0
        cursor.execute("select email,senha from usuario")
        result = cursor.fetchall()
        senha = str(Login_senha_entry.get())
        email = str(login_usuario_entry.get())
        print(senha)
        print(email)
        lista = (email,senha)
        print(lista)
        for i in result:
            print(i)
            if i == lista:
                login.destroy()
                Logado = Tk()
                print("Login efetuado com sucesso")
                sucesso = Label(text="Login efetuado com sucesso")
                sucessoms = Label(text="Seja bem vindo {nome} !")
                sucessoms.place(x=10,y=50)
                sucesso.place(x=10,y=25)
                flag = 1
                Logado.geometry("200x100")
                Logado.mainloop
        if flag == 0:
            print("Usuario ou senha incorretos")
            erro = Label(text="Usuario ou senha incorretos")
            erro.place(x=10,y=175)

    Titulo = Label(text="Tela de login",font=("Arial",20))
    Titulo.place(x=130,y=10)
    login_usuario_label = Label(text="Usuario")
    login_usuario_label.place(x=10, y=50)
    login_usuario_entry = Entry( width=40)
    login_usuario_entry.place(x=130, y=50)

    login_senha_label = Label(text="Senha")
    login_senha_label.place(x=10, y=75)
    Login_senha_entry = Entry(width=40,show="*")
    Login_senha_entry.place(x=130, y=75)

    entrar = Button(text="Entrar",width=50,command=entrar1)
    entrar.place(x=15,y=100)

    

    cadastrar = Button(text="Cadastrar",width=50,command=cadastro)
    cadastrar.place(x=15,y=125)

    esqueci_senha = Button(text="Esqueci minha senha.",width=50,command=esqueci)
    esqueci_senha.place(x=15,y=150)

    login.geometry('400x200')
    login.title("Tela de login")
    login.mainloop()
    
login1()
