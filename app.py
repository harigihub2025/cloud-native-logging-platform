from flask import Flask
import logging
import time

app = Flask(__name__)

# Application logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


@app.route("/")
def home():
    app.logger.info("Home page accessed")
    return "Cloud-Native Centralized Logging Platform is running!"


@app.route("/health")
def health():
    app.logger.info("Health check successful")
    return "Application is Healthy"


@app.route("/logs")
def generate_logs():
    app.logger.info("Starting log generation")

    for i in range(5):
        app.logger.info(f"Processing request {i + 1}")
        time.sleep(1)

    app.logger.info("Log generation completed")

    return "Logs generated successfully"


@app.route("/error")
def generate_error():
    app.logger.error("Sample application error generated")
    return "Error logged successfully", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)