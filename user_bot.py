import telebot
import sqlite3

# API token for User Bot (Bot B)
API_TOKEN_B = 'your token'

# Initialize User Bot
bot_user = telebot.TeleBot(API_TOKEN_B)

# Path to the shared database (must be the same as Driver Bot's database)
db_path = 'database.db'

# Function to retrieve the latest location for a given driver_id
def get_latest_location(driver_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Fetch the location link for the given driver_id
    cursor.execute('SELECT location_link FROM locations WHERE driver_id = ?', (driver_id,))
    result = cursor.fetchone()
    conn.close()

    # Return the location link if found, else None
    return result[0] if result else None

# Start command to greet the user
@bot_user.message_handler(commands=['start'])
def welcome_message(message):
    bot_user.send_message(message.chat.id, "Welcome! Use /find to get the live location of the bus.")

# Command to share the dynamically updated Google Maps live location link
@bot_user.message_handler(commands=['find'])
def share_location(message):
    # Replace 'YOUR_DRIVER_ID' with the driver's chat ID from Driver Bot
    driver_id = str(message.chat.id)  # For testing purposes, use the user's chat_id as driver_id
    live_location_link = get_latest_location(driver_id)

    if live_location_link:
        bot_user.send_message(message.chat.id, f"Here is the live location: {live_location_link}")
    else:
        bot_user.send_message(message.chat.id, "Sorry, the driver hasn't updated the location yet.")

# Error handler for invalid commands
@bot_user.message_handler(func=lambda message: True)
def handle_invalid_commands(message):
    bot_user.send_message(message.chat.id, "Invalid command. Use /find to get the bus location.")

# Start polling
bot_user.polling()
