# Makefile for building and deploying
#

NGINX=/etc/init.d/nginx

deploy: dependencies clean migrate minified_static_files

restart: $(NGINX)
	$(NGINX) restart
	systemctl restart gunicorn

stop: $(NGINX)
	$(NGINX) stop

dependencies:
	pip install -r requirements.txt

minified_static_files:
	python manage.py collectstatic
	@-mv staticfiles/ /tmp/ratamero-blog-api/

migrate:
	python manage.py migrate

clean:
	@-rm -rf /tmp/ratamero-blog-api/
	@-find ./ -name "*.pyc" -print0 | xargs -0 rm;
	@echo 'Successfully Cleaned!'

.PHONY: clean dependencies restart stop deploy
