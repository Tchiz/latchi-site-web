Procédure d'installation Pelican + Site Web
=============

By : Aurore de Amaral

/!\ (Les procédures d'installations varient en fonction du système d'exploitation)

1. Vérifier que python 2.7 est installé (`python --version`) et que la JRE java est installée, pour la compression JS/CSS (`java -version`). Il faut aussi vérifier que `jpegtran` et `optipng` est installé, sinon l'installer avec les dépôts, pour la compression JPEG.

2. Installer « pip » (paquet `python-pip`)

3. En ligne de commande :

	`pip install pelican fabric markdown jinja2 yuicompressor py_w3c`

4. Vérifier que git est installé et que la clé publique fonctionne avec github (https://help.github.com/articles/testing-your-ssh-connection/)

5. Cloner dans un répertoire le site web Pelican (les sources)

	`git clone https://github.com/auroredea/website-pelican.git`

6. Dans ce nouveau répertoire, cloner les plugins

	`git clone https://github.com/getpelican/pelican-plugins.git`
	`git clone https://github.com/auroredea/pelican-yuicompressor.git plugins/`

7. Tester le tout avec `fab build && fab serve` et tester si le site s'affiche bien en local !
