# Computational Thinking with Python
## Cálculo de Notas – FIAP Graduação

## O que é cada avaliação?

**Checkpoint (CP)**
Avaliação por disciplina. Cada matéria tem 3 checkpoints no semestre — provas ou entregas que testam o conteúdo específico daquela disciplina. A menor nota é descartada automaticamente, e só as 2 melhores entram no cálculo.

**Sprint Partner (SP)**
Avaliação ligada ao projeto do challenge semestral (como o JOVI). São 2 sprints por semestre, onde o grupo apresenta o andamento do projeto para um parceiro/empresa. Ambas as notas entram no cálculo.

**Global Solution (GS)**
Avaliação final semestral da FIAP — um desafio hands-on com temas de impacto para a sociedade, onde os alunos resolvem problemas reais propostos por empresas parceiras globais e big techs. É o componente de maior peso na nota.

---

## Fórmula por semestre

```
Média do Semestre = (média dos 2 melhores CPs) × 0.2
                  + (SP1 + SP2) × 0.2
                  + GS × 0.6
```

| Componente               | Peso |
|--------------------------|------|
| Média dos 2 melhores CPs | 20%  |
| SP1 + SP2 (soma)         | 20%  |
| Global Solution          | 60%  |

> O GS domina a nota com 60% de peso — é a avaliação que mais importa no semestre.

---

## Nota Final

O segundo semestre tem mais peso que o primeiro:

```
Nota Final = Semestre 1 × 0.4 + Semestre 2 × 0.6
```

| Semestre   | Peso |
|------------|------|
| Semestre 1 | 40%  |
| Semestre 2 | 60%  |

---

## Aprovação

```
Nota Final >= 6.0  →  Aprovado ✅
Nota Final <  6.0  →  Reprovado ❌
```

---

## Exemplo completo

**Semestre 1**
| Dado | Valor |
|------|-------|
| CPs | 2, 4, 10 → descarta o 2 → média(4, 10) = **7.0** |
| SPs | 9 + 1 = **10** |
| GS  | **9** |
| **M1** | (7.0 × 0.2) + (10 × 0.2) + (9 × 0.6) = 1.4 + 1.0 + 5.4 = **7.8** |

**Semestre 2**
| Dado | Valor |
|------|-------|
| CPs | 5, 8, 10 → descarta o 5 → média(8, 10) = **9.0** |
| SPs | 5 + 4 = **9** |
| GS  | **10** |
| **M2** | (9.0 × 0.2) + (9 × 0.2) + (10 × 0.6) = 1.8 + 0.9 + 6.0 = **8.7** |

**Nota Final**
```
(7.8 × 0.4) + (8.7 × 0.6) = 3.12 + 5.22 = 8.34 → Aprovado ✅
```
