class Palindromo:
    def __init__(self, palabra):
        self.palabra = palabra

    #Getters
    def get_palabra(self):
        return self.palabra
    
    #Metodos
    def es_palindromo(self):
        palabra = self.palabra.replace('', '').lower()
        return palabra == palabra[::-1]
    def resultado(self):
        if self.es_palindromo():
            return f"La palabra '{self.palabra}' es un palindromo"
        else:
            return f"La palabra '{self.palabra}' no es una palindromo"

    def test(self):
        return (self.palabra.upper())

    def __str__(self):
        return self.resultado()

def main():
    palabra = input("Escribe una palabra: ")
    palindromo = Palindromo(palabra)
    print(f">>> {palindromo.es_palindromo()} ")
    print(f"{palindromo.test()}")


main()