NAMES=LECOCQ-ALEXIS_CHEN-WU-DA
ZIP_FILE="../$(NAMES).zip"
DB_FILE=test_db.db

clean:
	find . -name "*.pyc" -delete
	if [ -e $(DB_FILE) ]; then rm $(DB_FILE); fi
zip: clean
	if [ -e $(ZIP_FILE) ]; then rm $(ZIP_FILE); fi
	zip -r $(ZIP_FILE) . --quiet
