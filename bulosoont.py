class Habilidade:
    def __init__(self, nomeHabilidade, grauDominio):
        self.nomeHabilidade = nomeHabilidade 
        self.grauDominio = grauDominio 

class Projeto:
    def __init__(self, nomeProjeto, dificuldadeProjeto):
        self.nomeProjeto = nomeProjeto 
        self.dificuldadeProjeto = dificuldadeProjeto 

class Professor:
    def __init__(self, nomeProfessor):
        self.nomeProfessor = nomeProfessor 

class Aluno:
    def __init__(self, nomeAluno, matricula, habilidades):
        if not habilidades or len(habilidades) < 1:
            raise ValueError(f"Restrição violada: {nomeAluno} deve ter no mínimo 1 habilidade.") 
        self.nomeAluno = nomeAluno 
        self.matricula = matricula 
        self.habilidades = habilidades
        self.grupo = None

    def get_maior_habilidade(self):
        # Retorna o objeto Habilidade que tem a maior nota 
        return max(self.habilidades, key=lambda hab: hab.grauDominio)

class Grupo:
    def __init__(self, nomeGrupo, projeto, professor):
        if projeto is None:
            raise ValueError("Restrição violada: Grupo deve desenvolver exatamente 1 projeto.") 
        self.nomeGrupo = nomeGrupo
        self.projeto = projeto
        self.professor = professor
        self.alunos = []

    def adicionar_aluno(self, aluno):
        if aluno.grupo is not None:
            return False 
        self.alunos.append(aluno)
        aluno.grupo = self
        return True

#INSTÂNCIAS 


alunos = [
   
    Aluno("João Silva", "2023001", [Habilidade("Python", 5)]),
    Aluno("Fernanda Gomes", "2023008", [Habilidade("Python", 3)]),
    Aluno("Ana Costa", "2023005", [Habilidade("Java", 5), Habilidade("Python", 2)]),
    Aluno("Maria Clara", "2023002", [Habilidade("C++", 4)]),
    Aluno("Pedro Henrique", "2023003", [Habilidade("Java", 4), Habilidade("C++", 2)]),
    Aluno("Lucas Souza", "2023004", [Habilidade("Java", 3), Habilidade("C++", 4)]),
    Aluno("Marcos Lima", "2023006", [Habilidade("Python", 5), Habilidade("Java", 3)]),
    Aluno("Julia Alves", "2023007", [Habilidade("C++", 3), Habilidade("Java", 2)]),
    Aluno("Diego Dias", "2023009", [Habilidade("C++", 5), Habilidade("Python", 1)]),
    Aluno("Camila Rocha", "2023010", [Habilidade("Java", 5)]),
    Aluno("Bruno Martins", "2023011", [Habilidade("C++", 5), Habilidade("Java", 2)]),
    Aluno("Letícia Faria", "2023012", [Habilidade("Python", 4)])
]

projetos = [
    Projeto("IA na Saúde", 5),
    Projeto("IoT na Agricultura", 4),
    Projeto("E-commerce", 3),
    Projeto("Site Institucional", 2)
]

professores = [
    Professor("Prof. Dr. Roberto Mendes"),
    Professor("Profa. Dra. Elaine Souza"),
    Professor("Prof. Dr. Carlos Silva"),
    Professor("Profa. Dra. Ana Costa")
]

nomes_grupos = ["Grupo Alpha", "Grupo Beta", "Grupo Gamma", "Grupo Delta"]

# ALGORITMO GULOSO
def formar_grupos_guloso(lista_alunos, lista_projetos, lista_professores):
    print(" INICIANDO ALGORITMO GULOSO \n")
    
    projetos_ordenados = sorted(lista_projetos, key=lambda p: p.dificuldadeProjeto, reverse=True)
    # Ordena os alunos com base na nota da sua melhor habilidade
    alunos_ordenados = sorted(lista_alunos, key=lambda a: a.get_maior_habilidade().grauDominio, reverse=True)
    
    grupos_formados = []
    
    for i, projeto in enumerate(projetos_ordenados):
        nome_grupo = nomes_grupos[i]
        professor = lista_professores[i]
        grupo = Grupo(nome_grupo, projeto, professor)
        
        print(f"=> Analisando Projeto Alvo: '{projeto.nomeProjeto}' (Dificuldade: {projeto.dificuldadeProjeto})")
        print(f"   [Ontologia] {professor.nomeProfessor} ORIENTA o {nome_grupo}")
        print(f"   [Ontologia] {nome_grupo} DESENVOLVE o projeto '{projeto.nomeProjeto}'")
        
        alunos_no_grupo = 0
        capacidade_maxima = 3 
        
        for aluno in alunos_ordenados:
            if alunos_no_grupo == capacidade_maxima:
                break 
                
            if aluno.grupo is None: 
                melhor_hab = aluno.get_maior_habilidade()
                print(f"   [Guloso] Alocando {aluno.nomeAluno} (Maior Grau: {melhor_hab.grauDominio} em {melhor_hab.nomeHabilidade})")
                grupo.adicionar_aluno(aluno)
                alunos_no_grupo += 1
                
        grupos_formados.append(grupo)
        print("-" * 65)
        
    print("\n FIM DO ALGORITMO ")
    return grupos_formados

formar_grupos_guloso(alunos, projetos, professores)