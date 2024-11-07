# WhatsApp Bot Integrado com ChatGPT

Este é um projeto de bot para WhatsApp que utiliza a API gratuita do ChatGPT e a API oficial do WhatsApp. Desenvolvido em Python, o bot é configurado com Flask como backend e NGROK para tunelamento seguro, permitindo respostas automatizadas e inteligentes para mensagens recebidas no WhatsApp.

## Índice
- [Visão Geral](#visão-geral)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Configuração do Ambiente](#configuração-do-ambiente)
- [Instalação](#instalação)
- [Uso](#uso)
- [Estrutura do Código](#estrutura-do-código)
- [Contribuição](#contribuição)
- [Licença](#licença)

---

## Visão Geral
Esse bot interage automaticamente com usuários do WhatsApp, usando a API do ChatGPT (g4f) para gerar respostas dinâmicas e personalizadas com base nas mensagens recebidas. É ideal para automação de atendimento ao cliente, oferecendo suporte e informações aos clientes em tempo real.

**Funcionalidades principais:**
- Responde automaticamente a mensagens do WhatsApp com conteúdo gerado pela IA.
- Configurável para dar respostas baseadas em instruções específicas.
- Implementação ágil usando Flask e NGROK para conectar e demonstrar o bot localmente.

---

## Tecnologias Utilizadas
- **Python 3.x**
- **Flask** - Web framework para o backend.
- **NGROK** - Para tunelamento seguro do servidor local.
- **g4f API** - Cliente ChatGPT para integração de IA.
- **API Oficial do WhatsApp** - Para enviar e receber mensagens.

---

## Configuração do Ambiente
Certifique-se de ter as seguintes variáveis de ambiente configuradas em um arquivo `.env`:
```plaintext
ACCESS_TOKEN=<seu_token_do_whatsapp>
RECIPIENT_WAID=<id_destinatario>
PHONE_NUMBER_ID=<id_do_numero_de_telefone>
VERSION=v12.0
APP_ID=<app_id_do_facebook>
APP_SECRET=<app_secret_do_facebook>
Instalação
Clone o repositório:

git clone https://github.com/seuusuario/seu-repositorio.git
cd seu-repositorio

Crie um ambiente virtual e ative-o:
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows

Instale as dependências:
pip install -r requirements.txt
Configure as variáveis de ambiente no arquivo .env, conforme mostrado na seção de Configuração do Ambiente.

Uso
Inicialize o servidor Flask:

flask run
Conecte-se ao NGROK: Abra um novo terminal e execute:

ngrok http 5000
Copie o link gerado pelo NGROK (ex: https://xxxx.ngrok.io) e configure no webhook do WhatsApp.

Testando o bot: Envie uma mensagem de teste para o número configurado no WhatsApp. O bot deve responder com base nas mensagens e instruções configuradas.

Estrutura do Código
g4f.client.Client: Interface para a API g4f, que gera respostas do ChatGPT.
Flask: Cria endpoints para receber e processar mensagens do WhatsApp.
NGROK: Proporciona uma URL pública para testar o bot localmente.




