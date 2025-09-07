# АСАИ – Тестовое задание – АРМ

---
### Prerequisites
- Установленный Docker на вашей системе  
- Установленный Docker Compose  
- Действительный файл `.env` с необходимыми переменными окружения  
---
### Configuration
1. Скопируйте пример файла конфигурации Odoo:<br>
    cp conf/odoo.conf.example conf/odoo.conf
2. Откройте файл `conf/odoo.conf` и замените переменные-заглушки на ваши актуальные значения:<br>
    [options]<br>
    addons_path = /mnt/extra-addons,/usr/lib/python3/dist-packages/odoo/addons<br>
    data_dir = /var/lib/odoo<br>
    admin_passwd = ваш_пароль_администратора<br>
    db_host = postgres<br>
    db_port = 5432<br>
    db_user = ваш_пользователь_базы_данных<br>
    db_password = ваш_пароль_базы_данных<br>
3. В файле `.env` определите следующие переменные:<br>
    #### PostgreSQL<br>
    POSTGRES_DB=odoo_db<br>
    POSTGRES_USER=odoo_user<br>
    POSTGRES_PASSWORD=сильный_пароль<br>

    #### Odoo config values<br>
    ODOO_ADMIN_PASSWD=ваш_пароль_администратора<br>
    ODOO_DB_HOST=postgres<br>
    ODOO_DB_PORT=5432<br>
    ODOO_DB_USER=odoo_user<br>
    ODOO_DB_PASSWORD=сильный_пароль<br>

### Проделанная работа

#### Уровень сложности - medium

1. АРМ с минимальным уровнем интерактивности, можно отмечать задания выполненными.
2. Реализован интерфейс АРМ и логика работы с заданиями.
3. Взаимодействие с заданиями полноценно функционирует, кнопки работают.
4. Указание брака - оператор может пометить любую деталь как брак с указанием причины.

### Запустите приложение
```docker compose up```<br>



Видео демонстрация - [https://drive.google.com/file/d/1e6Iu_czNaeW_K3Eb5DIOeBNnd9bXnLyQ/view?usp=sharing](https://drive.google.com/file/d/1e6Iu_czNaeW_K3Eb5DIOeBNnd9bXnLyQ/view?usp=sharing)
