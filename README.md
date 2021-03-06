#  T_app

Продукт находится в разработке

## Скачивание и подготовка проекта:

- Скачайте код
- Создайте виртуальное окружение
- Cоздайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`:
    - `SECRET_KEY` - произвольный ключ на латинице и цифры
    - `PRODUCTION="no"`
    - `TOKEN=""`
    - `ALLOWED_HOSTS=""`
    - `CHAT_ID=""`
    - `DB_ENGINE=""`
    - `DB_NAME=""`
    - `POSTGRES_USER=""`
    - `POSTGRES_PASSWORD=""`
    - `DB_HOST=""`
    - `DB_PORT=""`
- Установите зависимости командой `pip install -r requirements.txt`
- Создайте файл базы данных и сразу примените все миграции командой `python manage.py migrate`


## Ngrok:
- Скачайте [Ngrok](https://ngrok.com/download), если его нет
- В терминале переходим в папку с файликом ngrok и запускаем командой: 
```sh
./ngrok http http://127.0.0.1:8000
```
- Берем ссылку, например: `f5ac-193-31-192-28.ngrok.io` и вставляем ее в переменную окружения проекта `.env` в пункт `ALLOWED_HOSTS="f5ac-193-31-192-28.ngrok.io"`

## Запуск сервера:

- В папке проекта с включенным виртуальным окружением запустите сервер командой `python manage.py runserver`
- Теперь можно открыть браузер и перейти по ссылке `https://f5ac-193-31-192-28.ngrok.io`, чтобы проверить работает ли тоннель
- Проект также будет работать по адресу `http://127.0.0.1:8000`

## Регистрация и подготовка телеграм бота

- Открываем телеграм и ищем `https://t.me/BotFather` или `@BotFather`
- Нажимаем `/start`, далее `/newbot`, придумываем название
- После создания бота будет сообщение с адресом и токеном бота
- Токен бота необходимо записать в вируальное окружение проекта `.env` в пункт `TOKEN=`
- Далее устанавливаем web кнопку бота `/setmenubutton`
- Выбираем созданного бота
- Ставляем url endpointa созданного с помощью ngrok `https://f5ac-193-31-192-28.ngrok.io/webapp/`
- Пишем название кнопки

## Установка webhook telegram
- Прописываем в ардесной строке браузера: 
```sh
https://api.telegram.org/bot{TOKEN}/setWebhook?url=https://f5ac-193-31-192-28.ngrok.io/webhook/telegram/bot/
```
- Получаем ответ, что webhook was set

## Доступ к админке
- Прописываем в терминале `python manage.py createsuperuser`
- Входим по придуманному логину и паролю

ГОТОВО!



