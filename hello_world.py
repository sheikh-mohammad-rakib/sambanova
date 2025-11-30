import os
from unittest import result
from dotenv import load_dotenv
from sambanova import SambaNova

load_dotenv()

client = SambaNova(
    base_url="https://api.sambanova.ai/v1", 
    api_key=os.getenv("SAMBANOVA_API_KEY")
)

completion = client.chat.completions.create(
  model="Meta-Llama-3.3-70B-Instruct",
  messages = [
      {"role": "system", "content": "Answer the question in a couple sentences."},
      {"role": "user", "content": "Share a happy story with me"}
    ]
)

print(completion.choices[0].message.content)

result1 = "One day, a little girl named Sophie found a lost puppy in her neighborhood and decided to take care of it until she could find its owner. As she cared for the puppy, named Max, they formed an unbreakable bond, and when the owner was finally found, they were so grateful to Sophie that they asked her to be Max's permanent dog-sitter, bringing joy and companionship to Sophie's life."

result2 = """
py hello_world.py
One day, a little girl named Sophie found a lost puppy in her neighborhood and decided to take care of it until she could find its owner. As she cared for the puppy, named Max, they formed an unbreakable bond, and when the owner was finally found, they were so grateful to Sophie that they asked her to be Max's permanent dog-sitter, bringing joy and companionship to Sophie's life.
"""