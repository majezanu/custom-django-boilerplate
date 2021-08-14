FROM python:3.8
ENV PYTHONUNBUFFERED=1

# The working directory in the container
WORKDIR /usr/src/app

# Get the project dependences
COPY requirements ./requirements
COPY requirements.txt ./
RUN pip install -r requirements.txt

RUN adduser user
RUN chown user:user -R /usr/src/app
RUN chmod +x /usr/src/app
USER user

# Expose the 8000 default development port
EXPOSE 8000