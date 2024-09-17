# E-commerce API com Flask

<img style="width: 500px" alt="" src="https://i.imgur.com/YKwYE04.png">

Uma aplicação de e-commerce simples desenvolvida com **Flask**, **Flask-SQLAlchemy** e **Flask-Login**, que inclui funcionalidades básicas de autenticação de usuários, gerenciamento de produtos e carrinho de compras. Esta aplicação usa hashing de senhas para garantir a segurança dos dados dos usuários e oferece uma API para a criação, atualização, exclusão e listagem de produtos.

## Funcionalidades

- **Autenticação de usuários**: Registre, faça login e logout de usuários.
- **Gerenciamento de produtos**: Adicione, atualize, liste e exclua produtos.
- **Carrinho de compras**: Relaciona usuários com produtos em um carrinho de compras simples.
- **Segurança de senhas**: As senhas dos usuários são armazenadas utilizando hash seguro (usando `Werkzeug`).
- **CORS habilitado**: Preparado para interações com frontend de domínios diferentes.

## Tecnologias Utilizadas

- **Flask**: Framework web Python.
- **Flask-SQLAlchemy**: ORM para interagir com o banco de dados.
- **Flask-Login**: Gerenciamento de sessão de usuários.
- **Flask-CORS**: Habilita o suporte a CORS (Cross-Origin Resource Sharing).
- **SQLite**: Banco de dados simples para armazenar dados localmente.
- **Werkzeug**: Utilizado para hashing seguro de senhas.

## Requisitos

- Python 3.7+
- pip (gerenciador de pacotes)

## Instalação

1. Clone o repositório:

   ```bash
   git clone 
   cd ecommerce-flask
   pip install -r requirements.txt
   ```

## Estrutura do Projeto

```plaintext
ecommerce-flask/
│
├── app.py              # Código principal da aplicação
├── keys.py             # Arquivo contendo a chave secreta do Flask
├── requirements.txt    # Arquivo com as dependências do projeto
├── README.md           # Documentação da aplicação
├── models.py           # Definição dos modelos do banco de dados (User, Product, etc.)
├── __init__.py         # Inicialização do pacote
└── venv/               # Ambiente virtual (opcional)

```

# Flask Shell: Introdução ao Uso com SQLAlchemy

Este arquivo fornece instruções sobre como utilizar o **Flask Shell** para interagir com a aplicação Flask, o banco de dados SQLAlchemy e o gerenciamento de senhas com hashing seguro.

## Pré-requisitos

Certifique-se de que as seguintes dependências estão instaladas:

```bash
pip install Flask Flask-SQLAlchemy Flask-Login Flask-CORS Werkzeug
```

## Configuração do Flask Shell

No arquivo principal da aplicação (app.py), adicione o seguinte código para facilitar o uso do Flask Shell:

```python
@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "User": User,
        "Product": Product,
        "CartItem": CartItem
    }
```

## Iniciando o Flask Shell

Após configurar o shell_context_processor, você pode iniciar o Flask Shell no terminal com o seguinte comando:

```bash
flask shell
```

sso abrirá uma sessão interativa do Flask onde você pode executar comandos para interagir com a aplicação e o banco de dados.

## Exemplos no Flask Shell

A seguir, estão alguns exemplos de como usar o Flask Shell para criar o banco de dados, adicionar usuários com hashing de senhas e verificar senhas.

### 1. Criar o banco de dados

Para criar o banco de dados e as tabelas definidas no seu modelo, execute o seguinte comando dentro do Flask Shell:

```python
db.create_all()
```

Isso cria todas as tabelas baseadas nos modelos <code>User</code>, <code>Product</code>, e <code>CartItem</code> definidos no seu código.

### 2. Criar um novo usuário com senha hash

Você pode criar um novo usuário e garantir que a senha seja armazenada de forma segura, utilizando o método set_password. Execute os seguintes comandos:

```python
# Criar um novo usuário
user = User(username="novo_usuario")
user.set_password("minha_senha_secreta")  # Definir a senha com hash
db.session.add(user)
db.session.commit()
```

Isso adiciona o novo usuário <code>novo_usuario</code> ao banco de dados, com a senha armazenada de forma segura como um hash.

### 3. Verificar a senha hash

Para verificar se a senha fornecida é válida, você pode utilizar o método <code>verify_password</code>:

```python
# Buscar o usuário
user = User.query.filter_by(username="novo_usuario").first()

# Verificar a senha
user.verify_password("minha_senha_secreta")  # Retorna True se a senha estiver correta
```

Se a senha estiver correta, o método <code>verify_password</code> retornará <code>True</code>. Se a senha estiver incorreta, ele retornará <code>False</code>.

### Sessão Completa no Flask Shell

Aqui está um exemplo completo de uma sessão no Flask Shell, desde a criação do banco de dados até a criação de um novo usuário e verificação da senha:

```bash
$ flask shell
>>> db.create_all()  # Criar o banco de dados

>>> # Criar um novo usuário
>>> user = User(username="novo_usuario")
>>> user.set_password("minha_senha_secreta")
>>> db.session.add(user)
>>> db.session.commit()

>>> # Buscar e verificar o usuário
>>> user = User.query.filter_by(username="novo_usuario").first()
>>> user.verify_password("minha_senha_secreta")  # Deve retornar True
True
>>> user.verify_password("senha_incorreta")  # Deve retornar False
False
```

### Conclusão

Com o <strong>Flask Shell</strong>, você pode interagir de maneira simples e direta com seu banco de dados, facilitando o processo de desenvolvimento e testes de sua aplicação. Experimente criar usuários, adicionar produtos e verificar funcionalidades usando o shell interativo do Flask.

### O que foi incluído

1. **Configuração do Flask Shell**: Explicação de como adicionar o `@app.shell_context_processor` no código para carregar automaticamente as instâncias de `db` e os modelos.
2. **Iniciando o Flask Shell**: Comando para abrir a sessão do Flask Shell (`flask shell`).
3. **Exemplos detalhados**:
   - Criação do banco de dados com `db.create_all()`.
   - Criação de um novo usuário utilizando o método `set_password` para armazenar a senha de forma segura.
   - Verificação da senha utilizando o método `verify_password`.
4. **Sessão completa** no Flask Shell, mostrando os comandos em sequência desde a criação do banco até a verificação de senha.

Com esse arquivo `README.md`, você tem um guia passo a passo completo para interagir com o Flask Shell e testar suas funcionalidades de gerenciamento de senhas e banco de dados.
