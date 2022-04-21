FROM ubuntu:latest

# Install linux packages
RUN apt update
RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt install -y tzdata
RUN apt install -y python3-pip git zip curl htop screen libgl1-mesa-glx libglib2.0-0
RUN alias python=python3

# Create working directory
COPY . .

# Install python dependencies
RUN python3 -m pip install --upgrade pip
RUN pip install --no-cache -r requirements.txt

EXPOSE 5009

WORKDIR /weapons-detector-yolo

#CMD ["gunicorn", "--workers=2", "--bind=0.0.0.0:5016", "app:app"]
CMD ["python3", "app.py"]