def create_bot(name):
    from chatterbot import ChatBot
    Bot = ChatBot(name=name,
                  read_only=False,
                  logic_adapters=["chatterbot.logic.BestMatch"],
                  storage_adapter="chatterbot.storage.SQLStorageAdapter")
    return Bot

# ... (other functions remain the same)

def start_chatbot(Bot):
    print('\033c')
    print("Hello, I am Mido. How can I help you?")  # Updated name in the introductory message
    bye_list = ["bye mido", "bye", "good bye"]  # Updated name in the bye_list
    
    while True:
        user_input = input("me: ")
        if user_input.lower() in bye_list:
            print("Mido: Good bye and have a blessed day!")  # Updated name in the goodbye message
            break
        
        response = Bot.get_response(user_input)
        print("Mido:", response)  # Updated name in the bot's responses