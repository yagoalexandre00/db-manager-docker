# CRUD de Banco de Dados em Docker via CLI
### O que é?
Esse projeto serve para criar, deletar e listar contêineres de banco de dados mysql em docker via CLI de uma maneira facilitada.

### Requisitos
Tudo que você precisa ter é python, pip e docker instalados.

### Versão
- Python 3.12.3 
- pip 24.0
- Docker 26.1.3

### Como rodar o projeto
Faça primeiro o setup do projeto com o seguinte comando `sh setup.sh` ou `pip install -r requirements.txt`
Feito isso, digite `python main.py` no terminal e iniciará o projeto.

### Usando com Docker
Para rodar o projeto com docker, você pode fazer o seguinte:
`docker build -t nome_da_imagem .`
`docker run -v  /var/run/docker.sock:/var/run/docker.sock -it nome_da_imagem`
Com isso, o container iniciará em modo interativo.