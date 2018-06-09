# Makefile for building and deploying
#

NGINX=/etc/init.d/nginx

deploy: dependencies clean minified_static_files restart

restart: $(NGINX)
	$(NGINX) restart

stop: $(NGINX)
	$(NGINX) stop

dependencies:
	pip install -r requirements.txt # Or requirements.txt

minified_static_files:
	python manage.py collectstatic # Collect into staticfiles/

clean:
	@-rm -rf staticfiles/
	@-find . -name '__pycache__' -exec /bin/rm -rf {} ;
	@echo 'Successfully Cleaned!'

.PHONY: clean dependencies restart stop deploy
