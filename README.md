🏡 Django Property Management System
A robust and scalable property management application built with Django and containerized with Docker for easy setup and deployment.

This project provides a complete environment for managing properties, tenants, and leases, all running inside Docker containers. This guide provides all the necessary steps for Windows users to get the project up and running.

Prerequisites
Before you begin, ensure you have Docker Desktop installed on your Windows machine.

Download Docker Desktop: Get the official installer from the Docker website.

Enable WSL 2: Docker Desktop for Windows uses the Windows Subsystem for Linux 2 (WSL 2). You will be prompted to enable this during installation. Follow the on-screen instructions, which may require a system restart.

Start Docker Desktop: Launch Docker Desktop from the Start Menu. Wait for the Docker icon in your system tray to turn green, indicating that it's running.

🚀 Getting Started
Follow these steps to configure and launch the application.

1. Clone the Repository
First, clone this repository to your local machine.

git clone <your-repository-url>
cd <repository-directory>

2. Configure the Environment
The project uses a .env file to manage sensitive information and configuration variables. An example is provided in the repository.

Create a .env file in the project root and copy the contents from the example. You can modify these values if needed.

# PostgreSQL Database Settings
DB_HOST=db
DB_NAME=property_db
DB_USER=property_user
DB_PASSWORD=your_secure_password_here

# Django Settings
SECRET_KEY='your_strong_django_secret_key'
DEBUG=True

3. Build and Run the Docker Containers
Open your terminal (PowerShell, Command Prompt, or Windows Terminal) in the project's root directory and run the following command:

docker-compose up --build

This command will:

Pull the python:3.11-slim and postgres:15 images.

Build the Django application container.

Start the web (Django) and db (PostgreSQL) services.

You will see logs from both services in your terminal. Once you see a message indicating the development server is running, you're ready to go!

Accessing the Application
🌐 Web Application: Navigate to http://localhost:8000 in your browser.

⚙️ Admin Panel: Access the Django admin interface at http://localhost:8000/admin/.

🛠️ Development & Management
To run Django management commands, you need to execute them inside the running web container.

Open a new terminal window.

Get an interactive shell inside the web container:

docker-compose exec web /bin/bash

Now you can run standard manage.py commands.

Create a Superuser
To access the admin panel, you'll need a superuser account.

python manage.py createsuperuser

Follow the prompts to set up your admin username, email, and password.

Other Commands
# Create new database migrations if you change your models
python manage.py makemigrations

# Apply database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic

🛑 Stopping the Application
To stop the running containers, press Ctrl + C in the terminal where docker-compose up is running.

To stop and remove the containers and network, run:

docker-compose down

To stop, remove containers, and delete all database data (use with caution), run:

docker-compose down -v
