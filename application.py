from flask import Flask

# Elastic Beanstalk looks for an 'application' object
application = Flask(__name__)

@application.route('/')
def hello_world():
    return '''
    <html>
        <head>
            <title>Elastic Beanstalk App</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                }
                .container {
                    text-align: center;
                    padding: 40px;
                    background: rgba(255, 255, 255, 0.1);
                    border-radius: 10px;
                    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
                }
                h1 {
                    font-size: 3em;
                    margin-bottom: 20px;
                }
                p {
                    font-size: 1.2em;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🎉 Success!</h1>
                <p>Your Elastic Beanstalk application is running!</p>
                <p>Deployed via CI/CD Pipeline with AWS CodePipeline</p>
            </div>
        </body>
    </html>
    '''

@application.route('/health')
def health():
    return {'status': 'healthy'}, 200

# For local development
if __name__ == '__main__':
    application.run(host='0.0.0.0', port=80, debug=True)
