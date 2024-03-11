class Logger:
    def __init__(self):
        self.log_count = 0
        self.file = open('log.txt', 'w')
        self.file.write("--Start log--\n")

    def log(self, mensaje):
        self.log_count += 1
        self.file.write(mensaje + '\n')

    def __cerrar__(self):
        self.file.write("--End log: {} log(s)--\n".format(self.log_count))
        self.file.close()


class Test:
    def __init__(self):
        self.logger = Logger()

    def llamada(self, mensaje):
        self.logger.log(mensaje)


def main():
    test = Test()
    for i in range(1, 6): 
        if i == 1: 
            test.llamada("Primera llamada") 
        else: 
            test.llamada("{}ª llamada".format(i))

main()