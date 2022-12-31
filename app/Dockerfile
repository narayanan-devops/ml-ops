#Multi stage and using first stage to download the models.
FROM ubuntu:latest as download-model

## setup git lfs and download the models as a seperate build step
RUN \
  apt-get update && \
  apt-get install -y sudo curl git && \
  curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash
RUN sudo apt-get install git-lfs=3.3.0 -y
RUN git lfs install
RUN git clone https://huggingface.co/facebook/m2m100_418M /tmp/model/m2m100_418M
RUN rm -rf /tmp/model/m2m100_418M/.git


# Actual Container for Running
FROM python:3.9-slim

## Best practices for python docker container
## Stop writing byte code(pyc file), Non Buffering streams

ENV PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1 \
  PIP_NO_CACHE_DIR=on \
  PIP_DISABLE_PIP_VERSION_CHECK=on

#Setup directories for app and models
WORKDIR /app
ENV MODELS_DIR="/app/models"


# Creates a non-root user with an explicit UID and adds permission to access the /app folder
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# Copy script and files
COPY . /app

# Copy the models downloaded in the previous download stage
RUN mkdir -p ${MODELS_DIR}
COPY --from=download-model /tmp/model ${MODELS_DIR}

#install deps
RUN python -m pip install -r requirements.txt

#add new python bin path to PATH ENV variable as run under appuser user
ENV PATH="${PATH}:/home/appuser/.local/bin"

#Expose the port
EXPOSE 9527

#start the server
CMD ["uvicorn","main:app","--host=0.0.0.0", "--port=9527"]