# Configurando a Placa

## Conectando via SSH

> **Nota:** No Windows, o `.local` para conectar com a placa via SSH pode não funcionar.  
> Use o comando abaixo substituindo `<user>` e `<ip>` conforme necessário:
>
> ```sh
> ssh <user>@<ip>
> ```
> Exemplo:  
> ```sh
> ssh pi@rasp<NUMERO_DA_PLACA>.local
> ```

- **Senha padrão:** `raspberry`
- **IP:** `15.0.202.32`

---

## Conectando via SSH sem senha

Para evitar digitar a senha toda vez, copie sua chave pública para a Raspberry Pi:

### Linux

```sh
ssh-copy-id -i ~/.ssh/id_rsa.pub <user>@<ip>
```

### Windows (PowerShell)

1. Achar a sua chave pública (assumindo que já tenha uma):
    ```powershell
    type $env:USERPROFILE\.ssh\id_rsa.pub
    ```
2. Copia o conteúdo da chave pública.
3. Loga na Raspberry Pi.
4. Acessar o diretório `.ssh` (ou criar, se não existir):
    ```sh
    cd ~/.ssh
    ```
5. Editar o arquivo `authorized_keys`:
    ```sh
    nano ~/.ssh/authorized_keys
    ```
6. Colar a chave pública, salve e saia (`Ctrl+O`, `Enter`, `Ctrl+X`).
7. Corrigir as permissões:
    ```sh
    chmod 700 ~/.ssh
    chmod 600 ~/.ssh/authorized_keys
    ```
8. Cabou-se

---

## Copiando arquivos para a Raspberry Pi

- Para copiar arquivos, utilize o comando `scp`:
    ```sh
    scp <arquivo> <user>@<ip>:<destino>
    ```