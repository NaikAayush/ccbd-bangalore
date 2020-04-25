FROM ubuntu
RUN apt-get update
RUN apt-get install ssh wget curl openjdk-8-jdk -y --no-install-recommends
RUN mkdir hadoop && cd hadoop
RUN wget https://mirrors.estointernet.in/apache/hadoop/common/hadoop-3.1.3/hadoop-3.1.3.tar.gz
RUN tar -xvzf hadoop-3.1.3.tar.gz 
ENV HADOOP_CONF_DIR=/hadoop-3.1.3/etc/hadoop
ENv HADOOP_MAPRED_HOME=/hadoop-3.1.3
ENV HADOOP_COMMON_HOME=/hadoop-3.1.3
ENV HADOOP_HDFS_HOME=/hadoop-3.1.3
ENV YARN_HOME=/hadoop-3.1.3
ENV PATH=$PATH:/hadoop-3.1.3/bin
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-armhf/jre

