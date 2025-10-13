# ===============================
# Etapa 1 - Build da aplicação (Vite)
# ===============================
FROM node:18-alpine AS build

WORKDIR /app

# Copia arquivos de dependências e instala
COPY package*.json ./
RUN npm ci || npm install

# Copia o restante do código e gera o build
COPY . .
RUN npm run build

# ===============================
# Etapa 2 - Servir via Nginx
# ===============================
FROM nginx:alpine

# Copia o build Vite para o Nginx
COPY --from=build /app/dist /usr/share/nginx/html

# Gera o arquivo de configuração correto (default.conf)
RUN printf 'server {\n\
    listen 80;\n\
    root /usr/share/nginx/html;\n\
    index index.html;\n\
    location / {\n\
        try_files $uri /index.html;\n\
    }\n\
}\n' > /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
