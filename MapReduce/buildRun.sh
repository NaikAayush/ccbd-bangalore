docker stop hadocker
docker rm hadocker
docker build -t hadocker .
docker run -ti -d -p 5000:5000 --name=hadocker hadocker
