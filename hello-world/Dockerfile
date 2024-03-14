# Use python:slim as the base image
FROM python:slim

# Change the user to root so that I don't need to use sudo
USER root

# Copy the hello-world.py script to the working directory
COPY hello_world.py /

# Install the mlflow package
RUN pip install mlflow

# I think I need to use ADD instead of COPY 
ADD start.sh /
RUN chmod +x /start.sh

# Set bash as the default shell
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
# Run the start.sh script using the bash shell
CMD ["/start.sh"]
