# Function to create the chatbot
def create_bot(name):
    from chatterbot import ChatBot
    Bot = ChatBot(
        name=name,
        read_only=False,
        logic_adapters=["chatterbot.logic.BestMatch"],
        storage_adapter="chatterbot.storage.SQLStorageAdapter"
    )
    return Bot

# Function to train the bot with a variety of topics
def train_all_data(Bot):
    from chatterbot.trainers import ChatterBotCorpusTrainer
    corpus_trainer = ChatterBotCorpusTrainer(Bot)
    corpus_trainer.train("chatterbot.corpus.english")

# Function to train the bot with custom data
def custom_train(Bot, conversation):
    from chatterbot.trainers import ListTrainer
    trainer = ListTrainer(Bot)
    trainer.train(conversation)

# Function to start and take responses from the chatbot
def start_chatbot(bot):
    print('\033c')
    print("Hello, I am Mido. How can I help you?")
    
    while True:
        user_input = input("me: ")
        
        if user_input.lower() == "mido":
            print("Mido: Welcome, Mido. Happy to have you at home.")
            
            # Train the bot with personal information
            personal_info = [
                "Where was I born?",
                "You were born in _________.",
                "What is my favorite book?",
                "That is easy. Your favorite book is ________.",
                "What is my favorite movie?",
                "You have watched _________ more times than I can count.",
                "What is my favorite sport?",
                "You have always loved ________."
            ]
            custom_train(bot, personal_info)
            
            # Continue with the program here
            # ...
        
        elif user_input.lower() == "ema":
            print("Mido: Ema is out right now, but you are welcome to the house.")
            # Continue with the program here
            # ...
        
        else:
            print("Mido: Your access is denied here.")
            exit()

# Create chatbot 
home_bot = create_bot('Mido')

# Train all data
train_all_data(home_bot)

# Check identity
identity = input("State your identity please: ")

# Rules for responding to different identities
if identity.lower() == "mido":
    print("Welcome, Mido. Happy to have you at home.")
elif identity.lower() == "ema":
    print("Mido is out right now, but you are welcome to the house.")
else:
    print("Your access is denied here.")
    exit()

# Custom data
house_owner = [
    "Who is the best one?",
    "Mido Tarek."
]
custom_train(home_bot, house_owner)

print("------ Training custom data ------")

# Train custom data if the identity is Mido
if identity.lower() == 'mido':   
    city_born = [
        "Where was I born?",
        "Mido, you were born in Egypt."
    ]

    fav_book = [
        "What is my favorite book?",
        "That is easy. Your favorite book is The Godfather."
    ]

    fav_movie = [
        "What is my favorite movie?",
        "You have watched The Godfather more times than I can count."
    ]

    fav_sports = [
        "What is my favorite sport?",
        "You have always loved coding."
    ]

    # Train chatbot with custom data
    custom_train(home_bot, city_born)
    custom_train(home_bot, fav_book)
