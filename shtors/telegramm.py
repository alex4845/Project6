import telepot

token = '5735676241:AAHcn9LR9zeU5Xt9ZRsxRM8XdG312IWEJrc'
my_id = -1001739816541
telegramBot = telepot.Bot(token)


def send_message(text):
    telegramBot.sendMessage(-1001739816541, text)