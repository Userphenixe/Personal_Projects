import requests
import json
def emotion_detector(text_to_analyze):
    result = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }

    if not text_to_analyze:
        return result

    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    my_object = {"raw_document": {"text": text_to_analyze}}
    Header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(URL, json=my_object, headers=Header)

    if response.status_code == 400:
        return result

    json_response = json.loads(response.text)
    for item in json_response['emotionPredictions']:
        emotion_scores = item['emotion']
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        result = {
            'anger': emotion_scores['anger'],
            'disgust': emotion_scores['disgust'],
            'fear': emotion_scores['fear'],
            'joy': emotion_scores['joy'],
            'sadness': emotion_scores['sadness'],
            'dominant_emotion': dominant_emotion
        }

    return result
