# scholarship eligibility evaluator - suite de testes automatizados

[cite_start]este repositorio contem a implementacao de uma suite de testes automatizados para o sistema `scholarship eligibility evaluator`. [cite: 1, 8] [cite_start]a atividade integra tecnicas funcionais e estruturais de geracao de testes e analise de adequacao da suite. [cite: 4, 5, 6]

## 1. contexto do projeto
[cite_start]o sistema avalia a elegibilidade de candidatos a bolsas de estudo com base em cinco regras principais: [cite: 15, 30]
* [cite_start]**idade**: minima de 16 anos e revisao manual para menores de 18. [cite: 33]
* [cite_start]**gpa**: nota minima para aprovacao direta e faixas de revisao. [cite: 32]
* [cite_start]**frequencia**: taxa de presenca minima exigida. [cite: 35]
* [cite_start]**cursos obrigatorios**: verificacao de conclusao de grade necessaria. [cite: 36]
* [cite_start]**registro disciplinar**: checagem de historico de conduta. [cite: 36]

[cite_start]o sistema determina se o status do aluno e `approved`, `rejected` ou `manual_review`. [cite: 9, 10, 11]

## 2. escolha tecnologica
* [cite_start]**linguagem**: python 3.11.9. [cite: 13, 18]
* [cite_start]**framework de teste**: pytest 9.0.2. [cite: 14, 19]
* [cite_start]**justificativa**: o pytest permite a criacao de testes parametricos, facilitando a cobertura de multiplas classes de equivalencia e valores limite com codigo limpo e eficiente. [cite: 53]

## 3. estrutura dos testes
[cite_start]a suite de testes foi projetada sob duas perspectivas principais: [cite: 21]

### tecnicas funcionais
* [cite_start]**classes de equivalencia**: identificacao de faixas validas e invalidas para gpa, frequencia e idade. [cite: 22, 23, 79]
* [cite_start]**analise de valor limite**: testes focados nos pontos de transicao exatos das regras de negocio (ex: gpa 6.0 e 7.0). [cite: 24, 80]

### tecnicas estruturais
* [cite_start]**cobertura de decisoes**: exercicio de todos os desvios condicionais (`if/else`) relevantes. [cite: 25, 26, 81]
* [cite_start]**fluxos de execucao**: criacao de casos que percorrem diferentes caminhos do codigo para garantir que todos os cenarios de erro sejam detectados. [cite: 27, 28]

## 4. como executar os testes
[cite_start]para reproduzir a execucao da suite, siga os passos abaixo: [cite: 38, 47]

1. **instalar o pytest**:
   pip install pytest
2. **executar o programa**:
   python -m pytest test_scholarship.py
