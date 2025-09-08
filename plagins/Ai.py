from groq import Groq
from openai import OpenAI

import config

# client_Groq = Groq(api_key=os.getenv("groq_API_KEY"))
settings = config.load_settings()
client_Groq = Groq(api_key=settings["groqAI_API"])
client_OpenAi = OpenAI(api_key=settings["openAI_API"])


def ask_gpt(prompt: str):
    try:
        response = client_OpenAi.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=512
        )
        return response.choices[0].text.strip()
    except Exception as e:
        response = client_Groq.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "Ты — помощник."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content

def get_status_gpt():
    try:
        response = client_OpenAi.Completion.create(
            model="text-davinci-003",
            prompt="ping",
            max_tokens=1
        )
        return True, "OK"
    except Exception as e1:
        try:
            response = client_Groq.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": "ping"}],
                max_tokens=1
            )
            return True, "OK"
        except Exception as e2:
            return False, str(e1)
