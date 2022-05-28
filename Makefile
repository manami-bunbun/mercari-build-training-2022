# Task runner

.PHONEY: install
install:
	cd python && pip install -r requirements.txt
	cd typescript/simple-mercari-web && npm ci

.PHONEY: be
be:
	cd python && uvicorn main:app --reload --port 9000

.PHONEY: fe
fe:
	cd typescript/simple-mercari-web && npm run start
