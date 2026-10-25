#!/usr/bin/env python3
"""Gera a população sintética e os arquivos de apoio do dossiê acadêmico ALUPAR.
Nenhum registro gerado corresponde a lançamento ou contrato real da companhia."""
import csv, random
from datetime import date, timedelta
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "dados"
DATA.mkdir(exist_ok=True)
N = 500_000
SALDO_REAIS = 20_440_175_000
SEED = 20261021
rng = random.Random(SEED)
weights = [rng.randint(1, 10_000) for _ in range(N)]
weight_sum = sum(weights)
target_cents = SALDO_REAIS * 100
values = [(target_cents * w) // weight_sum for w in weights]
remainder = target_cents - sum(values)
for i in range(remainder):
    values[i] += 1

exception_indices = {17, 109, 2026, 9876, 45678, 89012, 123456, 234567,
                     345678, 400001, 450321, 499999}
components = ["Construção", "Melhoria", "Remuneração do ativo",
              "Atualização monetária", "Reclassificação"]
base_path = DATA / "base_sintetica_ativo_contratual_500000.csv"
exception_rows = []
with base_path.open("w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["registro_id", "contrato_sintetico_id", "componente",
                     "data_referencia", "valor_contabil_R$", "status_documental",
                     "data_documento", "excecao_inserida", "regra_teste_esperada"])
    for i, cents in enumerate(values):
        ref_date = date(2025, 1, 1) + timedelta(days=rng.randrange(365))
        status = "Documentado"
        doc_date = ref_date - timedelta(days=rng.randrange(45))
        rule = ""
        if i in exception_indices:
            k = i % 4
            if k == 0:
                status, rule = "Pendente", "E01_documento_ausente"
            elif k == 1:
                doc_date, rule = ref_date + timedelta(days=20), "E02_documento_posterior"
            elif k == 2:
                rule = "E03_componente_inusual"
            else:
                status, rule = "Em validação", "E04_status_pendente"
        component = "REVISAR" if rule == "E03_componente_inusual" else components[i % len(components)]
        value = Decimal(cents) / Decimal(100)
        record_id = f"SYN-{i+1:06d}"
        contract_id = f"CT-SYN-{(i % 2500)+1:05d}"
        writer.writerow([record_id, contract_id, component, ref_date.isoformat(),
                         f"{value:.2f}", status, doc_date.isoformat(),
                         "SIM" if i in exception_indices else "NÃO", rule])
        if i in exception_indices:
            exception_rows.append([record_id, rule, "SIM",
                                   "Inserção controlada exclusivamente para validar o código de teste."])

# Dictionary
dictionary = [
    ["variavel","tipo","descricao","limitação"],
    ["registro_id","texto","Identificador único sintético da linha analítica","Não corresponde a lançamento real da ALUPAR"],
    ["contrato_sintetico_id","texto","Identificador de contrato fictício, repetido em linhas de componentes","Não representa contratos reais"],
    ["componente","categoria","Componente fictício de mensuração do ativo contratual","Categoria gerada artificialmente"],
    ["data_referencia","data","Data fictícia dentro do exercício de 2025","Não deriva de documento da companhia"],
    ["valor_contabil_R$","decimal","Valor sintético em reais por linha; soma calibrada ao saldo publicado","Calibração aritmética não é conciliação de razão contábil"],
    ["status_documental","categoria","Status sintético de documentação","Não é resultado de inspeção documental real"],
    ["data_documento","data","Data fictícia para testar regra temporal","Não é evidência externa"],
    ["excecao_inserida","SIM/NÃO","Marca de controle para exceções plantadas","Metadado de teste, não atributo da companhia"],
    ["regra_teste_esperada","texto","Regra prevista para cada exceção inserida","Não constitui achado real"],
]
with (DATA / "dicionario_variaveis.csv").open("w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(dictionary)

with (DATA / "registro_excecoes_inseridas.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["registro_id","tipo_excecao","inserida_intencionalmente","criterio_de_insercao"])
    for row in exception_rows:
        w.writerow([row[0],row[1],row[2],row[3]])

# Run the exact detection rules over the generated population
detected = []
with base_path.open(newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        rules = []
        if row["status_documental"] == "Pendente":
            rules.append("E01_documento_ausente")
        if row["data_documento"] > row["data_referencia"]:
            rules.append("E02_documento_posterior")
        if row["componente"] == "REVISAR":
            rules.append("E03_componente_inusual")
        if row["status_documental"] == "Em validação":
            rules.append("E04_status_pendente")
        for rule in rules:
            detected.append([row["registro_id"], rule, row["excecao_inserida"],
                             "DETECTADA", "Regra aplicada a campos sintéticos; não é achado real."])
with (DATA / "resultado_testes_excecoes.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["registro_id","regra_detectada","excecao_inserida","resultado","observacao"])
    w.writerows(detected)

# Systematic selection: fixed start index 2026 (zero-based), interval 5,000
sample_indices = [2026 + j * 5000 for j in range(100)]
with base_path.open(newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
sample_fields = list(rows[0].keys())
with (DATA / "amostra_sistematica_100.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=sample_fields); w.writeheader()
    for idx in sample_indices:
        w.writerow(rows[idx])

# Directed selection: 25 largest absolute values; deterministic tie break by ID
directed = sorted(rows, key=lambda r: (-abs(Decimal(r["valor_contabil_R$"])), r["registro_id"]))[:25]
with (DATA / "amostra_dirigida_25_maiores.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=sample_fields); w.writeheader(); w.writerows(directed)

sum_cents = sum(int(Decimal(r["valor_contabil_R$"]) * 100) for r in rows)
if len(rows) != N or sum_cents != target_cents:
    raise RuntimeError(f"Validação falhou: linhas={len(rows)}, soma centavos={sum_cents}")
if len(exception_rows) != 12 or len(detected) != 12:
    raise RuntimeError(f"Validação das exceções falhou: inseridas={len(exception_rows)}, detectadas={len(detected)}")
print(f"Base sintética: {len(rows):,} linhas; soma R$ {sum_cents/100:,.2f}.")
print(f"Exceções plantadas/detectadas: {len(exception_rows)}/{len(detected)}.")
print(f"Amostras geradas: sistemática={len(sample_indices)}; dirigida={len(directed)}.")
print("Atenção: todos os registros são sintéticos; a soma igual ao saldo publicado é por construção.")
