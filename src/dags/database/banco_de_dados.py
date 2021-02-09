# Cria as tabelas


from database import ConexaoPostgres


class Banco:

    def __init__(self):
        conn = ConexaoPostgres()
        self.conexao = conn.conxexao_postgres()
        self.cria_tabela_jogos()
        self.cria_tabela_resultado()

    def cria_tabela_jogos(self):
        self.conexao.execute('''
                       CREATE TABLE if not exists mega.jogos(
                       cod_jogo SERIAL NOT NULL PRIMARY KEY ,
                       pri_num INT,
                       seg_num INT,
                       ter_num INT,
                       qua_num INT,
                       qui_num INT,
                       sex_num INT,
                       dt_carga DATE)''')

        return f'tabela criado com sucesso '

    def cria_tabela_resultado(self):
        self.conexao.execute('''
                       CREATE TABLE if not exists mega.resultados(
                       cod_jogo SERIAL NOT NULL PRIMARY KEY ,
                       num_concurso INT,
                       primeiro INT,
                       segundo INT,
                       terceiro INT,
                       quarto INT,
                       quinto INT,
                       sexto INT,
                       data_solteio DATE,
                       dt_carga DATE)''')

        return f'tabela criado com sucesso '
