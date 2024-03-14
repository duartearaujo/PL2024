# TPC5

## Máquina de vendas

**Nome:** Duarte Araújo
**Número:** A100750

## Explicação

Para este trabalho, foi desenvolvido um script que simula uma máquina de vendas, ao analisar o input do utilizador, recorrendo à biblioteca `ply`. Foi utilizado um ficheiro JSON para armazenar os dados da máquina, incluindo o inventário, e a lista de moedas que foram inseridas.

### Tokens

1. `LISTAR` - Indica um print da tabela com o inventário da máquina e os dados de cada produto.
2. `MOEDA` - Vem com uma lista de moedas (1c, 2c, 5c, 10c, 20c, 50c, 1€, ou 2€) separadas por espaço, que devem ser introduzidas na máquina e ser adicionadas ao saldo disponível.
3. `SELECT` - Contém um número que corresponde ao id do produto desejado.
4. `ADICIONAR` - Indica um aumento de uma certa quantidade especificada, do stock de um determinado produto.
5. `SAIR` - Sinaliza o fim das operações do utilizador e faz com que a máquina devolva o troco necessário, e, no caso de não haver moedas que cheguem, o possível.

### Funções relevantes
1. `handle_money()` - Função que trata de converter as *strings* que representam diferentes moedas em valores décimais, para que se possa calcular o saldo atual da máquina em qualquer momento crítico.
2. `handle_token()` - Função encarregue de definir o comportamento da máquina, face aos *tokens* identificados no input do utilizador.
3. `update_json()` - Função responsável pela atualização do ficheiro json com o estado da máquina de vendas. Esse *update* é feito ao **ADICIONAR** stock a um produto, e ao **SAIR**, quando o troco da operação é devolvido.

## Comando a executar

**python3 tpc5.py**
