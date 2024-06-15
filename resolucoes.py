import tkinter as tk
from media import media 
from mediana import mediana
from moda import moda
from minimo_ import minimo1
from maximo import maximo
from desvio_p import desvio_p
import statistics




def mostrar ():


    n1 =  i_entry.get()
    n2 =  i2_entry.get()
    n3 =  i3_entry.get()
    frequencia  = []
    frequencia.append(float(n1))
    frequencia.append(float(n2))
    frequencia.append(float(n3))
  

    text3.config(text =  f'Média :  {media(frequencia):.2f}')
    text4.config(text =  f'Moda :  {mediana(frequencia)}')
    text5.config(text =  f'Moda :  {moda(frequencia)}')
    text6.config(text =  f'Desvio padrão :  {desvio_p(frequencia):.2f}')
    text7.config(text =  f'Menor :  {min(frequencia)}')
    text8.config(text =  f'Maior :  {max(frequencia)}')
    
    



r = tk.Tk()
r.title('Teste')

r.geometry('600x700')

text = tk.Label(r, text = 'Média', font=80)
text.pack()



i_entry = tk.Entry(r)
i_entry.pack()
i2_entry = tk.Entry(r)
i2_entry.pack()
i3_entry = tk.Entry(r)
i3_entry.pack()



btn =  tk.Button(r, text =  'Clique aqui', command = mostrar)
btn.pack()


text3 = tk.Label(r, text = '', font = 150)
text3.pack()



text4 = tk.Label(r, text = '', font = 150)
text4.pack()



text5 = tk.Label(r, text = '', font = 150)
text5.pack()


text6 = tk.Label(r, text = '', font = 150)
text6.pack()


text7 = tk.Label(r, text = '', font = 150)
text7.pack()


text8 = tk.Label(r, text = '', font = 150)
text8.pack()



r.mainloop()