# Exemplo de Login usando Flask e Flask-Dance

Um simples app para fazer login no Twitter

## Começar

Instruções básicas para executar

### Pré-requisitos

Instale as bibliotecas necessárias para executar a aplicação

```
pip install -r requirements.txt
```

Substitua as chaves do seu Twitter APP em  TWITTER_OAUTH_API_KEY e TWITTER_OAUTH_API_KEY no arquivo config.py

```
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'chave-super-secreta'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')

    # Twitter App
    TWITTER_OAUTH_API_KEY = os.environ.get('TWITTER_OAUTH_API_KEY') or 'twitter-api-key'
    TWITTER_OAUTH_API_KEY = os.environ.get('TWITTER_OAUTH_API_KEY') or\
                         'twitter-api-secret'
```

Crie o banco de dados

```
python run.py --setup
```

### Executar

```
python run.py
```

### Referência

```
https://pythonhosted.org/Flask-Dance/quickstarts/sqla-multiuser.html
```
