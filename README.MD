From:
http://www.mpetroff.net/archives/2012/09/14/kindle-weather-display/

A .htpasswd file must be generated before using the system.

The easiest way to generate this is to install 'apache2-utils' and run the following command:

```
htpasswd -c ./kindle-image-server/secure/.htpasswd <username>
```