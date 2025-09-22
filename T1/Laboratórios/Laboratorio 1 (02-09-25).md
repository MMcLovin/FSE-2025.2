# Configurando a placa

* no windows, o .local para conectar com a placa via ssh não funciona. Então é preciso usar `ssh <user>@<ip>` (ssh pi@rasp<NUMERO_DA_PLACA>.local)
* **senha:** raspberry
* **ip:** 15.0.202.32

## Conectando via ssh sem utilizar senha

* vc precisa copiar a sua chave publica para o servidor remoto `ssh-copy-id -i ~/.ssh/id_rsa.pub <user>@<ip>` (linux)
1. copiar a sua chave publica (`type $env:USERPROFILE\.ssh\id_rsa.pub`)
2. logar na raspberry
3. acessar o ~/.ssh
4. acessar o authorized_keys -> nano ~/.ssh/authorized_keys
5. colar a chave pública, depois ctrl+o -> ctrl+x pra sair
6. corrigir as permissões (? é um passo do gepeto, o renato não falou sobre isso)
7. tcharam

## copiando arquivos para a raspberry

* não prestei atenção
* eu lembro que era pra copiar um shell para a placa, pra poder executar e instalar algumas coisas que vamos precisar