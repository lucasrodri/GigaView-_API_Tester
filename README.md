# Front-End

Contém o código do front-end do GigaView

# Deploy

1 - Instale o docker

```sh
sudo apt update
sudo apt install docker docker-compose
```

2 - Configure as variáveis de ambiente **APP_NAME**, **API_HOST** e **API_PORT**

- APP_NAME: Nome da aplicação
- API_HOST: IP do APIGateway
- API_PORT: Porta do APIGateway
- SECURE_MODE: Inteiro que indica se o modo seguro está habilitado (não obrigatório). Valor padrão: 0

```bash
touch .env
echo APP_NAME="GigaView" >> .env
echo API_HOST="127.0.0.1" >> .env
echo API_PORT=9000 >> .env
```

3 - Realize o deploy

```sh
sudo docker compose up
```

4 - Verifique se aplicação está rodando: [clique aqui](http://localhost:5000)
