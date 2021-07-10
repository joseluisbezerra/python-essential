# Python Essential
Atividade para nivelamento de conhecimento sobre o básico do python na empresa WLC Soluções

# O desafio
Um script que pegue as informações de um arquivo de planilha e mostre:
- O saldo total por pessoa;
- O saldo total por conta;
- O total de todas as contas por data.

## Regras
- As informações devem ser exibidas no console;
- Um registro sem conta deve ser ignorado;
- Um registro deve ter um valor;
- Um registro deve ter uma data válida;
- Todas as ocorrências acima devem ser registradas em um txt. O txt deve ter o número da linha que está com problema, qual informação está faltando e todas as informações que foram lidas da linha.

# Instalação
1. Crie um ambiente virtual:
```
python3 -m venv venv
```
2. Ative o ambiente virtual;
3. Instale as dependências:
```
(venv) pip install -r requirements.txt
```
4. Teste o script:
```
(venv) python main.py
```