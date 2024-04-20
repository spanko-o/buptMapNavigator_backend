import yaml

with open("./config.yaml", encoding='utf-8') as file:
    configfile = yaml.safe_load(file)

class Config(object):
    database = configfile["database"]
    SECRET_KEY = configfile["secret_key"]
    DEBUG = configfile["debug"]
    SQLALCHEMY_DATABASE_URI = f'postgresql://{database["user"]}:{database["password"]}@{database["host"]}:{database["port"]}/{database["name"]}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
