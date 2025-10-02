
## Placas Disponibilizadas para o Trabalho

Para acessar as placas:

```sh
ssh %user%@164.41.98.2 -p %PORTA%
```

| Placa   | IP            | Porta  | Dashboard |
| :-----: | :-----------: | :----: | :-------: |
| rasp40  | 164.41.98.2   | 15000  | [Estacionamento - rasp40](https://tb.fse.lappis.rocks/dashboard/54159c30-9c04-11f0-a4ce-1d78bb2310d8?publicId=86d17ff0-e010-11ef-9ab8-4774ff1517e8). |
| rasp41  | 164.41.98.2   | 15001  | [Estacionamento - rasp41](https://tb.fse.lappis.rocks/dashboard/362971f0-9e30-11f0-a4ce-1d78bb2310d8?publicId=86d17ff0-e010-11ef-9ab8-4774ff1517e8). |
| rasp42  | 164.41.98.2   | 15002  | [Estacionamento - rasp42](https://tb.fse.lappis.rocks/dashboard/a926da80-9e30-11f0-a4ce-1d78bb2310d8?publicId=86d17ff0-e010-11ef-9ab8-4774ff1517e8).   |
| rasp43  | 164.41.98.15  | 13508  | [Estacionamento - rasp43](https://tb.fse.lappis.rocks/dashboard/3b17f870-9e59-11f0-a4ce-1d78bb2310d8?publicId=86d17ff0-e010-11ef-9ab8-4774ff1517e8).  |
| rasp44  | (indisponível por enquanto)   | 15004  | [Estacionamento - rasp44](https://tb.fse.lappis.rocks/dashboard/b1c01980-9e59-11f0-a4ce-1d78bb2310d8?publicId=86d17ff0-e010-11ef-9ab8-4774ff1517e8).  |
| rasp45  | 164.41.98.2   | 15005  | [Estacionamento - rasp45](https://tb.fse.lappis.rocks/dashboard/ce56d340-9e59-11f0-a4ce-1d78bb2310d8?publicId=86d17ff0-e010-11ef-9ab8-4774ff1517e8).  |
| rasp46  | 164.41.98.2   | 15006  | [Estacionamento - rasp46](https://tb.fse.lappis.rocks/dashboard/ebaeba20-9e59-11f0-a4ce-1d78bb2310d8?publicId=86d17ff0-e010-11ef-9ab8-4774ff1517e8).  |
| rasp48  | 164.41.98.2   | 15008  | [Estacionamento - rasp48](https://tb.fse.lappis.rocks/dashboard/09080090-9e5a-11f0-a4ce-1d78bb2310d8?publicId=86d17ff0-e010-11ef-9ab8-4774ff1517e8).  |
| rasp49  | 164.41.98.2   | 15009  | [Estacionamento - rasp49](https://tb.fse.lappis.rocks/dashboard/22b4e0d0-9e5a-11f0-a4ce-1d78bb2310d8?publicId=86d17ff0-e010-11ef-9ab8-4774ff1517e8).  |

---

## Usando o SSHFS no Windows

### Pré-requisitos

- [WinFsp](https://winfsp.dev/rel/)
- [SSHFS-Win](https://github.com/winfsp/sshfs-win)

> 💡 Ambos podem ser instalados via:
> ```sh
> winget install SSHFS-Win.SSHFS-Win
> ```
> *Obs: Caso tenha problemas com o `winget`, talvez seja necessário instalar o [Visual C++ Redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170#latest-supported-redistributable-version).*

### Montando o Sistema de Arquivos Remoto

1. Abra o **File Explorer**.
2. Clique com o botão direito em **This PC** e selecione **Map network drive...**.
3. Escolha uma letra de unidade (ex: `Z:`).
4. No campo **Folder**, insira:
    ```
    \\sshfs\%user%@164.41.98.2!%PORTA%
    ```
5. Marque **Reconnect at sign-in** pra montar o drive automaticamente na inicialização.
6. Clique em **Finish**.
7. Insira sua senha.
8. Partir pro abraço.

---

## Copiando Arquivos com SCP

Para copiar arquivos entre a máquina local e a placa remota, utilize o comando `scp`:

- **Enviar arquivo local para a placa remota:**
  ```sh
  scp -P %PORTA% caminho/local/do/arquivo %user%@164.41.98.2:/caminho/remoto/do/arquivo
  ```
---

## Desenvolvendo na Placa

- **VSCode** com a extensão *Remote - SSH*.
- **WinFsp** e **SSHFS-Win** .
- **SCP** para transferir arquivos entre a máquina local e a placa remota.

### Dicas

- Montei meu ambiente com Python 3.13 (o python da rasp é 3.10, tlvz dê algum problema) e usei `pip freeze` para gerar o `requirements.txt`, o que pode incluir dependências do sistema. É bom criar um ambiente virtual do zero e instalar as dependências com:
  ```sh
  pip install -r requirements.txt
  ```
- Para instalar as dependências ignorando versões já instaladas:
  ```sh
  pip install --user --ignore-installed -r requirements.txt
  ```