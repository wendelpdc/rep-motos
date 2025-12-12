from tipomotos import TipoMotos

class Esportiva(TipoMotos):
    def __init__(self, modelo, ano, cilindrada):
        super().__init__(modelo, ano, cilindrada)
        self.posicao = "agachada"
    
    def analisar(self):
        return f"{self.descrever()}: {self.posicao}, alta performance em pista."
