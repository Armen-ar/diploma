# "Календарь" - планировщик задач.

## Требования к приложению:

1. Вход/регистрация/аутентификация через вк.

2. Создание целей.

 Выбор временного интервала цели с отображением кол-ва дней до завершения цели.
 Выбор категории цели (личные, работа, развитие, спорт и т. п.) с возможностью добавлять/удалять/обновлять категории.
 Выбор приоритета цели (статичный список minor, major, critical и т. п.).
 Выбор статуса выполнения цели (в работе, выполнен, просрочен, в архиве).

3. Изменение целей.

 Изменение описания цели.
 Изменение статуса.
 Дать возможность менять приоритет и категорию у цели.

4. Удаление цели.

 При удалении цель меняет статус на «в архиве».

5. Поиск по названию цели.

6. Фильтрация по статусу, категории, приоритету, году.
7. Выгрузка целей в CSV/JSON.
8. Заметки к целям.
9. Все перечисленные функции должны быть реализованы в мобильном приложении

## Приложение упаковано в Docker-контейнер.
### python3.9, Django, Postgres

## Запуск приложения: 

Установить зависимости;

Заполнить .env + какими значениями, в котором следует хранить настройки по умолчанию;

Накатить миграции;

Запустить проект.

### Действия:

1. Создать новый проект с виртуальным окружением.

2. Установить poetry в консоли: команда `pip install poetry`, а затем команда `poetry init`, отвечая 'no' на вопросы 
создаётся в корне проекта файл "pyproject.toml" и командой `poetry install` создаётся в корне проекта файл
"poetry.lock". Kомандой `poetry add django` установить Django создать и командой django-проект и после командой
`python ./manage.py runserver` можно запустить приложение.

3. Создать app командой `python ./manage.py startapp core`.

4. Создать модель пользователя, которая наследуется от AbstractUser.

5. Настроить подключение к базе данных: Установить Postgres командой `docker-compose up --build -d`, создать 
базу данных, создать пользователя, назначить пароль пользователю, предоставить права пользователю на базу данных, 
создать миграцию командой `python manage.py makemigrations` и применить миграции командой `python manage.py migrate`.

6. Создать superuser (пользователя с ролью admin) командой `python ./manage.py createsuperuser`.

7. Отобразить поля в списке username, email, first_name, last_name. В admin.py создать класс с декоратором
"@admin.register", который добавляет (регистрирует апишки) с полем "list_display" и передать в него список
отображаемых полей.

8. Добавить поиск по полям: email, first_name, last_name, username. В admin.py в классе добавить поле "search_fields"
и передать в него значения поиска.

9. Добавить фильтры по полям: is_staff , is_active , is_superuser. В admin.py в классе добавить поле "list_filter"
и передать в него значения по фильтру.

10. Скрыть поле Password. В admin.py в классе добавить поле "exclude" и передать в него кортеж значения.

11. Сделать поля неизменяемыми: Last login, Date joined. В admin.py в классе добавить поле "readonly_fields" и
передать в него значения.

## Deploy: 

Создание Docker-образа, Docker_compose, виртуальной машины, автоматическая сборка образов и автоматический деплой.

### Действия, потребуется 4 контейнера - front, api, migrations и postgres:

1. Создать Docker-образ, файл Dockerfile.

2. Настроить docker-compose.yaml и запустить приложение.

3. Командой "docker-compose up -d" создать контейнеры и открыть в браузере страничку авторизации.

4. В Docker Desktop в терминале контейнера api создать пользователя и зайти в админку по логину и паролю.

5. Командой "docker exec -it diploma /bin/bash" войти в контейнер и там командой "_____" выполнить миграции 

6. В dockerhub создать новый репозиторий и путь прописать в файле docker-compose.yaml.

7. Установить Docker-compose на виртуальную машину.

8. Создать в корне приложения директорию '.github' и внутри директорию 'workflows', а в этой директории файл
'action.yml' внутри описать джобу.

9. Создать repository secrets в Git Hub для конфигурации приложения и разворачивания на сервере.

10. Создать в корне приложения 'docker-compose-ci.yaml', в котором будет задана конфигурация для разворачивания 
на сервере.

11. Создать файл '.env_docker' для енвов на сервере.

12. Пропушить на Git Hub приложение с дальнейшим созданием Actions, который создаст Tag на Docker Hub.


## Аутентификация и авторизация.

1. Идентификация пользователя по username, а не по email, за счет этого отказаться от дополнительно 
этапа подтверждения по почте.

2. Добавить возможность войти через популярную социальную сеть без дополнительных вводимых полей, то есть 
начать пользоваться приложением в один клик.

### Действия

1. Командой `poetry add djangorestframework` установить DRF и добавить его в зависимости 'requirements.txt'.

2. Командой `poetry add django-cors-headers` установить библиотеку 'corsheaders' и добавить его в зависимости 
'requirements.txt'.

3. В приложении Core добавить 'urls.py' и в файле 'todolist/urls.py' включить 'urls.py' из приложения Core.

4. Добавить файл 'serializers.py' в приложение Core и описать 'ModelSerializer' для регистрации, авторизации, 
обновления данных и пароля.

5. Описать View для регистрации, авторизации, обновления данных и пароля пользователя, добавить их в 'core/urls.py'.

6. Добавить поддержку входа через социальные сети (VK): командой `poetry add social-auth-app-django` установить
библиотеку 'python social auth', добавить необходимые параметры в 'settings.py' и в '.env'.

## Веб-интерфейс по работе с целями

#### Графический интерфейс пользователя для работы с целями должен представлять собой доску, 
#### где каждая цель — это карточка на данной доске.

### Действия

1. Создать app командой `python ./manage.py startapp goals`, и подключаем приложение в INSTALLED_APPS.

2. Создать модели для категорий, целей и комментарий, создать миграцию и применить миграцию к БД.

3. Создать методы (views) и сериализаторы к ним, а после добавить админку.

4. Добавить функционал категорий (просмотр/редактирование/удаление и фильтрация).

5. Добавить функционал целей (статусы, приоритет, валидацию целей, просмотр/редактирование/удаление и фильтрация).

6. Добавить функционал комментариев (статусы, приоритет, валидацию комментария, просмотр/редактирование/удаление 
и фильтрация).


## Шеринг доски

#### Графический интерфейс пользователя для работы с целями должен представлять собой доску

### Действия

1. Создать модели Board и BoardParticipant.

2. Создать миграции и применить миграции (выше указаны команды).

3. Добить методы для создания/просмотра/обновления/редактирования доски.

4. Создать сериалайзеры для участников и для самой доски.

5. Создать вью для создания доски, просмотра списка досок и просмотра доски.

6. Отредактировать методы POST /goals/goal_category/create, GET /goals/goal_category/‹pk›, 
PUT /goals/goal_category/‹pk›, DELETE /goals/goal_category/‹pk› и GET /goals/goal_category/list.

7. Отредактировать методы POST /goals/goal/create, GET /goals/goal/‹pk›, PUT /goals/goal/‹pk›, 
DELETE /goals/goal/‹pk› и GET /goals/goal/list.

8. Отредактировать методы POST /goals/goal_comment/create, GET /goals/goal_comment/‹pk›, 
PUT /goals/goal_comment/‹pk›, DELETE /goals/goal_comment/‹pk› и GET /goals/goal_comment/list.


## Телеграм-бот

#### Мобильная версия сайта (создание и просмотр целей)

### Действия
 
 
1. Создать бота с помощью бота BotFather внутри Telegram.

2. Создать приложение bot внутри приложения.

3. Описать модель Телеграмм_пользователя TgUser.

4. Создать python package внутри приложения bot и там создать файл dc, в котором с помощью 
dataclass нужно описать ответы Telegram API.
 
5. Создать файл client, в котором описать класс для обращения в Telegram API.

6. Создать файл runbot (команду для получения уведомлений от бота и отправки в ответ пользователю текста).

7. Реализовать состояние 'Пользователя нет в БД' и 'Пользователь есть в БД'

8. Реализовать состояние 'Бот отправил verification_code' до тех пор пока 'Пользователя ввёл правильный
код подтверждения' 

9. Реализовать состояние: пользователь отправляет допустимые команды боту и бот пришлёт данные, но
при недопустимой команде сообщение 'неизвестная команда'

10. В docker-compose.yaml, docker-compose-ci.yaml нужно добавить секцию с ботом.

11. В docker-compose-ci.yaml добавить в environment TG_TOKEN, добавить его в action и в settings.py.

12. Добавить TG_TOKEN в repository secrets в Git Hub.

13. Реализовать команду для создания цели после выбора категории по предложению бота.


## Запуск проекта Django:

### Действия

1. Перед запуском проекта, накатываем миграции на базу данных командой `python ./manage.py migrate`.

2. Запуск проекта командой `python ./manage.py runserver`.


## Запуск телеграм бота:

### Действия

1. Запуск телеграм бота командой `python ./manage.py runbot`.
