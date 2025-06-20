import os
import sys
from dotenv import load_dotenv
from google import genai


if len(sys.argv) < 2:
    print("No prompt provided. Exiting.")
    sys.exit(1)

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

model = "gemini-2.0-flash-001"


prompt = sys.argv[1]

res = client.models.generate_content(
    model=model,
    contents=prompt,
)

print(res.text)
print(f"Prompt tokens: {res.usage_metadata.prompt_token_count}")
print(f"Response tokens: {res.usage_metadata.candidates_token_count}")
