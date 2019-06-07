FROM python:3.6

# Install Debian Packages
RUN apt-get update && apt-get install -y \
    gunicorn

# Install Python Packages
RUN pip install --trusted-host pypi.python.org \
    Django==2.2.1 \
    django-mysql==3.1.0 \
    gunicorn==19.9.0 \
    sqlparse==0.3.0 \
    mysqlclient \
    plotly \
    numpy \
    scipy
#    pandas

# For AWS Cloud9 Development
EXPOSE 8080

# django default port
EXPOSE 8000

# Copy App Code
COPY . /home/