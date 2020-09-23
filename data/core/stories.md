## happy path
* greet
  - utter_greet
  - utter_how_are_you
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
  - utter_how_are_you
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
  - utter_how_are_you
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## chitchat
* chitchat
  - respond_chitchat

## out of scope
* out_of_scope
  - action_freestyle

## covid
* COVID
  - respond_COVID