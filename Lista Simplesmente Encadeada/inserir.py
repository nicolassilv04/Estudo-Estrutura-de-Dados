class Lista:
    class No:
        def __init__(self, valor, proximo= None):
            self.valor = valor
            self.proximo = proximo

    def __init__(self):
        self.__cabeca = None
        self.__quantidade = 0

    def __len__(self):
        return self.__quantidade
    
    def inserir(self, posicao, valor):
        novo = self.No(valor)
        self.__quantidade +=1
        """para quando a lista esta vazia"""
        if self.__cabeca is None:#se cabeca for nulo ele recebe o No(valor), ou seja, novo
            self.__cabeca = novo
            return
        
        if posicao <= 0:
            """caso seja indicado o index 0 ou negativo ele vira a cabeça"""
            novo.proximo = self.__cabeca
            self.__cabeca = novo
            return
        
        i = 0 #indice do elemento atual
        atual = self.__cabeca
        #buscando o elemento anteiror a posição que queremos inserir
        while atual.proximo is not None and i < posicao - 1:
            atual = atual.proximo
            i += 1 

        novo.proximo = atual.proximo
        atual.proximo = novo

lista = Lista()

print(len(lista))

lista.inserir(posicao=0, valor=5)
lista.inserir(posicao=1, valor=20)
lista.inserir(posicao=2, valor=15)
lista.inserir(posicao=2, valor=7)

print(len(lista))