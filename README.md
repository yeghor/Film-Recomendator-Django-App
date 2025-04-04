# **Overview of Film Recomendator Django App**
This is web application written in Django. That allows users to get pretty accurate movie suggestion based on prompt.
This app uses **chromaDB vectorized database** that can vectorize movies data by:
- Title
- Overview
- Genre
- Release Date
- Key Words

And allows to make a query, and by using **chromaDB Embedding models** provide accurate results.

# **Features**
- Log in/Register/Logout
- Query to get movie suggestion by a prompt
- Top searches page
- Each user has his own search history
- Simple and nice Bootstrap5 design

# **Installation**

1. **Clone the repository:**
```bash
git clone https://github.com/yeghor/Film-Recomendator-Django-App.git
cd Learning-Log-Django
```
2. **Create a virtual enviroment:**
```bash
python -m venv venv

# On Windows
venv\Scripts\activate
# On MacOS/Linux
source venv/bin/activate
```

3. **Install the dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set up the database:**
```bash
python manage.py migrate
```

5. **Create a superuser:**
```bash
python manage.py createsuperuser
```

5. **Run the development server:**
```bash
python manage.py runserver
```

## Usage
- Navigate **to http://127.0.0.1:8000** in your web browser.
- Sign up for an account or log in.
- Open main page, and start making queries.
