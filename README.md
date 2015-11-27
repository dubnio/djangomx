djangomx
========

[![Build Status](https://travis-ci.org/djangomx/djangomx.svg?branch=master)](https://travis-ci.org/djangomx/djangomx)
[![Coverage Status](https://coveralls.io/repos/djangomx/djangomx/badge.svg?branch=master&service=github)](https://coveralls.io/github/djangomx/djangomx?branch=master)
[![Unete a la discución en slack](https://django-mx.herokuapp.com/badge.svg)](https://django-mx.herokuapp.com)

http://django.mx sitio en desarrollo

## Contributing

### Requerimientos

Asegurate de tener instalados los siguientes programas:

* Node.js
* Less
* Postgresql

Instala Node.js
```
brew install node
```

Instala less
```
npm install -g less
```

Instrucciones para instalar postgres: http://www.moncefbelyamani.com/how-to-install-postgresql-on-a-mac-with-homebrew-and-lunchy/

Crea la base de datos
```
createdb -E utf8 database
```

Installa los requerimientos del proyecto:

```
$ pip install -r requirements/development.txt
```

Crea el archivo de configuración:

```json
// conf/secrets.json

{
    "db_name": "database",
    "db_user": "user",
    "db_password": "password",
    "db_host": "",
    "secret_key": "baconislife"
}
```

## Cómo contribuir codigo?

Tomar un issue o crear uno nuevo[Issues](https://github.com/djangomx/djangomx/issues)

Recomendamos crear una rama separada por issue, tarea y trabajar sobre ella
```
git checkout -b task-566
```

Hacer tus commits con mensajes explicitos
```
git commit -m 'Python 3 support... Fixes #12'
```

Subes tu rama y creas un pull request
```
git push origin task-566
```

