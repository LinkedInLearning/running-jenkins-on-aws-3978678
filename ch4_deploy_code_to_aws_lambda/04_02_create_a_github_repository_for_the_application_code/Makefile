CODE=$(shell ls *.py)

ifneq (,$(findstring -staging,$(FUNCTION)))
	ENVIRONMENT = STAGING
else ifneq (,$(findstring -production,$(FUNCTION)))
	ENVIRONMENT = PRODUCTION
else
	ENVIRONMENT = undefined
endif

hello:
	@echo "Here are the targets for this Makefile:"
	@echo "  requirements   - install the project requirements"
	@echo "  lint           - run linters on the code"
	@echo "  black          - run black to format the code"
	@echo "  test           - run the tests"
	@echo "  build          - build the lambda.zip file"
	@echo "  deploy         - deploy the lambda.zip file to AWS"
	@echo "  testdeployment - test the deployment"
	@echo "  clean          - remove the lambda.zip file"
	@echo "  all            - clean, lint, black, test, build, and deploy"
	@echo
	@echo
	@echo "You must set the FUNCTION variables to use the deploy target."
	@echo "FUNCTION must be set to the name of an existing lambda function to update."
	@echo "For example:"
	@echo
	@echo "  make deploy FUNCTION=sample-application-staging"
	@echo
	@echo "Optional deploy variables are:"
	@echo "  VERSION       - the version of the code being deployed (default: undefined)"
	@echo "  BUILD_TAG     - the tag assigned by the deployment platform (default: undefined)"
	@echo "  BUILD_NUMBER  - the build number assigned by the deployment platform (default: undefined)"
	@echo "  URL           - the URL to use for testing the deployment (default: undefined)"
	@echo

requirements:
	pip install -U pip
	pip install --requirement requirements.txt

check:
	set
	zip --version
	python --version
	pylint --version
	flake8 --version
	aws --version

lint:
	pylint --exit-zero --errors-only --disable=C0301 --disable=C0326 --disable=R,C $(CODE)
	flake8 --exit-zero --ignore=E501,E231 $(CODE)
	black --diff $(CODE)
	isort --check-only --diff $(CODE)

fmt:
	black $(CODE)
	isort $(CODE)

test:
	python -m unittest -v index_test

build:
	zip lambda.zip index.py data.json template.html

deploy:
	@echo
	aws sts get-caller-identity

	@echo
	aws lambda wait function-active \
		--region=$(REGION) \
		--function-name="$(FUNCTION)"

	@echo
	aws lambda update-function-configuration \
		--region=$(REGION) \
		--function-name="$(FUNCTION)" \
		--environment "Variables={BUILD_TAG=$(BUILD_TAG),VERSION=$(VERSION),BUILD_NUMBER=$(BUILD_NUMBER),ENVIRONMENT=$(ENVIRONMENT)}"

	@echo
	aws lambda wait function-updated \
		--region=$(REGION) \
		--function-name="$(FUNCTION)"

	@echo
	aws lambda update-function-code \
		--region=$(REGION) \
		--function-name="$(FUNCTION)" \
	 	--zip-file=fileb://lambda.zip

	@echo
	aws lambda wait function-updated \
		--region=$(REGION) \
		--function-name="$(FUNCTION)"

testdeployment:
	curl -s $(URL) | grep $(VERSION)

clean:
	rm -vf lambda.zip

all: requirements clean lint test build deploy

.PHONY: test build deploy all clean
