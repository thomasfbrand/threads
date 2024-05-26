import threading

class meuThread(threading.Thread): # Criação classe Thread, assim como na aula
    def __init__(self, sublista, resultado, index):
        threading.Thread.__init__(self)
        self.sublista = sublista
        self.resultado = resultado
        self.index = index

    def run(self): # método run comandará a ação da thread
        self.resultado[self.index] = sum(self.sublista)

def soma_lista(lista): #funcao que divide lista em 2 sublistas e realização das threads para fazer a soma
    meio = len(lista) // 2
    sublista1 = lista[:meio]
    sublista2 = lista[meio:]

    # Lista para armazenar os resultados
    resultado = [0, 0]

    thread1 = meuThread(sublista1, resultado, 0)
    thread2 = meuThread(sublista2, resultado, 1)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    soma_total = sum(resultado)
    return soma_total

lista1 = [1, 23, 34, 45, 56, 67, 68, 100]
lista2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
lista3 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 200]

print("Soma da lista1:", soma_lista(lista1))
print("Soma da lista2:", soma_lista(lista2))
print("Soma da lista3:", soma_lista(lista3))
