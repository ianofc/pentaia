#!/usr/bin/env python3
"""
ZIOS - Proactive Intelligence
Motor de IA com Gemini, memória de sessão e interface de chat real.
Endpoint principal: POST /v1/chat/ask
"""

import os
import sys
import logging
from datetime import datetime
from typing import Optional, List, Dict, Any

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | ZIOS_NODE: %(message)s"
)
logger = logging.getLogger("ZIOS_MAIN")

from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# ─── Importação do núcleo ZIOS ────────────────────────────────────────────────
try:
    from core.zios import ZiosOrchestrator
    ZIOS_CORE_AVAILABLE = True
    logger.info("✅ ZiosOrchestrator carregado com sucesso.")
except Exception as e:
    ZIOS_CORE_AVAILABLE = False
    logger.warning(f"⚠️ ZiosOrchestrator indisponível ({e}). Usando fallback.")

# ─── Importação do Heimdall (segurança) ───────────────────────────────────────
try:
    from heimdall import attach_heimdall, settings_from_env, ThreatDetector
except ImportError:
    attach_heimdall = lambda *args, **kwargs: False

    class ThreatDetector:
        @classmethod
        def from_cidrs(cls, cidrs):
            return cls()

        def evaluate_ip(self, ip):
            class Verdict:
                allowed = True
                reason = "Heimdall indisponível"
            return Verdict()

    def settings_from_env():
        class Settings:
            blocked_networks = set()
        return Settings()

# ─── Memória de Sessão em memória (por user_id) ───────────────────────────────
# Estrutura: { user_id: [{"role": "user"|"zios", "text": str}, ...] }
SESSION_MEMORY: Dict[str, List[Dict[str, str]]] = {}
MAX_SESSION_HISTORY = 20  # Mantém as últimas 20 mensagens por sessão

# ─── Modelos Pydantic ─────────────────────────────────────────────────────────
class ChatRequest(BaseModel):
    user_id: str = "anonymous"
    message: str
    mode: str = "geral"  # geral, pedagogico, juridico, dev, estrategico
    context: Optional[Dict[str, Any]] = None

class ChatResponse(BaseModel):
    user_id: str
    message: str
    response: str
    mode: str
    timestamp: str
    engine: str
    session_length: int

class ChatHistoryItem(BaseModel):
    role: str
    text: str

# ─── App FastAPI ──────────────────────────────────────────────────────────────
app = FastAPI(
    title="ZIOS - Proactive Intelligence",
    description="Motor de IA autônomo do ecossistema PentaIA. Chat real com Gemini + memória de sessão.",
    version="3.0.0"
)

try:
    heimdall_active = attach_heimdall(app, service_name="zios")
    _heimdall_detector = ThreatDetector.from_cidrs(settings_from_env().blocked_networks)
except Exception:
    heimdall_active = False
    _heimdall_detector = ThreatDetector.from_cidrs(set())

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── Fallback de resposta quando Gemini está indisponível ─────────────────────
FALLBACK_RESPONSES = {
    "quem é você": "Sou o ZIOS — Zona de Inteligência Operacional Suprema. Começo como um tutorial de jogo, mas vou aprendendo com você para otimizar sua vida no LYV e tomar decisões cada vez mais autônomas.",
    "ajuda": "Posso ajudar a: escrever posts, resumir notícias do Mercúrio, sugerir conexões, analisar seu feed e responder perguntas. O que precisa?",
    "olá": "Sistema online. Pronto para otimizar sua experiência no LYV. Qual é sua missão?",
}

def _zios_fallback(message: str) -> str:
    msg_lower = message.lower()
    for key, response in FALLBACK_RESPONSES.items():
        if key in msg_lower:
            return response
    return f"Processando: '{message[:50]}...'. Meu núcleo neural está sincronizando com os servidores PentaIA. Tente novamente em instantes."

# ─── Endpoints ────────────────────────────────────────────────────────────────

@app.get("/")
async def root():
    return {
        "status": "OPERATIONAL",
        "engine": "ZIOS_PENTAIA_v3",
        "service": "Proactive-Intelligence",
        "core_available": ZIOS_CORE_AVAILABLE,
        "port": 8002,
        "timestamp": datetime.now().isoformat()
    }

@app.get("/health")
async def health():
    return {
        "status": "OPERATIONAL",
        "components": {
            "brain": "ACTIVE" if ZIOS_CORE_AVAILABLE else "FALLBACK",
            "memory": "ACTIVE",
            "resonance": "ACTIVE",
            "heimdall": "ACTIVE" if heimdall_active else "INACTIVE"
        }
    }


@app.post("/v1/chat/ask", response_model=ChatResponse)
async def chat_ask(req: ChatRequest):
    """
    Endpoint principal do ZIOS. Recebe uma mensagem do usuário e retorna
    a resposta do motor de IA (Gemini via ZiosOrchestrator).
    Mantém histórico de sessão por user_id em memória.
    """
    user_id = req.user_id or "anonymous"
    message = req.message.strip()

    if not message:
        raise HTTPException(status_code=400, detail="Mensagem não pode ser vazia.")

    # Inicializa sessão se não existir
    if user_id not in SESSION_MEMORY:
        SESSION_MEMORY[user_id] = []

    # Adiciona mensagem do usuário ao histórico
    SESSION_MEMORY[user_id].append({"role": "user", "text": message})

    # Tenta processar com o núcleo real do ZIOS
    response_text = ""
    engine_used = "FALLBACK"

    if ZIOS_CORE_AVAILABLE:
        try:
            # Constrói contexto rico para o ZIOS
            context = {
                "user_id": user_id,
                "mode": req.mode,
                "session_history": SESSION_MEMORY[user_id][-10:],  # Últimas 10 mensagens
                **(req.context or {})
            }

            orchestrator = ZiosOrchestrator(user_id)
            response_text = orchestrator.process(message, context)
            engine_used = "ZIOS_GEMINI_v3"
            logger.info(f"🧠 ZIOS respondeu para {user_id} no modo '{req.mode}'")
        except Exception as e:
            logger.error(f"❌ Erro no ZiosOrchestrator: {e}")
            response_text = _zios_fallback(message)
            engine_used = "ZIOS_FALLBACK"
    else:
        response_text = _zios_fallback(message)
        engine_used = "ZIOS_FALLBACK"

    # Adiciona resposta do ZIOS ao histórico
    SESSION_MEMORY[user_id].append({"role": "zios", "text": response_text})

    # Limita o histórico ao máximo configurado
    if len(SESSION_MEMORY[user_id]) > MAX_SESSION_HISTORY:
        SESSION_MEMORY[user_id] = SESSION_MEMORY[user_id][-MAX_SESSION_HISTORY:]

    return ChatResponse(
        user_id=user_id,
        message=message,
        response=response_text,
        mode=req.mode,
        timestamp=datetime.now().isoformat(),
        engine=engine_used,
        session_length=len(SESSION_MEMORY[user_id])
    )


@app.get("/v1/chat/history/{user_id}")
async def get_chat_history(user_id: str):
    """Retorna o histórico de sessão de um usuário."""
    history = SESSION_MEMORY.get(user_id, [])
    return {
        "user_id": user_id,
        "history": history,
        "count": len(history),
        "timestamp": datetime.now().isoformat()
    }


@app.delete("/v1/chat/history/{user_id}")
async def clear_chat_history(user_id: str):
    """Limpa o histórico de sessão de um usuário."""
    if user_id in SESSION_MEMORY:
        del SESSION_MEMORY[user_id]
    return {"status": "cleared", "user_id": user_id}


@app.get("/v1/proactive/heimdall/check")
async def heimdall_check(ip: str = Query(...)):
    logger.info(f"🔒 Heimdall verificando IP: {ip}")
    verdict = _heimdall_detector.evaluate_ip(ip)
    threat_detected = not verdict.allowed
    return {
        "status": "PROTECTED" if not threat_detected else "WARNING",
        "shield_level": "ELEVATED" if threat_detected else "OPTIMAL",
        "client_ip": ip,
        "threat_detected": threat_detected,
        "reason": verdict.reason,
        "heimdall": "active" if heimdall_active else "inactive",
        "recommendations": ["Ativar 2FA", "Revisar sessões ativas"] if threat_detected else [],
    }


@app.get("/api/v1/zios/status")
async def zios_status():
    return {
        "brain": "online" if ZIOS_CORE_AVAILABLE else "fallback",
        "memory_system": "synced",
        "resonance_engine": "calibrated",
        "active_sessions": len(SESSION_MEMORY),
        "gemini": "connected" if ZIOS_CORE_AVAILABLE else "disconnected"
    }


if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("PORT", "8002"))
    host = os.getenv("HOST", "0.0.0.0")
    reload = os.getenv("RELOAD", "true").lower() == "true"

    logger.info(f"🧠 Iniciando ZIOS v3 em {host}:{port}")

    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=reload,
        reload_dirs=["/app"] if reload else None,
        workers=1
    )
