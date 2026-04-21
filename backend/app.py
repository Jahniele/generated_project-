from flask import Flask
from flask_cors import CORS
from routes.auth import auth_bp
from routes.dashboard import dashboard_bp
from routes.customers import customers_bp

app = Flask(__name__)
CORS(app)

app.config["SECRET_KEY"] = "supersecretkey"

# Register routes
app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(dashboard_bp, url_prefix="/api/dashboard")
app.register_blueprint(customers_bp, url_prefix="/api/customers")

if __name__ == "__main__":
    app.run(debug=True)
