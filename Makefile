NAMES=LECOCQ-ALEXIS_DA-CHEN-WU
ZIP_FILE="../$(NAMES).zip"

clean:
	find . -name "*.pyc" -delete
zip: clean
	if [ -e $(ZIP_FILE) ]; then rm $(ZIP_FILE); fi
	zip -r $(ZIP_FILE) . --quiet
test:
	python test.py
