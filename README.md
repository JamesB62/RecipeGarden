# 🥗 Recipe Garden

Developed using the Django framework, Recipe Garden is a web application that allows users to browse, create, manage, and search for recipes using keywords. The project aims to provide a central hub where food enthusiasts can share their favorite dishes.

## ✨ Features

- User registration and login
- Create, edit, and delete recipes
- Keyword search for recipes
- Categorised pages
- Responsive layout and styling

## 📸 Screenshots

<img width="1920" height="1505" alt="home-page" src="https://github.com/user-attachments/assets/373eda99-15d8-4da0-88e2-b9dcafc52627" /> 

<img width="1920" height="951" alt="recipe-page" src="https://github.com/user-attachments/assets/2a7f1483-cfcd-4044-be12-3196c34300f8" />

## ⚙️ Prerequisites

- VSCode
- Git
- GitHub CLI
- Python

## 📦 Installation

Inside a new VSCode terminal, follow these steps:

1. Clone the repository

git clone https://github.com/JamesB62/RecipeGarden.git

2. Navigate to the repository folder

cd RecipeGarden

3. Create a virtual environment

python -m venv venv

4. Activate the virtual environment

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

5. Install dependencies

pip install -r requirements.txt

6. Navigate to the project folder

cd recipeproject

6. Run migrations

python manage.py migrate

7. Start the application server

python manage.py runserver

## ▶️ Usage

- Enter http://127.0.0.1:8000 into your web browser's address bar
- Register a new account or log into an existing account
- Browse the available recipes or add your own to the collection
- Use the search bar to find specific dishes using keywords

## 🛠️ Developed Using

- Python
- Django
- HTML
- CSS
- Bootstrap

## 🚧 Future Improvements

- Add recipe ratings and reviews
- Improve search filtering
- Replace action complete pages with dismissible alert

## 🔐 Getting Started

Create an admin account with:

python manage.py createsuperuser
    
Then register a regular user through the site's sign-up page.

## 📃 Credits

Created by James Buchan | GitHub: https://github.com/JamesB62
