import httplib2
import urllib
import json
from twilio.rest import TwilioRestClient


ACCOUNT_SID = "AC00d803972b9362bffd5a61fcba4be148"
AUTH_TOKEN = "6c7db3ebade20bd9df3f5a9df92ddc82"

GOOGLE_API_KEY = "AIzaSyC0XYY3AWKWKQlQbwm1mzI0-K4_CoFCCrk"

BASE_URL = "https://www.googleapis.com/"
PATH = "language/translate/v2?"
KEY = "key=" + GOOGLE_API_KEY
PARAMETERS = "&source=en&"

http = httplib2.Http()

def translate(text, language="es"):
    text_encode = urllib.quote_plus(text)
    translate_url = BASE_URL + PATH + KEY + PARAMETERS + "target=" + language + "&q=" + text_encode
    response, body = http.request(translate_url, "GET")
    # Error handling 
    parsed_body = json.loads(body)
    translated_text = parsed_body["data"]["translations"][0]["translatedText"]

    print(translated_text)
    return translated_text
translate("I think I like this class!")
translate("I think I like this class!", "es")

def translate_multiple_texts(array, language_chosen):
    translated_arr = []
    for query in array:
        translated_arr.append(translate(query, language_chosen))
    print(translated_arr)
    return translated_arr

translate_multiple_texts(["HI, How are you?", "Nice", "Amazing"], "es")

def sendMessage(recipient, sender, text, chosen_language):
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    translated_text = translate(text, chosen_language)
    print(translated_text)
    try:
        message = client.messages.create(to=recipient, from_=sender, body=translated_text)
    except:
        print("error")


sendMessage(+1415939113, +14159801894, "Hey, how are you?", "zh-CN")
