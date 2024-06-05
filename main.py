from dotenv import load_dotenv
import os
import docker
from docker import errors

con = docker.from_env()


def criar_container():
    password = input("Insira uma senha para o root: ")
    if password == '':
        root_password = '123456'
    else:
        root_password = password
    try:
        print("Criando container. Aguarde...")
        container = con.containers.run(image="mysql:8.4", environment={
            'MYSQL_ROOT_PASSWORD': root_password}, publish_all_ports=True, detach=True)
        print(f"Container criado com sucesso! ID: {container.short_id}")
    except errors.APIError as error:
        print(f"Container não foi criado. Erro: {error}")


def listar_container(lista):
    lista_containers = lista
    if len(lista_containers) == 0:
        print("Não há containers rodando...")
    else:
        print("Lista de containers rodando atualmente:")
        for container in lista_containers:
            print(f"Container: {lista_containers.index(container) + 1}")
            print(f"ID:  {container.short_id}")
            print(f"Porta: {container.ports["3306/tcp"][0]['HostPort']}")
            print(f"Status: {container.status}")
            print("----------------------------------")


def parar_containers(lista):
    lista_containers = lista
    if len(lista_containers) == 0:
        print("Não há containers rodando...")
    else:
        for container in lista_containers:
            print(f"Removendo container {container.short_id}...")
            container.remove(force=True)

print("----------------------------------")
print("1 - Criar")
print("2 - Listar")
print("3 - Remover")
opcao = int(input("Insira a opção que deseja: "))
print("----------------------------------")

if opcao == 1:
    criar_container()
elif opcao == 2:
    list_con = con.containers.list()
    listar_container(list_con)
elif opcao == 3:
    list_con = con.containers.list()    
    parar_containers(list_con)