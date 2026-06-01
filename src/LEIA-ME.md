# src/

Esta pasta contém todo o código fonte Python do projeto,
organizado segundo a arquitetura em três camadas.

## Estrutura

```
src/
│
├── main.py          ← Ponto de entrada — executa a aplicação
│
├── dal/             ← Data Access Layer (Acesso a Dados)
│   ├── __init__.py
│   └── [nome]_dal.py    ← ex: produto_dal.py, utilizador_dal.py
│
├── bll/             ← Business Logic Layer (Lógica de Negócio)
│   ├── __init__.py
│   └── [nome]_bll.py    ← ex: produto_bll.py, utilizador_bll.py
│
└── ui/              ← Interface com o utilizador
    ├── __init__.py
    └── menu.py          ← Menus e interação com o utilizador
```

## Responsabilidades de cada camada

### `main.py`
Inicializa a aplicação — cria a ligação à BD, instancia o DAL e o BLL,
e arranca a interface. Não deve conter lógica de negócio.

```python
from dal.produto_dal import ProdutoDAL
from bll.produto_bll import ProdutoBLL
from ui.menu import Menu

if __name__ == "__main__":
    dal = ProdutoDAL("database.db")
    bll = ProdutoBLL(dal)
    menu = Menu(bll)
    menu.iniciar()
```

### `dal/`
Responsável por toda a comunicação com a base de dados.
Cada ficheiro corresponde a uma entidade do sistema.

```python
# dal/produto_dal.py
import sqlite3

class ProdutoDAL:
    def __init__(self, db_path):
        self._db = db_path

    def obter_todos(self):
        conn = sqlite3.connect(self._db)
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM produtos")
            return cursor.fetchall()
        finally:
            conn.close()
```

### `bll/`
Contém as regras de negócio. Não sabe como os dados são guardados —
delega essa responsabilidade ao DAL.

```python
# bll/produto_bll.py
class ProdutoBLL:
    def __init__(self, dal):
        self._dal = dal

    def listar_produtos(self):
        return self._dal.obter_todos()

    def adicionar_produto(self, nome, preco, stock):
        if not nome:
            raise ValueError("O nome do produto é obrigatório.")
        if preco < 0:
            raise ValueError("O preço não pode ser negativo.")
        return self._dal.inserir(nome, preco, stock)
```

### `ui/`
Gere a interação com o utilizador — menus, inputs, outputs.
Não deve conter lógica de negócio nem queries SQL.

```python
# ui/menu.py
class Menu:
    def __init__(self, bll):
        self._bll = bll

    def iniciar(self):
        while True:
            print("\n1 - Listar produtos")
            print("2 - Adicionar produto")
            print("0 - Sair")
            opcao = input("Opção: ")
            if opcao == "0":
                break
            elif opcao == "1":
                self._listar()

    def _listar(self):
        produtos = self._bll.listar_produtos()
        for p in produtos:
            print(p)
```

## Nota sobre `__init__.py`

Os ficheiros `__init__.py` (que podem estar vazios) são necessários para que
Python trate as pastas `dal/`, `bll/` e `ui/` como módulos importáveis.
