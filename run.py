import os
from app import create_app

# Explicitly set the config name
config_name = 'production'

# Create application instance  
app = create_app(config_name)

# Make sure config is loaded
if app.config.get('CAT_API_URL') is None:
    app.config['CAT_API_URL'] = 'https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}'

if __name__ == '__main__':
    app.run()
