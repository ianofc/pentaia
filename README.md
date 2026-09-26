# 🌿 Craft Horta — Jogo de Agroecologia & Painel Pedagógico Escolar

<div align="center">

![Craft Horta Banner](https://raw.githubusercontent.com/shadcn-ui/ui/main/apps/www/public/og.jpg)

**Uma plataforma gamificada no estilo pixel-art (Minecraft & Mario Bros) para ensino prático e interdisciplinar de Agroecologia, Sustentabilidade e Gestão de Hortas Escolares.**

[![React](https://img.shields.io/badge/React-19-61DAFB?logo=react&logoColor=black)](https://react.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.8-3178C6?logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![TanStack Router](https://img.shields.io/badge/TanStack-Router%20%26%20Start-FF4154?logo=tanstack&logoColor=white)](https://tanstack.com/router)
[![Tailwind CSS v4](https://img.shields.io/badge/Tailwind_CSS-v4.2-06B6D4?logo=tailwindcss&logoColor=white)](https://tailwindcss.com/)
[![Supabase](https://img.shields.io/badge/Supabase-Database%20%26%20Auth-3FCF8E?logo=supabase&logoColor=white)](https://supabase.com/)
[![Vite](https://img.shields.io/badge/Vite-8.1-646CFF?logo=vite&logoColor=white)](https://vitejs.dev/)

</div>

---

## 📖 Sumário

- [Visão Geral](#-visão-geral)
- [Principais Funcionalidades](#-principais-funcionalidades)
- [Design do Jogo & Gamificação](#-design-do-jogo--gamificação)
  - [As 5 Fases da Horta](#as-5-fases-da-horta)
  - [Sistema de Estrelas (3 por fase = 15 totais)](#sistema-de-estrelas)
  - [Níveis de Agroecologia & XP](#níveis-de-agroecologia--xp)
  - [Mesa de Crafting Agroecológico 3x3](#-mesa-de-crafting-agroecológico-3x3)
  - [Árvore de Talentos RPG (Maestria Agroecológica)](#-árvore-de-talentos-rpg-maestria-agroecológica)
  - [Missões Diárias & Desafios Práticos](#-missões-diárias--desafios-práticos-daily-quests)
  - [Motor de Áudio Retrô 8-Bit](#-motor-de-áudio-retrô-8-bit)
  - [Bosses Pedagógicos & Quizzes](#bosses-pedagógicos--quizzes)
  - [Inventário, Power-ups e Medalhas](#inventário-power-ups-e-medalhas)
  - [Tela de Vitória & Certificado Oficial](#tela-de-vitória--certificado-oficial)
- [Área do Professor / Gestor (`/admin`)](#-área-do-professor--gestor-admin)
- [Arquitetura & Tecnologias](#-arquitetura--tecnologias)
- [Estrutura de Pastas](#-estrutura-de-pastas)
- [Modelo de Dados (Supabase / PostgreSQL)](#-modelo-de-dados-supabase--postgresql)
- [Como Executar Localmente](#-como-executar-localmente)
- [Variáveis de Ambiente](#-variáveis-de-ambiente)
- [Scripts Disponíveis](#-scripts-disponíveis)
- [Diretrizes de Manutenção do Projeto](#-diretrizes-de-manutenção-do-projeto)

---

## 🌟 Visão Geral

O **Craft Horta** é uma aplicação web interativa concebida para transformar a criação e o manejo de hortas escolares em uma experiência pedagógica gamificada, imersiva e divertida.

Combinando a estética nostálgica de blocos do **Minecraft**, desafios inspirados em **Super Mario Bros** e elementos de **RPGs de Sobrevivência & Talentos**, o projeto guia turmas, alunos e equipes por meio de 5 etapas essenciais da agroecologia — desde o mapeamento solar e pesquisa nutricional na cantina até a engenharia de irrigação sustentável, síntese de insumos na mesa de trabalho, consórcio biológico de culturas e construção prática dos canteiros.

---

## 🚀 Principais Funcionalidades

### 🎮 Para os Alunos / Jogadores

- **HUD Gamificado em Tempo Real:** Visualização dinâmica do XP total (base + bônus de crafting/missões), barra de progresso em blocos estilo Minecraft, nível agroecológico atual e estrelas conquistadas.
- **Seletor de Equipes/Players:** Troca rápida e criação instantânea de equipes para gerenciar o progresso do grupo.
- **🔨 Mesa de Crafting 3x3:** Grade de trabalho onde os jogadores combinam insumos reais (_Terra_, _Composto Orgânico_, _Minhocas_, _Mulching_, _Garrafa PET_, _Sementes_, _Manjericão_) para sintetizar super itens sustentáveis e ganhar XP extra.
- **🌳 Árvore de Talentos RPG:** 5 Tiers de habilidades passivas agroecológicas desbloqueadas conforme o avanço de nível da equipe.
- **📜 Missões Diárias (Daily Quests):** Desafios práticos diários no canteiro da escola com recompensas imediatas de XP.
- **🔊 Efeitos Sonoros Retrô 8-bit:** Áudio sintetizado via Web Audio API para coleta de moedas, conclusão de checklists, acertos/erros em quizzes e fanfarras de vitória com botão de controle de som.
- **Checklists Interativos de Campo:** Ações práticas que conectam o aprendizado teórico às atividades físicas na terra.
- **Batalhas de Boss em Quizzes:** Desafios de múltipla escolha com perguntas pedagógicas sobre fotossíntese, controle biológico, mulching, compostagem e soberania alimentar.
- **Inventário de Ferramentas e Itens Sintetizados:** Visualização de insumos desbloqueados e receitas craftadas pela equipe.
- **Certificado Oficial Emitido:** Geração e impressão com formatação oficial após a conclusão das 5 fases.

### 👨🏫 Para Professores & Gestores Pedagógicos (`/admin`)

- **Dashboard Estatístico Completo:** Indicadores de total de alunos, equipes, XP acumulado da turma (incluindo bônus de gamificação), estrelas totais e taxa de conclusão.
- **Gráficos Interativos (Recharts):**
  - Gráfico de barras da _Distribuição de Níveis dos Alunos_.
  - Gráfico de barras da _Taxa de Conclusão por Fase da Horta_.
- **Gestão de Alunos e Equipes:** Cadastro de integrantes, edição de nomes e exclusão de grupos.
- **Avaliação Formativa Personalizada:**
  - Lançamento de notas formativas.
  - Registro de parecer descritivo do professor.
  - Concessão de estrelas bônus.
  - Atribuição de medalhas de honra temáticas (Compostagem, Irrigação, Policultura, Cooperação, Cientista do Solo e Cantina Verde).
- **Filtro de Pesquisa Instantâneo:** Busca ágil por nome da equipe, nome de qualquer aluno integrante ou nível alcançado.
- **Tabela de Fechamento Escolar Pronta para Impressão:** Tabela consolidada com todas as notas, fases e alunos pronta para geração de PDF e relatórios impressos.

---

## 🕹️ Design do Jogo & Gamificação

```
  [ Fase 1: Chunk & Sol ]  -->  [ Fase 2: Loot Cantina ]  -->  [ Fase 3: Redstone Água ]
             |                                                             |
             +--------------------> [ Fase 4: Boss Monocultura ] <---------+
                                                |
                                                v
                               [ Fase 5: A Grande Construção ] 🏆
                                                |
            +-----------------------------------+-----------------------------------+
            |                                   |                                   |
            v                                   v                                   v
  [ 🔨 Mesa de Crafting 3x3 ]       [ 🌳 Árvore de Talentos RPG ]        [ 📜 Missões Diárias ]
```

### As 5 Fases da Horta

|  Fase   | Título                   | Desafio de Campo                                                                | Boss / Quiz                                          | Entregável Pedagógico                        | Recompensa Desbloqueada                    |
| :-----: | :----------------------- | :------------------------------------------------------------------------------ | :--------------------------------------------------- | :------------------------------------------- | :----------------------------------------- |
|  **I**  | **Escolher Local**       | Avaliar 4–6h de insolação diária, proximidade de água e ausência de entulho.    | _Guardião Solar da Escola_ (Fotossíntese e Luz)      | Minimap do canteiro com orientação Norte-Sul | +20 XP • Lote de Terra Desbloqueado ⭐     |
| **II**  | **Pesquisar Cantina**    | Entrevistar os cozinheiros/nutricionistas sobre as hortaliças mais necessárias. | _Chef Mestre da Cantina_ (Soberania Alimentar)       | Tabela de Loot de Sementes & Mudas           | +20 XP • Pouch de Sementes Desbloqueado ⭐ |
| **III** | **Projetar Irrigação**   | Criar circuito por gotejamento/capilaridade e cobrir solo com mulching.         | _Engenheiro Redstone das Águas_ (Eficiência Hídrica) | Esquema técnico do circuito hidráulico       | +20 XP • Balde e Canos de Irrigação ⭐     |
| **IV**  | **O Quiz dos Guardiões** | Entender sinergia biológica entre culturas e combate natural a pragas.          | _Boss da Monocultura & Pragas_ (Policultura)         | Ficha de Estratégia Agroecológica validada   | +20 XP • Pás e Enxadas de Diamante ⭐      |
|  **V**  | **A Grande Construção**  | Arar a terra, compostar, plantar em consórcio e ativar a irrigação.             | _Grande Mestre da Colheita_ (Economia Circular)      | Canteiro 100% plantado e funcional           | +20 XP • Troféu Mestre Crafter 🏆          |

---

### Sistema de Estrelas

Cada fase disponibiliza até **3 Estrelas (⭐⭐⭐)**, totalizando **15 Estrelas no jogo**:

1. ⭐ **Estrela de Campo:** Cumprimento de 100% dos checklists práticos da fase.
2. ⭐ **Estrela de Conhecimento:** Vitória no Quiz contra o Boss da fase.
3. ⭐ **Estrela de Maestria:** Validação do entregável físico com o Professor e conclusão da fase.

---

### Níveis de Agroecologia & XP

| Nível | Título                             | Emoji | XP Mínimo | Descrição Pedagógica                                         | Badge de Conquista        |
| :---: | :--------------------------------- | :---: | :-------: | :----------------------------------------------------------- | :------------------------ |
| **1** | **Broto Aprendiz**                 |  🌱   |   0 XP    | Início da exploração e mapeamento dos chunks da escola       | _Semente Pioneira_        |
| **2** | **Jardineiro de Blocos**           |  🌿   |   20 XP   | Domínio da pesquisa de insumos e sementes agroecológicas     | _Guardião da Cantina_     |
| **3** | **Engenheiro Hidráulico**          |  💧   |   40 XP   | Criação de sistemas de irrigação sustentável sem desperdício | _Mestre Redstone da Água_ |
| **4** | **Guardião da Biodiversidade**     |  🍄   |   60 XP   | Vitória sobre a monocultura usando consórcios e policultura  | _Defensor dos Biomas_     |
| **5** | **Mestre Crafter da Agroecologia** |  👑   |   80 XP   | Horta viva, produtiva e integrada ao ecossistema escolar     | _Lenda da Colheita_       |

---

### 🔨 Mesa de Crafting Agroecológico 3x3

A bancada de criação permite sintetizar soluções sustentáveis a partir dos insumos coletados:

| Receita Craftada                            | Ingredientes Requeridos                             | Efeito Agroecológico                                          | Recompensa |
| :------------------------------------------ | :-------------------------------------------------- | :------------------------------------------------------------ | :--------: |
| **Super Húmus Turbinado**                   | Terra + Composto da Cantina + Minhocas              | Eleva o pH e microbiota viva, acelerando o crescimento em 2x. |  `+15 XP`  |
| **Consórcio Defensivo Alface + Manjericão** | Semente de Alface + Muda de Manjericão              | Odor aromático que repele a mosca-branca e lagartas.          |  `+20 XP`  |
| **Circuito de Irrigação Gota a Gota**       | Garrafa PET + Micro-Mangueira + Palhada de Mulching | Economia de 80% de água e proteção contra choque térmico.     |  `+25 XP`  |
| **Calda Bio-Repelente Natural**             | Alho & Pimenta + Garrafa PET                        | Defensivo natural contra pulgões e fungos patogênicos.        |  `+20 XP`  |
| **Salada Real da Cantina Verde**            | Alface + Tomate + Manjericão                        | Banquete 100% orgânico e soberano para os alunos.             |  `+30 XP`  |

---

### 🌳 Árvore de Talentos RPG (Maestria Agroecológica)

Progressão de habilidades passivas que refletem o amadurecimento técnico da turma:

- **Tier 1 — 🔍 Olhar de Botânico (Nível 1):** Mapeamento e identificação precisa de insolação solar Norte-Sul.
- **Tier 2 — 🪱 Alquimista do Húmus (Nível 2):** Domínio sobre compostagem termofílica e vermicompostagem escolar.
- **Tier 3 — 💧 Engenheiro da Água Viva (Nível 3):** Controle de retenção hídrica por cobertura vegetal morta permanente.
- **Tier 4 — 🛡️ Escudo da Policultura (Nível 4):** Sinergia entre espécies companheiras e atração de inimigos naturais.
- **Tier 5 — 👑 Coroa do Mestre Agroecológico (Nível 5):** Liderança exemplar e emissão de Certificado com Selo Ouro.

---

### 📜 Missões Diárias & Desafios Práticos (Daily Quests)

Atividades práticas rápidas para engajamento contínuo no canteiro da escola:

- ☀️ **Ronda Solar da Manhã (+10 XP):** Verificar e registrar a projeção de sombras nos blocos do canteiro.
- 💧 **Toque do Dedo na Terra (+10 XP):** Testar a umidade real a 2cm de profundidade sob o mulching.
- 🪱 **Alimentar os Minhocões (+15 XP):** Abastecer a composteira escolar com resíduos orgânicos da cantina.
- 🐞 **Patrulha das Joaninhas (+15 XP):** Registrar a presença de polinizadores ou predadores benéficos.
- 🌾 **Reforço da Cobertura Morta (+15 XP):** Aplicar 3 a 5cm de folhas secas para reter umidade no solo.

---

### 🔊 Motor de Áudio Retrô 8-Bit

Efeitos sonoros nativos sintetizados via **Web Audio API** (sem arquivos de áudio pesados):

- 🟫 **Check Sound:** Clique em checklists e blocos.
- 🪙 **Coin Sound:** Coleta de moedas, estrelas e missões cumpridas.
- ✨ **Power-Up Sound:** Arpejo clássico ao desbloquear fases e talentos.
- 🔨 **Crafting Sound:** Efeito sonoro de síntese na bancada 3x3.
- 👾 **Boss Hit & Fanfarra:** Sons de batalha e vitória épica nos Quizzes.
- Botão de controle de áudio (🔊 / 🔇) com memória persistente via `localStorage`.

---

### Medalhas Especiais de Conquista

Professores podem condecorar equipes com medalhas de mérito no painel administrativo:

- 🪱 **Mago da Compostagem:** Produção exemplar de húmus e matéria orgânica viva.
- 💧 **Guardião da Água:** Eficiência hídrica máxima com desperdício zero.
- 🌻 **Escudo da Policultura:** Defesa biológica inteligente com consórcio de plantas aromáticas.
- 🤝 **Super Cooperação:** Trabalho em equipe e colaboração exemplar no canteiro.
- 🔬 **Cientista do Solo:** Análise detalhada de pH, aeração e fertilidade do solo.
- 🥗 **Chef da Cantina Verde:** Integração direta das hortaliças na alimentação dos alunos.

---

### Tela de Vitória & Certificado Oficial

Ao completar a 5ª fase:

1. É liberada a **Tela de Celebração Épica** com artes temáticas e estatísticas consolidadas.
2. O sistema gera automaticamente o **Certificado Oficial de Mestre da Agroecologia**, personalizado com os nomes de todos os alunos da equipe, nota final, estrelas, data formatada e campos de assinatura para o Professor e a Coordenação Pedagógica, pronto para impressão em folha A4 / PDF.

---

## 👨🏫 Área do Professor / Gestor (`/admin`)

O painel administrativo foi projetado para facilitar a rotina docente:

- **URL Direta:** Acesse via `/admin` ou clicando no botão no canto superior direito da tela inicial.
- **Controle de Membros:** Adicione e edite os nomes dos estudantes vinculados a cada grupo.
- **Fechamento de Notas:** Campo direto para nota numérica ou conceitual, com parecer pedagógico.
- **Relatório de Turma para Impressão:** Botão de impressão com estilos CSS otimizados para remover elementos decorativos e focar nas tabelas de notas.

---

## 🛠️ Arquitetura & Tecnologias

```
┌─────────────────────────────────────────────────────────┐
│                    Frontend Layer                       │
│  React 19 + TypeScript + Vite 8 + TanStack Router       │
│  Tailwind CSS v4 + Radix UI + Lucide Icons + Recharts   │
│  Retro Audio Engine (Web Audio API Sintética)           │
└───────────────────────────┬─────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│                 Data & State Management                 │
│  TanStack Query (React Query) + Supabase JS Client      │
└───────────────────────────┬─────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│                     Backend Layer                       │
│  Supabase PostgreSQL (Tables: grupos, grupo_fases)      │
│  Row-Level Security (RLS) & Realtime Synchronization    │
└─────────────────────────────────────────────────────────┘
```

- **Frontend Core:** [React 19](https://react.dev/) com [TypeScript](https://www.typescriptlang.org/)
- **Roteamento:** [TanStack Router](https://tanstack.com/router) & [TanStack Start](https://tanstack.com/start)
- **Gerenciamento de Estado de Servidor:** [TanStack React Query v5](https://tanstack.com/query)
- **Estilização:** [Tailwind CSS v4](https://tailwindcss.com/) com fontes e tema pixel-art personalizado
- **Componentes de UI:** [Radix UI](https://www.radix-ui.com/), [Lucide React](https://lucide.dev/), [Sonner](https://sonner.emilkowal.ski/)
- **Gráficos & Métricas:** [Recharts](https://recharts.org/)
- **Backend as a Service:** [Supabase](https://supabase.com/) (PostgreSQL)
- **Build Tool:** [Vite 8](https://vitejs.dev/) + [Nitro](https://nitro.unjs.io/)

---

## 📁 Estrutura de Pastas

```text
crafthortaceeps/
├── public/                       # Arquivos estáticos e ícones públicos
├── src/
│   ├── assets/                   # Imagens pixel-art das fases (fase1 a 5, vitoria_final)
│   ├── components/               # Componentes React reutilizáveis
│   │   ├── ui/                   # Componentes base Radix/Tailwind (botões, cards, dialogs)
│   │   ├── CraftingTableModal.tsx# Mesa de crafting 3x3 interativa e livro de receitas
│   │   ├── DailyQuestsModal.tsx  # Modal de missões diárias e desafios práticos no canteiro
│   │   ├── PhaseCard.tsx         # Card interativo de cada uma das 5 fases
│   │   ├── PlayerManagerModal.tsx# Modal de gestão e avaliação pelo Professor
│   │   ├── QuizModal.tsx         # Modal de batalha de Boss e Quiz agroecológico
│   │   ├── SkillTreeModal.tsx    # Modal de árvore de talentos RPG e maestria agroecológica
│   │   └── VictoryModal.tsx      # Modal de vitória final e emissão de Certificado
│   ├── hooks/                    # React Custom Hooks (use-toast, use-mobile)
│   ├── integrations/
│   │   └── supabase/             # Cliente de conexão Supabase e tipagens geradas
│   ├── lib/
│   │   ├── craft-horta.ts        # Regras de gamificação, níveis, fases, bosses e XP
│   │   ├── craft-horta-api.ts    # Camada de comunicação com o banco de dados Supabase
│   │   ├── crafting-recipes.ts   # Definições de receitas, talentos RPG e missões diárias
│   │   ├── retro-audio.ts        # Motor de áudio 8-bit sintetizado via Web Audio API
│   │   └── utils.ts              # Utilitários de classes CSS (cn, clsx, tailwind-merge)
│   ├── routes/                   # Sistema de rotas TanStack Router
│   │   ├── __root.tsx            # Layout raiz e provedores globais
│   │   ├── index.tsx             # Rota principal (Jogo do Aluno, HUD & Ações de Gamificação)
│   │   └── admin.tsx             # Rota do Professor (Painel de Gestão & Relatórios)
│   ├── router.tsx                # Configuração do router
│   ├── routeTree.gen.ts          # Árvore de rotas gerada automaticamente
│   ├── server.ts                 # Configuração do servidor Nitro / Start
│   ├── start.ts                  # Ponto de entrada TanStack Start
│   └── styles.css                # Folha de estilos global, temas e classes pixel-art
├── supabase/                     # Configurações e migrações do Supabase
├── .env                          # Variáveis de ambiente
├── package.json                  # Dependências e scripts do projeto
├── tsconfig.json                 # Configurações do TypeScript
└── vite.config.ts                # Configurações do Vite e plugins
```

---

## 🗄️ Modelo de Dados (Supabase / PostgreSQL)

### 1. Tabela `grupos`

Representa um jogador individual ou equipe de estudantes.

| Coluna         | Tipo          | Descrição                                                                                                                                                                                  |
| :------------- | :------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`           | `UUID` (PK)   | Identificador único da equipe/player.                                                                                                                                                      |
| `nome`         | `TEXT`        | Nome visível da equipe ou estudante.                                                                                                                                                       |
| `nota_unidade` | `TEXT` (JSON) | Metadados formativos: membros `[]`, nota `string`, feedback `string`, medalhas `[]`, estrelas bônus `number`, `xp_bonus` `number`, `crafts_desbloqueados` `[]`, `missoes_concluidas` `[]`. |
| `status`       | `TEXT`        | `"EM PROGRESSO"` ou `"CONCLUÍDO"`.                                                                                                                                                         |
| `created_at`   | `TIMESTAMPTZ` | Data e hora de cadastro.                                                                                                                                                                   |

### 2. Tabela `grupo_fases`

Controla o progresso individual de cada uma das 5 fases para cada equipe.

| Coluna         | Tipo          | Descrição                                                              |
| :------------- | :------------ | :--------------------------------------------------------------------- |
| `id`           | `UUID` (PK)   | Identificador único do registro de fase.                               |
| `grupo_id`     | `UUID` (FK)   | Chave estrangeira referenciando `grupos.id`.                           |
| `fase`         | `INTEGER`     | Número da fase (1 a 5).                                                |
| `status`       | `TEXT`        | `"BLOQUEADO"`, `"EM PROGRESSO"` ou `"CONCLUÍDO"`.                      |
| `checklist`    | `JSONB`       | Lista de itens práticos `[{ texto: string, feito: boolean }]`.         |
| `inventario`   | `TEXT[]`      | Itens e conquistas desbloqueadas (ex: `["Lote de Terra", "quiz_ok"]`). |
| `xp`           | `INTEGER`     | Pontos de experiência atribuídos à fase (20 XP por fase).              |
| `concluido_em` | `TIMESTAMPTZ` | Data/hora de conclusão.                                                |

---

## 💻 Como Executar Localmente

### Pré-requisitos

- [Node.js](https://nodejs.org/) (versão 18 ou superior) ou [Bun](https://bun.sh/)
- Gerenciador de pacotes `npm`, `yarn`, `pnpm` ou `bun`
- [Git](https://git-scm.com/)

### Passo a Passo

1. **Clonar o Repositório:**

   ```bash
   git clone https://github.com/seu-usuario/crafthortaceeps.git
   cd crafthortaceeps
   ```

2. **Instalar as Dependências:**

   ```bash
   npm install
   # ou com bun:
   bun install
   ```

3. **Configurar as Variáveis de Ambiente:**
   Crie ou edite o arquivo `.env` na raiz do projeto com as credenciais do seu projeto Supabase:

   ```env
   VITE_SUPABASE_URL="https://seu-projeto.supabase.co"
   VITE_SUPABASE_PUBLISHABLE_KEY="sua-chave-publica-anon"
   ```

4. **Iniciar o Servidor de Desenvolvimento:**

   ```bash
   npm run dev
   # ou
   bun run dev
   ```

5. **Acessar no Navegador:**
   - **Área do Jogo:** `http://localhost:3000` ou `http://localhost:5173`
   - **Área do Professor:** `http://localhost:3000/admin`

---

## 🔐 Variáveis de Ambiente

| Variável                        | Obrigatória | Descrição                                        |
| :------------------------------ | :---------: | :----------------------------------------------- |
| `VITE_SUPABASE_URL`             |     Sim     | URL base da instância Supabase                   |
| `VITE_SUPABASE_PUBLISHABLE_KEY` |     Sim     | Chave pública `anon` para requisições de cliente |
| `SUPABASE_PROJECT_ID`           |  Opcional   | ID de referência do projeto no Supabase          |

---

## 📜 Scripts Disponíveis

| Comando           | Descrição                                                           |
| :---------------- | :------------------------------------------------------------------ |
| `npm run dev`     | Inicia o servidor Vite em modo de desenvolvimento com Hot Reload.   |
| `npm run build`   | Compila o projeto TypeScript e gera o bundle de produção otimizado. |
| `npm run preview` | Executa o preview local da versão de produção compilada.            |
| `npm run lint`    | Executa a verificação estática de código com o ESLint.              |
| `npm run format`  | Formata automaticamente os arquivos do projeto usando Prettier.     |

---

## 📌 Diretrizes de Manutenção do Projeto

> [!IMPORTANT]
> **Atualização da Documentação:**
> Sempre que novas fases, medalhas, funcionalidades ou rotas forem adicionadas ou alteradas no código, atualize este README.md para refletir com fidelidade as novas capacidades do sistema.

---

<div align="center">
Desenvolvido com 💚 e Agroecologia para transformar a educação sustentável.
</div>
