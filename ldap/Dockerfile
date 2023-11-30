FROM osixia/openldap

#ドメイン
#ENV LDAP_DOMAIN=example.com
#管理者パスワード
#ENV LDAP_ADMIN_PASSWORD=password
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 0E98404D386FA1D9
RUN apt-get update && apt-get install -y rsyslog
#COPY 90-ldap.conf /etc/rsyslog.d/
# ユーザーデータを作成するためのLDIFファイルをコンテナにコピー（構築時にユーザーデータを登録しないなら不要）
COPY user.ldif /container/service/slapd/assets/config/bootstrap/ldif/custom
COPY logging.ldif /container/service/slapd/assets/config/bootstrap/ldif/custom
COPY rsyslog.conf /etc
