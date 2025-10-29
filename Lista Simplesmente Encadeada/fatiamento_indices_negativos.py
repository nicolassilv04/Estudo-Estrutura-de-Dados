class Lista:
    class No:
        def __init__(self, valor, proximo= None):
            self.valor = valor
            self.proximo = proximo

        def __str__(self):
            return str(self.valor)

    def __init__(self):
        self.__cabeca = None
        self.__quantidade = 0

    def __len__(self):
        return self.__quantidade
    
    #PARA CONVERTER PARA STRING NO FORMATO [str, str, str]
    def __str__(self):
        return '[' +  ', '.join([str(valor) for valor in self]) + ']'
    
    #FUNÇÃO QUE ITERA OS ITENS
    def __iter__(self):
        atual = self.__cabeca
        while atual is not None:
            yield atual.valor #quando chegar nessa parte pausa a execução, então a partir da proxima começa aqui jáff
            atual = atual.proximo
    
    
    #FUNÇÃO QUE RECUPERA OS ELEMENTOS
    def __getitem__(self,posicao):
        if posicao < 0:
            posicao = len(self) + posicao

        if posicao < 0 or posicao >= self.__quantidade:
            raise IndexError('Posiçao invalidas')
        
        atual = self.__cabeca
        for i in range(posicao):
            atual = atual.proximo

        return atual.valor
    
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

lista.inserir(posicao=0, valor=5)
lista.inserir(posicao=1, valor=20)
lista.inserir(posicao=2, valor=15)
lista.inserir(posicao=2, valor=7)

print(lista)