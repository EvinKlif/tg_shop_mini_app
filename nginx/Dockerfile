FROM node:20 as builder

WORKDIR /app
COPY frontend/web-app/package.json frontend/web-app/package-lock.json ./
RUN npm ci
COPY frontend/web-app/. .
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/build /usr/share/nginx/html

# Создаем папку для Certbot
RUN mkdir -p /var/www/certbot

# Удаляем дефолтный конфиг
RUN rm -rf /etc/nginx/conf.d/default.conf

EXPOSE 80 443
CMD ["nginx", "-g", "daemon off;"]