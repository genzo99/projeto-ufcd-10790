# tests/

Esta pasta é **opcional** — destina-se a testes automáticos da aplicação.

Se não implementares testes, podes deixar esta pasta vazia ou removê-la.

## O que testar

Foca os testes na camada **BLL** (Business Logic Layer), pois é onde
estão as regras de negócio que mais importa validar.

## Exemplo simples

```python
# tests/test_produto_bll.py

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from bll.produto_bll import ProdutoBLL

# DAL simulado (mock) — não precisa de base de dados real para testar a BLL
class ProdutoDALMock:
    def obter_todos(self):
        return [("Produto A", 10.0, 5), ("Produto B", 25.0, 0)]
    def inserir(self, nome, preco, stock):
        return True

def test_listar_produtos():
    dal = ProdutoDALMock()
    bll = ProdutoBLL(dal)
    produtos = bll.listar_produtos()
    assert len(produtos) == 2
    print("✅ test_listar_produtos passou")

def test_preco_negativo():
    dal = ProdutoDALMock()
    bll = ProdutoBLL(dal)
    try:
        bll.adicionar_produto("Teste", -5.0, 10)
        print("❌ test_preco_negativo falhou — devia lançar erro")
    except ValueError:
        print("✅ test_preco_negativo passou")

if __name__ == "__main__":
    test_listar_produtos()
    test_preco_negativo()
```

## Como executar

```bash
cd tests
python test_produto_bll.py
```
