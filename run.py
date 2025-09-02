import os
from app import create_app

# Create application instance
app = create_app(os.getenv('FLASK_ENV') or 'production')

if __name__ == '__main__':
    app.run()
