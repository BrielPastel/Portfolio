from controllers.app_controller import create_app
from utils.create_db import create_db

#criar db no MySQL
#CREATE DATABASE ra3;

if __name__ == "__main__":
    app = create_app()
    create_db(app)
    app.run(host='0.0.0.0', port=8080, debug=False)
