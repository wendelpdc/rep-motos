from tipomotos import TipoMotos

class Custom(TipoMotos):
    def __init__(self, modelo, ano, cilindrada):
        super().__init__(modelo, ano, cilindrada)
        self.estilo = "cruiser baixo"
    
    def analisar(self):
        return f"{self.descrever()}: {self.estilo}, conforto em longas distâncias."
