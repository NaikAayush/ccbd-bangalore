FROM ubuntu
RUN apt-get update && apt-get install -y --no-install-recommends \
    ssh \
    wget \
    curl \
    openjdk-8-jdk \
    && rm -rf /var/lib/apt/lists/*
RUN wget --no-verbose https://mirrors.estointernet.in/apache/hadoop/common/hadoop-3.1.3/hadoop-3.1.3.tar.gz
RUN tar -xzf hadoop-3.1.3.tar.gz 
RUN apt-get update && apt-get install -y python3 \
    && rm -rf /var/lib/apt/lists/*
ENV HADOOP_CONF_DIR=/hadoop-3.1.3/etc/hadoop
ENV HADOOP_MAPRED_HOME=/hadoop-3.1.3
ENV HADOOP_COMMON_HOME=/hadoop-3.1.3
ENV HADOOP_HDFS_HOME=/hadoop-3.1.3
ENV YARN_HOME=/hadoop-3.1.3
ENV PATH=$PATH:/hadoop-3.1.3/bin
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre

WORKDIR ccbd-bangalore
RUN apt-get update && apt-get install -y --no-install-recommends python3-pip && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
ADD *.csv ./
ADD static/ ./static
ADD *.py ./
ADD *.sh ./
ADD templates/ ./templates
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:$PORT app:app"]

