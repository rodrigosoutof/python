#05 - Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor.
from tkinter import *

#def ordem_numerica():
 #   n1 = int(input('Digite um numero: '))
  #  texto_exibicao['text'] = print(f'O número antecessor é {valor-1}\n O numero sucessor é {valor+1}')

def atualizar_exibicao():
    valor = int(valor_entrada.get())
    texto_exibicao.config(text= f'O número antecessor é {valor-1}\n O número sucessor é {valor+1}')

janela = Tk()
janela.title = 'Ordem numerica'
janela.geometry('360x200')

texto_orientacao = Label(janela, text='Vamos verificar o número antecessor e sucessor da sua escolha.')
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

valor_entrada = Entry(janela)
valor_entrada.grid(column=0, row=1, pady=10, padx=10)

botao = Button(janela, text='Executar', command=atualizar_exibicao)
botao.grid(column=0, row=2, padx=10, pady=10)

texto_exibicao = Label(janela, text=' ')
texto_exibicao.grid(column=0, row=3, padx=10, pady=10)


janela.mainloop()




