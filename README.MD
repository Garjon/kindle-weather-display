![License MIT][1]

### What's this all about?
This is a basic weather dashboard that plays nicely with the Kindle experimental browser. Making use of the beautiful e-ink display, this dashboard can help bring that much needed weather information to you in a crisp and easy to read form!

### Usage
Out of the box, the server endpoint has basic auth turned on. If you also wish to use this, you will need to generate a .htpasswd file. The file should be added to the `./kindle-image-server/nginx/.htpasswd` location.

The easiest way to generate this is to install 'apache2-utils' and run the following command:

```
htpasswd -c ./kindle-image-server/secure/.htpasswd <username>
```

The location is hard coded using latitude and longitude coordinates, you'll need to point those at somewhere near you to get weather updates that you care about.

Open the `./kindle-image-generator/weather-script.py` file for editing and replace `longitude` and `latitude` values with ones near you.

### Attribution
This didn't all magically come out of my own head, some "smarter than I" individuals have helped me put this together:

* [Kindle Weather Display][2] by [Matthew Petroff][3]

[1]: https://img.shields.io/badge/license-MIT-blue.svg
[2]: http://www.mpetroff.net/archives/2012/09/14/kindle-weather-display/
[3]: https://mpetroff.net/