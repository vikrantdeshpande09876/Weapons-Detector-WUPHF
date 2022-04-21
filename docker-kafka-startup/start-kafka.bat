docker-compose rm -svf
docker-compose up

# docker exec -it kafka kafka-console-producer --broker-list localhost:9092 --topic REPORT_WEAPONS