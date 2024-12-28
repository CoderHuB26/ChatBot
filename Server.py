from flask import Flask, request, jsonify
from textblob import TextBlob
import requests

app = Flask(__name__)

# Replace 'YOUR_GPT_API_KEY' with your actual GPT API key
GPT_API_KEY = 'YOUR_GPT_API_KEY'
GPT_API_URL = 'https://api.openai.com/v1/engines/davinci-codex/completions'

conversation_context = []

# List of offensive words and their less offensive synonyms
offensive_words = {
    'badword1': 'betterword1',
    'badword2': 'betterword2',
    # Add more offensive words and their synonyms here
}

def replace_offensive_words(message):
    words = message.split()
    cleaned_message = ' '.join([offensive_words.get(word.lower(), word) for word in words])
    return cleaned_message

def analyze_sentiment(message):
    blob = TextBlob(message)
    return blob.sentiment.polarity

@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    message = data.get('message')
    user_id = data.get('user_id')

    # Replace offensive words in the message
    cleaned_message = replace_offensive_words(message)

    # Update conversation context
    conversation_context.append((user_id, cleaned_message))

    # Analyze sentiment
    sentiment_score = analyze_sentiment(cleaned_message)

    # Generate GPT response
    gpt_response = requests.post(
        GPT_API_URL,
        headers={
            'Authorization': f'Bearer {GPT_API_KEY}',
            'Content-Type': 'application/json'
        },
        json={
            'prompt': '\n'.join([f"User {uid}: {msg}" for uid, msg in conversation_context]),
            'max_tokens': 150
        }
    )

    gpt_response_json = gpt_response.json()
    gpt_reply = gpt_response_json.get('choices', [])[0].get('text', '').strip()

    # Return the response to be sent to the other user
    return jsonify({'reply': gpt_reply, 'sentiment': sentiment_score})

if __name__ == '__main__':
    app.run(debug=True)
