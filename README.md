# Django ❤️ Vue server template
Django server with the ablity to serve a vue application and to talk with it using Django Rest Framework

### Installation
Clone as you would any other project

Create a virtual python environment for the project (Do this outside of the project scope)

`python3.10 -m venv virtualEnvLocation/DjangoServer`

`source virtualEnvLocation/DjangoServer/bin/activate`

Install python packages (Do this in project root (where requirements.txt is))

`python -m pip install -r requirements.txt`

Run Django migrations (run while virtual environment is active)

⚠️ If you want to customize core.User, do it before running any migrations or you will have to yeet and delete your database later on!

`python manage.py migrate`

Install npm modules (run in folder vue/client/)

`npm install`

Build vue distribution files for Django (run in vue/client/)

`npm run build`

Run Django server on port 9000 (run while virtual environment is active)

`python manage.py runserver 9000`

Note! Google authentication only works on 127.0.0.1 and not on localhost

### Development 🔥

Make vite track any Vue changes and build them automatically into the django project, makes you not have to run vite development server. (requires manual page refresh for changes to apply)

`npx vite build --watch --emptyOutDir`

Old method: Command for building files and immediately running Django server afterwards

`cd vue/client/ && npm run build && cd ../.. && python manage.py runserver 9000`

Steps it does:
 - Build distribution files for vue (makes django see vue changes)
 - run server on port 9000

Run vite server for quick Vue change prototyping, note that you don't have a server connection while using this. (run in vue/client/)

`npm run dev`


