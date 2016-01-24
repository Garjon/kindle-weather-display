FROM garjon/alpine-nginx

COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/app.conf /etc/nginx/conf.d/app.conf
COPY nginx/.htpasswd /etc/nginx/.htpasswd

COPY src /data/www

EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"] 