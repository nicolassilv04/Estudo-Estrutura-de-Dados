class Lista:
    class No:
        def __init__(self, valor, proximo= None):
            self.valor = valor
            self.proximo = proximo

        def __str__(self):
            return str(self.valor)

    def __init__(self, iteravel = None):
        self.__cabeca = None
        self.__cauda = None
        self.__quantidade = 0

        if iteravel is not None and hasattr(iteravel, '__iter__'):
            for item in iteravel:
                self.inserir_no_fim(item)
        elif iteravel is not None:
            raise TypeError(f'O objeto{type(iteravel)} não é iteravel')

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
    
    def __delitem__(self,posicao):
        if posicao < 0:
            posicao = len(self) + posicao

        if posicao < 0 or posicao >=self.__quantidade:
            raise IndexError('Posição Invalida')
        
        self.__quantidade -= 1

        #removendo da cabeça
        if posicao == 0:
            self.__cabeca = self.__cabeca.proximo
            if self.__cabeca is None:
                self.__cauda == None
            return

        i = 0
        atual = self.__cabeca

        while atual.proximo is not None and i < posicao - 1:
            atual = atual.proximo
            i = i + 1

        #removendo da cauda
        if atual.proximo == self.__cauda:
            self.__cauda = atual

        atual.proximo = atual.proximo.proximo

    def __setitem__(self, posicao, valor):
        if posicao < 0:
            posicao = len(self) + posicao

        if posicao < 0 or posicao >= self.__quantidade:
            raise IndexError('Posição Invalida')
        
        atual = self.__cabeca
        for i in range(posicao):
            atual = atual.proximo

        atual.valor = valor

    #FUNÇÃO QUE RECUPERA OS ELEMENTOS
    def __getitem__(self, posicao):
        if isinstance(posicao, slice):
            passo = posicao.step if posicao.step is not None else 1

            if passo == 0:
                raise ValueError('Passo não pode ser zero')

            if passo > 0:
                inicio = posicao.start if posicao.start is not None else 0
                fim = posicao.stop if posicao.stop is not None else len(self)
            else: 
                inicio = posicao.start if posicao.start is not None else len(self) - 1
                fim = posicao.stop if posicao.stop is not None else -1

            if inicio < 0:
                inicio = len(self) + inicio
            if fim < 0 and posicao.stop is not None:
                fim = len(self) + fim

            fatia = Lista()
            
            if passo > 0:
                i = 0
                indices = range(inicio, fim, passo)
                it = iter(self)
                while i < fim:
                    try:
                        v = next(it)
                    except StopIteration:
                        break
                    if i in indices:
                        fatia.inserir_no_fim(v)
                    i += 1
            else:
                for i in range(inicio, fim, passo):
                    fatia.inserir_no_fim(self[i])

            return fatia  # <<< return aqui, fim do slice

        # <<< A PARTIR DAQUI: só executa se NÃO for slice >>>
        else:
            if posicao < 0:
                posicao = len(self) + posicao

            if posicao < 0 or posicao >= self.__quantidade:
                raise IndexError('Posiçao invalidas')
            
            atual = self.__cabeca
            for _ in range(posicao):
                atual = atual.proximo

            return atual.valor
        
    def inserir_no_fim(self, valor):
        novo = self.No(valor)
        self.__quantidade += 1

        #quando a lista é vazia
        if self.__cabeca is None:
            self.__cabeca = novo
            self.__cauda = novo
            return
        
        self.__cauda.proximo = novo
        self.__cauda = novo



    def inserir(self, posicao, valor):
        novo = self.No(valor)
        self.__quantidade +=1
        """para quando a lista esta vazia"""
        if self.__cabeca is None:#se cabeca for nulo ele recebe o No(valor), ou seja, novo
            self.__cabeca = novo
            self.__cauda = novo
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

        if atual.proximo is None:
            self.__cauda = novo
 
        novo.proximo = atual.proximo
        atual.proximo = novo

lista = Lista()

lista.inserir(posicao=0, valor=5)
lista.inserir(posicao=1, valor=20)
lista.inserir(posicao=2, valor=15)
lista.inserir(posicao=2, valor=7)
lista.inserir_no_fim(10)

print(lista)