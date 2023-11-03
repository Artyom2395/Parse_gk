Данная документация описывает Django-проект, который позволяет пользователям сохранять закладки и автоматически парсить информацию о веб-сайтах, чтобы заполнить эти закладки более полными данными.
1. Установка
Для установки проекта выполните следующие шаги:

Клонируйте репозиторий:
git clone <repo>

Перейдите в каталог проекта:
cd your-project-folder

Установите зависимости с помощью pip:
pip install -r requirements.txt

Примените миграции для базы данных, в качесвте БД используется SQlite:
python manage.py migrate

Установка redis в качестве броке сообщений:
Нужно установить Redis, существуют разные способы, мы используем Docker
Можно легко получить образ Redis платформы Docker. Запустите следующую ниже команду из оболочки:
docker pull redis

Исполните следующую ниже команду в оболочке, чтобы запустить контейнер Docker для Redis в отдельном терминале:
docker run -it --rm --name redis -p 6379:6379 redis

Для данного проекта в качестве распределенной очереди задач используется сервис huey (аналог Celery) https://huey.readthedocs.io/en/latest/index.html
Вы можете указать другой брокер, если Redis не установлен. В файле huey.py и settings.py, вы должны указать нужный брокер для RedisHuey.
в settings.py:
HUEY_REDIS_URL = 'redis://localhost:6379'
Внутри проекта после установки всех зависимостей:
Запустим очередь задач huey внутри проекта выполнив команду в отдельном терминале(не закрывая терминал redis):
manage.py run_huey

Запустите Django-сервер в отдельом терминале:
python manage.py runserver

Проект предоставляет следующие функции:
Добавление закладок с автоматическим парсингом информации о веб-сайтах.
Предотвращение добавления дублирующихся закладок.
Отображение списка закладок, принадлежащих текущему пользователю.
Регистрация и авторизация пользователей

В качестве примера для тестирвоания уже были использованы некоторые сайты с разными разметками
Доступ в профиль для просмотра
логин: artyr
пароль: 124689Artyr

в кчасевте шаблона за основу был взят http://www.tooplate.com/view/2105-input