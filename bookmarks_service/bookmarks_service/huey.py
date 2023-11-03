from huey import RedisHuey

# Создание экземпляра объекта Huey
huey = RedisHuey()  # Можно использовать другой брокер, если Redis не установлен

# Импорт задач
from bookmarks.tasks import parse_and_save_link

# Регистрация задач
huey.task()(parse_and_save_link)