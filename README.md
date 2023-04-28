# PlayerApi instructions:

Requirements:
```
Python version 3.10.2
Create a venv in the working directory
pip install sqlalchemy fastapi uvicorn
```
To run the server: 
```
uvicorn app.main:app --reload
```
When the server is up you can test out the endpoints by opening http://localhost:8000/docs