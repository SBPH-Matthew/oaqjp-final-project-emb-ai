import requests
import json


def emotion_detector(text_to_analyze):
    # Define the URL and headers
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    # Handle blank input early
    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    # Send request
    response = requests.post(url, headers=headers, json=input_json)

    # If API returns error (e.g., 400 Bad Request)
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    # Convert JSON response
    response_dict = json.loads(response.text)
    emotion_scores = response_dict["emotionPredictions"][0]["emotion"]

    # Extract emotions
    anger = emotion_scores["anger"]
    disgust = emotion_scores["disgust"]
    fear = emotion_scores["fear"]
    joy = emotion_scores["joy"]
    sadness = emotion_scores["sadness"]

    # Determine dominant emotion
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Return formatted output
    return {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion,
    }
