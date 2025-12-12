from tipomotos import TipoMotos

class Street(TipoMotos):
    def __init__(self, modelo, ano, cilindrada):
        super().__init__(modelo, ano, cilindrada)
        self.posicao = "vertical"
    
    def analisar(self):
        return f"{self.descrever()}: Urbana, posição {self.posicao}, ideal para cidade."
