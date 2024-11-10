import requests, json 

def emotion_detector(text_to_analyse): 
    URL= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input_json= { "raw_document": { "text": text_to_analyse } }
    response = requests.post(URL, json = Input_json, headers=Headers) 
    formated_response = json.loads(response.text) 

    emotions = formated_response.get("emotionPredictions", [])[0].get("emotion", {})
    
    dominant_emotion = max(emotions, key=emotions.get)
    
    return {
        'anger': emotions.get('anger', 0),
        'disgust': emotions.get('disgust', 0),
        'fear': emotions.get('fear', 0),
        'joy': emotions.get('joy', 0),
        'sadness': emotions.get('sadness', 0),
        'dominant_emotion': dominant_emotion
    }