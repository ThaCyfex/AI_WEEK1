"""
CryptoBuddy - Your Friendly Cryptocurrency Advisor 🤖💚
A simple rule-based chatbot that gives advice on crypto profitability and sustainability.
"""

import random

# ========== BOT PERSONALITY & DISCLAIMER ==========
BOT_NAME = "CryptoBuddy"
INTRO = f"""
👋 Hey there! I'm {BOT_NAME}, your friendly crypto sidekick.
Let's find you a green and growing crypto! 🌱📈

⚠️ Crypto is risky—always do your own research! This is not financial advice.
"""

# ========== PREDEFINED CRYPTO DATASET ==========
# You can add more coins here easily!
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

# ========== CHATBOT LOGIC ==========
def get_most_sustainable():
    """Return the most sustainable crypto."""
    return max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])

def get_most_profitable():
    """Return the most profitable crypto (rising trend, high market cap)."""
    candidates = [k for k, v in crypto_db.items() if v["price_trend"] == "rising" and v["market_cap"] == "high"]
    if candidates:
        return candidates[0]
    # fallback: any rising
    rising = [k for k, v in crypto_db.items() if v["price_trend"] == "rising"]
    return rising[0] if rising else list(crypto_db.keys())[0]

def process_query(user_query):
    user_query = user_query.lower()
    if "sustainable" in user_query or "eco" in user_query or "green" in user_query:
        coin = get_most_sustainable()
        return f"Invest in {coin}! 🌱 It’s eco-friendly and has long-term potential!"
    elif "trend" in user_query or "rising" in user_query or "up" in user_query:
        rising = [k for k, v in crypto_db.items() if v["price_trend"] == "rising"]
        return f"Trending up: {', '.join(rising)} 🚀" if rising else "No coins are trending up right now."
    elif "profit" in user_query or "grow" in user_query or "return" in user_query:
        coin = get_most_profitable()
        return f"For growth, check out {coin}! It's showing strong momentum."
    elif "advice" in user_query or "recommend" in user_query or "suggest" in user_query:
        coin = get_most_sustainable()
        return f"Based on sustainability, {coin} is a great choice!"
    elif "help" in user_query:
        return ("I can help with:\n- Finding sustainable cryptos\n- Identifying profitable coins\n- Recommending based on your goals\nTry: 'What's the most eco-friendly crypto?' or 'Recommend a long-term investment'")
    elif any(word in user_query for word in ["bye", "exit", "quit"]):
        return "Happy investing! Remember: only invest what you can afford to lose! 💸"
    else:
        return ("Sorry, I didn't get that.\nTry asking about sustainable cryptos, trending coins, or type 'help' for options!")

# ========== MAIN INTERFACE ==========
def main():
    print(INTRO)
    while True:
        user = input("\nYou: ")
        if user.lower() in ["exit", "quit", "bye"]:
            print("\nCryptoBuddy: Happy investing! 💸")
            break
        response = process_query(user)
        print(f"\n{BOT_NAME}: {response}")

if __name__ == "__main__":
    main()