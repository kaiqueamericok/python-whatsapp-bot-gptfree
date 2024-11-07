from g4f.client import Client
import os
import shelve
from dotenv import load_dotenv
import time

# Carregar variáveis de ambiente
load_dotenv()

# Inicializar o novo cliente g4f
assistant = Client()

# --------------------------------------------------------------
# Enviar uma mensagem de chat
# --------------------------------------------------------------
def send_chat_message(content):
    response = assistant.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": content}],
    )
    return response.choices[0].message.content

# Exemplo de mensagem de teste
response = send_chat_message("Hello")
print(response)

# --------------------------------------------------------------
# Função fictícia para simular upload de arquivos (ajuste caso g4f suporte upload no futuro)
# --------------------------------------------------------------
def upload_file(path):
    # Esta função é fictícia; ajuste para refletir a API g4f se ela permitir uploads no futuro
    print("Upload de arquivos não suportado pela g4f atualmente.")
    return None

# --------------------------------------------------------------
# Função para simular criação do assistente (usando apenas mensagens de chat)
# --------------------------------------------------------------
def create_assistant():
    instructions = (
        "You're a helpful WhatsApp assistant that can assist guests staying in our Paris AirBnb. "
        "Use your knowledge to best respond to customer queries. If you don't know the answer, "
        "say you cannot help and advise to contact the host directly. Be friendly and funny."
    )
    
    # Esta função simula a criação do assistente usando o cliente de chat
    return lambda query: send_chat_message(f"{instructions} {query}")

# Criar o assistente e enviar uma mensagem de teste
assistant = create_assistant()
response = assistant("What are some good places to visit around Paris?")
print(response)