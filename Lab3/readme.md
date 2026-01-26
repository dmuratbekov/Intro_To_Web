# Lab 3

## Python Installation Guide with Virtual Environments (venv)
In this laboratory work, I verified the existing Python installation and worked with virtual environments using the `venv` module.  
The main focus of this work was to isolate project dependencies and run Python scripts inside a virtual environment.

---

## Virtual Environment Setup
### Creating a Virtual Environment

A new project directory was created, and a virtual environment was initialized using the venv module:
```bash
python -m venv venv
```
As a result, a venv directory was created inside the project folder.

### Activating the Virtual Environment

The virtual environment was activated successfully.
- On Windows:
```bash
venv\Scripts\activate
```
- On macOS / Linux:
```bash
source venv/bin/activate
```

To deactivate the Virtual Environment use:
```bash
deactivate
```

---

## Installing Dependencies

Inside the active virtual environment, external libraries were installed using pip.
The requests library was installed successfully:
```bash
pip install requests
```

---

## Working with Libraries
### Script Creation

I created a Python script (main.py) to test installed libraries.
The script used:
- requests for sending HTTP requests
- json for processing JSON data

### Running the Script
The script was executed inside the virtual environment:
```bash
python main.py
```

---

## Notes

- Virtual environments were used to isolate project dependencies
- The requests library was installed only inside the virtual environment