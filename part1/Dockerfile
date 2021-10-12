FROM debian:buster-slim 

# Configure the version you want here for chrome and chromedriver
ARG CHROME_DRIVER_VERSION="94.0.4606.61"
ARG CHROME_VERSION="94.0.4606.81-1"

# Preinstall the tools needed for the job
RUN apt-get update \
    &&  apt-get install -y \
        python3-pip \
        wget \
        unzip

# Setup the registries for google
RUN echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' >> /etc/apt/sources.list.d/google.list \
    && wget https://dl.google.com/linux/linux_signing_key.pub \
    && apt-key add linux_signing_key.pub

# Install Chrome
RUN apt-get update \
    &&  apt-get install -y \
        google-chrome-stable=${CHROME_VERSION} \
    && apt-get clean

# Install Chrome Driver
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/${CHROME_DRIVER_VERSION}/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin

# copy our test files
COPY ./tests /tests

WORKDIR /tests

ENTRYPOINT [ "/tests/run.sh" ]