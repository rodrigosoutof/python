from tkinter import * #importanto todas informações da biblioteca tkinter

texto_resposta['text'] = variavel de resposta # edita o espaço em branco do parametro texto

janela = Tk()
janela.title('Primeira Tela')
janela.geometry('250x250')

texto_orientacao = Label(janela, text='Texto de exibição') #criando um texto na tela
texto_orientacao.grid(column=0, row=0, padx=10, pady=10) #definindo a posição da label de acordo com linhas e colunas

botao = Button(janela, text='Função executada', command= colocar função) #inserir função sem colocar parentes para que seja executado assim que clicar
botao.grid(column=0, row=1, padx=10, pady=10)

texto_resposta = Label(janela, text=' ')
texto_resposta.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop() #para manter a janela exibida


