"""Lista = [3,"/",9,"*",8]
for i in range(0,5):
	if Lista[i]
	print (Lista[i])


precio = 5
cadenas = ['9+3*2+2']

for cadena in cadenas:
    print(eval(cadena))
"""


from tkinter import *

raiz=Tk()

miFrame=Frame(raiz)

miFrame.pack()

operacion=""

reset_pantalla=False

resultado=0

#-------------pantalla---------------------------------------

numeroPantalla=StringVar()

pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")


#-------------------pulsaciones teclado--------------------------

def numeroPulsado(num):

	global operacion

	global reset_pantalla

	if (num =="0" and len(numeroPantalla.get())==0):
		numeroPantalla.set("")
		reset_pantalla=True

	elif (num=="0" and reset_pantalla==True):
		reset_pantalla=True

	elif reset_pantalla!=False:

			numeroPantalla.set(num)
			reset_pantalla=False

	else:

		numeroPantalla.set(numeroPantalla.get() + num)


def el_resultado():

	global reset_pantalla

	numeroPantalla.set(eval(numeroPantalla.get()))

	reset_pantalla=True




#-------------fila 1---------------------------------------------

boton7=Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8=Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9=Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)
botonDiv=Button(miFrame, text="/", width=3, command=lambda:numeroPulsado("/"))
botonDiv.grid(row=2, column=4)


#-------------fila 2---------------------------------------------

boton4=Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=3, column=1)
boton5=Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6=Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)
botonMult=Button(miFrame, text="x", width=3, command=lambda:numeroPulsado("*"))
botonMult.grid(row=3, column=4)

#-------------fila 3---------------------------------------------

boton1=Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2=Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3=Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)
botonRest=Button(miFrame, text="-", width=3, command=lambda:numeroPulsado("-"))
botonRest.grid(row=4, column=4)


#-------------fila 4---------------------------------------------

boton0=Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=1)
botonIgual=Button(miFrame, text="=", width=3, command=lambda:el_resultado())
botonIgual.grid(row=5, column=3)
botonSum=Button(miFrame, text="+", width=3, command=lambda:numeroPulsado("+"))
botonSum.grid(row=5, column=4)





raiz.mainloop()