

## bash
sudo apt install apache2=2.4.52*
sudo apt install libnghttp2-dev

sudo a2enmod ssl
sudo a2enmod http2
sudo a2ensite default-ssl
sudo ufw allow 80/tcp
sudo ufw allow 8080/tcp

sudo systemctl restart apache2

sudo vi /etc/apache2/sites-available/default-ssl.conf
<IfModule mod_ssl.c>
    <VirtualHost _default_:443>
        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html

        SSLEngine on
        SSLCertificateFile /etc/ssl/certs/apache-selfsigned.crt
        SSLCertificateKeyFile /etc/ssl/private/apache-selfsigned.key

        <FilesMatch "\.(cgi|shtml|phtml|php)$">
            SSLOptions +StdEnvVars
        </FilesMatch>
        <Directory /usr/lib/cgi-bin>
            SSLOptions +StdEnvVars
        </Directory>

        Protocols h2 http/1.1

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
    </VirtualHost>
</IfModule>

sudo systemctl restart apache2

sudo vi /etc/apache2/apache2.conf
LimitRequestFieldSize 16384
LimitRequestFields 1000

