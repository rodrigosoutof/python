from tkinter import *


def manipulacao():
    nome = nome_entrada.get()
    lista = nome.split()
    espaco = nome.replace(' ', '')
    resultado.config(text=f''' Nome com todas letras maisculas: {nome.upper()}\n
                               Nome com todas letras minuscula: {nome.lower()}\n
                               O primeiro nome tem {len(lista[0])} letras\n
                               A quantidade de letras no seu nome são {len(espaco)} letras''')


janela = Tk()
janela.title = 'Manipulação de Strings'
janela.geometry('500x500')

texto01 = Label(janela, text='Digite seu nome completo: ')
texto01.grid(column=0, row=0, pady=5, padx=5)

nome_entrada = Entry(janela)
nome_entrada.grid(column=0, row=1, padx=5, pady=5)

botao = Button(janela, text=' OK ', command=manipulacao)
botao.grid(column=0, row=2, pady=5, padx=5)

resultado = Label(janela, text='')
resultado.grid(column=0, row=2, padx=5, pady=5)

janela.mainloop()







