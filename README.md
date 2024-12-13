# Telagram_bus_route_bot
bus tracker
Bus Location Tracker Bot
This project consists of two Telegram bots (Driver Bot and User Bot) that work together to provide real-time bus location tracking. The bots are built using the Python-telebot library and store location data in a shared SQLite database. It allows drivers to update their live bus location, and users to request the location of specific buses.

Features
Driver Bot:

Allows drivers to register their bus location by sending a Google Maps live location link.
Drivers can update their bus locations anytime using their bus ID.
The location data is saved in an SQLite database for future reference.
User Bot:

Users can query live bus locations by providing the bus ID.
Retrieves the latest location for the given bus ID from the database.
Shares the live Google Maps link for the requested bus location.
Technologies Used
Python: Backend programming language for bot development.
Python-telebot: Library for building Telegram bots.
SQLite: Lightweight database to store bus location data.
Google Maps: Used for generating live location links.
Database Structure
The database consists of two tables:

buses:
bus_id: Unique identifier for each bus.
bus_name: Name of the bus (optional).
locations:
bus_id: Identifier for the bus associated with the location.
driver_id: Unique identifier for each driver.
location_link: Google Maps live location link for the bus.
How It Works
Driver Bot:

The driver sends a command /updatelocation <bus_id> <location_link>, where <location_link> is a live Google Maps link.
The bot updates the database with the bus ID and driver ID, storing the location link.
User Bot:

The user sends the command /find <bus_id>.
The bot retrieves the latest location for the bus from the database and sends the Google Maps link.
Getting Started
To run this project locally, you need to:

Install the required Python libraries:

bash
Copy code
pip install pyTelegramBotAPI sqlite3
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/bus-location-tracker.git
Update the API_TOKEN_A and API_TOKEN_B with your bot tokens from BotFather.

Ensure the SQLite database is created using the initialize_db() function before running the bots.

Contributing
Feel free to fork the repository, open issues, and contribute. Improvements such as adding more features, optimizing the code, or enhancing the user experience are always welcome.

License
