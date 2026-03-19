# Recipe Garden

Recipe Garden is a recipe management web application built with Django. Users can browse recipes, create their own, edit existing ones, and search for dishes using keywords. The goal of the project is to provide a clean and simple way to organise and discover new recipes online.

## Features

- User registration and login
- Create, edit, and delete recipes
- Keyword search for recipes
- Categorised pages
- Responsive layout and styling

## Screenshots

Home Page  

<img width="1920" height="1505" alt="home-page" src="https://github.com/user-attachments/assets/373eda99-15d8-4da0-88e2-b9dcafc52627" />

Recipe Page  

<img width="1920" height="951" alt="recipe-page" src="https://github.com/user-attachments/assets/2a7f1483-cfcd-4044-be12-3196c34300f8" />

## Installation

Using GitHub CLI inside your prefered IDE, follow these steps:

1. Clone the repository

git clone https://github.com/JamesB62/L6SD_26T1_W7_Recipe_Project.git

2. Navigate to the project folder

cd recipeproject

3. Create a virtual environment

python -m venv venv

4. Activate the virtual environment

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

5. Install dependencies

pip install -r requirements.txt

6. Run migrations

python manage.py migrate

7. Start the development server

python manage.py runserver

## Usage

- Enter http://127.0.0.1:8000 into your web browser's address bar
- Register a new account or log into an existing account
- Browse the available recipes or add your own to the collection
- Use the search bar to find specific dishes using keywords

## Developed Using

- Python
- Django
- HTML
- CSS
- Bootstrap

## Future Improvements

- Add recipe ratings and reviews
- Improve search filtering

Created by James Buchan | GitHub: https://github.com/JamesB62
