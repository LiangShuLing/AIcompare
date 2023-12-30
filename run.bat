docker build -t liangshuling/aicompare .
#docker stop aicompare
#docker rm aicompare
docker run -p 5000:5000 --name aicompare liangshuling/aicompare