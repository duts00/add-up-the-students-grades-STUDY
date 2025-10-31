# Sistema de Avaliação de Alunos

Este repositório contém uma classe Python `aluno` que permite registrar uma nota de 0 a 10 e retorna a situação do aluno como **Aprovado**, **Recuperação** ou **Reprovado**.

## Funcionalidade

- Solicita ao usuário a nota do aluno.
- Valida a entrada (entre 0 e 10).
- Retorna a situação:
  - Nota ≥ 7.0 → Aprovado
  - Nota 5.0–6.9 → Recuperação
  - Nota < 5.0 → Reprovado

## Exemplo de uso

```python
from notas import aluno

a = aluno("Eduardo")
a.soma()
