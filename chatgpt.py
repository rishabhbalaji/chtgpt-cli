import openai
import psycopg2
import argparse

openai.api_key = "<OPENAI API KEY HERE>"

def generate_text(prompt, conn):
    model_engine = "text-davinci-002"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    generated_text = response.choices[0].text.strip()

    # Save the interaction to the database
    cur = conn.cursor()
    cur.execute("INSERT INTO interactions (input, output) VALUES (%s, %s)", (prompt, generated_text))
    conn.commit()
    cur.close()

    return generated_text

def main():
    parser = argparse.ArgumentParser(description="CLI interface for ChatGPT")
    parser.add_argument("--radio", "-r", help="The value of the selected radio button", required=True)
    args = parser.parse_args()

    radio_value = args.radio

    # Connect to the database
    conn = psycopg2.connect(
        host="your_database_host",
        database="your_database_name",
        user="your_database_username",
        password="your_database_password"
    )

    prompt = f"What is your preferred method of contact? {radio_value}\n"

    while True:
        user_input = input("You: ")
        prompt += f"You: {user_input}\n"
        generated_text = generate_text(prompt, conn)
        print(f"ChatGPT: {generated_text}")
        prompt += f"ChatGPT: {generated_text}\n"

    # Close the database connection
    conn.close()

if __name__ == '__main__':
    main()
