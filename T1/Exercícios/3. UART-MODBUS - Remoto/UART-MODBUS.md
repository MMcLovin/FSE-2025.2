# Exercício UART-MODBUS (Remoto)

## Configuração das Placas

- **[rasp45](https://youtube.com/live/0nQ8VKl0zU4?feature=share)**
    - Porta: `15005`
- **[rasp46](https://youtube.com/live/0nQ8VKl0zU4?feature=share)**
    - Porta: `15006`
- **[Enunciado](https://gitlab.com/fse_fga/raspberry-pi/exercicios/exercicio-2-uart-modbus)**

```sh
ssh <user>@164.41.98.2 -p <LISTA DE PORTAS>
```

- **Usuário:** combinação de seu primeiro e último nomes em minúsculo e sem acento
- **Senha:** sua matrícula

---

## Protocolo MODBUS

O Modbus é um protocolo de comunicação da camada de aplicação (Modelo OSI), muito utilizado em comunicação serial com interfaces físicas RS-232, RS-485 e Ethernet.

Existem três variações do protocolo:
- **Modbus RTU (Remote Terminal Unit)**
- **Modbus ASCII**
- **Modbus TCP**

O protocolo funciona em modo cliente-servidor (master-slave), onde o cliente inicia a comunicação e o servidor responde.  
No modo RS-232, geralmente a comunicação é ponto-a-ponto entre dois dispositivos.  
No RS-485, é possível conectar até 127 dispositivos no mesmo barramento.

Este trabalho irá se basear no **Modbus RTU** em modo de comunicação ponto-a-ponto entre dois dispositivos.

### Estrutura da Mensagem Modbus RTU

A mensagem é composta por 4 partes distintas:

| Parte | Descrição                | Tamanho   |
|-------|-------------------------|-----------|
| A     | Endereço do dispositivo | 1 byte    |
| B     | Código da função        | 1 byte    |
| C     | Dados                   | n bytes   |
| D     | CRC-16                  | 2 bytes   |

#### Detalhes

- **A. Endereço do dispositivo:**  
    Primeiro byte define o endereço do dispositivo a ser acessado.  
    Em comunicação ponto-a-ponto, pode ser `0x0` ou `0x1`.

- **B. Código da função:**  
    Segundo byte define o comando a ser enviado.  
    O protocolo Modbus define funções públicas e reservadas para customização.  
    Em caso de erro, o servidor retorna o mesmo código com o bit mais significativo invertido (igual a 1).

- **C. Dados:**  
    Preenchidos conforme a função/comando.  
    O comprimento pode ser variável.  
    O campo de dados pode incluir sub-comandos, endereço de registradores, quantidade de dados, etc.  
    Em caso de erro, pode retornar um código de exceção.

    > **Nota:**  
    > No final do payload (antes do CRC), inclua os últimos 4 dígitos da matrícula do aluno para identificação.  
    > Cada byte contém o valor inteiro de um dígito (não o valor ASCII).

    **Exemplo correto:**
    ```c
    uint8_t matricula[4] = {1, 2, 3, 4}; // também pode ser 'char'
    ```
    **Exemplo incorreto:**
    ```c
    uint8_t matricula[4] = {'1', '2', '3', '4'};
    ```

- **D. CRC-16:**  
    Últimos dois bytes são o código CRC-16 (Cyclic Redundancy Check), calculados a partir do corpo da mensagem para verificação de erros.  
    O Modbus utiliza o CRC-16-ANSI (CRC-16-IBM).

---

## Lista de Códigos

Neste exercício, vamos modificar os códigos do Exercício 01 para nos adequar ao padrão do Modbus.  
Utilizaremos o código `0x23` (reservado para leitura/escrita de múltiplos registradores, lendo/escrevendo 2 registradores de 16 bits por vez) seguido de um sub-código que indicará o endereço de cada registrador.

### Tabela 1 - Códigos do Protocolo de Comunicação

| Código | Sub-código | Comando de Solicitação de Dados | Mensagem de Retorno |
|--------|------------|---------------------------------|---------------------|
| 0x23   | 0xA1       | Solicitação de dado inteiro: integer | int (4 bytes)      |
| 0x23   | 0xA2       | Solicitação de dado real: float      | float (4 bytes)    |
| 0x23   | 0xA3       | Solicitação de dado do tipo string: char[] | char (1 byte com o tamanho da string) + char[] (n bytes com o conteúdo da string) |
| 0x16   | 0xB1       | Envio de um dado no formato integer | int (4 bytes)      |
| 0x16   | 0xB2       | Envio de um dado no formato float   | float (4 bytes)    |
| 0x16   | 0xB3       | Envio de uma string: char[]         | char (1 byte com o tamanho da string) + char[] (n bytes com o conteúdo da string) |

### Exemplos de Mensagens

#### Solicitação de inteiro

| Mensagem           | A. Endereço do dispositivo | B. Código da função | C. Dados | D. CRC-16 |
|--------------------|---------------------------|---------------------|----------|-----------|
| Solicita inteiro   | 0x01                      | 0x23                | 0xA1     | 2 bytes   |

#### Envio de inteiro 3245

| Mensagem           | A. Endereço do dispositivo | B. Código da função | C. Dados                        | D. CRC-16 |
|--------------------|---------------------------|---------------------|----------------------------------|-----------|
| Envia o inteiro    | 0x01                      | 0x16                | 0xB1 0x00 0x00 0x0C 0xAD         | 2 bytes   |
