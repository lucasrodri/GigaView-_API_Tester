FROM python:latest

# Copia a aplicação para a pasta
COPY . /app

# Configura o local padrão
WORKDIR /app

# Instala as dependências
RUN pip install -r requirements.txt

#ENTRYPOINT [ "python" , "-m", "gunicorn", "--reload", "-w", "1", "-b", "0.0.0.0:5000", "app:app" ]
