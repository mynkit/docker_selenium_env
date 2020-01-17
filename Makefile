run:
	docker-compose build
	docker-compose up -d

stop:
	docker stop scraping
	docker rm scraping
