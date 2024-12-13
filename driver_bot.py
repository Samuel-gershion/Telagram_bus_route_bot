import telebot
import sqlite3

# API token for Driver Bot (Bot A)
API_TOKEN_A = 'your token'

# Initialize Driver Bot
bot_driver = telebot.TeleBot(API_TOKEN_A)

# Path to the shared database
db_path =  'database.db'

# Debugging message to verify bot is running
print("Driver Bot is running...")

# Function to initialize the SQLite database
def initialize_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS locations (
            driver_id TEXT PRIMARY KEY,
            location_link TEXT
        )
    ''')
    conn.commit()
    conn.close()
    print("Database initialized successfully.")

# Function to update the driver's location in the database
def update_location(driver_id, location_link):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO locations (driver_id, location_link)
        VALUES (?, ?)
    ''', (driver_id, location_link))
    conn.commit()
    conn.close()
    print(f"Location updated for driver_id: {driver_id}")

# Initialize the database when the bot starts
initialize_db()

# Start command for the driver to update their bus location link
@bot_driver.message_handler(commands=['start'])
def welcome_message(message):
    bot_driver.send_message(message.chat.id, "Welcome, Driver! Use /updatelocation to share your live location.")

# Command for driver to update their bus location link
@bot_driver.message_handler(commands=['updatelocation'])
def request_location_link(message):
    chat_id = message.chat.id
    bot_driver.send_message(chat_id, "Please send your live location link (any valid URL starting with http/https).")

    # Register the next message to get the link
    bot_driver.register_next_step_handler(message, process_location_update, chat_id)

# Process the location link sent by the driver and store it in the database
def process_location_update(message, chat_id):
    location_link = message.text

    # Check if the location link starts with "http" or "https"
    if location_link.startswith("http"):
        # Save the updated location in the database (using chat_id as driver_id)
        update_location(str(chat_id), location_link)
        bot_driver.send_message(chat_id, "Location updated successfully!")
        print(f"Location updated for chat_id {chat_id}: {location_link}")
    else:
        bot_driver.send_message(chat_id, "Invalid location link. Please send a valid URL starting with http or https.")

# Error handler for invalid commands
@bot_driver.message_handler(func=lambda message: True)
def handle_invalid_commands(message):
    bot_driver.send_message(message.chat.id, "Invalid command. Use /updatelocation to update location.")

# Start polling
bot_driver.polling()
