from Model.cnx import conectar

def ExibirAllModel(tabela):
    try:
        conn=conectar()
        cursor=conn.cursor()
        cursor.execute(f"SELECT * FROM {tabela}")
        resultado = cursor.fetchall()
        cursor.close()
        conn.close()
        if resultado:
            #print(f"Dados exibidos da tabela {tabela}: {resultado}")
            return resultado
        else:
            return False
    except Exception as e:
        print(f"Erro ao exibir dados selecionados: {e}")
        return False