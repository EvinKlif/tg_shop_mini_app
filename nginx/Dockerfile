FROM node:20 as builder

WORKDIR /app
COPY frontend/web-app/package.json frontend/web-app/package-lock.json ./
RUN npm ci
COPY frontend/web-app/. .
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/build /usr/share/nginx/html
RUN mkdir -p /var/www/certbot && \
    rm -rf /etc/nginx/conf.d/default.conf  # Удаляем дефолтный конфиг
EXPOSE 80 443
CMD ["nginx", "-g", "daemon off;"]
