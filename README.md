# Property Management Django Project

This README provides a comprehensive guide for Windows users to set up and run this Django-based property management application using Docker.

## Prerequisites

Before you begin, you will need to install Docker Desktop on your Windows machine.

### Install Docker Desktop for Windows

1.  **Download Docker Desktop:** Get the official installer from the [Docker website](https://www.docker.com/products/docker-desktop/).

2.  **Enable WSL 2:** Docker Desktop for Windows uses the Windows Subsystem for Linux 2 (WSL 2) as its backend. You will likely be prompted to enable this feature during the installation. Follow the on-screen instructions, which may require a system restart.

3.  **Start Docker Desktop:** Once installed, launch Docker Desktop from the Start Menu. You should see the Docker icon in your system tray. Make sure it indicates that Docker is running before you proceed.

## Project Setup

Follow these steps to configure and launch the application.

### 1. Create the Environment File

The project uses a `.env` file to manage environment variables for the database and other settings. You will need to create this file in the root of the project directory.

Environment  file named `.env` is already there u can edit it as u like:

```env
# PostgreSQL Database Settings
DB_HOST=db
DB_NAME=property_db
DB_USER=property_user
DB_PASSWORD=property@144

# Django Settings in settings.py
SECRET_KEY='django-insecure-un*zrsikhfy7d&$c9@(nka7)f703$=r2&=dh#q2!e8ae7ex_0r'
DEBUG=True

2. Build and Run the Docker Containers
Open your preferred terminal (PowerShell, Command Prompt, or Windows Terminal) in the root of the project directory and execute the following command:

docker-compose up --build

This command will:

Pull the necessary Docker images (python:3.11-slim and postgres:15).

Build the Django application container as defined in the Dockerfile.

Create and start the web (Django) and db (PostgreSQL) services as defined in docker-compose.yml.

Automatically apply database migrations and create a superuser on the initial startup.

You will see logs from both the Django application and the PostgreSQL database in your terminal.

Accessing the Application
Web Application: Once the containers are running, you can access the Django application by navigating to http://localhost:8000 in your web browser.

Admin Panel: The Django admin interface is available at http://localhost:8000/admin/.

Superuser Credentials
A default superuser is created for you based on the docker-compose.yml file. Use the following credentials to log in to the admin panel:

Username: admin

Password: property@144

Development
To run Django management commands, you can execute them inside the running web container.

Open a new terminal window.

Use the following command to get an interactive shell inside the web container:

docker-compose exec web /bin/bash

Now you can run standard Django manage.py commands, for example:

# Create a new superuser
python manage.py createsuperuser

# Create new database migrations if you change your models
python manage.py makemigrations

# Apply database migrations
python manage.py migrate

Stopping the Application
To stop the running Docker containers, press Ctrl + C in the terminal where docker-compose up is running.

To remove the containers and the network they use, run:

docker-compose down

To remove the containers and delete all database data, use the -v flag to remove the volume:

docker-compose down -v
