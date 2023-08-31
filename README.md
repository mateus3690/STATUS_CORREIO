# IA_CORREIO

* Forma Manual:
  
 - 1° Clone o projeto:
   >> git clone https://github.com/mateus3690/STATUS_CORREIO.git

 - 2° Abra o CMD no caminho do projeto e execute o comando:
   >> pip install -r ./requirements.txt
 
 - 3° Configure o arquivo .env com base no .env.exemple

 - 4° Se tudo tiver configurado execute o arquivo __init__.py:
   >> python ./__init__.py

* Forma automatica:

  - 1° crie dentro do caminho .github a seguinte pasta e arquivo:
    >> workflows/automacao.yml

  -2° depois dentro do automacao.yml insira as seguintes configurações:
   
  
name: Automação com Selenium

on:
  schedule:
    - cron: '0 */2 * * *'  # a cada 2hs

jobs:
  automacao:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout do código
      uses: actions/checkout@v2

    - name: Configurar Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.x

    - name: Instalar dependências
      run: |
        python -m pip install --upgrade pip
        pip install -r ./requirements.txt

    - name: Executar script
      run: python ./__init__.py
