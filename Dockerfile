FROM python:3.6

# Install Debian Packages
RUN apt-get update && apt-get install -y \
    gunicorn

# Install Python Packages
RUN pip install --trusted-host pypi.python.org \
    django \
    gunicorn \
    sqlparse \
    
#    plotly \
#    pandas

# For AWS Cloud9 Development
EXPOSE 8080

# django default port
EXPOSE 8000

# Copy App Code
COPY . /home/
