SERVICE_NAME=hello-world-printer
MY_DOCKER_NAME=$(SERVICE_NAME)
.PHONY: test deps test_ui test-api

deps:
	pip install -r requirements.txt; \
	pip install -r test_requirements.txt

lint:
	flake8 hello_world test test_xunit

test:
	PYTHONPATH=. py.test --verbose -s -v -m "not uitest"

test_cov:
	PYTHONPATH=. py.test --verbose -s --cov=. -v -m "not uitest"

test_xunit:
	PYTHONPATH=. py.test -s --cov=. --junit-xml=test_results.xml  -v -m "not uitest"

test_smoke:
	curl -I --fail 127.0.0.1:5000

test-api:
	python test-api/check_api.py

test_ui:
	PYTHONPATH=. py.test test_ui/test_ui.py

run:
	python main.py

docker_build:
	docker build -t $(MY_DOCKER_NAME) .

docker_run: docker_build
	docker run \
		--name hello-world-printer-dev \
	  -p 5000:5000 \
		-d $(MY_DOCKER_NAME)

USERNAME=akola2017
TAG=$(USERNAME)/$(MY_DOCKER_NAME)

docker_push: docker_build
	 		@docker login --username $(USERNAME) --password $${DOCKER_PASSWORD}; \
			docker tag hello-world-printer $(TAG); \
			docker push $(TAG); \
			docker logout;
