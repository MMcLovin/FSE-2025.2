# Exercício GPIO - Remoto

## Links dos Dashboards:

* [rasp48](https://tb.fse.lappis.rocks/dashboard/d465c460-8e5c-11f0-a4ce-1d78bb2310d8?publicId=86d17ff0-e010-11ef-9ab8-4774ff1517e8) 
    * Porta 15008

* [rasp49](https://tb.fse.lappis.rocks/dashboard/7ad9cbd0-8e7f-11f0-a4ce-1d78bb2310d8?publicId=86d17ff0-e010-11ef-9ab8-4774ff1517e8) 
    * Porta 15009

* [Enunciado](https://gitlab.com/fse_fga/raspberry-pi/exercicios/exercicio-gpio-remoto)

* `ssh <user>@164.41.98.2 -p <LISTA DE PORTAS>`
* `Usuário`: combinação de seu primeiro e último nomes em minusculo e sem acento
* `Senha`: é a sua matrícula.
* Tentei fazer o exercício dia 13/09, mas as placas estão com problema de import das bibliotecas em python, então talvez tenha que tentar em c.

## Exercício 1

Neste exercício a porta GPIO deve ser ativada como saída digital.
1. Acionar o LED ligando e desligando;
2. Acionar o LED em modo liga/desliga temporizado.
3. Acionar os LEDs em sequência ativando um padrão temporizado.

## Exercício 2

Neste exercício as saídas PWM devem ser ativadas utilizando modulação por largura de pulso (PWM).
1. Acionar as saídas PWM utilizando a técnica de PWM para ativar a saída em um valor entre 0 e 100% e observar o valor correspondente no Dashboard.
2. Programar a ativação de PWM em rampas acendentes e descendentes, variando o sinal de PWM de 0 a 100% em cada uma das saídas PWM.

## Exercício 3 (Não terminei a tempo e mataram o dashboard, pqp)

Neste exercício, as entradas digitais devem ser lidas utilizando técnicas de polling e debounce.
1. Utilize a técnica de polling para ler o estado de um botão (ou jumper) e imprimir na tela cada vez que houver uma mudança de estado.
2. Implemente a técnica de debounce para filtrar mudanças de estado espúrias do botão, garantindo que apenas transições reais sejam registradas.

### Anotações

* **Polling:**  técnica de programação onde o programa verifica continuamente o estado de uma entrada
    * **Exemplo**: verificar o estado de um botão em um loop infinito.
* **Debounce:**  técnica usada para resolver um problema comum com entradas físicas, como botões.
    * **Exemplo**: implementar um atraso após a detecção de uma mudança de estado para garantir que o sinal esteja estável antes de registrá-lo.
    * **Exemplo no cotidiano**: Quando você pressiona um botão, o contato elétrico não é perfeito e instantâneo; ele "quica" algumas vezes antes de se estabilizar em um estado ligado (ou "desliga" algumas vezes antes de se estabilizar em um estado desligado). Esses "quiques" geram múltiplos sinais rápidos de ligado e desligado, o que o microcontrolador interpretaria como várias pressões curtas do botão, em vez de uma única.

