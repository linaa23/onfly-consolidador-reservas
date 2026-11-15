# Entrega — Consolidador de reservas de hotel (Onfly)

## Resumo

Foram identificados e corrigidos cinco defeitos que afetavam o processamento de reservas, a contagem de noites, o câmbio, a definição de reservas faturáveis e a ordem do ranking de hotéis. Mantive o contrato da CLI, as estruturas de retorno JSON, o formato dos valores e os arquivos de dados originais. Os testes da empresa foram mantidos sem alterações.

## Defeitos corrigidos e causa raiz

1. **Noites de hospedagem (`src/onfly_report/services/stay_calculator.py`).** Causa raiz: o código subtraía apenas `.day` de duas datas, ignorando mudanças de mês/ano; a correção usa a diferença entre as datas completas e multiplica pelo número de quartos.
2. **Status faturável (`src/onfly_report/services/status_policy.py`).** Causa raiz: o predicado `status != "CANCELLED"` tratava `NO_SHOW` como faturável; a correção aceita exclusivamente `CONFIRMED`.
3. **Conversão monetária (`src/onfly_report/services/currency_converter.py`).** Causa raiz: o código dividia o valor pela taxa e convertia para `float`, o que contrariava a regra de câmbio e comprometia a precisão; a correção multiplica `Decimal` por `Decimal`.
4. **Ranking de hotéis (`src/onfly_report/services/report_builder.py`).** Causa raiz: o `sorted()` ordenava o valor monetário em ordem crescente; a correção ordena por total em ordem decrescente e por `hotel_id` em ordem ascendente nos empates.
5. **Leitura incompleta do CSV (`src/onfly_report/repositories/csv_reservation_repository.py`).** Causa raiz: um `break` interrompia a leitura após 200 linhas; a correção processa todas as reservas do arquivo.

## Investigação e abordagem

- Leitura do README original para levantar o contrato e as regras de negócio.
- Inspeção dos módulos Python e dos cinco testes fornecidos.
- Execução inicial do Pytest para reproduzir as cinco falhas esperadas (resultado documentado em `resultado-testes-originais.txt`).
- Correções pontuais nos cinco módulos relacionados aos defeitos, mantendo a estrutura do projeto.
- Execução dos testes originais e criação de cinco novos testes em `tests/test_extra_contract.py`, cobrindo: leitura de mais de 200 reservas, empates no ranking, ausência de reservas confirmadas, arredondamento monetário e virada de ano.
- Execução do CLI com a amostra de validação e com o arquivo completo.

## Como validar

Use Python 3.11 ou superior. Na pasta raiz do projeto, instale as dependências de teste e execute:

```powershell
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

No PowerShell do Windows, execute o CLI com os caminhos originais:

```powershell
$env:PYTHONPATH = (Resolve-Path .\src).Path
python -m onfly_report --input data/reservas_hoteis.csv --rates data/taxas_cambio.csv --output output/report.json --top 5
python -m onfly_report --input data/exemplo-validacao.csv --rates data/taxas_cambio.csv --output output/exemplo.json --top 5
```

Em Linux/macOS, na raiz do projeto:

```bash
PYTHONPATH=src python -m onfly_report --input data/reservas_hoteis.csv --rates data/taxas_cambio.csv --output output/report.json --top 5
```

**Validação da amostra (`data/exemplo-validacao.csv`):** 12 reservas, 9 confirmadas, 2 canceladas, 1 `NO_SHOW`, 28 noites, R$ 7.566,00 em reservas confirmadas, diária média R$ 270,21. As divisões por mês e ranking também coincidiram com o README original.

**Execução do arquivo completo (`data/reservas_hoteis.csv`):** 300 reservas, 235 confirmadas, 31 canceladas, 34 `NO_SHOW`, 1.347 noites de quarto, total R$ 396.170,00 e diária média R$ 294,11.

## Resultado dos testes

```text
10 passed in 6.66s
```

Execução de referência: Python 3.13.5 e Pytest 9.0.2. O arquivo `requirements-dev.txt` original foi preservado e lista `pytest==8.3.4` e `ruff==0.8.4`; para reproduzir no computador do candidato, instale as dependências conforme indicado acima.

## Preservação do contrato

- Comando, parâmetros `--input`, `--rates`, `--output` e `--top` preservados.
- Nome e tipo dos campos do JSON preservados; dinheiro permanece `string` com duas casas, arredondado `ROUND_HALF_UP` na serialização.
- `generated_at` mantém offset fixo `-03:00`.
- Nenhum teste fornecido foi editado; novos testes foram acrescentados em arquivo separado.
- Os dois CSVs originais de entrada foram copiados sem alterações.

## Uso de inteligência artificial

O ChatGPT (OpenAI, modelo GPT-6) foi usado no estudo da linguagem Python, interpretação das regras, análise de defeitos, implementação das correções, criação dos testes extras, execução das verificações e elaboração da documentação. A descrição e o registro da assistência estão em `uso-de-ia/`. A pessoa candidata deve revisar e complementar a declaração com suas ações próprias e anexar o histórico da conversa conforme as exigências da avaliação.
