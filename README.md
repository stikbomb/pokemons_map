# Карта покемонов

![sample text](https://dvmn.org/filer/canonical/1563275070/172/)

### Предметная область

Сайт для помощи по игре [Pokemon GO](https://www.pokemongo.com/en-us/). Это игра про ловлю [покемонов](https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D0%BA%D0%B5%D0%BC%D0%BE%D0%BD).

Суть игры в том, что на карте периодически появляются покемоны, на определённый промежуток времени. Каждый игрок может поймать себе покемона, и пополнить свою личную коллекцию.

На карте может быть сразу несколько особей одного и того же покемона: например, 3 Бульбазавра. Каждую особь могут поймать сразу несколько игроков. Если игрок поймал себе особь покемона, она исчезает для него, но остаётся для других.

В игре есть механика эволюции. Покемон одного вида может "эволюционировать" в другого. Так, например, Бульбазавр превращается в Ивизавра, а тот превращается в Венузавра.

![bulba evolution](https://dvmn.org/filer/canonical/1562265973/167/)

### Как запустить

- Скачайте код
- Установите зависимости командой `pip install -r requirements.txt`
- Выполните подлючение и настройку базы данных последовательным выполнением команд
```
python3 mamage.py makemigrations
python3 manage.py migrate
```
- Запустите сервер командой `python3 manage.py runserver`


### Доступ к административной панели
- Для получения логина и пароля для доступа к административной панели используйте команду `python3 manage.py createsuperuser`
- По умолчанию административная панель доступна по адресу `your_host/admin/`, где `your_host` адрес вашего сервера
### Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 2 переменные:
- `DEBUG` — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта

### Прочая информация
На данном этапе выход из дебаг-режима не гарантирует стабильную работу приложения - возможны проблемы с подгружаемыми и статичными файлами.
## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
