class A: 
    def z(self): 
        return self
     
    #Devuelve la longitud
    def y(self, t): 
        return len(t) 


#Asignar clase 'A' a la variable 'a' (a=clase de tipo 'A') 
a = A 
"""
Comprobar que a es clase con metodo type(): 
"""
print(type(a))

#Asigna metodo z de clase 'a' a la variable 'y' (asigna clase 'A')
y = a.z 
#Devuelve que 'y' es la clase 'A' (<class '__main__.A'>)
print(y(a)) 

#Crear objeto de la clase 'A' y se lo asigno a la variable 'aa'
aa = a()
#Verificar si 'aa' y 'a()' son del mismo tipo
"""
Es falso ya que a() es el constructor y aa es el objeto creado
""" 
print(aa is a()) 

#Del objeto 'aa', asigno el metodo 'y' a 'z'
z = aa.y 
#Devuelve '0' ya que z no tiene longitud
print(z(())) 
#Crea otro objeto de tipo A, llama al metodo 'y' con parametro la tupla (a,) devolviendo '1'
print(a().y((a,))) 

#Llamo  al metodo 'y' de la clase 'A', pasandole los parametros 'aa' (objeto) y la tupla '(a,z)', devolviendo la longitud de '(a,z)' que es '2'
print(A.y(aa, (a,z))) 

#Llamo al metodo 'y' del objeto 'aa' y le paso la tupla '(z,1,'z')', devolviendo longitud '3'
print(aa.y((z,1,'z'))) 
