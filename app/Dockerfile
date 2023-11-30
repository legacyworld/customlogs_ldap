FROM python:bullseye
USER root
RUN apt-get update && apt-get install -y libsasl2-dev python-dev libldap2-dev libssl-dev
RUN pip3 install werkzeug==2.3.0 Flask-Login Flask-WTF python-ldap flask flask_ldap3_login playwright
RUN playwright install
RUN playwright install-deps
WORKDIR /src
ENV PYTHONUNBUFFERED=1
ENTRYPOINT ["python", "-u", "app.py"]
