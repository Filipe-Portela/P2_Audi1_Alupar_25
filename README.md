# Dossiê de Auditoria Contábil — ALUPAR

**Disciplina:** Auditoria 1 — CCA0024 — Turma 02 — 2026.2  
**Professor:** Lucas Oliveira Gomes Ferreira  
**Companhia:** ALUPAR INVESTIMENTO S/A — ALUP11  
**Preparador:** Filipe Mateus Sanxo Parente Portela  
**Matrícula:** 221018138  
**Versão:** 4.0 — 21/10/2026

## 1. Finalidade e limites

Este repositório reúne um dossiê acadêmico de auditoria estruturado conforme o roteiro P2. A análise concentra-se no ativo contratual de concessão, conta de grande relevância nas demonstrações consolidadas de 2025 e destacada no relatório do auditor independente como principal assunto de auditoria.

O material não é um trabalho de auditoria independente efetivamente contratado ou executado. Não contém opinião profissional, não substitui os papéis de trabalho do auditor independente e não permite concluir sobre a razoabilidade integral das demonstrações financeiras da ALUPAR. Cada procedimento é identificado como realizado com evidência pública, planejado por falta de acesso ou simulado para fins didáticos.

## 2. Conteúdo do repositório

> **Importante para o link de download:** o CSV precisa estar publicado no repositório no caminho `dados/base_sintetica_ativo_contratual_500000.csv` e na branch `main`. Se o arquivo ainda não foi enviado ao GitHub, o link retornará 404; envie o CSV da pasta `dados` para esse caminho e mantenha o nome exatamente igual.

- `documentos/dossie_auditoria_alupar_v4.pdf` — dossiê principal, papéis de trabalho e suplemento de procedimentos específicos por norma.
- `documentos/fontes.md` — fontes consultadas, endereços eletrônicos, referências de páginas, data de acesso e limitações.
- `documentos/relacao_fontes_utilizadas.pdf` — versão PDF da relação de fontes, documentos e links.
- `documentos/registro_de_alteracoes.md` — resumo das alterações e das limitações remanescentes.
- `documentos/suplemento_procedimentos_por_norma.pdf` — complemento com riscos, procedimentos, status e conclusões específicos para cada papel de trabalho.
- `documentos/anexo_rastreabilidade_e_programas_v4.pdf` — referências de itens normativos, vigência, programas detalhados por ciclo e recálculo independente.
- `documentos/rastreabilidade_itens_normativos.csv` — itens/parágrafos selecionados por papel de trabalho.
- `documentos/matriz_cobertura_normas.csv` — rastreabilidade entre normas, papéis de trabalho, status e limitações.
- `dados/base_sintetica_ativo_contratual_500000.csv` — população sintética de 500.000 linhas, gerada para fins didáticos.  
  **DOWNLOAD DA BASE (CSV):** [Acessar a pasta da base sintética no Google Drive](https://drive.google.com/drive/folders/1Fcz8pnE3SeA_7Bfe9hEiyXvy0znEf3s4?usp=sharing)  

- `dados/dicionario_variaveis.csv` — descrição das variáveis e limites de interpretação.
- `dados/amostra_sistematica_100.csv` — seleção sistemática didática de 100 linhas.
- `dados/amostra_dirigida_25_maiores.csv` — seleção não probabilística dos 25 maiores valores absolutos.
- `dados/registro_excecoes_inseridas.csv` — registro das exceções inseridas intencionalmente.
- `dados/resultado_testes_excecoes.csv` — resultado das regras aplicadas para detectar as exceções na população.
- `dados/resultado_testes_amostras.csv` — exceções que aparecem nas amostras sistemática e dirigida.
- `dados/relatorio_validacao_base.json` — resumo da validação independente da base.
- `planilhas/calculos_materialidade_amostragem.xlsx` — premissas, fórmulas, comparação aritmética, amostragem e limitações.
- `codigo/gerar_base.py` — código de geração da base, dicionário, amostras e arquivos de exceções.
- `codigo/analisar_base.py` — validação independente de contagem, IDs, soma, amostras e reconciliação entre exceções inseridas/detectadas.
- `dados/relatorio_validacao_base.json` — resultado estruturado da última validação independente.
- `documentos/rastreabilidade_itens_normativos.csv` — referências de parágrafos por papel e norma, com status de vigência para o exercício de 2025.
- `MANIFEST.json` — inventário, tamanho e hash SHA-256 dos arquivos do pacote.

## 3. Fonte e valores financeiros

A DFP consolidada de 2025 indica ativo contratual de concessão de R$ 20.440.175 mil em 31/12/2025, comparado a R$ 19.434.422 mil em 31/12/2024. O ativo total consolidado em 2025 é de R$ 32.114.316 mil e a receita líquida consolidada é de R$ 4.397.883 mil. Os valores, originalmente apresentados em milhares de reais, foram convertidos para reais nas planilhas e no texto quando explicitamente indicado.

A fonte primária consultada é a DFP fornecida e a página oficial de demonstrações financeiras da ALUPAR. Ver `documentos/fontes.md` para links, localização e limitações. As páginas físicas citadas se referem ao arquivo PDF específico examinado e podem variar em outras versões.

## 4. Base sintética e comparação do saldo

A base contém 500.000 registros artificiais. Os identificadores, contratos, datas, componentes, valores e status documentais foram gerados por código e não correspondem a lançamentos ou contratos reais da ALUPAR. O total foi calibrado matematicamente para igualar R$ 20.440.175.000, saldo publicado para a rubrica.

A diferença aritmética de R$ 0,00 é resultado da calibração deliberada. **Não é conciliação contábil substantiva**, pois não houve comparação com razão auxiliar, subledger, contratos, memórias de cálculo ou documentos de suporte reais. O valor serve apenas para demonstrar a estrutura do procedimento exigido pelo trabalho.

## 5. Exceções e amostragem

Foram inseridas 12 exceções controladas para testar as regras de detecção. O código registra cada exceção inserida e compara-a com os resultados encontrados. Essas exceções são artificiais, não são achados reais e não devem ser atribuídas à companhia.

A amostra sistemática e a seleção dirigida são demonstrações didáticas aplicadas à base sintética. A seleção dirigida dos maiores valores é não probabilística e não admite projeção estatística. O exercício não estima risco amostral nem projeta distorções para a contabilidade real da companhia.

## 6. Como reproduzir

Requisitos: Python 3.10 ou compatível; bibliotecas padrão do Python. A planilha Excel já é fornecida e não é gerada pelo script. O arquivo `dados/relatorio_validacao_base.json` é gerado por `codigo/analisar_base.py`.

1. Descompacte o pacote.
2. Abra um terminal na pasta raiz do projeto, que contém `codigo`, `dados`, `documentos` e `planilhas`.
3. Execute os dois comandos, nesta ordem:

```bash
python codigo/gerar_base.py
python codigo/analisar_base.py
```

O script recria a base sintética, o dicionário, as amostras e os dois arquivos de exceções. A semente é fixa para tornar os resultados reproduzíveis. Como o script recria arquivos em `dados/`, faça uma cópia dos arquivos originais antes de executá-lo se quiser preservá-los.

## 7. Materialidade e julgamento

Os percentuais usados na planilha são premissas didáticas preliminares, e não percentuais impostos pela NBC TA 320. Em auditoria real, a materialidade depende do julgamento profissional, das necessidades dos usuários, das rubricas relevantes, do risco e das circunstâncias do trabalho. Os cálculos devem ser interpretados em conjunto com as justificativas e limitações registradas.

## 8. Limitações das evidências

Não foram disponibilizados razão auxiliar real, cadastro completo de contratos, memórias de cálculo por concessão, documentação interna de controles, confirmações externas, acesso aos sistemas da companhia ou papéis de trabalho do auditor independente. Assim, os procedimentos dependentes desses elementos permanecem planejados ou ilustrativos. Não se deve afirmar que foram executados.

A leitura de documentos públicos e os cálculos derivados desses documentos foram realizados no contexto acadêmico. Isso não equivale a obter evidência suficiente e apropriada para opinar sobre as demonstrações financeiras.

## 9. Checklist de validação final

- [x] Arquivos internos e caminhos conferidos.
- [x] PDF integrado conferido quanto à matrícula, estrutura, paginação e referências cruzadas.
- [x] Valores financeiros conferidos com a DFP fornecida, incluindo unidade, período e comparativos.
- [x] Itens normativos selecionados por papel e aplicabilidade temporal documentados no CSV e no anexo.
- [x] Código de geração e script de análise executados; linhas, IDs, soma, amostras e exceções validados.
- [x] Fórmulas da planilha recalculadas no LibreOffice e resultados principais conferidos independentemente.
- [ ] Publicar o repositório no GitHub e testar o acesso pelo link exigido pelo professor. Não há URL externa verificada nesta versão.
- [x] Registros sintéticos, exceções plantadas e igualdade aritmética por calibração explicitamente separados de achados e conciliação real.

## 10. Formato de entrega

Mantenha este `README.md` na raiz do repositório. O PDF é uma versão de leitura complementar e não substitui o Markdown quando o comando pede um arquivo README. A atividade exige disponibilizar o link do GitHub; o link deve ser inserido na plataforma pelo aluno após publicação e teste de acesso.
