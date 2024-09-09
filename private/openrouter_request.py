import requests
import json

response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": f"Bearer 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",
    "HTTP-Referer": f"https://github.com/berriai/berriai",
    "X-Title": f"Berriai",
  },
  data=json.dumps({
    "model": "google/gemini-flash-1.5-exp",
    "messages": [
      { "role": "user", "content": "What is the meaning of life?" }
    ]
  })
)

print(response.json())