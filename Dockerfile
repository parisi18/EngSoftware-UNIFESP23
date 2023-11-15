# pull official base image
FROM python:3.10-alpine

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

# coleta arquivos estáticos
RUN python EngSoft/manage.py collectstatic --noinput

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
# EXPOSE 80 parece que o heroku disponibiliza uma porta de maneira dinamica atraves da var PORT

# Run the application 
CMD gunicorn EngSoft.wsgi:application --bind 0.0.0.0:$PORT