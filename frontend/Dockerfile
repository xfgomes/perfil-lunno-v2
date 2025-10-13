# Etapa 1 - Build da aplicação React
FROM node:18-alpine AS build

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Etapa 2 - Servir o build via Nginx (será sobrescrito no Dokploy)
FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
