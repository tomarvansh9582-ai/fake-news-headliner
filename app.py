import random

# =========================
# Funny Headline Templates
# =========================

templates = [
    "{celebrity} accidentally becomes CEO of {company} after clicking 'Accept All Cookies'",
    "{country} declares {object} a national treasure after it wins an argument on WhatsApp",
    "Scientists confirm {animal} has been judging humans since 2012",
    "{politician} promises to fix traffic using {object} and positive vibes",
    "{company} launches subscription plan for breathing near its headquarters",
    "Man spends {number} hours watching productivity videos and achieves absolutely nothing",
    "{celebrity} caught arguing with a microwave over life choices",
    "{country} introduces a new tax on people who say 'bro trust me'",
    "{animal} elected mayor after outperforming all human candidates",
    "Experts warn that eating {food} while reading comments may cause existential damage",
    "{company} accidentally sends memes to the entire board of directors",
    "{politician} blames {object} for missing a deadline by three years",
    "{celebrity} announces retirement from being dramatic and returns 12 minutes later",
    "{country} bans Monday mornings and happiness levels increase by 87%",
    "New study reveals {animal} is secretly running customer support departments",
    "{company} replaces meetings with staring silently at a loading screen",
    "{celebrity} writes an apology letter to {object} and the internet demands a sequel",
    "{politician} challenges {celebrity} to a chess match and loses to the timer",
    "{country} reports a mysterious shortage of common sense",
    "Local man invents an app that reminds him to open reminder apps",
    "Scientists discover that {food} tastes better when someone else pays",
    "{company} unveils AI that specializes in making group projects worse",
    "{celebrity} spotted taking career advice from a pigeon",
    "{country} launches a space mission to find who asked",
    "{animal} files a complaint against humans for excessive nonsense",
    "{politician} accidentally leaks a playlist titled 'Speeches I Hope Nobody Hears'",
    "{company} introduces premium silence for only $9.99 per month",
    "Breaking: {food} officially defeats diet plans in a landslide victory",
    "{celebrity} confirms they also ignore alarm clocks",
    "Researchers conclude that {object} has better emotional stability than most group chats"
]

# =========================
# Data Lists
# =========================

celebrities = [
    "Elon Musk", "Taylor Swift", "Cristiano Ronaldo", "Lionel Messi",
    "Virat Kohli", "Rohit Sharma", "MS Dhoni", "Jasprit Bumrah",
    "Shah Rukh Khan", "Salman Khan", "Aamir Khan", "Ranbir Kapoor",
    "Ranveer Singh", "Hrithik Roshan", "Akshay Kumar", "Ajay Devgn",
    "Deepika Padukone", "Alia Bhatt", "Kiara Advani", "Kartik Aaryan",
    "Tom Cruise", "Ryan Reynolds", "Keanu Reeves", "Zendaya",
    "Margot Robbie", "Beyoncé", "Ariana Grande", "Ed Sheeran",
    "Justin Bieber", "Billie Eilish", "MrBeast", "PewDiePie",
    "Mark Zuckerberg", "Sundar Pichai", "Satya Nadella", "Sam Altman",
    "Narendra Modi", "Donald Trump", "Barack Obama", "Rajinikanth",
    "Allu Arjun", "Prabhas", "Rashmika Mandanna", "Kapil Sharma",
    "CarryMinati", "Bhuvan Bam"
]

countries = [
    "India", "Japan", "Canada", "Germany", "Australia",
    "Brazil", "France", "Italy", "South Korea", "New Zealand"
]

companies = [
    "Google", "Meta", "Amazon", "Tesla", "OpenAI",
    "Microsoft", "Apple", "Netflix", "SpaceX", "Samsung"
]

politicians = [
    "a minister", "a senator", "a mayor", "a governor",
    "a parliament member", "a spokesperson"
]

animals = [
    "a pigeon", "a cat", "a dog", "a monkey", "a goat",
    "a cow", "a crow", "a squirrel", "a penguin", "a camel"
]

foods = [
    "samosa", "pizza", "momos", "jalebi", "paneer",
    "biryani", "maggi", "golgappa", "burger", "chai"
]

objects = [
    "a toaster", "a potato", "a traffic cone", "a selfie stick",
    "a pressure cooker", "a drone", "a rubber duck", "a shopping cart",
    "an umbrella", "a giant spoon"
]

numbers = [3, 7, 12, 18, 24, 36, 48, 72, 100, 999]

# =========================
# Headline Generator
# =========================

def generate_headline():
    template = random.choice(templates)

    return template.format(
        celebrity=random.choice(celebrities),
        country=random.choice(countries),
        company=random.choice(companies),
        politician=random.choice(politicians),
        animal=random.choice(animals),
        food=random.choice(foods),
        object=random.choice(objects),
        number=random.choice(numbers)
    )

# =========================
# Main Program
# =========================

print("=" * 60)
print("        📰 FAKE NEWS HEADLINE GENERATOR 😂")
print("=" * 60)

for i in range(10):
    print(f"{i+1}. {generate_headline()}")