# AI_Sales_ChatBot
Welcome to AI Sales Chatbot built with Rasa. This bot processes sales queries and predicts data. It features a user-friendly GUI. Feel free to clone, add stories, and train the bot with your data.
## Key Features:

- Sales Query Handling: The bot processes sales queries and provides responses.
- Sales Data Prediction: It predicts sales data based on time periods specified by users.
- GUI: A user-friendly Graphical User Interface is implemented using Tkinter.
- Customization: You're free to clone the project, add more conversational stories, and train the bot with your own data.

## Files

**Domain.yml**: Defines the chatbot's universe, including intents, actions, responses, and slots.

**Actions.py**: Contains custom Python code that the chatbot runs in response to specific intents.

**Stories.yml**: Defines the conversation paths that the chatbot can take.

**GUI.py**: Contains the code for the GUI where users interact with the bot.

## Installation and Setup

1. Clone this repository to your local machine.
2. Make sure you have Python 3.6 or newer installed.
3. Install Rasa and other dependencies using `pip install -r requirements.txt`.
4. Train the model by running `rasa train`.
5. Start the Rasa server with `rasa run`.
6. To interact with the bot, run `rasa shell` or run the `gui.py` script for a GUI interface.

## Contribution

Contributions are always welcome! Feel free to clone the project, add more conversational stories, and train the bot with your data.

This project provides a great opportunity to learn more about AI, Machine Learning, and how to integrate these into a functional chatbot. If you have any issues or questions, please open a GitHub issue or pull request. 

## License

This project is open-source.
