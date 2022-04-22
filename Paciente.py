class Paciente:
    def __init__(self, nome_completo, tipo_sanguineo, data_nascimento):
        self.nome_completo = nome_completo
        self.tipo_sanguineo = tipo_sanguineo
        self.data_nascimento = data_nascimento
    
    def __repr__(self) -> str:
        return f'Paciente: {self.nome_completo}, Tipo Sanguíneo: {self.tipo_sanguineo}, Data de Nascimento: {self.data_nascimento}'
