# Install requirements
init:
	cd de; pip install -r requirements.txt
# start docker container
up:
	cd de; docker-compose up -d
# command stops docker container
down:
	cd de; docker-compose down
# command add data to minio bucket
add:
	python3 de/de.py --name_bucket={name_bucket}
