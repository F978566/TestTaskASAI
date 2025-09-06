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

1. Copy the example Odoo configuration file:
    cp conf/odoo.conf.example conf/odoo.conf

2. Open `conf/odoo.conf` and replace the placeholder variables with your actual values:
    [options]
    addons_path = /mnt/extra-addons,/usr/lib/python3/dist-packages/odoo/addons
    data_dir = /var/lib/odoo
    admin_passwd = your_admin_password
    db_host = postgres
    db_port = 5432
    db_user = your_db_user
    db_password = your_db_password

3. In your `.env` file, define the following variables:
    PostgreSQL
    POSTGRES_DB=odoo_db
    POSTGRES_USER=odoo_user
    POSTGRES_PASSWORD=strongpassword

    Odoo config values
    ODOO_ADMIN_PASSWD=your_admin_password
    ODOO_DB_HOST=postgres
    ODOO_DB_PORT=5432
    ODOO_DB_USER=odoo_user
    ODOO_DB_PASSWORD=strongpassword

Video demonstration - https://drive.google.com/file/d/1e6Iu_czNaeW_K3Eb5DIOeBNnd9bXnLyQ/view?usp=sharing