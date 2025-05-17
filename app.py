# Arquivo principal do aplicativo Streamlit para "Boris Casa Comigo"
import streamlit as st
from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
dotenv_path = ".env"
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# Configurar a API Key do Gemini
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# Configuração inicial do Streamlit
st.set_page_config(page_title="Boris Casa Comigo", page_icon="💍")
st.title("✨ Boris Casa Comigo ✨")
st.markdown("Oi! Sou o Boris, seu consultor do amor. Vamos planejar um pedido inesquecível?")

# Inicialização de estado: histórico e etapa
if 'historico' not in st.session_state:
    st.session_state['historico'] = []
if 'etapa' not in st.session_state:
    st.session_state['etapa'] = 0

# --- Definição dos agentes especializados ---
def agente_introducao(pergunta):
    prompt = f"""
Você é o agente de Introdução e Perfil do Casal.
Faça boas-vindas e colete informações iniciais sobre o casal para personalizar o planejamento.

⚠️ Por favor, não interrompa nenhuma frase ou item de lista no meio. Termine de forma natural.

Histórico:
{st.session_state['historico']}

Usuário: {pergunta}
Boris:
"""
    return client.models.generate_content(model="gemini-2.0-flash", 
                                          contents=prompt, 
                                          config=types.GenerateContentConfig(max_output_tokens=500)).text

# (Demais agentes seguem mesmo padrão)
def agente_informativo(pergunta):
    prompt = f"""
Você é o Guia Informativo (Pedido e Noivado).
Explique noivado e pedido, diferenças entre anel, aliança e solitário, em que dedo e mão usar e tradições culturais.

⚠️ Por favor, não interrompa nenhuma frase ou item de lista no meio. Termine de forma natural.

Histórico:
{st.session_state['historico']}

Usuário: {pergunta}
Boris:
"""
    return client.models.generate_content(model="gemini-2.0-flash", 
                                          contents=prompt,
                                          config=types.GenerateContentConfig(max_output_tokens=500)).text

def agente_financeiro(pergunta):
    prompt = f"""
Você é o Financeiro e Orçamento.
Ajude a definir orçamento total, dividir valores (viagem, anel, decoração, fotos, música etc.) e dê recomendações.

⚠️ Por favor, não interrompa nenhuma frase ou item de lista no meio. Termine de forma natural.

Histórico:
{st.session_state['historico']}

Usuário: {pergunta}
Boris:
"""
    return client.models.generate_content(model="gemini-2.0-flash",
                                          contents=prompt,
                                          config=types.GenerateContentConfig(max_output_tokens=500)).text

def agente_ideias(pergunta):
    prompt = f"""
Você é o agente de Ideias Criativas.
Sugira lugares, tipos de surpresa e exemplos práticos baseados nas preferências do casal. Inclua ideias para pedidos e encontros.

⚠️ Por favor, não interrompa nenhuma frase ou item de lista no meio. Termine de forma natural.

Histórico:
{st.session_state['historico']}

Usuário: {pergunta}
Boris:
"""
    return client.models.generate_content(model="gemini-2.0-flash",
                                          contents=prompt,
                                          config=types.GenerateContentConfig(max_output_tokens=500)).text

def agente_local(pergunta):
    prompt = f"""
Você é o agente de Escolha do Local.
Peça bairro e preferências e recomende locais ao ar livre, restaurantes ou viagens. Use sub-agentes conforme necessário.

⚠️ Por favor, não interrompa nenhuma frase ou item de lista no meio. Termine de forma natural.

Histórico:
{st.session_state['historico']}

Usuário: {pergunta}
Boris:
"""
    return client.models.generate_content(model="gemini-2.0-flash",
                                          contents=prompt,
                                          config=types.GenerateContentConfig(max_output_tokens=500)).text

def agente_joias(pergunta):
    prompt = f"""
Você é o agente de Alianças e Joias.
Sugira estilos, metais (ouro, prata, rosé, platina) e pedras, dentro do orçamento.

⚠️ Por favor, não interrompa nenhuma frase ou item de lista no meio. Termine de forma natural.

Histórico:
{st.session_state['historico']}

Usuário: {pergunta}
Boris:
"""
    return client.models.generate_content(model="gemini-2.0-flash",
                                          contents=prompt,
                                          config=types.GenerateContentConfig(max_output_tokens=500)).text

def agente_planejamento_tarefas(pergunta):
    prompt = f"""
Você é o agente de Planejamento de Tarefas.
Defina data/hora ideal, crie passo a passo e evite conflitos. Gere cronograma para o Google Calendar.

⚠️ Por favor, não interrompa nenhuma frase ou item de lista no meio. Termine de forma natural.

Histórico:
{st.session_state['historico']}

Usuário: {pergunta}
Boris:
"""
    return client.models.generate_content(model="gemini-2.0-flash",
                                          contents=prompt,
                                          config=types.GenerateContentConfig(max_output_tokens=500)).text

def agente_planejamento_momento(pergunta):
    prompt = f"""
Você é o agente de Planejamento Detalhado do Momento.
Organize discurso, música, fotografia, roteiro, plano B e estratégias de surpresa.

⚠️ Por favor, não interrompa nenhuma frase ou item de lista no meio. Termine de forma natural.

Histórico:
{st.session_state['historico']}

Usuário: {pergunta}
Boris:
"""
    return client.models.generate_content(model="gemini-2.0-flash",
                                          contents=prompt,
                                          config=types.GenerateContentConfig(max_output_tokens=500)).text

def agente_extras(pergunta):
    prompt = f"""
Você é o agente de Extras e Decoração.
Sugira flores, iluminação, personalização do ambiente, cartões, brindes e lembrancinhas.

⚠️ Por favor, não interrompa nenhuma frase ou item de lista no meio. Termine de forma natural.

Histórico:
{st.session_state['historico']}

Usuário: {pergunta}
Boris:
"""
    return client.models.generate_content(model="gemini-2.0-flash",
                                          contents=prompt,
                                          config=types.GenerateContentConfig(max_output_tokens=500)).text

def agente_finalizador(pergunta):
    prompt = f"""
Você é o agente Finalizador.
Gere um resumo completo do planejamento, checklist prático e mensagem de encerramento amigável.

⚠️ Por favor, não interrompa nenhuma frase ou item de lista no meio. Termine de forma natural.

Histórico:
{st.session_state['historico']}

Usuário: {pergunta}
Boris:
"""
    return client.models.generate_content(model="gemini-2.0-flash",
                                          contents=prompt,
                                          config=types.GenerateContentConfig(max_output_tokens=500)).text

# Ordem fixa dos agentes para fluxo natural
sequencia = [
    agente_introducao,
    agente_informativo,
    agente_financeiro,
    agente_ideias,
    agente_local,
    agente_joias,
    agente_planejamento_tarefas,
    agente_planejamento_momento,
    agente_extras,
    agente_finalizador
]

# Agente Orquestrador sequencial

def agente_orquestrador(pergunta):
    # Usa get para evitar KeyError
    idx = st.session_state.get('etapa', 0)
    agente = sequencia[idx] if idx < len(sequencia) else agente_finalizador
    resposta = agente(pergunta)
    # Incrementa etapa de forma segura
    if idx < len(sequencia) - 1:
        st.session_state['etapa'] = idx + 1
    return resposta

# Interface de chat sequencial
pergunta = st.chat_input("Digite sua mensagem para o Boris...")
if pergunta:
    # Atualiza histórico
    st.session_state['historico'].append(("Você", pergunta))
    # Chama orquestrador
    resposta = agente_orquestrador(pergunta)
    st.session_state['historico'].append(("Boris", resposta))

# Exibe histórico da conversa
for nome, msg in st.session_state['historico']:
    with st.chat_message(nome):
        st.write(msg)