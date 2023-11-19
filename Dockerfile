# pull official base image
FROM python:3.10.12

# Set environment variables
# Usado para evitar a criacao de arquivos bytecode .pyc, tornando a execucao mais eficiente
ENV PYTHONDONTWRITEBYTECODE 1
# Evita o buffer de saida padrao, garantindo que a saida seja impressa diretamente no terminal sem ser armazenada em buffer
ENV PYTHONUNBUFFERED 1
# DEBUG sempre FALSO em produção
ENV DEBUG 0

# Configura o diretorio de trabalho dentro do conteiner como /app, onde os comandos subsequentes serao executados
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# coleta arquivos estáticos
RUN python EngSoft/manage.py collectstatic --noinput

# já dou release na imagem
RUN heroku container:release web -a petscan-ressurections

# Run the application
CMD gunicorn --pythonpath EngSoft EngSoft.wsgi:application --bind 0.0.0.0:${PORT##\\}