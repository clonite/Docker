#lightweight image file
FROM alpine:latest 

#installing python
RUN apk update && apk add python3

# Create the required directories
RUN mkdir /home/data && mkdir /home/output

# moving file to 
COPY base.py /home

# Set the working directory to /home
WORKDIR /home

# command to run base.py
CMD ["python3", "base.py"]