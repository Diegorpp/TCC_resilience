FROM python:3.10

RUN mkdir /app

COPY api.py /app

COPY requirements.txt /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8000
EXPOSE 80

# uvicorn main:app --reload
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "80"]

