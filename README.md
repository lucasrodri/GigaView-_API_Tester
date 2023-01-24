# Front-End

Contém o código do front-end do GigaView

# Deploy

1 - Instale o docker

```sh
sudo apt update
sudo apt install docker docker-compose
```

2 - Crie uma rede externa:
```sh
docker network create external-gigaview-network
```

3 - Adicione as seguintes linhas no docker-compose.yml do Front-End

```sh
networks: 
  default: 
    external: 
      name: external-gigaview-network
```

4 - Modifique o arquivo .env do Front-End

```sh
APP_NAME=GigaView
API_HOST=frontend-tester
API_PORT=5000
```

5 - Realize o deploy

```sh
sudo docker compose up
```

6 - Verifique se aplicação está rodando: [clique aqui](http://localhost:5005)
