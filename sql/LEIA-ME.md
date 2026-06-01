# sql/

Esta pasta é **opcional** — usa-a se o teu projeto utilizar SQL externo ao código Python.

## Quando usar esta pasta

- Se criares o esquema da base de dados com um script `.sql` separado
- Se quiseres guardar queries complexas fora do código Python
- Se tiveres dados de exemplo para popular a base de dados em testes

## Ficheiros sugeridos

| Ficheiro              | Descrição                                              |
|-----------------------|--------------------------------------------------------|
| `criar_tabelas.sql`   | DDL — instruções `CREATE TABLE` para criar o esquema   |
| `dados_exemplo.sql`   | Dados iniciais de teste (`INSERT INTO ...`)            |

## Exemplo de `criar_tabelas.sql`

```sql
-- Criar tabela de utilizadores
CREATE TABLE IF NOT EXISTS utilizadores (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    nome      TEXT    NOT NULL,
    email     TEXT    NOT NULL UNIQUE,
    password  TEXT    NOT NULL,
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Criar tabela de produtos
CREATE TABLE IF NOT EXISTS produtos (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    nome      TEXT    NOT NULL,
    preco     REAL    NOT NULL CHECK (preco >= 0),
    stock     INTEGER NOT NULL DEFAULT 0,
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

## Nota

Se usas SQLite com Python e crias as tabelas diretamente no DAL (`CREATE TABLE IF NOT EXISTS`),
esta pasta pode ficar vazia ou ser omitida. Nesse caso, remove este ficheiro e a pasta.
