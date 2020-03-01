# This bot script was written by Codefred from Fiverr

# A luckydraw bot 

# Importing the needed libraries
import os
import telebot
from telebot import types
import emoji
from random import choice
import telegram
from datetime import date
from flask import Flask, request

# Server
server = Flask(__name__)

# Initializing the bot
token = '1083080676:AAHU7aAZtHnIH-mX0JW1gq7vs9Sfi7w9fOs'

# Needed variables for the application
message_id = '' #previous message to be deleted

luckyNumbers = [choice(range(1,501)) for i in range(30)] # random 30 numbers in range(500)

drawNumbers = [i for i in range(1,501)]

winners = {} # dictionary of winners  
members = [] # username of lucky draws

participants = {} # Unlucky memebers

chat = '' # Instance Chat
user = '' # Instance User

bot = telebot.TeleBot(token=token, threaded=True)

@bot.message_handler(commands=['start'])
def start(msg):
    "Sending Welcome to Bot Message"

    global user
    global chat
    global message_id
    
    if msg.from_user.username is None:
        bot.send_message("Sorry! You are only qualified for a lucky draw if you have username.")
    else:
        chat = msg.chat.id
        user = msg.from_user
        message_id = msg.message_id
        beginning()


def beginning():
    """
    Starting the Lottery
    """

    global message_id

    # Keyboard Input
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    a = types.InlineKeyboardButton(text=emoji.emojize(":gift:Lucky Draw:gift:", use_aliases=True), callback_data="1")
    keyboard.add(a)

    # Ask Request
    bot.send_message(
        user.id,
        emoji.emojize(f"""
        Hello {user.username},

        :fire: Welcome to JanjiLuckyBot :fire:
        """,
        use_aliases=True),
        reply_markup=keyboard
        )

        # Deleting previous message
    bot.delete_message(chat, message_id)
    message_id = int(message_id) + 1
    return message_id


def get_lucky():
    "Identifying Each User For The Lucky Draw"

    global message_id

    #Keyboard
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    a = types.InlineKeyboardButton(text=emoji.emojize(":slot_machine: Try Your Luck :slot_machine:", use_aliases=True), callback_data="2")
    b = types.InlineKeyboardButton(text=emoji.emojize(" Back To Menu :arrow_left:", use_aliases=True), callback_data="3")
    keyboard.add(a, b)

    # Lucky draw board
    bot.send_message(
        user.id,
        emoji.emojize(f"""
        :fire: JanjiLuckyBot Lottery :fire:


    :hourglass: <b>Event</b>: 00.00AM ~ 23.59PM (16/2/2020)

    :alarm_clock: <b>At 12PM, new winners can claim</b>

    :gift: <b>30 Gifts 5 Credits Free ID</b>

    Contact at ; @JanjiLuckyBot


    :one: Your Lucky Number - A Lucky Draw Number would be generated for you when you press the <b>Try Your Luck</b> button

    :two: Gifts - Gifts provided by Admin, each gift has its own <b>Lucky Number</b>

    :three: If your <b>Lucky Number</b> is the same as the gift code number, your name will be on the <b>Winners Member</b> List and eligible for the prize
    
    :four: To those customers whose <b>Lucky Draw Number</b> doesn't match the gift code, your name will be on the <b>Last 20 Participants</b> list

        """,
        use_aliases=True),
        parse_mode=telegram.ParseMode.HTML,
        reply_markup=keyboard
        )

    # Deleting previous message
    bot.delete_message(chat, message_id)

    message_id = int(message_id) + 1
    return message_id


def lottery():
    "Identifying Each User For The Lucky Draw"

    global message_id
    global members
    global winners
    global participants

    if user.username not in members:

        #register user into members
        userNumber = choice(drawNumbers)
        drawNumbers.remove(userNumber)

        members.append(user.username) # Update Users Registered
        
        # Update user information
        dict = {user.username: userNumber}

        # Check if he/her is lucky
        if userNumber in luckyNumbers:

            winners.update(dict)

        else:

            participants.update(dict)

    display_result()


def display_result():
    """
    Lottery Results
    """
    
    global message_id


    # Deleting previous message
    bot.delete_message(chat, message_id)

    #Keyboard
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    a = types.InlineKeyboardButton(text=emoji.emojize(":phone: Contact :phone:", use_aliases=True), callback_data="4")
    b = types.InlineKeyboardButton(text=emoji.emojize(" Back To Menu :arrow_left:", use_aliases=True), callback_data="5")
    keyboard.add(a, b)

    today = date.today()
    
    if user.username in winners:
        value = winners[user.username]

    else:
        value = participants[user.username]

    win_data = ["@{}(Lucky No. {}), ".format(each, winners[each]) for each in list(winners.keys())]
    loss_data = ["@{}(Lucky No. {}), ".format(each, participants[each]) for each in list(participants.keys())] # Lossers list

    # Main Draw board
    bot.send_message(
        user.id,
        emoji.emojize(f"""
        :slot_machine: JanjiLuckyBot Lottery :slot_machine:

    :alarm_clock: <b>{today} Lucky Draw Event</b>

    :one: If your name is on the <b>Winner Member List</b>, it means you have won the prize

    :two: Claim by contacting ---- between 11.59PM - 12AM ({today}), after which no claim can be made again


    :8ball: <b>Your Lucky Number is {value}</b>

    <b>
    Gifts:
    No 1. FREE 5 (Lucky no: {luckyNumbers[0]})
    No 2. FREE 5 (Lucky no: {luckyNumbers[1]})
    No 3. FREE 5 (Lucky no: {luckyNumbers[2]})
    No 4. FREE 5 (Lucky no: {luckyNumbers[3]})
    No 5. FREE 5 (Lucky no: {luckyNumbers[4]})
    No 6. FREE 5 (Lucky no: {luckyNumbers[5]})
    No 7. FREE 5 (Lucky no: {luckyNumbers[6]})
    No 8. FREE 5 (Lucky no: {luckyNumbers[7]})
    No 9. FREE 5 (Lucky no: {luckyNumbers[8]})
    No 10. FREE 5 (Lucky no: {luckyNumbers[9]})
    No 11. FREE 5 (Lucky no: {luckyNumbers[10]})
    No 12. FREE 5 (Lucky no: {luckyNumbers[11]})
    No 13. FREE 5 (Lucky no: {luckyNumbers[12]})
    No 14. FREE 5 (Lucky no: {luckyNumbers[13]})
    No 15. FREE 5 (Lucky no: {luckyNumbers[14]})
    No 16. FREE 5 (Lucky no: {luckyNumbers[15]})
    No 17. FREE 5 (Lucky no: {luckyNumbers[16]})
    No 18. FREE 5 (Lucky no: {luckyNumbers[17]})
    No 19. FREE 5 (Lucky no: {luckyNumbers[18]})
    No 20. FREE 5 (Lucky no: {luckyNumbers[19]})
    No 21. FREE 5 (Lucky no: {luckyNumbers[20]})
    No 22. FREE 5 (Lucky no: {luckyNumbers[21]})
    No 23. FREE 5 (Lucky no: {luckyNumbers[22]})
    No 24. FREE 5 (Lucky no: {luckyNumbers[23]})
    No 25. FREE 5 (Lucky no: {luckyNumbers[24]})
    No 26. FREE 5 (Lucky no: {luckyNumbers[25]})
    No 27. FREE 5 (Lucky no: {luckyNumbers[26]})
    No 28. FREE 5 (Lucky no: {luckyNumbers[27]})
    No 29. FREE 5 (Lucky no: {luckyNumbers[28]})
    No 30. FREE 5 (Lucky no: {luckyNumbers[29]})
    </b>

    :heavy_minus_sign: :heavy_minus_sign: :heavy_minus_sign: :heavy_minus_sign: :heavy_minus_sign: :heavy_minus_sign:

    :trophy: <b>Winner Members List</b> :trophy:

    {','.join(each for each in win_data)}


    :heavy_minus_sign: :heavy_minus_sign: :heavy_minus_sign: :heavy_minus_sign: :heavy_minus_sign: :heavy_minus_sign:

    :busts_in_silhouette: <b>Winner Members List</b>


    {','.join(each for each in loss_data[:20])}

        """,
        use_aliases=True),
        parse_mode=telegram.ParseMode.HTML,
        reply_markup=keyboard
        )

    message_id = int(message_id) + 1


def contact():
    """
    Contact information
    """
    global message_id

    # Deleting previous message
    bot.delete_message(chat, message_id)

    #Keyboard
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    a = types.InlineKeyboardButton(text=emoji.emojize(" Back To Menu :arrow_left:", use_aliases=True), callback_data="2")
    keyboard.add(a)

    # Main Draw board
    bot.send_message(
        user.id,
        emoji.emojize(f"""
        :fire: JanjiLuckyBot Contact :fire:

    :alarm_clock: <b>Telegram</b>:

    :alarm_clock: <b>WhatsApp</b>:

    :alarm_clock: <b>WeChat</b>:

    :alarm_clock: <b>Website</b>:


        """,
        use_aliases=True),
        parse_mode=telegram.ParseMode.HTML,
        reply_markup=keyboard
        )

    message_id = int(message_id) + 1

# Callback Handlers
@bot.callback_query_handler(func=lambda call: True)
def callback_answer(call):
    """
    Button Response
    """

    if call.data == "1":
        get_lucky()

    elif call.data == "2":
        lottery()

    elif call.data == "3":
        beginning()
    
    elif call.data == "4":
        contact()

    elif call.data == "5":
        get_lucky()
    
    else:
        bot.send_message(user.id, "Wrong Input Content!! ")



# Development server
print("Bot running.....")
bot.remove_webhook()
bot.polling(none_stop=True)



# Production server
@server.route('/' + token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "Lucky Draw Bot Running!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://obscure-island-36357.herokuapp.com/' + token)
    return "Lucky Draw Bot Active!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

