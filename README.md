# NEEDTOBREATHE Fan Website

## Description

A website that lists all the recent albums from the band NEEDTOBREATHE.

## Setup

Follow the steps below to set up and run the project locally.

### Prerequisites

- [Python](https://www.python.org/downloads/) installed
- [Docker](https://docs.docker.com/get-docker/) installed (optional, for Docker deployment)

### Virtual Environment (Optional but recommended)

```bash
# Clone the repository
git clone https://github.com/your-username/needtobreathe-fan-website.git

# Navigate to the project directory
cd needtobreathe-fan-website

# Create a virtual environment (optional but recommended)
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate

# Install project dependencies
pip install -r requirements.txt

```
# Run migrations to set up the database
python manage.py migrate

# Start the development server
python manage.py runserver

# Creating a new super admin user
Make sure that you are in the root directory inside your venv before continuing

Once the app is running enter the following in your terminal: 
python manage.py createsuperuser 

You will be prompted with a username and password
You will now have access to add new users from the admin panel and remove other users. 
To gain access to the admin page - once on the homepage, at the end of the url add the following: /admin

# Build the Docker image
docker build -t needtobreathe-fan-website .

# Run the Docker container
docker run -p 8000:8000 needtobreathe-fan-website
