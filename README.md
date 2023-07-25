# Test-stage-developpeur-application-dorsale

Pour pouvoir lancer app.py:

Il faut faire les commandes suivantes à l'aide du powershell terminal de VSCode:
1. Il faut faire: pip3 install virtualenv
2. vitualenv env
3. Set-ExecutionPolicy Unrestricted -Scope Process
4. env/Scripts/activate.ps1
5. pip3 install flask
6. pip3 install psycopg2
7. pip3 install pytest
8. pip3 install python-dotenv

Ensuite il faut ajouter un ficher .env avec les variables suivante:

HOST="server address"
DATABASE="stagiaires"
NAME = "username"
PASSWORD="password"

Il faut remplacer les valeurs pour les vraies valeurs.

Finalement pour lancer l'application il faut faire la commande suivante dans le powershell de VSCode:

- python app.py

Pour lancer les unit tests il faut faire la commande suivante dans le powershell de VSCode:

- python unit_test.py