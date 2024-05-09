import mysql.connector
import mysql

def conectarBd():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="loja",
    )

    cursor = conexao.cursor()
    print("Conexão como o banco de dados feita com sucesso! \n")

    return conexao,cursor


# funcao inserir
def cadastrar(nome: str, preco: float, id: str, img: str):
    ''' Faz a inserção de um produto no banco de dados. A imagem é a URL da imagem do produto na web.
    Utilizar formatos encurtados com quantidade de caracteres inferiores a 100
    Você poderá usar o https://www.encurtarlink.com/ para ajustar ao formato adequado'''

    conexao, cursor = conectarBd()
    comando_sql = f"insert into produtos (nome, preco, id, imagem) value ('{nome}', {preco},'{id}','{img}')"

    cursor.execute(comando_sql)
    conexao.commit() # aqui é onde vamos inserir os dados
    print("Produto cadastrado com sucesso!")
    conexao.close()

# funcao selecionar
def selecionarTodosProdutos():
    conexao, cursor = conectarBd()
    comando_sql = f'select id, nome, preco from produtos'
    cursor.execute(comando_sql)
    resultado_consulta = cursor.fetchall()
    return resultado_consulta


# funcao atualizar
def atualizarPreco(id: str, novo_preco: float):
    conexao, cursor = conectarBd()
    comando_sql = f'UPDATE loja.produtos SET preco = {novo_preco}, WHERE nome = "{id}"'
    cursor.execute(comando_sql)
    conexao.commit()

#Alterar Produtos
def atualizarProdutos(id: str, novo_nome: str, nova_imagem: str, novo_preco: float):
    conexao, cursor = conectarBd()
    comando_sql = f'UPDATE loja.produtos SET nome = "{novo_nome}", preco = {novo_preco}, imagem= "{nova_imagem}" WHERE id = "{id}";'
    cursor.execute(comando_sql)
    conexao.commit()
    
# funcao deletar
def deletarProduto(id: str):
    conexao, cursor = conectarBd()
    comando_sql = f'DELETE FROM loja.produtos WHERE id = "{id}"'
    cursor.execute(comando_sql)
    conexao.commit()


