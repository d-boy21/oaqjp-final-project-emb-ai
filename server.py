"""
This module provides functionality for detecting emotions in text.

Functions:
- emotion_detector: Analyzes text and returns the dominant emotion.

Usage:
Import this module and use the emotion_detector function to analyze the emotions in a given string.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():

    """
    Analyzes the given text and returns the dominant emotion.

    Parameters:
    text (str): The input text to analyze.

    Returns:
    str: The dominant emotion detected in the text.
    """

    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid input! Try again."

    return (
        f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, "
        f"'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}."
        f"The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """
    Renders the index page template
    Returns:
    template: the index page tempalte.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
