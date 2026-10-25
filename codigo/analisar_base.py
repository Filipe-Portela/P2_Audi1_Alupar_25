#!/usr/bin/env python3
"""Validação independente da população sintética, amostras e exceções.
Não valida registros reais da ALUPAR e não constitui conciliação contábil.
"""
import csv, hashlib, json
from decimal import Decimal
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; DATA=ROOT/'dados'
BASE=DATA/'base_sintetica_ativo_contratual_500000.csv'
def sha(path):
 h=hashlib.sha256()
 with path.open('rb') as f:
  for chunk in iter(lambda:f.read(1024*1024),b''): h.update(chunk)
 return h.hexdigest()
with BASE.open(encoding='utf-8',newline='') as f: rows=list(csv.DictReader(f))
values=[Decimal(r['valor_contabil_R$']) for r in rows]
total=sum(values,Decimal('0.00'))
with (DATA/'registro_excecoes_inseridas.csv').open(encoding='utf-8',newline='') as f: ins=list(csv.DictReader(f))
with (DATA/'resultado_testes_excecoes.csv').open(encoding='utf-8',newline='') as f: det=list(csv.DictReader(f))
inserted={(r['registro_id'],r['tipo_excecao']) for r in ins}
detected={(r['registro_id'],r['regra_detectada']) for r in det if r['resultado']=='DETECTADA'}
with (DATA/'amostra_sistematica_100.csv').open(encoding='utf-8',newline='') as f: sys_sample=list(csv.DictReader(f))
with (DATA/'amostra_dirigida_25_maiores.csv').open(encoding='utf-8',newline='') as f: dir_sample=list(csv.DictReader(f))
def rules_for(row):
 rules=[]
 if row['status_documental']=='Pendente': rules.append('E01_documento_ausente')
 if row['data_documento']>row['data_referencia']: rules.append('E02_documento_posterior')
 if row['componente']=='REVISAR': rules.append('E03_componente_inusual')
 if row['status_documental']=='Em validação': rules.append('E04_status_pendente')
 return rules
with (DATA/'resultado_testes_amostras.csv').open('w',encoding='utf-8',newline='') as f:
 w=csv.writer(f); w.writerow(['tipo_amostra','registro_id','regra_detectada','excecao_inserida','resultado'])
 for typ, sample in [('sistematica',sys_sample),('dirigida',dir_sample)]:
  for row in sample:
   for rule in rules_for(row): w.writerow([typ,row['registro_id'],rule,row['excecao_inserida'],'DETECTADA_NA_AMOSTRA'])
expected_total=Decimal('20440175000.00')
summary={
 'base_linhas':len(rows),'ids_unicos':len({r['registro_id'] for r in rows}),
 'soma_base_R$':str(total),'saldo_publicado_R$':str(expected_total),
 'diferenca_aritmetica_R$':str(total-expected_total),
 'excecoes_inseridas':len(inserted),'excecoes_detectadas':len(detected),
 'inseridas_nao_detectadas':sorted(inserted-detected),'detectadas_nao_inseridas':sorted(detected-inserted),
 'amostra_sistematica_linhas':len(sys_sample),'amostra_dirigida_linhas':len(dir_sample),
 'excecoes_na_amostra_sistematica':sum(1 for r in sys_sample if r['excecao_inserida']=='SIM'),
 'excecoes_na_amostra_dirigida':sum(1 for r in dir_sample if r['excecao_inserida']=='SIM'),
 'hash_sha256_base':sha(BASE),
 'limitacao':'A igualdade é calibrada; não é conciliação contábil real. Exceções e registros são sintéticos.'}
if len(rows)!=500000 or len({r['registro_id'] for r in rows})!=500000: raise SystemExit('FALHA: quantidade/IDs da base')
if total!=expected_total: raise SystemExit('FALHA: total da base')
if len(inserted)!=12 or inserted!=detected: raise SystemExit('FALHA: correspondência entre exceções inseridas e detectadas')
if len(sys_sample)!=100 or len(dir_sample)!=25: raise SystemExit('FALHA: tamanho das amostras')
(DATA/'relatorio_validacao_base.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(summary,ensure_ascii=False,indent=2))
