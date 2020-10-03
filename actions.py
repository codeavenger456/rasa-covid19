# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

import json
import requests

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

#########################################################################
# COVID-19 API Available Here
# https://documenter.getpostman.com/view/10808728/SzS8rjbc
#########################################################################


class ActionGetCovidCases(Action):

    def name(self) -> Text:
        return "action_get_covid_cases"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        country = tracker.latest_message["entities"][0]["value"]
        print(country)

        response = requests.get('https://api.covid19api.com/total/country/{}/status/confirmed'.format(country.lower()))
        response_json = json.loads(response.content)
        num_cases = response_json[-1]["Cases"]
        print(response.status_code)

        dispatcher.utter_message(text="There are {} total confirmed cases of COVID-19 in {}.".format(num_cases, country))

        return []
