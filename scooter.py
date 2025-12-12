from tipomotos import TipoMotos

class Scooter(TipoMotos):
    def __init__(self, modelo, ano, cilindrada):
        super().__init__(modelo, ano, cilindrada)
        self.transmissao = "automática"
    
    def analisar(self):
        return f"{self.descrever()}: {self.transmissao}, urbana prática."
