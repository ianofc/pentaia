# 🌌 PentaIA — Ecossistema de Inteligência & Segurança (LYV)

<div align="center">

**Um ecossistema avançado de microsserviços para distribuição de dados em tempo real, inteligência de tendências e segurança estrutural.**

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)

</div>

---

## 📖 Sumário

- [Visão Geral](#-visão-geral)
- [Os 5 Pilares do Ecossistema](#-os-5-pilares-do-ecossistema)
  - [Heimdall (Segurança)](#1-heimdall-segurança)
  - [Mercurio (Hub de Distribuição)](#2-mercurio-hub-de-distribuição)
  - [Iris (Extração e Varredura)](#3-iris-extração-e-varredura)
  - [Tas (Tendências e Recomendações)](#4-tas-tendências-e-recomendações)
  - [Zios (Monitoramento Proativo)](#5-zios-monitoramento-proativo)
- [Arquitetura & Tecnologias](#-arquitetura--tecnologias)
- [Estrutura de Pastas](#-estrutura-de-pastas)
- [Como Executar Localmente](#-como-executar-localmente)
- [Diretrizes de Manutenção do Projeto](#-diretrizes-de-manutenção-do-projeto)

---

## 🌟 Visão Geral

O **PentaIA** (também conhecido como ecossistema **LYV**) é uma arquitetura de microsserviços escalável desenvolvida pelo **IO Santos Group**. 

Ele foi projetado para atuar como uma infraestrutura centralizada que orquestra a coleta de dados externos, análise de tendências, distribuição de eventos em tempo real e segurança robusta "secure-by-default". O nome "Penta" faz referência aos seus 5 nós principais que operam em conjunto para entregar inteligência contínua com baixa latência e alta tolerância a falhas.

---

## 🚀 Os 5 Pilares do Ecossistema

### 1. 🛡️ Heimdall (Segurança)
A fundação de segurança do ecossistema. Funciona como um middleware plugável (FastAPI/Starlette) que protege e audita todos os acessos.
- **Controle de Acesso:** Login/registro e validação de tokens.
- **Defesa Ativa:** Rate limiter de janela deslizante e bloqueio de IPs/redes suspeitas.
- **Auditoria e Privacidade:** Log de eventos com mascaramento automático de dados sensíveis.
- **Telemetria:** Endpoints de saúde e status de integridade.

### 2. 🛰️ Mercurio (Hub de Distribuição)
O serviço de ponte e distribuição de dados em tempo real.
- **Bundles Dinâmicos:** Consolida dados de múltiplas fontes (ZIOS, TAS, IRIS) para entrega otimizada aos clientes.
- **Broadcasting:** Roteamento de eventos e fallback automático caso serviços adjacentes falhem.
- **Integração de Segurança:** Consulta constante de integridade junto ao Heimdall e Zios.

### 3. 👁️ Iris (Extração e Varredura)
O motor de coleta de dados e *scrapping*.
- **Varreduras:** Busca de dados estruturados e não-estruturados externos.
- **Integrações Específicas:** Inclui a API de Notícias do G1, utilizando Selenium e web scraping em Python.

### 4. 📈 Tas (Tendências e Recomendações)
O motor analítico para recomendação.
- **Tendências:** Processa os dados recebidos para extrair tópicos em alta, hashtags e volume de discussões.
- **Sinergia:** O Mercurio consome ativamente a API do Tas (`/api/v1/recommend/trends`) para enriquecer a experiência do usuário.

### 5. ⚙️ Zios (Monitoramento Proativo)
O cérebro backend focado em operação inteligente e estabilidade.
- Trabalha ao lado do Heimdall (através de rotas como `/v1/proactive/heimdall/check`) para garantir que tudo opere dentro das políticas de segurança.
- Gerencia o processamento mais pesado de inteligência do ecossistema.

---

## 🛠️ Arquitetura & Tecnologias

A stack centraliza Python moderno para IA, velocidade e segurança.

- **Backend Core:** Python 3.11+
- **Framework Web:** FastAPI (com uvicorn e Starlette)
- **Scraping / Crawling:** Selenium, Beautiful Soup 4, Requests
- **Segurança:** Políticas de Redação de Logs, Rate Limiting nativo
- **Infraestrutura:** Docker e Docker Compose para orquestração local

---

## 📁 Estrutura de Pastas

```text
pentaia/
├── heimdall/             # Core de Segurança e Middleware
├── iris/                 # Motor de Scraping (ex: Notícias G1)
├── mercurio/             # Hub de Distribuição (API Gateway / Bridge)
├── tas/                  # Motor de Recomendações e Trends
└── zios/                 # Backend de Monitoramento e Lógica de IA
```

---

## 💻 Como Executar Localmente

### Pré-requisitos

- [Docker](https://www.docker.com/) e Docker Compose
- [Python 3.11+](https://www.python.org/)

### Executando com Docker Compose (Recomendado)

Cada microsserviço possui configurações para ser executado via container. Para levantar todo o ecossistema ou um nó específico (ex: Mercurio):

```bash
docker-compose up --build
```
*(Consulte os READMEs individuais de cada pasta para comandos específicos, como `docker compose up --build mercurio` ou executar a API do Iris localmente).*

---

## 📌 Diretrizes de Manutenção do Projeto

> [!IMPORTANT]
> **Arquitetura Desacoplada:**
> Cada microsserviço (Heimdall, Iris, Mercurio, Tas, Zios) deve manter sua independência funcional. Modificações nos contratos de API devem ser comunicadas a todos os nós que dependem da informação, especialmente ao **Mercurio**, que atua como o agregador central.

---

<div align="center">
Desenvolvido por <b>IO Santos Group</b> para o ecossistema <b>LYV</b>.
</div>
