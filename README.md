# README

## To use the barebones-flask-postgresql app as a starting point:
- Create new repo on GitHub. In Quick Setup, copy URL (do not initialize the new reop with README, license, or gitignore file)
- In a local shell:
```sh
$ cd ~/gitRepos
$ git clone https://github.com/jjocemac/barebones-flask-postgresql.git
$ mv barebones-flask-postgresql <new-app-name>
$ cd new-app-name
$ rm -rf .git
$ git init
$ git add .
$ git commit -m "First commit"
$ git remote add origin <remote-repository-URL-copied-from-GitHub>
$ git push -u origin master
```
- Set up pipenv:
```sh
$ pipenv --three install
$ pipenv shell
```
- Use pipenv to install new dependencies when needed, and commit new Pipfile/Pipfile.lock to the git repo each time
- Setup local (development) environment. Make sure pipenv shell is disabled first (exit), autoenv is installed (pip install autoenv), and "source <path-to-activate.sh>" is in your bashrc file:
```sh
$ echo "pipenv shell; " > .env
$ echo 'export APP_SETTINGS="config.DevelopmentConfig"' >> .env
```
- Create heroku app:
```sh
$ heroku create <unique-app-name>
$ heroku config:set APP_SETTINGS=config.ProductionConfig
$ git push heroku master
```
