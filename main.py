import argparse
from reddit_scraper import fetch_user_data
from persona_generator import generate_persona
import os

def extract_username(url):
    return url.strip('/').split('/')[-1]

def save_persona(username, content):
    with open(f'output/{username}_persona.txt', 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="Reddit profile URL")
    args = parser.parse_args()

    username = extract_username(args.url)
    user_data = fetch_user_data(username)
    full_text = "\n\n".join(user_data["posts"] + user_data["comments"])

    persona = generate_persona(full_text)
    save_persona(username, persona)
    print(f"[+] Persona for '{username}' saved at output/{username}_persona.txt")

if __name__ == "__main__":
    main()
