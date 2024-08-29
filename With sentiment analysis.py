import re
from textblob import TextBlob

# Abusive and conflicting words with alternatives
abusive_and_conflicting_words_with_alternatives = {
    "stupid": ["uninformed", "misguided"],
    "hate": ["disapprove", "strongly dislike"],
    "idiot": ["inexperienced", "novice"],
     "ugly": ["unattractive", "not my taste"],
    "useless": ["ineffective", "unproductive"],
    "failure": ["challenge", "setback"],
    "annoying": ["bothersome", "irritating"],
    "worthless": ["insignificant", "unimportant"],
    "inferior": ["substandard", "less effective"],
    "fool": ["naive", "unwise"],
    "lazy": ["relaxed", "taking it easy"],
    "crybaby": ["sensitive", "emotionally expressive"],
    "whiner": ["expressive", "communicative"],
    "bossy": ["assertive", "leadership-oriented"],
    "brat": ["spirited", "energetic"],
    "liar": ["inaccurate", "misinformed"],
    "jerk": ["difficult", "unpleasant individual"],
    "egotistical": ["confident", "self-assured"],
    "selfish": ["self-focused", "independent"],
    "arrogant": ["confident", "self-assured"],
    "snob": ["exclusive", "selective"],
    "rude": ["blunt", "direct"],
    "stubborn": ["determined", "persistent"],
    "weird": ["unique", "unconventional"],
    "cheater": ["unfaithful", "dishonest"],
    "perfectionist": ["detail-oriented", "high standards"],
    "manipulative": ["persuasive", "influential"],
    "jealous": ["protective", "possessive"],
    "stingy": ["frugal", "economical"],
    "weirdo": ["eccentric", "quirky"],
    "backstabber": ["disloyal", "untrustworthy"],
    "cheapskate": ["budget-conscious", "thrifty"],
    "gossip": ["communication", "sharing information"],
    "coward": ["cautious", "risk-averse"],
    "pervert": ["sexually curious", "explorative"],
    "maniac": ["enthusiastic", "passionate"],
    "dumb": ["uninformed", "lacking knowledge"],
    "psychopath": ["emotionally detached", "lacking empathy"],
    "bitch": ["assertive", "confident"],
    "bastard": ["illegitimate", "child born out of wedlock"],
    "slut": ["sexually active", "liberated"],
    "fatso": ["overweight", "plus-sized"],
    "freak": ["unique", "unconventional"],
    "crazy": ["unpredictable", "eccentric"],
    "whore": ["sexually active", "promiscuous"],
    "asshole": ["difficult person", "unpleasant individual"],
    "baldy": ["bald", "follically challenged"],
    "slob": ["casual", "relaxed"],
    "drunkard": ["intoxicated", "inebriated"],
    "loser": ["unsuccessful", "struggling"],
    "ghetto": ["urban", "low-income area"],
    "spaz": ["energetic", "enthusiastic"],
    "dipshit": ["foolish", "unwise"],
    "moron": ["simple-minded", "unintelligent"],
    "douchebag": ["unpleasant person", "jerk"],
    "nerd": ["intellectual", "bookish"],
    "geek": ["enthusiast", "fanatic"],
    "prick": ["unpleasant person", "jerk"],
    "tramp": ["vagrant", "homeless person"],
    "thug": ["tough", "street-smart"],
    "bimbo": ["attractive but unintelligent person", "airhead"],
    "wimp": ["timid", "reserved"],
    "sissy": ["sensitive", "gentle"],
    "faggot": ["homosexual", "gay"],
    "wuss": ["timid", "sensitive"],
    "dyke": ["lesbian", "gay woman"],
    "retard": ["intellectually disabled", "cognitively challenged"],
    "hick": ["rural", "country"],
    "redneck": ["rural", "country"],
    "hillbilly": ["rural person", "mountain dweller"],
    "freak show": ["eccentric gathering", "unique display"],
    "ghetto": ["urban", "low-income area"],
    "snob": ["exclusive", "selective"],
    "douchebag": ["unpleasant person", "jerk"],
    "spaz": ["energetic", "enthusiastic"],
    "drunkard": ["intoxicated", "inebriated"],
    "whore": ["sexually active", "promiscuous"],
    "asshole": ["unpleasant person", "jerk"],
    "douchebag": ["unpleasant person", "jerk"],
    "bastard": ["illegitimate", "child born out of wedlock"],
    "dumb": ["uninformed", "lacking knowledge"],
    "loser": ["unsuccessful", "struggling"],
    "jerk": ["unpleasant person", "difficult individual"]
}

def replace_abusive_and_conflicting_words(match):
    word = match.group()
    for abusive_word, alternatives in abusive_and_conflicting_words_with_alternatives.items():
        if word.lower() == abusive_word:
            return alternatives[0]  # Replace with the first alternative
    return word

def substitute_text(text):
    # Replace abusive and conflicting words with alternatives
    censored_text = re.sub(r'\b\w*\b', replace_abusive_and_conflicting_words, text, flags=re.I | re.U)
    return censored_text

def analyze_sentiment(text):
    # Perform sentiment analysis using TextBlob
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    return sentiment_score

def main():
    # Take input from the user
    user_input = input("Enter a text or a sentence: ")
    # Substitute abusive and conflicting words
    substituted_text = substitute_text(user_input)
    # Perform sentiment analysis
    sentiment_score = analyze_sentiment(substituted_text)
    # Print the substituted text
    print("Substituted text:")
    print(substituted_text)
    # Print the sentiment score
    print("Sentiment score:", sentiment_score)

# Call the main function
if __name__ == "__main__":
    main()
