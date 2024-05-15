import streamlit as st
from funcoesCrud import *
import pandas as pd

st.title('Loja Do Gabriel')
st.write('teste Crud para meu portfolio')

col1, col2 = st.columns(2)
containercadastrar = col1.container(border=True)
containerAlterar = col2.container(border=True)
containercadastrar.markdown("**Cadastro produtos**")

with containercadastrar:
    st.header("Sistema de Cadastro de produtos")    

    st.write("Esse programa foi desenvolvido como teste")

    nome = st.text_input("Nome do produto", placeholder="max 50 caracteres")
    preco = float(st.number_input("Digite o valor do produto: "))
    imagem = st.text_input("imagem do produto", placeholder="url da imagem produto de até 100 caracteres")
    codigo = st.text_input("Código do produto:", placeholder="codigo do produto")

    btncadastro = st.button("Cadastrar produto")
with containerAlterar:

    containerAlterar.markdown('## Alterar Produtos')

    novo_nome = str(st.text_input("Digite o novo Nome Do Produto:"))
    novo_preco = float(st.number_input("Digite o novo valor do produto: "))
    nova_imagem = str(st.text_input("Digite o nova imagem do Produto", placeholder= "URL DA SUA IMAGEM"))
    id = st.text_input("Código do produto", placeholder="codigo do produto")

    btnatualizarproduto = st.button('alterar produto')
if btncadastro:
    cadastrar(nome, preco, codigo, imagem)
    st.write("Cadastro feito com sucesso")
elif  btnatualizarproduto:
    atualizarProdutos(id, novo_nome, nova_imagem, novo_preco)
    st.write("Alteraçao Feita Com Sucesso")




st.markdown("----------------------------------------")
st.markdown("**Atualiação do valor**")
novo_preco = float(st.number_input("Digite o novo valor do produto:"))
id = st.text_input("Código do produto", placeholder="codigo do produto", key=0)

btnatualizarpreco = st.button("Atualizar preço")

if btnatualizarpreco:
    atualizarPreco(id, novo_preco)
    st.write("Preço atualizado")

st.markdown("---------------------------------------")

st.markdown('**Deletar produto**')

id = st.text_input("Código do produto a ser deletado", placeholder="código do produto")
btndeletar = st.button("produto deletado")

if btndeletar:
    deletarProduto(id)
    st.write("Deletar produto")
containerListar = st.expander("todos os produtos")
with containerListar:
    listarProdutos = selecionarTodosProdutos()
    st.title("todos os produtos")
    tabelaProdutos = pd.DataFrame(listarProdutos, columns=('id','nomes', 'preço'))
    st.write(tabelaProdutos)

st.title('Pesquise seus produtos')
col3 = st.columns(1)
containerProcurar = st.container(border=True)

with containerProcurar:
    containerProcurar.markdown('## BUSCAR UM PRODUTO')
    id = containerProcurar.text_input('ID DO PRODUTO')
    btnpesquisar = containerProcurar.button('Pesquisar') 

if btnpesquisar:
    produto = ProcurarProduto(id)
    if produto:
        subcol1 = containerProcurar.container()
        subcol1.write(f'nome: {produto[0][1]}')  # Acessa o segundo elemento da tupla dentro da lista
        subcol1.write('image:')
        try: 
            print (produto[0][3])
            st.image(f'{produto[0][3]}', width=200)  # Você pode querer acessar o link da imagem também
        except:
            subcol1.write('null')