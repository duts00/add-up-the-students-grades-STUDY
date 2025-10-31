# Sistema de Notas de Alunos em Python

> Projeto educacional para prática de programação orientada a objetos e controle de fluxo em Python.

---

## Objetivo

Criar uma classe `aluno` capaz de:

* Receber o nome do aluno
* Solicitar a nota do aluno
* Informar se o aluno está **aprovado**, **em recuperação** ou **reprovado** com base na nota

### Critérios de avaliação

* Nota >= 7: Aprovado
* Nota <= 4.99: Recuperação
* Nota entre 5 e 6.99: Reprovado

---

## Funcionamento

1. Instanciar a classe `aluno` passando o nome do aluno:

```python
from notas import aluno

a2 = aluno("Eduardo")
a2.soma()
```

2. O método `soma()` solicita a nota e imprime a situação do aluno.
3. Valida entradas:

   * Aceita apenas números de 0 a 10
   * Trata erros de digitação (ex.: texto ou símbolos)

---

## Execução

```bash
python3 nome_do_arquivo.py
```

> Substitua `nome_do_arquivo.py` pelo arquivo que contém a definição da classe e a execução.

---

## Conceitos praticados

* Programação orientada a objetos (`class`, `__init__`, `self`)
* Estruturas condicionais (`if`, `elif`, `else`)
* Entrada e saída de dados (`input()`, `print()`)
* Tratamento de exceções (`try`, `except`)
* Validação de dados

---

## Nota final

Este projeto é **educacional**, voltado ao aprendizado de Python e POO. Permite entender como criar classes, métodos e validações simples de dados.

---

