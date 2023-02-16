import os.path
from datetime import datetime
#from tkinter import *
from tkinter import messagebox, scrolledtext, INSERT,END,Tk,Menu,Label,Button,W,NW,E,S,N,Entry,IntVar,Radiobutton
from tkinter.ttk import Combobox

localGastos = "C:\\Users\\hleit\\Documents\\Carteira\\gastos.txt"

class Gasto:
    cat = ""
    valor = 0.0
    coment = ""

def pastaExiste():
    if os.path.exists("C:/Users/hleit/Documents/Carteira"): 
        if os.path.isfile("C:/Users/hleit/Documents/Carteira/gastos.txt") == 0:
            arq = open(localGastos, "w")
            arq.close()
    else:
        os.mkdir("C:/Users/hleit/Documents/Carteira")
        arq = open(localGastos, "w")
        arq.close()

def apagaArq():
    f = open(localGastos, "w")
    f.close()

def confirma():
    res = messagebox.askyesno('Aviso !','Você deseja mesmo apagar todos os gastos ?')
    if res == True:
        apagaArq()

def frameGasto(str):
    txtA.insert(INSERT,"============================================================\n")
    txtA.insert(INSERT,"Data: %s/%s/%s\n" %(str[1],str[2],str[0]))
    txtA.insert(INSERT,"Categoria: %s\n" %str[3])
    txtA.insert(INSERT,"Valor: %s\n" %str[4])
    txtA.insert(INSERT,"Comentário:")
    for i in range(5,len(str)):
        txtA.insert(INSERT," %s" %str[i])
    txtA.insert(INSERT,"\n")

def limpaTudo():
    txt.delete(0,"end")
    txt1.delete(0,"end")

def salvaInf(gasto):
    pastaExiste()
    
    f = open(localGastos, "a")

    d = datetime.today()

    f.write("%s " %d.year)
    f.write("%s " %d.day)
    f.write("%s " %d.month)

    f.write("%s " %gasto.cat)
    f.write("%.2f " %gasto.valor)
    f.write("%s\n"  %gasto.coment)

    f.close()

    messagebox.showinfo('Aviso !!!','Tudo foi concluido com sucesso !!!')

    limpaTudo()

def atualizaLista():
    txtA.delete(0.0,END)
    procuraArq("Ano","")

def atualizaListaM():
    txtA.delete(0.0,END)
    procuraArq("Mes","")

def procuraArq(tipo,cat):

    pastaExiste()

    d = datetime.today()
    anoAtual = d.year
    mesAtual = d.month
    diaAtual = d.day
    gastoTot = 0.0
    cont = 0
    global txtA

    txtA.delete(0.0,END)

    f = open(localGastos,"r")

    linhas = f.readlines()

    for i in range(0,len(linhas)):
        linhaAtual = linhas[i]
        str = linhaAtual.split()

        if len(str) == 0:
            break

        if tipo == "Ano":
            if int(str[0]) == anoAtual:
                frameGasto(str)

                cont += 1
                gastoTot += float(str[4])

        elif tipo == "Mes":
            if int(str[2]) == mesAtual or (int(str[1]) <= diaAtual and int(str[2]) == mesAtual-1):
                frameGasto(str)

                cont += 1
                gastoTot += float(str[4])

        elif tipo == "Filtro":
            if str[3] == cat:
                frameGasto(str)

                cont += 1
                gastoTot += float(str[4])

    if cont == 0:
        txtA.insert(INSERT,"============================================================\n")            
        txtA.insert(INSERT,"                 Nenhum gasto Encontrado !!!\n")   
        txtA.insert(INSERT,"============================================================\n")
    else:
        txtA.insert(INSERT,"============================================================\n")   
        txtA.insert(INSERT,"                Gasto total: %.2f\n" %gastoTot)   
        txtA.insert(INSERT,"============================================================\n")   
    f.close()

def gastoAnual():

    ############################################################ Criando a Janela #########################################################

    anual = Tk()
    anual.title("Gasto Anual")

    windowWidth = 500
    windowHeight = 500

    positionRight = int(anual.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(anual.winfo_screenheight()/2 - windowHeight/2)

    anual.geometry("{}x{}+{}+{}".format(windowWidth,windowHeight,positionRight, positionDown))

    ############################################################ Criando o menu ##########################################################

    menu = Menu(anual)
    anual.config(menu=menu,background=cor)
    opcoes = Menu(menu, tearoff=0)
    menu.add_cascade(label= "Opções",menu = opcoes)

    opcoes.add_command(label= "Ver gastos do mês", command = gastoMensal)
    opcoes.add_command(label= "filtrar gastos por categoria", command = filtro)
    opcoes.add_command(label= "Atualizar lista", command = atualizaLista)
    opcoes.add_separator()
    opcoes.add_command(label= "Voltar", command= anual.destroy)

    ############################################################ Código ##################################################################
    global txtA

    txtA = scrolledtext.ScrolledText(anual,width=60,height=31,background=corSec)
    txtA.grid(column=0,row=0)

    procuraArq("Ano","")

    anual.mainloop()

def gastoMensal():
    ############################################################ Criando a Janela #########################################################

    mensal = Tk()
    mensal.title("Gasto Mensal")

    windowWidth = 500
    windowHeight = 500

    positionRight = int(mensal.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(mensal.winfo_screenheight()/2 - windowHeight/2)

    mensal.geometry("{}x{}+{}+{}".format(windowWidth,windowHeight,positionRight, positionDown))

    ############################################################ Criando o menu ##########################################################

    menu = Menu(mensal)
    mensal.config(menu=menu,background=cor)
    opcoes = Menu(menu, tearoff=0)
    menu.add_cascade(label= "Opções",menu = opcoes)

    opcoes.add_command(label= "Ver gastos do Ano", command = gastoAnual)
    opcoes.add_command(label= "filtrar gastos por categoria", command = filtro)
    opcoes.add_command(label= "Atualizar lista", command = atualizaListaM)
    opcoes.add_separator()
    opcoes.add_command(label= "Voltar", command= mensal.destroy)

    ############################################################ Código ##################################################################
    global txtA

    txtA = scrolledtext.ScrolledText(mensal,width=60,height=31,background=corSec)
    txtA.grid(column=0,row=0)

    procuraArq("Mes","")

    mensal.mainloop()

def filtro():
    ############################################################ Criando a Janela #########################################################

    filtro = Tk()
    filtro.title("Gasto por Categoria")
    filtro.configure(background=cor)

    windowWidth = 500
    windowHeight = 620

    positionRight = int(filtro.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(filtro.winfo_screenheight()/2 - windowHeight/2)

    filtro.geometry("{}x{}+{}+{}".format(windowWidth,windowHeight,positionRight, positionDown))

    ############################################################ Criando o menu ##########################################################

    menu = Menu(filtro)
    filtro.config(menu=menu)
    opcoes = Menu(menu, tearoff=0)
    menu.add_cascade(label= "Opções",menu = opcoes)

    opcoes.add_command(label= "Ver gastos do Ano", command = gastoAnual)
    opcoes.add_command(label= "Ver gastos do Mes", command = gastoMensal)
    opcoes.add_separator()
    opcoes.add_command(label= "Voltar", command= filtro.destroy)

    ############################################################ Código ##################################################################
    global txtA
    coisas = []

    def mandaProcurar():
        cat = combo.get()
        procuraArq("Filtro",cat)


    lbl4 = Label(filtro,text= "Escolha uma categoria para filtrar ", font=("Arial", 14),background=cor )
    lbl4.place(relx = 0, rely = 0.02, anchor = W)

    f = open(localGastos,"r")

    linhas = f.readlines()

    for i in range(0,len(linhas)):
        linhaAtual = linhas[i]
        str = linhaAtual.split()

        if str[3] not in coisas:
            coisas.append(str[3])
    f.close()

    tupla = tuple(coisas)

    combo = Combobox(filtro)
    combo['values']= tupla
    combo.current(0) #set the selected item
    combo.place(relx = 0.6, rely = 0.022, anchor = W)

    txtA = scrolledtext.ScrolledText(filtro,width=60,height=30,background=corSec)
    txtA.place(relx = 0, rely = 0.15, anchor = NW)

    btn1 = Button(filtro, text= "Continuar", font=("Arial", 14), command= mandaProcurar,background=corSec)
    btn1.place(relx = 0.84, rely = 0.1, anchor = E )

    cat = combo.get()
    procuraArq("Filtro",cat)

    filtro.mainloop()

def CadastraCatNova():
    def pegaSTR():
        if " " in cat.get() :
            messagebox.showwarning('Aviso !!!','A categoria não pode conter espaços')
            janelaCat.focus_force()
        else:
            global catNova

            catNova = str(cat.get())
            janelaCat.quit()
            janelaCat.destroy()

    janelaCat = Tk()
    janelaCat.title("Gerenciador")

    windowWidth = 400
    windowHeight = 150

    positionRight = int(janelaCat.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(janelaCat.winfo_screenheight()/3 - windowHeight/2)

    janelaCat.geometry("{}x{}+{}+{}".format(windowWidth,windowHeight,positionRight, positionDown))

    lbl4 = Label(janelaCat, text= "Por favor digite uma categoria para o gasto", font=("Arial", 14))
    lbl4.place(relx = 0.5, rely = 0, anchor = N)

    cat = Entry(janelaCat,width = 40)
    cat.place(relx = 0.5, rely = 0.4, anchor = N)

    btn1 = Button(janelaCat, text= "Continuar", font=("Arial", 14), command= pegaSTR)
    btn1.place(relx = 0.5, rely = 0.9, anchor = S )
    cat.focus_set()
    janelaCat.mainloop()

def recolheInf():
    gasto = Gasto

    if selected.get() > 0:
            if len(txt.get()) == 0:
                messagebox.showwarning('Aviso !!!','Por favor, Digite o valor que foi gasto !')

            else:
                gasto.valor = float(txt.get())

                if selected.get() == 1:
                    gasto.cat = "Transporte"
                elif selected.get() == 2:
                    gasto.cat = "Estudos" 
                elif selected.get() == 3:
                    gasto.cat = "Alimentacao" 
                elif selected.get() == 4:
                    CadastraCatNova()
                    gasto.cat = catNova

                gasto.coment = txt1.get()

                salvaInf(gasto)

    else:
         messagebox.showwarning('Aviso !!!','Por favor, selecione uma Categoria !')

############################################################ Criando a Janela #########################################################
master = Tk()
master.title("Gerenciador")

windowWidth = 500
windowHeight = 500

positionRight = int(master.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(master.winfo_screenheight()/3 - windowHeight/2)

master.geometry("{}x{}+{}+{}".format(windowWidth,windowHeight,positionRight, positionDown))


############################################################ Criando o menu #########################################################

cor = "navajo white"
corSec = "linen"

menu = Menu(master,background=corSec,foreground= corSec,activebackground= cor,activeforeground =cor)
opcoes = Menu(menu, tearoff=0)
menu.add_cascade(label= "Mais opções",menu = opcoes)
master.configure(background=cor,menu=menu)

opcoes.add_command(label= "Ver Gastos do ano", command = gastoAnual)
opcoes.add_command(label= "Ver gastos do mês", command = gastoMensal)
opcoes.add_command(label= "filtrar gastos por categoria", command = filtro)
opcoes.add_separator()
opcoes.add_command(label= "Apagar todos os gastos", command = confirma)
opcoes.add_separator()
opcoes.add_command(label= "Sair", command= master.quit)

############################################################ Label ##################################################################

lbl = Label(master, text="Gerenciador Financeiro", font=("Arial Bold", 18),background=cor)
lbl.place(relx = 0.5, rely = 0., anchor = N)

lbl1 = Label(master, text= "Escolha uma categoria para o gasto:", font=("Arial", 14),background=cor )
lbl1.place(relx = 0.5, rely = 0.1, anchor = N)

lbl2 = Label(master,text= "Valor do gasto: ", font=("Arial", 14),background=cor)
lbl2.place(relx = 0.5, rely = 0.27, anchor = N)

lbl3 = Label(master,text= "Digite um comentario: ", font=("Arial", 14),background=cor)
lbl3.place(relx = 0.5, rely = 0.37, anchor = N)

############################################################ Textos #################################################################

txt = Entry(master,width = 20,background=corSec)
txt.place(relx = 0.5, rely = 0.32, anchor = N)

txt1 = Entry(master,width = 30,background=corSec)
txt1.place(relx = 0.5, rely = 0.43, anchor = N)

############################################################ Rad Buttons ############################################################

selected = IntVar()

rad = Radiobutton(master, text= "Transporte", value= 1, var= selected,background=cor)
rad.place(relx = 0.4, rely = 0.15, anchor = N )

rad1 = Radiobutton(master, text= "Estudos", value= 2, var= selected,background=cor)
rad1.place(relx = 0.6, rely = 0.15, anchor = N )

rad2 = Radiobutton(master, text= "Alimentação", value= 3, var= selected,background=cor)
rad2.place(relx = 0.405, rely = 0.2, anchor = N )

rad3 = Radiobutton(master, text= "Outros", value= 4, var= selected,background=cor)
rad3.place(relx = 0.595, rely = 0.2, anchor = N )

############################################################ Botões ##################################################################

btn = Button(master, text= "Continuar", font=("Arial", 14), command= recolheInf,background=cor)
btn.place(relx = 0.5, rely = 0.7, anchor = S )

txt.focus_set()
master.mainloop()
