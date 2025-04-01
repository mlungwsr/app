# Sample App Runner Application

This is a simple Flask application configured to run on AWS App Runner.

## Local Development

1. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python app.py
   ```

4. Access the application at http://localhost:8080

## Deployment with AWS App Runner

This application is configured to be deployed with AWS App Runner. The `apprunner.yaml` file contains the configuration needed for AWS App Runner to build and run this application.

When connected to a code repository, AWS App Runner will:
1. Clone the repository
2. Install dependencies specified in requirements.txt
3. Start the application using the command specified in apprunner.yaml
4. Expose the application on the configured port (8080)
