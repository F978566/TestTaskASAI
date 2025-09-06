# Odoo Docker Setup

This repository contains the configuration needed to run **Odoo** with **PostgreSQL** using Docker Compose.  

The setup allows you to run Odoo in a containerized environment with persistent volumes for configuration, data, and custom modules.

---

### Prerequisites
- Docker installed on your system  
- Docker Compose installed  
- A valid `.env` file with the required environment variables  

---

### Configuration

1. Copy the example Odoo configuration file:<br>
    cp conf/odoo.conf.example conf/odoo.conf

2. Open `conf/odoo.conf` and replace the placeholder variables with your actual values:<br>
    [options]<br>
    addons_path = /mnt/extra-addons,/usr/lib/python3/dist-packages/odoo/addons<br>
    data_dir = /var/lib/odoo<br>
    admin_passwd = your_admin_password<br>
    db_host = postgres<br>
    db_port = 5432<br>
    db_user = your_db_user<br>
    db_password = your_db_password<br>

3. In your `.env` file, define the following variables:<br>
    PostgreSQL<br>
    POSTGRES_DB=odoo_db<br>
    POSTGRES_USER=odoo_user<br>
    POSTGRES_PASSWORD=strongpassword<br>

    Odoo config values<br>
    ODOO_ADMIN_PASSWD=your_admin_password<br>
    ODOO_DB_HOST=postgres<br>
    ODOO_DB_PORT=5432<br>
    ODOO_DB_USER=odoo_user<br>
    ODOO_DB_PASSWORD=strongpassword<br>

### Running the Application
```docker compose up```

Video demonstration - https://drive.google.com/file/d/1e6Iu_czNaeW_K3Eb5DIOeBNnd9bXnLyQ/view?usp=sharing
