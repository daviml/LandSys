# LandSys
- Systema Landix

# Dependências
- Pyhton 3.8+
- PostgreSQL
- Django 3+ 
- Django Rest Framework

# Instalação
1 Ative o DB
- Credenciais em /../settings.py

2 Crie o virtualenv para o projeto. Escolha um diretório fora do diretório do projeto.
- python3.8 -m venv

3 Ative o venv criado.
- ~/my_venvs/unnamed/bin/activate

4 Acesse o diretório do projeto.
- /LandSys

5 Aplique as migrations.
- python manage.py migrate

6 Execute o servidor de desenvolvimento
- python manage.py runserver
