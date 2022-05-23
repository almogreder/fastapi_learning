# Dockerfile,Image, Container
FROM python:3.9.12

ADD countries_api.py . 
add countries.json .

RUN pip install fastapi typing pydantic uvicorn

CMD ["python", "./countries_api.py"]