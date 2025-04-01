from flask import Flask, jsonify
import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Flask application
app = Flask(__name__)

@app.route('/')
def home():
    logger.info("Home endpoint accessed")
    return jsonify({
        "status": "success",
        "message": "Hello from AWS App Runner!"
    })

@app.route('/health')
def health():
    logger.info("Health check endpoint accessed")
    return jsonify({
        "status": "healthy"
    })

# This block is only used when running with 'python app.py' directly
# When using Gunicorn, this block is not executed
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    logger.info(f"Starting application on port {port}")
    app.run(host='0.0.0.0', port=port)
