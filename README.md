## Django app
Pour lancer l'application:
1. Creation d'un environement: 
```
python -m venv venv 
```

2. installation des packages:
```
pip install -r requirements.txt
```
3. ajout du variable d'environement "secret_key":
```
set secret_key= "secret"
```

4. Faire la migration de la base de données:
```
python -m manage migrate
```

5. Créer un utilisateur:
```
python -m manage createsuperuser
```
4. Pour lancer l'application à l'aide de docker compose:\
**PS**: Docker doit ètre installer et en cours d'exécution
    
    1. Build l'image
    ```
    docker-compose build
    ```
   2. Start
    ```
    docker-compose start
    ```
5. Pour lancer les tests unitaires:
```
python -m manage test app
```