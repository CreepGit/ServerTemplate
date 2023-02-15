# Django x Vue template server
Django server that comes with a **built in** vue app!

### Installation
Clone as you would any other project
Create a virtual python environment for the project (Do this outside of the project scope)
`python3.10 -m venv [venvLoc]/DjangoServer`
`source [venvLoc]/DjangoServer/bin/activate`
Run Django migrations (run while virtuan environment is active)
`python manage.py migrate`
Install npm modules (run in vue/client/)
`npm install`
Build vue distribution files for django (run in vue/client/)
`npm run build`
Run Django server on port 9000 (run while virtuan environment is active)
`python manage.py runserver 9000`


### Development
Shortcut to make life a bit easier run in project root!!
Steps it does:
 - Go to client
 - Build distribution files for vue (makes django see vue changes)
 - Go back to project root
 - copy built index.html file from static files into template folder where django can find it
 - run server on port 9000

`cd vue/client/ && npm run build && cd ../.. && cp vue/static/vue/index.html vue/templates/vue/index.html && python manage.py runserver 9000`
