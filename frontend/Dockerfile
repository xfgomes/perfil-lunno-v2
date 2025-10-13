# ===============================
# Etapa 1 - Build do frontend (Vite)
# ===============================
FROM node:18-alpine AS build

# Define diretório de trabalho
WORKDIR /app

# Copia arquivos de dependências e instala
COPY package*.json ./
RUN npm install

# Copia o restante do código e gera o build
COPY . .
RUN npm run build

# ===============================
# Etapa 2 - Servidor Nginx para o build
# ===============================
FROM nginx:alpine

# Copia o build do Vite para a pasta servida pelo Nginx
COPY --from=build /app/dist /usr/share/nginx/html

# (Opcional) Copia configuração customizada do nginx, se houver
# COPY nginx.conf /etc/nginx/conf.d/default.conf

# Porta padrão HTTP
EXPOSE 80

# Inicia o Nginx
CMD ["nginx", "-g", "daemon off;"]
