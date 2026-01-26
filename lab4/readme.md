# Lab 4
##  Creating Flask Application
In this laboratory work, I created my first web application using the Flask framework.  
The main objective was to set up a Flask project, configure a virtual environment, run a local web server, and implement basic routes and HTML templates.

---

## Project Setup
I created a new project for the Flask application.
I installed Flask using 'pip'.

---

## Structure

```
lab4/
├── templates
│   └──hello.html
├── venv/
├── app.py
└── requirements.txt
```

---

## Application Creation
The main application logic was implemented in the `app.py` file.

The Flask application was created and configured with basic routes:
- A root route (`/`) that returns a simple text response
- A dynamic route (`/hello/<name>`) that accepts a parameter and displays a personalized message

---

## Running the Application
You can run the application using the Python interpreter:
```bash
python app.py
```

After running, the Flask development server ran locally at:
```cpp
http://127.0.0.1:5000
```

## Notes
- Flask was installed inside a virtual environment
- The application was tested locally