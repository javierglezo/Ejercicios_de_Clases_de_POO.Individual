class Zapato: 
    def metodo_1(self): 
        return self
     
    #Devuelve la longitud
    def metodo_2(self, t): 
        return len(t) 


#Asignar clase 'Zapato' a la variable 'zapato' (zapato=clase de tipo 'Zapato') 
zapato = Zapato 
"""
Comprobar que zapato es clase con metodo type(): 
"""
print(type(zapato))

#Asigna metodo 'metodo_1' de clase 'zapato' a la variable 'y' (asigna clase 'Zapato')
y = zapato.metodo_1 
#Devuelve que 'y' es la clase 'Zapato' (<class '__main__.Zapato'>)
print(y(zapato)) 

#Crear objeto de la clase 'Zapato' y se lo asigno a la variable 'nike'
nike = zapato()
#Verificar si 'nike' y 'zapato()' son del mismo tipo
"""
Es falso ya que zapato() es el constructor y nike es el objeto creado
""" 
print(nike is zapato()) 

#Del objeto 'nike', asigno el metodo 'metodo_2' a 'count_nike'
count_nike = nike.metodo_2 
#Devuelve '0' ya que count_nike no tiene longitud
print(count_nike(())) 
#Crea otro objeto de tipo Zapato, llama al metodo 'metodo_2' con parametro la tupla (zapato,) devolviendo '1'
print(zapato().metodo_2((zapato,))) 

#Llamo  al metodo 'metodo_2' de la clase 'Zapato', pasandole los parametros 'nike' (objeto) y la tupla '(nike,count_nike)', devolviendo la longitud de '(nike,count_nike)' que es '2'
print(Zapato.metodo_2(nike, (zapato,count_nike))) 

#Llamo al metodo 'metodo_2' del objeto 'nike' y le paso la tupla '(count_nike,1,'z')', devolviendo longitud '3'
print(nike.metodo_2((count_nike,1,'z'))) 
