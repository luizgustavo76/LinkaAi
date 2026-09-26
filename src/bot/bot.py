from groq import Groq
from linkaBotsSdk import LinkaBotSdk # Teu SDK nativo
import time
from dotenv import load_dotenv
load_dotenv("bot.env")
bot = LinkaBotSdk()
client = Groq()

def process_messages():
    friends = bot.view_friends()
    for user in friends:
        last_msg = bot.get_last_interaction(user)
        
        if not last_msg:
            continue
        sender = last_msg.get("sender")
        content = last_msg.get("message")
        if sender == user:
            print(f"Nova mensagem de {user}: {content}")
            completion = client.chat.completions.create(
                model="openai/gpt-oss-120b", # Ou llama-3.3-70b-versatile
                messages=[
                    {"role": "system", "content": "You are the assistant for Linka, a social network. Answer questions about the platform—such as how to post or general inquiries—but also act as a personal AI. Don't be dry; be humorous (though without crossing the line) and delightfully nonsensical."},
                    {"role": "user", "content": content}
                ]
            )
            reply_text = completion.choices[0].message.content
            bot.send_chat(message=reply_text, receiver=user)

while True:
    try:
        process_messages()
    except Exception as e:
        print(f"Erro no loop do bot: {e}")
    time.sleep(2)