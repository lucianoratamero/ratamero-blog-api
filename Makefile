# Makefile for building and deploying
#

NGINX=/etc/init.d/nginx

deploy: dependencies clean migrate minified_static_files

restart: $(NGINX)
	$(NGINX) restart

stop: $(NGINX)
	$(NGINX) stop

dependencies:
	pip install -r requirements.txt # Or requirements.txt

minified_static_files:
	python manage.py collectstatic # Collect into staticfiles/

migrate:
	python manage.py migrate

clean:
	@-rm -rf staticfiles/
	@-find ./ -name "*.pyc" -print0 | xargs -0 rm;
	@echo 'Successfully Cleaned!'

.PHONY: clean dependencies restart stop deploy
