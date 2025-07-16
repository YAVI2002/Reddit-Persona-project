# Reddit User Persona Generator

This project generates a psychological and behavioral persona for a Reddit user using their posts and comments.

## 🔧 Setup

1. Create a `.env` file with the following content:

```
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
OPENAI_API_KEY=your_openai_api_key
```

2. Install dependencies:
```
pip install -r requirements.txt
```

## 🚀 Usage

Run the script by passing the Reddit user URL:
```
python main.py https://www.reddit.com/user/kojied/
```

The output will be saved in the `output/` folder as a `.txt` file.
