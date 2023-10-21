FROM pywin-demo

WORKDIR /app
COPY . .
RUN chmod 777 -R .

RUN apt-get update -y
RUN python -m pip install --upgrade pip pywin32 cx_Freeze==6.8 importlib-metadata==4.8.1 setuptools==60.6.0

CMD python setup.py bdist --format=msi && mv dist/*Demo*.msi dist/DemoPywin.msi
