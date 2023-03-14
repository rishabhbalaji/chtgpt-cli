
import openai
import argparse

openai.api_key = "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"

def generate_text(prompt):
    model_engine = "text-davinci-002"
    response = openai.Completion.create(
      engine=model_engine,
      prompt=prompt,
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.5,
    )
    return response.choices[0].text.strip()

def main():
    parser = argparse.ArgumentParser(description="CLI interface for ChatGPT")
    parser.add_argument("--radio", "-r", help="The value of the selected radio button", required=True)
    args = parser.parse_args()

    radio_value = args.radio

    prompt = f"What is your preferred method of contact? {radio_value}\n"

    while True:
        user_input = input("You: ")
        prompt += f"You: {user_input}\n"
        generated_text = generate_text(prompt)
        print(f"ChatGPT: {generated_text}")
        prompt += f"ChatGPT: {generated_text}\n"

if __name__ == '__main__':
    main()
