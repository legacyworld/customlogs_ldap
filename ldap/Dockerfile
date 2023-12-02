FROM osixia/openldap
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 0E98404D386FA1D9
RUN apt-get update && apt-get install -y rsyslog
COPY user.ldif /container/service/slapd/assets/config/bootstrap/ldif/custom
COPY logging.ldif /container/service/slapd/assets/config/bootstrap/ldif/custom
COPY rsyslog.conf /etc
