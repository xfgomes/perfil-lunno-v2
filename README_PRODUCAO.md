# Perfil Lunno HUBX — Monorepo (Produção com Dokploy)

Monorepo com **Backend (Flask/Python)**, **Frontend (React/Tailwind/Chart.js)**, **PostgreSQL** e **Nginx**.
CI/CD com **GitHub Actions** + deploy automático no **Dokploy**.

## Como usar (resumo)
1. Faça upload deste repositório no GitHub (nome recomendado: `perfil-lunno-hubx`).  
2. Em **Settings → Secrets and variables → Actions**, adicione (uma das opções):
   - `DOKPLOY_WEBHOOK_URL` (Webhook de Auto Deploy) **OU**
   - `DOKPLOY_API_URL`, `DOKPLOY_API_KEY`, `DOKPLOY_APP_ID` (API do Dokploy)
3. Copie `.env.example` para `.env` e preencha credenciais (OpenAI, Banco, JWT).  
4. No **Dokploy**: crie a App (Compose) importando `dokploy.yml`, cole `.env` em *Environment*, aponte o **domínio** para o serviço `nginx` e habilite HTTPS.  
5. Faça **push na `main`** → o pipeline compila imagens (backend + frontend), publica no GHCR e dispara o deploy.

## Pastas
- `backend/` — API Flask + engine psicométrico + endpoints de scoring e relatórios
- `frontend/` — painel React (tema **claro minimalista corporativo**)
- `nginx/` — proxy para `/api` e arquivos estáticos
- `.github/workflows/deploy.yml` — CI/CD (build & deploy)
- `docker-compose.prod.yml` — Compose de produção
- `dokploy.yml` — definição para o Dokploy
- `.env.example` — variáveis de ambiente de produção

Boa instalação! 🚀
