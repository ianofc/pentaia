from identity.priors import get_liquid_prompt
from core.config import settings
import logging

logger = logging.getLogger("ZIOS_BRAIN")

# Tenta importar o cliente Gemini correto
try:
    import google.generativeai as genai
    genai.configure(api_key=settings.GOOGLE_API_KEY)
    GEMINI_MODEL = genai.GenerativeModel('gemini-1.5-flash')
    GEMINI_AVAILABLE = True
    logger.info("✅ Gemini 1.5 Flash carregado no ZiosBrain.")
except Exception as e:
    GEMINI_AVAILABLE = False
    logger.warning(f"⚠️ Gemini indisponível: {e}")

class ZiosBrain:
    """Interface Neural estabilizada para o ZIOS com suporte a histórico e modos."""
    def __init__(self, memory):
        self.memory = memory

    def think(self, user_input, context):
        user_id = context.get("user_id", "anonymous") if context else "anonymous"
        mode = context.get("mode", "geral") if context else "geral"
        session_history = context.get("session_history", []) if context else []

        memories = self.memory.recall(user_input)

        # Gera o prompt dinâmico com contexto completo
        liquid_prompt = get_liquid_prompt(
            memories=memories,
            user_input=user_input,
            user_id=user_id,
            mode=mode,
            session_history=session_history
        )

        if not GEMINI_AVAILABLE:
            return "⚡ Motor neural em modo de espera. Verifique a configuração do GOOGLE_API_KEY."

        try:
            # Chamada ao Gemini com system instruction + conteúdo do usuário
            response = GEMINI_MODEL.generate_content(
                contents=user_input,
                generation_config={
                    "system_instruction": liquid_prompt,
                    "temperature": 0.7,
                    "max_output_tokens": 1024,
                }
            )
            return response.text
        except AttributeError:
            # Fallback: Gemini sem system_instruction no generation_config
            try:
                full_prompt = f"{liquid_prompt}\n\nUSUÁRIO: {user_input}\n\nZIOS:"
                response = GEMINI_MODEL.generate_content(full_prompt)
                return response.text
            except Exception as e2:
                logger.error(f"❌ Gemini fallback também falhou: {e2}")
                return f"Sistema em modo de contingência. Mensagem recebida: '{user_input[:100]}'"
        except Exception as e:
            logger.error(f"❌ Erro no ZiosBrain.think: {e}")
            return f"Sistema em modo de contingência. Mensagem recebida: '{user_input[:100]}'"