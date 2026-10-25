# Registro de alterações — versão 4.0

**Projeto:** Dossiê acadêmico de auditoria contábil ALUPAR  
**Preparador:** Filipe Mateus Sanxo Parente Portela — Matrícula 221018138  
**Data:** 21/10/2026

## Correções realizadas

1. **Dossiê principal:** atualizado o identificador de versão para 3.0 e incorporado suplemento com análise específica de cada papel de trabalho, incluindo objetivo, risco/assertões, procedimentos, status e conclusão/limitação.
2. **Identificação:** preservados nome e matrícula nos documentos; a área de identificação dos papéis foi verificada no PDF. O campo de revisão permanece reservado e não simula assinatura de terceiro.
3. **README:** ampliado com objetivo, escopo, estrutura dos arquivos, reprodução, interpretação dos saldos, amostragem, exceções, materialidade, limitações e checklist.
4. **Código:** ampliado para gerar a população de 500.000 linhas, dicionário, amostra sistemática, seleção dirigida, registro de exceções e resultados dos testes.
5. **Reprodutibilidade:** o script foi executado duas vezes; hashes dos seis arquivos de dados gerados foram idênticos entre as execuções. O script validou 500.000 linhas, soma sintética de R$ 20.440.175.000,00 e 12 exceções inseridas/detectadas.
6. **Planilha:** adicionadas fórmulas rastreáveis aos cálculos principais de materialidade e variações; a pasta de trabalho está configurada para recalcular ao abrir no Excel/LibreOffice.
7. **Fontes:** organizada a relação de fontes em Markdown e PDF; incluída página oficial do CFC para verificação de identificação e revisão das normas.
8. **Matriz normativa:** atualizado o status para refletir que os procedimentos internos são planejados e os testes de dados são simulados, com remissão ao suplemento por norma.
9. **Manifesto:** gerado inventário de arquivos com tamanho e hash SHA-256 para facilitar a verificação de integridade.

## Limitações remanescentes que devem ser respeitadas

- A base é inteiramente sintética; os identificadores, contratos, datas, componentes, valores e status não são registros da ALUPAR.
- A igualdade entre o total da base e o saldo divulgado é calibrada por construção, não conciliação com razão auxiliar ou suporte contábil real.
- As exceções plantadas são testes de regras, não achados da companhia.
- Não foram obtidos razão auxiliar, contratos, memória de cálculo, controles internos, confirmações, acesso a sistemas nem papéis do auditor independente. Os procedimentos que dependem desses elementos continuam planejados ou ilustrativos.
- A identificação de norma/revisão é fornecida como trilha de consulta. Antes da entrega final, confira o texto oficial integral e a vigência aplicável; não atribua item/parágrafo normativo específico sem conferi-lo no texto oficial.
- O link do GitHub não foi criado nem publicado por este processo. O aluno deve publicar o repositório e verificar as permissões antes de entregar o link na plataforma.


## Correções e validações da versão 4.0

1. Reestruturada a planilha para que materialidade de execução, materialidade específica e limite de acumulação referenciem por fórmula a materialidade global, evitando bases digitadas manualmente e desatualização quando as premissas forem alteradas.
2. Incluídas variações nominais e percentuais do ativo contratual, do ativo total e da receita líquida, além da participação do ativo contratual no ativo total.
3. Recalculadas as fórmulas no LibreOffice e verificados os valores armazenados; fórmulas sem erros nas células principais.
4. Criado script independente `codigo/analisar_base.py`, que verifica linhas, IDs únicos, soma, amostras, hashes e correspondência exata entre exceções inseridas e detectadas; inclui testes nas amostras.
5. Adicionada a aba de cruzamento entre exceções inseridas e detectadas na planilha.
6. Adicionado `documentos/rastreabilidade_itens_normativos.csv` com itens/parágrafos selecionados por papel, e anexo PDF com vigência normativa, programas detalhados por ciclo e recálculo independente.
7. Corrigidas referências de paginação física da DFP e explicitada a vigência para 2025 das versões de NBC TA 240 e 570.
8. Gerado PDF integrado versão 4.0, com capa e paginação contínua, substituindo o checklist antigo por status de validação real.
9. Pendente exclusivamente a publicação externa no GitHub e a confirmação de acesso por link real; o pacote local não finge que essa etapa foi concluída.
