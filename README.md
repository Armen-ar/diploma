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

#### Приложение должно быть упаковано в Docker-контейнер.
стек (python3.9, Django, Postgres)

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

3. Создать app командой `python ./manage.py startapp core`, в корне создаётся папка приложение "core" с файлами.

4. В файле "core/models.py" добавить модель пользователя, которая наследуется от AbstractUser.

5. Настроить подключение к базе данных: Установить Postgres командой `docker-compose up --build -d`, создать базу данных, 
создать пользователя, назначить пароль пользователю, предоставить права пользователю на базу данных, создать 
миграцию командой `python manage.py makemigrations` и применить миграции командой `python manage.py migrate`.

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

1. 

 
