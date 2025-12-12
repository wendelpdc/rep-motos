# Assistente de Escolha de Motos - POO Python

## 🎯 **Propósito**
Sistema acadêmico que demonstra **Programação Orientada a Objetos (POO)** através de um assistente inteligente para recomendar tipos de motos baseado no perfil do usuário. O programa implementa herança de classes, polimorfismo e modularidade, simulando um sistema real de recomendação de veículos.

**Objetivos principais:**
- Demonstrar herança com superclasse `TipoMotos` e 4 subclasses
- Criar questionário inteligente para sugestão automática
- Permitir escolha manual com análise detalhada
- Exibir exemplos de todos os tipos de motos

## 🛠️ **Tecnologias Utilizadas**
| Tecnologia | Versão | Propósito |
|------------|--------|-----------|
| **Python** | 3.6+ | Linguagem principal |
| **POO Python** | - | Herança, Polimorfismo, Encapsulamento |
| **Sistema de Módulos** | Nativo | Modularização (1 classe = 1 arquivo) |
| **Input/Output** | Nativo | Interface de linha de comando |

**Sem dependências externas** - 100% Python puro.
**Relação**: Todas as subclasses **HERDAM** de `TipoMotos` e **SOBRESCREVEM** o método `analisar()`.

**Tempo estimado: 30 segundos**

## 💻 **Como Usar**

### Fluxo Completo
1. **Execute**: `python main.py`
2. **Responda 3 perguntas rápidas**:
3. **Veja a sugestão automática** (ex: "Street")
4. **Escolha manter ou alterar** (ENTER = manter)
5. **Digite dados da moto** (modelo, ano, cilindrada)
6. **Resultado**: Análise + exemplos de todos os tipos

### Exemplo de Saída
## 🔍 **Funcionalidades**

| Funcionalidade | Descrição |
|----------------|-----------|
| **Questionário Inteligente** | 3 perguntas → sugestão automática |
| **Herança OOP** | 4 subclasses herdam de `TipoMotos` |
| **Polimorfismo** | `analisar()` diferente por tipo |
| **Modularidade** | 6 arquivos organizados |
| **Flexibilidade** | Sugestão + escolha manual |

## 📚 **Conceitos OOP Demonstrados**

| Conceito | Exemplo no Código | Benefício |
|----------|------------------|-----------|
| **Herança** | `class Street(TipoMotos)` | Reutiliza código comum |
| **Polimorfismo** | `analisar()` diferente em cada subclasse | Mesmo método, comportamentos distintos |
| **Encapsulamento** | `self.modelo`, `self.ano` | Dados protegidos dentro das classes |
| **Abstração** | Interface uniforme no `main.py` | Simplicidade para o cliente |
| **Modularidade** | 1 classe = 1 arquivo | Manutenção e escalabilidade |

## 🎓 **Funcionalidades por Tipo de Moto**

| Tipo | Características | Uso Ideal |
|------|----------------|-----------|
| **Street** | Posição vertical, ágil | Cidade, trabalho diário |
| **Custom** | Guidão alto, banco baixo | Viagens longas, conforto |
| **Esportiva** | Posição agachada, potente | Pista, velocidade |
| **Scooter** | Transmissão automática | Mobilidade urbana |

## 🛠️ **Lógica de Recomendação Inteligente**

## 👨‍🎓 **Autor**
**Desenvolvido por**: [Wendel Victor Santos Coelho]  
**Disciplina**: Programação Orientada a Objetos  
**Período**: 2025/2
