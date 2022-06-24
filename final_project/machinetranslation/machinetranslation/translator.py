from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('pzxRb7KAD6hAyBoMzYJ03TA5VsGiv500NpHNoAFy7QQ-')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com')

def english_To_French(englishtext):
    """Text translated to French from English"""
    if englishtext is None:
        return None
    else:
        trans_res = language_translator.translate(\
            text=englishtext, model_id='en-fr')
        translation = trans_res.get_result()
        french_text = translation['translations'][0]['translation']
        return french_text

def french_To_English(french_text):
    """Text translated to English from French"""
    if french_text is None:
        return None
    else:
        trans_res = language_translator.translate(\
            text=french_text, model_id='fr-en')
        translation = trans_res.get_result()
        english_text = translation['translations'][0]['translation']
        return english_text