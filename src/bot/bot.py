from groq import Groq
from dotenv import load_dotenv
from linkaBotsSdk import LinkaBotSdk as sdk
load_dotenv("bot.env")
client = Groq()
def send_prompt(message):
  completion = client.chat.completions.create(
      model="openai/gpt-oss-120b",
      messages=[
        {
          "role": "user",
          "content": message
        }
      ],
      temperature=1,
      max_completion_tokens=2048,
      top_p=1,
      reasoning_effort="medium",
      stream=True,
      stop=None
  )

  for chunk in completion:
      print(chunk.choices[0].delta.content or "", end="")
