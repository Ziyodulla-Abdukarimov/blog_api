## Blog Api sample application

### Setup
The first thing to do is to clone the repository:
```sh
$ git clone https://github.com/Ziyodulla-Abdukarimov/blog_api.git
$ cd blog_api
```
Create a virtual environment to install dependencies in and activate it:
```sh
$ pip install pipenv
$ pipenv shell
```
Then install the dependencies:
```sh
(env)$ pip install -r requirements.txt
```
Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/swagger/`.

![alt text](https://github.com/Ziyodulla-Abdukarimov/blog_api/blob/master/readme_files/swagger.png?raw=true)