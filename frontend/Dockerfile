FROM node:18-alpine3.17
WORKDIR /app
COPY . .
RUN npm install
RUN npm run build

FROM nginx:1.25.2-alpine
WORKDIR /etc/nginx/conf.d
RUN rm -rf *
WORKDIR /app
COPY --from=0 /app/dist /app/dist
COPY --from=0 /app/server_configs/verum_frontend.conf /etc/nginx/conf.d

