from tkinter import *

janela = Tk()
janela.title('Calculadora 2.0')
janela.geometry('250x250')

texto_escolha = Label(janela, text='\nEscolha a função que deseja\n'
                                   '1 - SOMA\n'
                                   '2 - MULTIPLICAÇÃO\n'
                                   '3 - MAIOR\n'
                                   '4 - TROCAR VALORES\n'
                                   '5 - FINALIZAR PROGRAMA\n'
                                   'ESCOLHA: ')
texto_escolha.pack(fill='both', expand=True)
texto_escolha.grid(column=0, row=0, padx=10, pady=10)

janela.mainloop()
