# Домашнее задание к лекции «Flask»

## REST API (backend) для сайта объявлений, написанное на Flask.

Для сборки образа из файла Dockerfile необходимо перейти в текущий каталог и выполнить команду:

#### docker build --tag flask_rest_api_image .

Команда для запуска контейнера на основе собранного образа:

#### docker run -P -d --name rest_api_container flask_rest_api_image
