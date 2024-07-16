from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    Renders the index.html page.

    Returns:
        Response object with the rendered index.html page.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    """
    Processes the text sent in the POST request and returns the emotion analysis.

    Returns:
        JSON response with the emotion analysis or an error message if the input is invalid.
    """
    data = request.json
    text_to_analyze = data.get('text', '')
    result = emotion_detector(text_to_analyze)
    
    if result['dominant_emotion'] is None:
        return jsonify({"error": "Invalid text! Please try again!"}), 400
    else:
        response = {
            "anger": result['anger'],
            "disgust": result['disgust'],
            "fear": result['fear'],
            "joy": result['joy'],
            "sadness": result['sadness'],
            "dominant_emotion": result['dominant_emotion']
        }
        return jsonify(response)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
