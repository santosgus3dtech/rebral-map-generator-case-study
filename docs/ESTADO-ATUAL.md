# Estado atual — Rebral Map Generator Case Study

Revisão documental: 13/10/2026. Nenhuma planilha ou prévia foi gerada nesta sessão.

## Demo observada

`map_demo/cli.py` lê JSON e encaminha para `generate_workbook`; também permite prévia via `render_preview`. `map_demo/generator.py` contém geração e `validate_payload`, com openpyxl e cálculos Decimal. `pyproject.toml` registra Python >=3.10, openpyxl, Pillow, pytest opcional e comando `map-demo`.

## Fronteira de escopo e regras

[Case study](case-study.md) documenta SQLite, OCR, GUI e FastAPI do sistema privado como relato anterior. O código público analisado é a demo JSON/XLSX; não inferir que esses outros componentes existam aqui. O README identifica entradas e imagens como sintéticas; não foram lidos documentos fiscais, bancos ou planilhas privadas.

## Operação e validação

[README](../README.md) fornece `python -m pip install -e ".[dev]"`, `python -m map_demo.cli examples/synthetic-map.json outputs/demo-map.xlsx --preview outputs/demo-preview.png` e `pytest -q`. Todos não executados nesta tarefa. A configuração pytest aponta para `tests`; testes existentes não certificam a saída sem execução.

## Retomada

Última etapa comprovada: navegação documental e revisão estática da demo. O case study contém ideias para reaproveitamento público; são sugestões documentadas, não compromissos desta sessão.

Sugestões: conferir validações do payload na próxima tarefa; manter materiais sintéticos; distinguir cobertura da demo da narrativa privada. Não foram criadas decisões ou aprendizados novos sem evidência.

[Índice](INDEX.md)
