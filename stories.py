version: "3.1"

stories:

- story: happy path
  steps:
  - intent: greet
  - action: utter_greet
  - intent: mood_great
  - action: utter_happy

- story: sad path 1
  steps:
  - intent: greet
  - action: utter_greet
  - intent: mood_unhappy
  - action: utter_cheer_up
  - action: utter_did_that_help
  - intent: affirm
  - action: utter_happy

- story: sad path 2
  steps:
  - intent: greet
  - action: utter_greet
  - intent: mood_unhappy
  - action: utter_cheer_up
  - action: utter_did_that_help
  - intent: deny
  - action: utter_goodbye

- story: Sales Query Path
  steps:
  - intent: greet
  - action: utter_greet
  - intent: sales_query
  - action: action_process_sales_query
  - intent: goodbye
  - action: utter_goodbye

- story: User asks for sales data and provides time period
  steps:
  - intent: greet
  - action: utter_greet
  - intent: ask_sales
  - action: utter_ask_time_period
  - intent: provide_time_period
  - action: action_process_sales_data
  - intent: goodbye
  - action: utter_goodbye

- story: User asks for sales prediction and provides prediction period
  steps:
  - intent: greet
  - action: utter_greet
  - intent: ask_sales_prediction
  - action: utter_ask_prediction_period
  - intent: provide_prediction_period
  - action: action_process_sales_prediction
  - intent: goodbye
  - action: utter_goodbye

- story: User asks for sales data, then asks for sales prediction
  steps:
  - intent: greet
  - action: utter_greet
  - intent: ask_sales
  - action: utter_ask_time_period
  - intent: provide_time_period
  - action: action_process_sales_data
  - intent: ask_sales_prediction
  - action: utter_ask_prediction_period
  - intent: provide_prediction_period
  - action: action_process_sales_prediction
  - intent: goodbye
  - action: utter_goodbye
