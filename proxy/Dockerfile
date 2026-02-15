FROM nginx:stable-alpine

RUN rm /etc/nginx/conf.d/default.conf

COPY default.conf /etc/nginx/conf.d/default.conf

RUN mkdir -p /var/log/nginx/aedis
RUN chown -R nginx:nginx /var/log/nginx/aedis

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
