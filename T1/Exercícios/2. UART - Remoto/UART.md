# Exercício UART - Remoto

## Configuração das Placas

- **[Enunciado](https://gitlab.com/fse_fga/raspberry-pi/exercicios/exercicio-1-uart)**
- **[Feedback](https://youtube.com/live/0nQ8VKl0zU4?feature=share)**
    - Placa: `rasp42`
    - Porta: `15002`

```sh
ssh <user>@164.41.98.2 -p <LISTA DE PORTAS>
```

- **Usuário:** combinação de seu primeiro e último nomes em minúsculo e sem acento
- **Senha:** sua matrícula
---

# Exercício 1 - Comunicação UART

## 1. Objetivos

Neste trabalho, o(a) aluno(a) irá exercitar o acesso a dispositivos utilizando as funções de acesso a arquivos do POSIX. O objetivo é implementar uma comunicação serial (UART) entre a placa Raspberry Pi e um microcontrolador Arduino.

## 2. Circuito Esquemático

Para conectar o Raspberry Pi ao Arduino, utilize a porta serial através dos pinos 8 (UART_TXD) e 10 (UART_RXD) do Raspberry Pi e os respectivos pinos RX, TX do Arduino. Atenção: o Raspberry Pi opera a 3.3V e a maioria dos Arduinos a 5V. É necessário usar um método de conversão de tensão (Level Shifter, Divisor de Tensão, Optoacopladores, etc.).

## 3. Funções POSIX para UART

- **open()**: Abre o arquivo que aponta para a porta serial (UART).
    ```c
    int fd;
    fd = open("/tmp/teste.txt", O_WRONLY);
    ```

- **close()**: Fecha o arquivo referente à porta serial.
    ```c
    int fd;
    close(fd);
    ```

- **write()**: Escreve dados na porta serial.
    ```c
    short siX16 = 0x7FFF;
    int res = write(fid, &siX16, sizeof(short));
    ```

- **read()**: Lê dados da porta serial.
    ```c
    short siX16;
    int res = read(fid, &siX16, sizeof(short));
    ```

## 4. Roteiro

Crie um programa em C, no Raspberry Pi, capaz de usar a comunicação UART para ler e escrever conforme o protocolo abaixo:

- **Escrita de dados**: Mensagens de solicitação devem seguir o padrão: Código do comando (Tabelas 1 e 2) + quatro últimos dígitos da matrícula (char).
    - Exemplo: comando `0xA3` (163 decimal) e matrícula "4521": `char[] = {163, 4, 5, 2, 1}`.
    - Mensagens de envio: Comando + Dado + Matrícula. Para strings: Comando + Tamanho da String (1 byte) + String + Matrícula.

- **Leitura de dados**: Siga o padrão de retorno da Tabela 1.
    - Inteiros (int) ou reais (float): leia 4 bytes e armazene em uma variável.
    - Strings: primeiro byte indica o tamanho, seguido pelo conteúdo da mensagem.

- **Impressão**: Cada mensagem recebida deve ser impressa na tela (stdout).

Estruture o programa em funções. Cada acesso à porta serial deve abrir e fechar o arquivo referente ao device UART para evitar concorrência.

Implemente um menu na linha de comando para acessar cada função de solicitação ou envio de dados.

## 5. Tabelas de Protocolo

### Tabela 1 - Solicitação de Informações

| Código | Comando de Solicitação | Mensagem de Retorno |
|--------|-----------------------|---------------------|
| 0xA1   | Solicitação de inteiro | int (4 bytes)       |
| 0xA2   | Solicitação de float   | float (4 bytes)     |
| 0xA3   | Solicitação de string  | char (1 byte tamanho) + char[] (conteúdo) |

### Tabela 2 - Envio de Dados

| Código | Comando de Envio      | Mensagem de Retorno |
|--------|-----------------------|---------------------|
| 0xB1   | Envio de inteiro      | int (4 bytes)       |
| 0xB2   | Envio de float        | float (4 bytes)     |
| 0xB3   | Envio de string       | char (1 byte tamanho) + char[] (conteúdo) |

## 6. Formato dos Pacotes

- **Solicitação de Dados**: Código + Matrícula
- **Envio de Dados**: Código + Dado + Matrícula
- **Recebimento de Dados**: Conforme tipo solicitado (int, float, string)

## 7. Dicas

- Considere um tempo de resposta do dispositivo (aguarde pelo menos 100 ms após enviar uma solicitação).
- A UART possui buffers de entrada e saída; a leitura pode retornar parte ou toda a mensagem.
- Consulte o código de exemplo do Arduino disponível no repositório para entender a ordem dos bytes.

## 8. Observações

- O código pode ser testado no Linux, mas deve ser compilado para rodar no Raspberry Pi em sala de aula.
- O código base em C para uso da UART no Raspberry Pi está disponível em: [Código UART](#).

