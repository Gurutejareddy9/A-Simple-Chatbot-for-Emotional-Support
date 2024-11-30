import random
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')  # Download required NLTK resources if not already

# Initialize Sentiment Intensity Analyzer
sia = SentimentIntensityAnalyzer()

# Predefined responses for different sentiments
responses = {
    'positive': [
        "That's great to hear! What’s been the highlight of your day?",
        "Awesome, let’s keep that positivity going! Would you like some fun suggestions?",
        "Wonderful! How can I assist you in making the most of this good mood?"
    ],
    'neutral': [
        "Let's explore more. How are you feeling today, and what’s on your mind?",
        "I'm all ears. Would you like to talk about something specific or just see where our conversation goes?",
        "That's quite an interesting point. Care to delve deeper into your thoughts?"
    ],
    'negative': [
        "Sorry to hear that you’re feeling down. Would you like some resources for emotional support or just someone to talk to?",
        "That can be really tough. Remember, you’re not alone. How about we focus on something uplifting for a bit?",
        "I’m here to listen. If you’re comfortable, could you tell me more about what’s bothering you?"
    ]
}

def analyze_sentiment(user_input):
    """Analyze the sentiment of the user's input."""
    sentiment_scores = sia.polarity_scores(user_input)
    compound_score = sentiment_scores['compound']
    if compound_score >= 0.05:
        return 'positive'
    elif compound_score <= -0.05:
        return 'negative'
    else:
        return 'neutral'

def engage_user():
    """Engage the user in conversation."""
    print("Welcome to MoodMingle! I’m here to listen and offer support. How are you feeling today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "bye", "exit"]:
            print("It was nice chatting with you. Remember, you’re not alone. Take care!")
            break
        sentiment = analyze_sentiment(user_input)
        response_list = responses[sentiment]
        print("MoodMingle:", random.choice(response_list))

if __name__ == "__main__":
    engage_user()
