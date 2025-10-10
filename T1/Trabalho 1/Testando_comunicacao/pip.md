# Configurando binarios.caixa
python -m pip config set global.index-url http://binario.caixa:8081/repository/pypi-repo/simple/
python -m pip config set global.trusted-host binario.caixa

python -m pip install pip --upgrade --user

# Com pip configurado
python -m pip install PySide6
python -m pip install pandas

# Forma verbosa, caso necessário
python -m pip install PySide6 --index-url http://binario.caixa:8081/repository/pypi-repo/simple/ --trusted-host binario.caixa

# Usando um arquivo de texto
python -m pip install -r requirements.txt