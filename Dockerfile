FROM python:3

WORKDIR /app

COPY Market_API.py /app

RUN pip3 install flask
RUN pip3 install bs4
RUN pip3 install lxml

EXPOSE 5000

CMD ["python3","Market_API.py"]



