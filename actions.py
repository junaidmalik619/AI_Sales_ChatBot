# Custom actions for the Rasa bot.

from rasa_sdk import Action
import pandas as pd

class ActionProcessSalesQuery(Action):
    def name(self):
        return "action_process_sales_query"

    def run(self, dispatcher, tracker, domain):
        # Logic for processing the sales query here
        # Placeholder: read a CSV file and get the sum of a column

        df = pd.read_csv('sales_data.csv')
        total_sales = df['sales_amount'].sum()

        response = f"Total sales amount: {total_sales}"

        dispatcher.utter_message(text=response)

        return []
