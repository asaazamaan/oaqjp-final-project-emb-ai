# server.py
"""
This module defines a Flask web server for the Emotion Detector application.
It includes routes for emotion analysis and the index page.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Route to analyze the emotion of a given text.
    Fetches 'textToAnalyze' from the request, analyzes its emotions, 
    and returns a formatted string with the results.
    
    Returns:
        str: Formatted response with emotion scores and dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    return (
        f"For the given statement, the system response is 'anger': {response['anger']} "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Route for the main index page.
    
    Returns:
        str: Rendered HTML template for the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
