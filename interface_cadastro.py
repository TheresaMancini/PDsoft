from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import ttk
import psycopg2
from tkinter.ttk import *



###Classe Conexão
########################################################################################################
class Conexao(object):
    _db=None    
    def __init__(self, mhost, db, usr, pwd):
     self._db = psycopg2.connect(host='', database=dbInclude, user=postgres,  password=teste)
    def manipular(self, sql):
       try:
            cur=self._db.cursor()
            cur.execute(sql)
            cur.close();
            self._db.commit()
       except:
           return False;
       return True;
    def consultar(self, sql):
       rs=None
       try:
           cur=self._db.cursor()
           cur.execute(sql)
           rs=cur.fetchall();
       except:
           return None
       return rs
    def proximaPK(self, tabela, chave):
       sql='select max('+chave+') from '+tabela
       rs = self.consultar(sql)
       pk = rs[0][0]  
       return pk+1
    def fechar(self):
       self._db.close()

##################################################################################################################################
class Membro:
	nome = 

########################################################################################################################

window = Tk()

window.title("Include Engenharia")

tab_control = ttk.Notebook(window)


tab1 = ttk.Frame(tab_control)

tab2 = ttk.Frame(tab_control)

tab3 = ttk.Frame(tab_control)

tab4 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Ver Projetos')

tab_control.add(tab2, text='Ver Membros')

tab_control.add(tab3, text='Cadastrar Membros')

tab_control.add(tab4, text='Cadastrar Projetos')

#################################################################################################################################

combo = Combobox(tab1)

combo['values']= ("Otimização Wi-fi", "Mobile", "Automação")

combo.current(0) #set the selected item

combo.pack()

lista = scrolledtext.ScrolledText(tab1,width=40,height=10)
lista.pack()

#################################################################################################################################
### Aba de Ver Membros

combo = Combobox(tab2)

combo['values']= ("Presidência", "Projetos ", "Vice Presidência", "Marketing ", "Gestão de Pessoas", "Administrativo-Finânciero")

combo.current(0) #set the selected item

combo.pack()

lista = scrolledtext.ScrolledText(tab2,width=40,height=10)
lista.pack()
#################################################################################################################################
### Aba de Cadastro de Membros 

nomelbl = Label(tab3, text="Nome")

nomelbl.grid(column=0, row=0)

txt_nome = Entry(tab3,width=40)

txt_nome.grid(column=1, row=0)

cpflbl = Label(tab3, text="Cpf")

cpflbl.grid(column=0, row=2)

txt_cpf = Entry(tab3,width=40)

txt_cpf.grid(column=1, row=2)

emaillbl = Label(tab3, text="E-mail")

emaillbl.grid(column=0, row=3)

txt_email = Entry(tab3,width=40)

txt_email.grid(column=1, row=3)

cursolbl = Label(tab3, text="Curso")

cursolbl.grid(column=0, row=4)

txt_curso = Entry(tab3,width=40)

txt_curso.grid(column=1, row=4)

cursolbl = Label(tab3, text="Diretoria")

cursolbl.grid(column=0, row=5)

combo = Combobox(tab3)

combo['values']= ("Presidência", "Projetos ", "Vice Presidência", "Marketing ", "Gestão de Pessoas", "Administrativo-Finânciero")


combo['width']=38

combo.current(0) #set the selected item

combo.grid(column=1, row=5)

nascimentolbl = Label(tab3, text="Data de Nascimento")

nascimentolbl.grid(column=0, row=6)

nascimento = Entry(tab3,width=40)

nascimento.grid(column=1, row=6)


def clicked():

    messagebox.showinfo('Cadastro', 'Cadastro Realizado')

btn = Button(tab3,text='Cadastrar', command=clicked)
btn. grid(column = 0, row = 7, columnspan = 3, rowspan = 1, sticky=N+S+E+W)


tab_control.pack(expand=1, fill='both')

#################################################################################################################################
### Aba de Cadastro de Projetos

nomelbl = Label(tab4, text="Nome do Projeto")

nomelbl.grid(column=0, row=0)

txt_nome = Entry(tab4,width=40)

txt_nome.grid(column=1, row=0)

nomeprojetolbl = Label(tab4, text="Categoria do Projeto")

nomeprojetolbl.grid(column=0, row=1)

combo = Combobox(tab4)

combo['values']= ("Otimização Wi-fi", "Mobile", "Automação")

combo['width']=38

combo.current(0) #set the selected item

combo.grid(column=1, row=1)

def clicked():

    messagebox.showinfo('Cadastro', 'Cadastro Realizado')

btn = Button(tab4,text='Cadastrar', command=clicked)
btn.grid(column = 0, row = 2, columnspan = 2, rowspan = 1, sticky=N+S+E+W)


tab_control.pack(expand=1, fill='both')


try:
    conn=psycopg2.connect("dbname='dbInclude' user='postgres' password='teste'")
except:
    print ("I am unable to connect to the database.")

window.mainloop()


