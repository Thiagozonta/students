class Endereco:
    def __init__(self,rua,nr,bairro,cidade,estado,pais):
        self.rua = rua
        self.nr = nr
        self.bairro = bairro
        self.cidade = cidade

    def __repr__(self):
        return f"Rua={self.rua}, Nr={self.nr}, Bairro:{self.bairro}, Cidade={self.cidade}"