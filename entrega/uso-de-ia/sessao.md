# Registro consolidado de prompts e respostas — ChatGPT / Onfly

Este registro foi produzido a partir da conversa da pessoa candidata com o ChatGPT. Contém os prompts centrais literalmente e um resumo identificado das respostas e ações técnicas. **Não é uma exportação integral automática da conversa**; a pessoa candidata deve complementar com o histórico/exportação das sessões caso a avaliação exija o registro completo.

## Interação 1 — Recebimento do desafio

**Prompt da pessoa candidata:**

> recebi um teste para uma vaga de emprego que é realizado com pyton me ajuda a entender e aprender tudo que preciso para realizar? está tudo nesse link pelo que eu entendi [https://drive.google.com/drive/folders/1Y3rgsjZZhHqZxRx_Aht5AEBnLS4hsHFl](https://drive.google.com/drive/folders/1Y3rgsjZZhHqZxRx_Aht5AEBnLS4hsHFl)  
> o readme caso voce não consiga abrir https://docs.google.com/document/d/1bEckBhfjMY-JGSwoOyqETOeru1y_5VnC/edit

**Resposta e assistência (resumo, não transcrição literal):** a IA identificou que era necessário depurar um consolidador de reservas de hotéis em Python, descreveu a estrutura do projeto, as regras de negócio, o uso de Pytest e a obrigação de declarar IA.

## Interação 2 — Estudo introdutório

**Prompts centrais da pessoa candidata (excertos literais):**

> sim, me ensine coisas básicas como "como inicia código" "variáveis" etc... Tenha em mente que eu ja sei um pouco sobre linguagem c e bem pouco sobre java, entao use isso para fazer assossiações para eu entender

> Chat, faz pra mim um PDF me explicando sobre a base do Python que eu preciso saber pra poder fazer isso, as coisas mais básicas, por exemplo, declaração de variável, como que inicia um código, como que faz, por exemplo, uma conta, as coisas que estão lá nesse código pra eu conseguir identificar o que significa, tipo, cada coisa.

**Resposta e assistência (resumo, não transcrição literal):** a IA forneceu aulas comparando Python, C e Java, exercícios sobre funções, condicionais, listas e dicionários, orientações de VS Code e uma apostila em PDF.

## Interação 3 — Pedido de execução imediata

**Prompt literal da pessoa candidata:**

> Chat não dá tempo de aprender mais preciso fazer

**Resposta literal da IA (início):**

> Vamos direto à execução do desafio da Onfly, sem continuar as aulas agora. Vou corrigir os arquivos, testar o relatório e preparar a entrega com a documentação exigida, incluindo a declaração de uso de IA.

**Resultado consolidado das ações da IA (não transcrição literal do processo interno):**

1. Acessou os arquivos originais da pasta conectada no Google Drive.
2. Copiou o projeto para uma pasta local de trabalho, preservando os dados e testes originais.
3. Rodou os testes de partida, que mostraram cinco falhas.
4. Corrigiu os seguintes comportamentos:
   - diferença entre datas completas para noites de quarto;
   - faturamento apenas de status `CONFIRMED`;
   - conversão para BRL por multiplicação com `Decimal`;
   - ranking de hotéis decrescente por valor, com desempate por ID crescente;
   - leitura de todas as linhas do CSV, sem limite de 200.
5. Criou testes adicionais, executou o Pytest e validou a amostra e o conjunto completo de dados.
6. Preparou um pacote ZIP, documentação do processo e instruções para uso no Windows.

**Resultado verificado:** 10 testes passaram na cópia corrigida (5 fornecidos e 5 adicionados). A validação da amostra coincidiu com os números do README.

## Complementação da pessoa candidata

Para máxima transparência com o recrutador, acrescente a exportação ou a transcrição completa das mensagens relevantes do ChatGPT, incluindo eventuais próximas revisões, decisões e validações realizadas no computador da pessoa candidata. Não omita o uso da IA na implementação.
