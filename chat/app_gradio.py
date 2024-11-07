from g4f.client import Client
import gradio as gr

# iniciar o g4f

client = Client()

def chatbot_response(user_input):
	response = client.chat.completion(
		model="gpt-3-5-turbo",
		messages={{"role": "user", "content": user_input}}
	)
	return response.choices[0].message.content

#gradio interface
interface = gr.Interface(
	fn=chatbot_response,
	inputs=gr.Textbox(lines=2, placeholder="Type your question here..."),
	outputs="text",
	title="Ai Assistant Chatbot",
	description="Ask any question"
)

# launch interface
if __name__ == "__main__":
	interface.launch()