import copy  

class ConfiguracaoSessao:
    def __init__(self, volume=8, luzes="médio", mostrar_trailer=True, legendas=False, adicionais=None):
        self.volume = volume
        self.luzes = luzes
        self.mostrar_trailer = mostrar_trailer
        self.legendas = legendas
        self.adicionais = adicionais if adicionais is not None else []

    def clonar(self):
        """
        Cria uma cópia (clone) independente deste objeto.
        """
       
        return copy.deepcopy(self)

    def descrever(self):
        """
        Retorna uma descrição legível da configuração da sessão.
        """
        return (f"Volume: {self.volume}, Luzes: {self.luzes}, "
                f"Trailer: {self.mostrar_trailer}, Legendas: {self.legendas}, "
                f"Adicionais: {self.adicionais}")




padrao = ConfiguracaoSessao()


sessao1 = padrao.clonar()
sessao2 = padrao.clonar()


sessao1.volume = 5
sessao1.adicionais.append("pipoca com borda de queijo")

sessao2.luzes = "baixa"
sessao2.legendas = True


print("Sessão padrão:", padrao.descrever())
print("Sessão 1 (clone modificado):", sessao1.descrever())
print("Sessão 2 (clone modificado):", sessao2.descrever())
