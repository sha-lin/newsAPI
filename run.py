import os
from app import create_app

# Set the configuration environment
config_name = os.getenv('FLASK_ENV', 'production')

# Create application instance
app = create_app(config_name)

if __name__ == '__main__':
    app.run()
