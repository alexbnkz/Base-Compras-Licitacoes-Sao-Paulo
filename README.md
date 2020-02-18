# Base de Compras e Licitacoes da Cidade de Sao Paulo
Extração de dados com Requests para listar Compras e Licitações da Cidade de São Paulo

## Modo de usar

Execute o arquivo run.py:

```bash
python run.py
```

## Resultado

**Schema**

- orgao: string
- retranca: string
- modalidade: string
- numero_licitacao: string
- numero_processo: string
- evento: string
- objeto: string
- data_publicacao_extrato: string
- fornecedor: string
- fornecedor_tipo: string
- fornecedor_documento: string
- data_assinatura_extrato: string
- validade_extrato: string
- tipo_validade_extrato: string
- valor_contrato: string
- numero_contrato: string

**Dados**

```json
{
    "orgao": "HABITAO",
    "retranca": "EKAAADM",
    "modalidade": "CONCORRNCIA",
    "numero_licitacao": "09/13/2012          ",
    "numero_processo": "2011-0.362.986-3    ",
    "evento": "EXTRATO DE ADITAMENTO",
    "objeto": ": EXECUO DE OBRAS DO PROGRAMA DE SANEAMENTO, PROTEO AMBIENTAL E RECUPERAO DA QUALIDADE DAS GUAS EM REAS DEGRADADAS DE MANANCIAL HDRICO DAS BACIAS GUARAPIRANGA E BILLINGS, URBANIZAO DE FAVELAS E REGULARIZAO DE LOTEAMENTOS PRECRIOS  LOTE 09, NO MBITO DA COORDENADORIA DE HABITAO DA SECRETARIA MUNICIPAL DE HABITAO  SEHAB, INTEGRADA PELA SUPERINTENDNCIA DE HABITAO POPULAR  HABI, PELO PROGRAMA MANANCIAIS E PELO DEPARTAMENTO DE REGULARIZAO DE PARCELAMENTO DO SOLO - RESOLO.",
    "data_publicacao_extrato": "12/07/2017",
    "fornecedor": "Andrade valladares Engenharia e Const ltda",
    "fornecedor_tipo": "PJ",
    "fornecedor_documento": "17304221000156",
    "data_assinatura_extrato": "23/06/2017",
    "validade_extrato": "0",
    "tipo_validade_extrato": "Dias",
    "valor_contrato": "102.000.542,93",
    "numero_contrato": "037/2012-SEHAB"
}
```