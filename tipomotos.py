class TipoMotos:
    def __init__(self, modelo, ano, cilindrada):
        self.modelo = modelo
        self.ano = ano
        self.cilindrada = cilindrada
    
    def descrever(self):
        return f"Moto {self.modelo} {self.ano}, {self.cilindrada}cc"
    
    def analisar(self):
        return f"{self.descrever()}: Análise genérica."
