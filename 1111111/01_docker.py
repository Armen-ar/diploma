"""
Публикация в интернете сайта:
1-ый способ через виртуальный хостинг:
создаём аккаунт в хостинге, заходим в систему администрирования и там есть доступ к некоторой папке,
через которую можем загружать файлы; хостинг поддерживается одним большим web-сервером, который включает
в себя множество таких папок, т.е. делим пространство между всеми остальными участниками хостинга; хостинг
хостинг позволяет одновременно раздавать все эти файлы и опубликованный сайт будет работать; это медленно,
потому что делится пространство между большим количеством участников, но очень низкая стоимость;
2-оы способ это виртуальная машина:
 там есть выделенный сервер там устанавливается специальное ПО,
которая может создавать виртуальные машины; виртуальные машины это отдельные независимые операционные системы,
к которым разработчик получает полный администраторский доступ (создавать, менять любые файлы внутри машины);
3-ий способ с выделенным сервером:
это железный комп, стоящий у провайдера, к которому выдаётся доступ и весь комп принадлежит разработчику;
высокая скорость загрузки, но высокая стоимость;
оптимальный вариант - это виртуальная машина
на сервере устанавливается ПО гипервизор (инструмент, который позволяет запускать и управлять виртуальной машиной)
там их несколько и в каждом из них своя операционная система, набор библиотек;

Заходим в cloud.yandex.ru (Ar_Ar, логин arar) кнопки по очереди: Compute Cloud(первая), Создать ВМ(внизу),
заполняем имя 'armen' виртуальной машины и выбираем операционную систему Ubuntu и ниже выбираем диск для ВМ
(ТИП самое дешёвое HDD размер выбрать маленький 10) ниже выбираем платформу Intel Cascade Lake, выбираем минимальное
количество ядер 2 и для уменьшения стоимости выбираем 5% и RAM выбираем 1 Гб и ниже в Доступ
в консоли по команде 'ssh-keygen' после 3 Enter ов создадутся папки где будут храниться ключи публичные
C:\Users\armen/.ssh\id_rsa.pub.

"Order Number is: 9987143667"

Дальше вводим 'type .ssh\id_rsa.pub' и получаем содержимое этого файла публичный ключ
'ssh-rsa AAAAB3N...................7Uhzx4I6ZYhaz838= armen@LAPTOP-H91KOO13', копируем это содержимое и переходим
в cloud.yandex.ru в поле SSH-ключ вставляем и нажимаем создать ВМ, после в графе таблицы 'Публичный адрес'
указан публичный IP адрес, копируем и переходим в консоль(терминал) вводим 'ssh arar@84.201.174.34' далее
'yes' и Enter и поподаем внутрь виртуальной машины. С помощью команды 'ls' можем посмотреть какие файлы существуют,
пока покажет пустоту и командой 'ls -a' покажет скрытые файлы (.  ..  .bash_logout  .bashrc  .cache  .profile  .ssh).
Дальше командой 'ls .ssh' получим 'authorized_keys' и с помощью команды 'cat .ssh/authorized_keys' получим
содержимое того файла: публичный ключ 'ssh-rsa AAAAB3N...................7Uhzx4I6ZYhaz838= armen@LAPTOP-H91KOO13'
КОМАНДЫ:
'ls' - содержимое в папке;
'ls -а' - содержимое в папке, скрытые файлы папки(наименования начинаются с точки);
'type' или 'cat' - содержимое файла;
'ps aux' - выводит все запущенные процессы, как в диспетчере задач;
'top' - всё это в интерактивном режиме;

К виртуальной машине можно подключаться не только через IP адрес, но и через доменное имя (уникальное имя сайта)
Для регистрации доменного имени воспользуемся бесплатным сайтом freenom
в окошке 'Проверить доступность' забиваем наименование домена 'arutyunyan.ga' далее нажимаем оформить заказ, там
выбираем период, на который мы регистрируем доменное имя (выбираем max бесплатное время 12 месяцев)
и нужно указать NS адреса, которые будут обрабатывать запросы на этот домен 'Use DNS' и во вкладке 'Use your own DNS'
заполняем Nameserver: ns1.yandexcloud.net и Nameserver: ns2.yandexcloud.net и на кнопку 'Continue'
Заходим в личный кабинет, в корзину(Hello Armen/View cart) и ставим галочку и кнопка 'Complete order'.
Через консоль командой 'nslookup -type=ns arutyunyan.ga' выводим информацию о домене:
arutyunyan.ga   nameserver = ns2.yandexcloud.net
arutyunyan.ga   nameserver = ns1.yandexcloud.net
'dig +trace ararutyun.ga' можно прочитать логи

Зходим в виртуальную машину и во вкладку 'Все сервисы/Cloud DNS', в правом верхнем углу 'Создать зону',
в окошке зона записываем 'arutyunyan.ga.' (в конце точка), выбираем тип 'Публичная',
имя 'arutyunyan-ga' и 'Создать'.
После создания кликаем на имя 'arutyunyan-ga' открываются записи и нажимаем 'Создать запись'. Откроется создание записи
Тип A, значение записываем Публичный IPv4 (84.201.174.34) и 'Создать'.
Если в консоли запросим 'nslookup -type=any arutyunyan.ga' выводим информацию о домене:
arutyunyan.ga text = "84.201.174.34" (т.е. домен под названием arutyunyan.ga это IP 84.201.174.34) или по команде
'host arutyunyan.ga' выводит '84.201.174.34 это arutyunyan.ga'

Дальше в консоли вводим 'ssh arar@arutyunyan.ga' и поподаем внутрь виртуальной машины куда заходили по команде
'ssh arar@84.201.174.34'

Войдя в виртуальную машину и дальше как администратор по команде 'sudo su' выводит 'root@armen:/home/arutyunyan#'
для добавления репозитория (для установки Python) по команда 'add-apt-repository ppa:deadsnakes/ppa' далее вводим
команду 'apt install python3.10'  проверить можно ввести команду 'python3.10 --version' получим 'Python 3.10.4'
Так же можно установить Docker-compose: для этого по адресу 'https://docs.docker.com/engine/install/ubuntu/'
выполнить Set up the repository 1-3 команды, после Install Docker Engine 1-3 команды. Дальше по адресу
'https://docs.docker.com/compose/install/other/' выполнить On Linux 1 и 3 команды и команду
'sudo chmod +x /usr/local/bin/docker-compose' после чего командой 'docker-compose --version' проверить наличие
установки Docker-compose.

Загрузка приложения в виртуальную машину:
в терминале приложения(в PyCharm) выходя на верхнюю папку командой 'cd ..' передаём команду
'scp -r homework_19_hard arar@arutyunyan.ga:insta' загружаем приложение на машину в папку insta
Перейдя в командную строку и заходя в виртуальную машину командой 'ssh arar@arutyunyan.ga' и по команде
'ls' убедимся, что появилась папка insta, войдя в него 'ls' увидим все папки, которые были в приложении.
Командой 'cd ..' выходим из директории insta в верхний уровень. Входим в режим админ. 'sudo su'
'apt install python3.10-venv'
'python3.10 -m venv env' создание виртуального окружения
'. env/bin/activate' активируем его.
Дальше устанавливаем библиотеки:
'pip install -r insta/requirements.txt'.

Для создания unit файла (работа приложения в фоновом режиме):

1)
Начинаем настраивать приложение:
создание юнит-файла
'vim flask-app.service' открывается файл и кнопкой 'I' вводим текст:
[Unit]
Description=Flask-app
After=network.target

[Service]
WorkingDirectory=/home/arar/insta (уровень папки где находится папка env)
ExecStart=/home/arar/env/bin/python -m flask run -h 0.0.0.0 -p 80
Environment="FLASK_APP=run.py"
Restart=always

[Install]
WantedBy=multi-user.target

для сохранения и выхода из документа 'Ctrl + C', ':' и 'wq'

ИЛИ
2)
в консоли подключаемся к машине команда
'ssh arar@arutyunyan.ga' переходим в режим администратора 'sudo su' и создаём файл команда
'vim /etc/systemd/system/flask-app.service'. 'flask-app.service' это название файла. Открывается этот файл и описываем
секциями файл:
[Unit]
Description=flask-app(текстовое описание)
After=network.target(значит приложение должно запустится после того, как запустятся все демоны, отвечающие за сеть на
этой виртуальной машине)

[Service]
WorkingDirectory=/home/arutyunyan/flask_app/ (папка где код приложение находится)
ExecStart=/home/arutyunyan/env/bin/python -m flask run -h 0.0.0.0 -p 80 (команда запускается при старте)
Environment="APP_SETTINGS=/home/arutyunyan/config.py" (переменная окружения, путь откуда брать конфиг)
Restart=always (в случае чего приложение будет остановлено это перезапустит)

[Install]
WantedBy=multi-user.target

для сохранения и выхода из документа 'Ctrl + C', ':' и 'wq'

В консоли, как админ команда для загрузки Unit-файл:
'systemctl daemon-reload' и после мы можем запустить Unit.
'systemctl restart flask-app' стартует Unit-файл.
С помощью команды 'systemctl status flask-app' смотрим запущено ли приложение.
Открываем браузер и вводим наш домен увидим работающую страницу. Для отключения от виртуальной машины
вводим команду 'exit', но приложение будет работать в фоновом режиме, страница в браузере будет отвесать.


Зарегистрировать специального пользователя Skyprouser и задать ему пароль в соответствии:
'adduser skypro' дальше запросит ввести пароль, вводим и просит повторно, вводим и Enter ами доходим до 'Y/n' вводим
Y и Enter. Дальше вводим команду 'usermod -aG sudo skypro' Enter.
'vim /etc/ssh/sshd_config' открывается файл и кнопкой 'I' редактируем: проматываем вниз и
PasswordAuthentication вместо 'on' записываем 'yes' и сохраняем ':wq'
Дальше команда 'sudo service ssh restart' Enter. Пользователь создан.
======================================================================================================================
С postgres

Для работы приложения нужно установить базу данных устанавливаем 'apt install postgresql' далее 'Y' установится.
'sudo su postgres' заходим как администратор пользователь postgres выводит 'postgres@armen:/home/arutyunyan$'
'createuser --interactive -P' это команда, что хотим задать пароль
'Enter name of role to add' нас спрашивают какого пользователя хотим создать (например arm_postgres)
'Enter password for new role:' ввести пароль '12345' в консоли не видно как вводим
'Shall the new role be a superuser? (y/n)' пользователь будет суперпользователем, отказываем 'n'
'Shall the new role be allowed to create databases? (y/n)' разрешить создавать базы данных? отказываем 'n'
'Shall the new role be allowed to create more new roles? (y/n)' разрешить создавать больше новых ролей?  отказываем 'n'
Пользователь создан.

Создаём БД.
'createdb postgresdb --owner arm_postgres' создаём БД с названием flask_app и владелец(owner) пользователь arm_postgres
для проверки выполнения команды 'psql -U postgresdb -h 127.0.0.1 arm_postgres' по названию postgresdb БД пользователь
arm_postgres, запросит ввести пароль и попадаем в работающий postgrestsql (postgresdb=>)
по команде '\l' выводит все записи в БД:

   Name    |     Owner     | Encoding |   Collate   |    Ctype    |   Access privileges
-----------+-----------+----------+-------------+-------------+-----------------------
 postgresdb | arm_postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 |
 postgres  | postgres      | UTF8     | en_US.UTF-8 | en_US.UTF-8 |
 template0 | postgres      | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |               |          |             |             | postgres=CTc/postgres
 template1 | postgres      | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |               |          |             |             | postgres=CTc/postgres

'Shift C' - можно отсортировать в порядке потребления процессорного времени;
'Shift M' - можно отсортировать по памяти.
--------------------------------------------------------------------------------------------------
Начинаем настраивать приложение: команда 'vim config.py(или другое название)'
открывается текстовый редактор vim и туда записываем содержимое 'SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"'
файла 'default_config' нашего приложения, но вместо sqlite записываем postgrestsql и добавляем имя пользователя
'arm_postgres', через двоеточие пароль '12345' потом '@', а дальше хост, на котором будет запущена postgrestsql
так как та же машина 'localhost' и после слэш название базы данных, у нас это 'postgresdb' получится:
'SQLALCHEMY_DATABASE_URI = "postgrestsql:///arm_postgres:12345@localhost/postgresdb"' и сохраняем файл.
Теперь заходим в директорию командой 'cd flask_app/'
(нолики указываем для того, чтоб смогли извне слать запросы на эту машину)
Переопределяем переменную окружения поэтому командой 'export APP_SETTINGS../config.py' и дальше применяем
миграции: команда 'flask db upgrade' (миграция применяется) и можем запускать приложение: 'flask run -h 0.0.0.0 -p 80'
открываем браузер и забиваем адрес: 'arutyunyan.ga' появится {"total":0,"users":[]} нет пользователей пока.
С помощью Postman создаём пользователя: http://arutyunyan.ga/api/register, в 'Body' формат 'row' 'json'
записываем {"username":"test3","password":"test"} 'Send' увидим {"username": "test3"} и обновляя страничку браузера
увидим {"total":1,"users":[{"username": "test3"}]}
======================================================================================================================

Пароль "nV1Cf@Q@" для пользователя 'skypro' (это для д/з)
"""


"""
Докер это система контейнеризации, позволяющая изолировать приложение на одной машине друг от друга. Контейнер это
запущенное приложение, которое изолировано от всех остальных. Это делается с помощью двух механизмов в ядре
операционной системы (namespaces и cgroups).
Для установки Docker на компьютер: в браузере, в командной строке docker.com и на странице 'Get Started'.
После установки заходим в консоль и командой 'docker' видим что докер установлен, командой 'ps' увидим какие сейчас
запущены контейнеры.
Для просмотра образа команда 'docker images', скачать - 'docker pull <образ>', удалить - 'docker rm <образ>'


Команды:

'docker -p' запуск контейнера;

'docker ps' запущенные контейнеры;

'docker -d' запуск контейнера в режиме демона;

'docker logs' выводит логи контейнера;

'docker rm -f' и указываем (id контейнера) удаляет контейнер;

'docker ps -a' запущенные и остановленные контейнеры(все);

'docker system prune' удалить все остановленные контейнеры;

'docker exec (id контейнера) ls' выполняет команду внутри контейнера;

'docker exec -it (id контейнера) /bin/bash' в интерактивном режиме можем попасть внутрь контейнера и внутри как
в виртуальной машине работать командами:
внутри командой 'ls' выводит все директории,
командой 'pwd' выводит в какой директории находимся ('/' означает, что находимся в корне),
команда 'apt',
команда 'apt update' обновляет базу репозитория,
команда 'apt install procps' устанавливает пакет,
команда 'ps aux' выводит аля, диспетчер задач все запущенные процессы;
команда 'kill (PID[порядковый номер] из таблицы)' убивает(останавливает) процесс, но пересоздаёт под другим PID;
команда 'kill 1' выкидывает из контейнера (останавливает все процессы в этом контейнере)
командой 'docker ps -a' увидим, что этот контейнер был запущен и остановлен;
команда 'docker start (id контейнера)' перезапускает контейнер

----------------------------------------------------------------------------------------------------------------------
В PyCharm создаём файл Dockerfile
1)
---------------------
FROM ubuntu:20.04 (образ с операционной системой)

RUN apt update && apt install -y nginx (устанавливает в ubuntu nginx, а '-y' это без вопросов установить,
предварительно обновив базу пакетов)
CMD nginx -g 'daemon off;' (указываем, какую команду должен запустить этот образ при запуске)

В терминале приложения: docker build -t (название образа) my_custom_nginx . (директория, откуда будут браться
файлы для сборки, точка-это текущая директория)

команда 'docker exec -it (id контейнера) /bin/bash' вход внутрь контейнера;
командой 'curl localhost:80' позволяет посылать запросы http;
командой 'curl -I' получить заголовки;
команда 'exit' выход из контейнера не убивая его;

командой 'ifconfig', но предварительно обновив и установив пакет 'apt update' и 'apt install net-tools' выводит
конфигурацию данного контейнера, в том числе 'inet 172.17.0.3' IP адрес, после по команде 'curl -I 172.17.0.2'
обращаемся к конфигурации другого контейнера 'Server: nginx/1.19.10', а по команде 'curl -I localhost'
выведет информацию о текущем контейнере 'Server: nginx/1.20.2';

Для создания сети:
команда 'docker network create my_nginxes' создаём сеть;
для каждого контейнера отправляем команду:
'docker run -d --name=nginx_1_20 --network=my_nginxes --network-alias=nginx_1_20 nginx:1.20' и
'docker run -d --name=nginx_1_19 --network=my_nginxes --network-alias=nginx_1_19 nginx:1.19' дальше входим в любой
из них (уже можно не по id 'd33bf57e5d05', а по имени 'nginx_1_19')

команда 'apt install dnsutils' предварительно обновив пакеты 'apt update'
и по команде 'host nginx_1_19' можем проверить IP адрес
---------------------------------------------------------

2)

FROM python:3.10-slim (образ с операционной системой, весит меньше и меньше библиотек)

WORKDIR /code (весь код будет лежать в отдельной директории /code)
COPY requirements.txt . (копируем файл библиотек)
RUN pip install -r requirements.txt (выполняем команду установки библиотек)
COPY app.py . (копируем файл приложения)
COPY migrations migrations (копируем файл для миграций)
COPY docker_config.py default_config.py(копируем конфигурацию приложения, заранее создав отдельный такой файл
docker_config.py, в котором будет настройка для config и его подменим, вместо стандартного config положим нужный нам)

CMD flask run -h 0.0.0.0 -p 80(команда запуска приложения, host 0.0.0.0, для того чтоб извне можно было достучаться до
контейнера и указываем порт '80')

'docker build -t flask_app .' создаём контейнер с названием flask_app (загружается приложение)
для создания контейнера с postgres нужно создать сеть командой 'docker network create flask_app'
'docker run -d --network=flask_app --network-alias pg -e POSTGRES_USER=flask_app_user
-e POSTGRES_PASSWORD=flask_app_password -e POSTGRES_DB=flask_app_db --name=pg postgres' создаём контейнер postgres
с названием pg
'docker build -t flask_app .' создаём контейнер postgres с flask приложением
'docker run --network=flask_app -d -p 80:80 --name=flask_app flask_app' прокидываем порты и название контейнера
'docker exec -it (id контейн.) /bin/bash' входим в контейнер
и там запускаем команду 'flask db upgrade' для применения миграций
===================================================================================================================
"""


"""
Docker volumes
'docker run -d --network=flask_app --network-alias pg -e POSTGRES_USER=flask_app_user
-e POSTGRES_PASSWORD=flask_app_password -e POSTGRES_DB=flask_app_db --name=pg
-v $(pwd)/pd:/var/lib/postgresql/data postgres' создаём контейнер postgres с названием pg
(-v $(pwd)/pd_data:/var/lib/postgresql/data запись для создания директории, куда будет сохранятся данные)
В корне приложения создастся папка pd_data

Docker Compose
Создаём файл: docker-compose.yaml

И после заполнения этого файла уже вводим команду:
'docker-compose down' останавливаем докер компос 
'docker-compose up --build -d' 

Удаляем папку pd_data и запустим приложение заново:
'docker-compose up --build -d' напишет, что миграции не выполнены
сначала 'docker-compose exec -it api /bin/bash' для применения миграции попадаем внутрь контейнера,
вводим команду 'flask db update'
заново создаст директорию pd_data в корне приложения

Развёртывание приложения на сервере:
Для этого можем скопировать весь код проекта, залить в машину и запустить с помощью docker-compose,
но обычно так не делают. Процесс сборки достаточно нагруженный и не надо нагружать сервера постоянной сборкой.
Поэтому заранее можно собрать образ и отправить в Docker Hub и далее на сервере использовать только файлик
docker-compose.yaml с конфигурацией без кода приложения и запускать оттуда через docker-compose приложение.
Для этого нужен аккаунт в Docker Hub создать репозиторий новый, например с названием 'insta'

Теперь для сборки образа в терминале PyCharm пишем команду 'docker-compose build'
для отправки образа в Docker Hub пишем команду 'docker login' выводит запись:
Username: (записываем имя при регистрации)
Password: (записываем пароль, которую ввели при регистрации)
и после успешного входа вводим команду 'docker-compose push'

Для запуска приложения на сервере в терминале пишем команду 'ssh arar@arutyunyan.ga'
чтоб установить docker-compos на сервер переходим в режим админ 'sudo su' и с помощью команды 'curl' скачиваем
специальный репозиторий, после этого запускаем команду 'echo \', дальше обновляем 'apt-get update',
после команда 'apt install dosker-ce dosker-ce-cli containerd.io' дальше Y

Заходим в терминал PyCharm и пишем команду
'ssh arar@arutyunyan.ga' создаём директорию для файла docker_config.py
'mkdir insta_docker' - создание папки и 'logout' - ??????
'scp docker_config.py arar@arutyunyan.ga:insta/docker_config.py' скопируем во вновь созданную директорию файл
'scp docker-compose.yaml arar@arutyunyan.ga:insta' скопируем во вновь созданную директорию файл

Возвращаемся в терминал сервера:
в контейнере вводим 'docker ps' видим пустой докер
===================================================================================================================
"""


"""
Создание CI приложения

I стадия:
создаём папку .github в корне проекта
внутри этой папки создаём папку workflows
внутри этой папки создаём файла с расширением .yaml

action.yaml
name: Build and deploy workflow  # название workflow
on: [push]  # событие, по которому будет запускаться workflow
jobs: # перечисляем массив
  build_and_push:  # часть CI
    run_on: ubuntu_latest  # указываем, на каком run-ере запускать наши job-ы
    steps:  # скрипты, которые будут запущены на run-ере
      - name: list dir # описание команды для первого
        run: ls -la  # распечатать текущую директорию
      - name: clone cod # описание команды
        uses: actions/checkout@v2  # используем готовый action
      - name: list dir 2 # описание команды
        run: ls -la  # ещё раз распечатать текущую директорию
        
В терминале PyCharm
находясь в папке проекта
' git add .'
'git commit -m "start use actions"'
Открываем GitHub и в репо проекта входим во вкладку Actions там есть workflow и можем зайти в него и посмотреть образ

шаг docker build
----------------

action.yaml
name: Build and deploy workflow  # название workflow
on: [push]  # событие, по которому будет запускаться workflow
jobs: # перечисляем массив
  build_and_push:  # часть CI
    run_on: ubuntu_latest  # указываем, на каком run-ере запускать наши job-ы
    steps:  # скрипты, которые будут запущены на run-ере
      - name: clone cod # описание команды
        uses: actions/checkout@v2  # используем готовый action
      - name: docker build
        run: docker build -t armenar/insta:$GITHUB_REF_NAME-$GITHUB_RUN_ID .  # команда для сборки образа на
                                                                               локальном компьютере
        
        armenar/insta - адрес из Docker Hub (по логину armenar наименование образа insta)
        Специальные переменные из GitHub Actions:
        GITHUB_REF_NAME - при изменении кода нужно сообщить серверам о новой версии образа, переменная содержит в себе
        либо название ветки, которую отправили на GitHub, либо название тэга
        GITHUB_RUN_ID - с каждым запуском будет увеличиваться и не нужно будет дополнительной логики (каждый
        последующий запуск workflow приводил к сборке нового образа)

В терминале PyCharm
находясь в папке проекта
'git add .'
'git commit -m "docker build stop"'
'git push'
Открываем GitHub и в репо проекта входим во вкладку Actions там появился второй workflow и можем зайти в него
и посмотреть образ

после записываем шаг для отправки в DockerHub дописываем верхний кодЖ
      
      - name: docker login # описание команды допуск к репозиторию
        run: echo ${{ secrets.DOCKER_TOKEN }} | docker login -u ${{ secrets.DOCKER_USERNAME }} --password-stdin
        # для получения скрытого пароля переходим в DockerHub (Account Settings левый верх, Security вкладка слева,
        создаём новый Access Token, называем его как хотим и генерируем) заходим в GitHub (в раздел Settings вверху,
        вкладка Secrets слева, вкладка Actions и на верху New repository secret вводим в NAME 'DOCKER_USERNAME',
        а в VALUE пользователь в DockerHub 'armenar' и нажимаем Add secret. Снова New repository secret вводим в
        NAME 'DOCKER_TOKEN', а в VALUE скопированный токен. Для того, чтоб docker login считывал пароль --password-stdin
      - name: docker push # описание команды пушим докер
        run: docker push armenar/insta:$GITHUB_REF_NAME-$GITHUB_RUN_ID .  # пушим вновь созданный образ

В терминале PyCharm
находясь в папке проекта
'git add .'
'git commit -m "docker login and push"'
'git push'
Открываем GitHub и в репо проекта входим во вкладку Actions там появился третий workflow и можем зайти в него
и посмотреть образ

Теперь открываем DockerHub, переходим в репо 'insta' и видим, что появился тэг с ID

Создание CD приложения

Для того чтоб разложить приложение на сервере потребуется 2 файла: конфигурация docker-compose и конфигурация
самого приложения. Копируем файл docker-compose.yaml и сохраняем в корне проекта ci версию docker-compose-ci.yaml.
Ключевое отличие в том, что собирать образы не придётся, т.е. убираем секции build и образ имеет конкретную версию,
которую нужно передать из файла .github/worcflows/action.yaml (образ тегировали в секции docker build) теги в этом
файле и api и migrations. И для того, чтоб не показывать параметры POSTGRES_USER, POSTGRES_PASSWORD и POSTGRES_DB
заменяем их значения на $DB_USER, $DB_PASSWORD и $DB_NAME(или DB_DB) 
-------------------------
docker-compose-ci.yaml

version: "3.9"

services:
  api:
    image: armenar/insta:$GITHUB_REF_NAME-$GITHUB_RUN_ID
    ports:
      - 80:80
    volumes:
      - ./docker_config.py:/code/default_config.py
    depends_on:
      pg:
        condition: service_healthy
      migrations:
        condition: service_completed_successfully
  migrations:
    image: armenar/insta:$GITHUB_REF_NAME-$GITHUB_RUN_ID
    volumes:
      - ./docker_config.py:/code/default_config.py
    depends_on:
       pg:
        condition: service_healthy
    command: flask db upgrade
  pg:
    image: postgres:latest
    environment:
      POSTGRES_USER: $DB_USER
      POSTGRES_PASSWORD: $DB_PASSWORD
      POSTGRES_DB: $DB_NAME
    volumes:
      - ./pg_data/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isredy -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5
--------------------------------------------------
для локального запуска команды envsubst
в терминале PyCharm вводим команду 'type docker-compose-ci.yaml | envsubst > docker-compose-test.yaml'  # открываем
файл docker-compose-ci.yaml и отправляем его в команду envsubst и результат вывода перевести в файл
docker-compose-test.yaml, который создастся в корне проекта.
---------------------------
docker-compose-test.yaml

version: "3.9"

services:
  api:
    image: armenar/insta:-
    ports:
      - 80:80
    volumes:
      - ./docker_config.py:/code/default_config.py
    depends_on:
      pg:
        condition: service_healthy
      migrations:
        condition: service_completed_successfully
  migrations:
    image: armenar/insta:-
    volumes:
      - ./docker_config.py:/code/default_config.py
    depends_on:
       pg:
        condition: service_healthy
    command: flask db upgrade
  pg:
    image: postgres:latest
    environment:
      POSTGRES_USER:
      POSTGRES_PASSWORD:
      POSTGRES_DB:
    volumes:
      - ./pg_data/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isredy -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5
--------------------------------------------------
Заметим, что значения image: и для api и для migrations отсутствуют и значения POSTGRES_USER:, POSTGRES_PASSWORD и 
POSTGRES_DB также отсутствуют.  
"""
"""
p0XSPt1%
"""
"""
docker login -u armenar

dckr_pat_km8ZiSAzVnqdlWu4mvuLfPHcs5I
"""

