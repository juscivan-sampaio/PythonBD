import MySQLdb

def conectar():
    try:
        conn = MySQLdb.connect(
            db= 'pmysql',
            host= 'localhost',
            user= 'root',
            passwd= '',
        )
        return conn
    except MySQLdb.Error as e:
        print(f'erro ao se conectar: {e}')

def desconectar(conn):
    if conn:
        conn.close()

def listar():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()

    if len(produtos) > 0:
        print('Listando produtos...')
        print('------------------------')
        for produtos in produtos:
            print(f'ID: {produtos[0]}')
            print(f'Nome: {produtos[1]}')
            print(f'Preço: {produtos[2]}')
            print(f'Estoque: {produtos[3]}')
    else:
        print('Não existe produtos cadastrados.')
    desconectar(conn)

def inserir():
    conn = conectar()
    cursor = conn.cursor()

    nome = input('Insira o nome do produto:')
    preco = float(input('Informe o preço do produto: '))
    estoque = int(input('Insira o estoque do produto: '))

    cursor.execute(f"INSERT INTO produtos (nome, preco, estoque) VALUES ('{nome}', {preco}, {estoque})")
    conn.commit()

    if cursor.rowcount == 1:
        print(f'O produto {nome} foi inserido com sucesso!')
    else:
        print('Não foi possivel inserir o produto.')

    desconectar(conn)

def atualizar():
    conn = conectar()
    cursor = conn.cursor()

    codigo = int(input('Insira o codigo do produto: '))
    nome = input('Informe o novo nome do produto:')
    preco = float(input('Informe o novo preço do produto: '))
    estoque = int(input('Informe a nova quantidade em estoque: '))

    cursor.execute(f"UPDATE produtos SET nome='{nome}', preco={preco}, estoque={estoque} WHERE id={codigo}")
    conn.commit()

    if cursor.rowcount == 1:
        print(f'Produto {nome} foi atualizado com sucesso!')
    else:
        print('Erro ao atualizar o produto.')
    desconectar(conn)

def deletar():
    conn = conectar()
    cursor = conn.cursor()

    codigo = int(input('Insira o codigo do produto: '))
    cursor.execute(f"DELETE FROM produtos WHERE id={codigo}")
    conn.commit()

    if cursor.rowcount == 1:
        print('Produto foi deletado com sucesso!')
    else:
        print(f'Erro ao excluir o produto com id = {codigo}')
    desconectar(conn)

def menu():
    print('=============Gerenciamento de produtos=============')
    while True:
        print('''
    Selecione uma opção:
    1- Listar Produtos
    2- Inserir Produto
    3- Atualizar Produto
    4- Deletar Produto
    5- Sair do sistema''')
        op = int(input())
        if op == 1:
            listar()
        elif op == 2:
            inserir()
        elif op == 3:
            atualizar()
        elif op == 4:
            deletar()
        elif op == 5:
            break
        else:
            print('Opção invalida!')
