from Model.cnx import conectar
def limpar_banco_de_dados():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            DROP TABLE IF EXISTS 
                nota, 
                aluno_disciplina, 
                disciplina, 
                aluno, 
                professor 
            CASCADE;
        """)

        conexao.commit()
        cursor.close()
        conexao.close()
        print("Todas as tabelas foram removidas com sucesso!")
    except Exception as e:
        print(f"Erro ao limpar banco de dados: {e}")
