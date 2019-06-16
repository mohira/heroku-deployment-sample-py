Heroku deployment sample in python with Pipenv, Flask, and Gunicorn
=================
You can access [here](https://heroku-deployment-sample-py.herokuapp.com/), and see very simple web page.
JSON server sample is [here](https://heroku-deployment-sample-py.herokuapp.com/json).

## Environment
- Python 3.7.0
- Gunicorn 19.9.0
- Flask 1.0.3
- Pipenv: 2018.10.13

## How to deploy
If you want to deploy your application to heroku, you do the below steps.

### Install Heroku CLI
Heroku CLI is required([Document: The Heroku CLI | Heroku Dev Center](https://devcenter.heroku.com/articles/heroku-cli))

### Login to Heroku
```bash
heroku login
```

### Create your application
```bash
heroku create sample-app-name
```

### Set the environment variable(`MODE`) in your Heroku application
```bash
heroku config:set MODE=Production
```

### Open your application in your browser
```bash
heroku open
```

## Run Development Mode
### Install packages via Pipenv
- [Pipenv: Python Dev Workflow for Humans — pipenv 2018.11.27.dev0 documentation](https://docs.pipenv.org/en/latest/)

```bash
pipenv install
```

### Set local the environment variable(`MODE`)
You have to set environment variable `MODE=Development` in your setting file (e.g. `.bashrc`).

```bash
export MODE=Development
```

In my case, I use PyCharm to execute `web/server.py`.

cf: [How to set environment variables for your Python application from PyCharm - Techcoil Blog](https://www.techcoil.com/blog/how-to-set-environment-variables-for-your-python-application-from-pycharm/)

### Check by curl
```bash
$ curl  http://127.0.0.1:5000/json
{
  "messge": "Hello, world",
  "status": 200
}
```

```bash
$ curl  http://127.0.0.1:5000/
<!doctype html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>Heroku Deployment Sample</title>
</head>
<body>
<h1>Hello from index.html</h1>
</body>
</html>
```
