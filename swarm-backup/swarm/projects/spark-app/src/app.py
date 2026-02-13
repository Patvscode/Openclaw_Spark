from flask import Flask, render_template
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Register blueprints - import after app creation to avoid circular imports
try:
    from api.status import status_bp
    app.register_blueprint(status_bp)
except ImportError as e:
    print(f"Warning: status API not loaded: {e}")

try:
    from api.tasks import tasks_bp
    app.register_blueprint(tasks_bp)
except ImportError as e:
    print(f"Warning: tasks API not loaded: {e}")

try:
    from api.findings import findings_bp
    app.register_blueprint(findings_bp)
except ImportError as e:
    print(f"Warning: findings API not loaded: {e}")

try:
    from api.training import training_bp
    app.register_blueprint(training_bp)
except ImportError as e:
    print(f"Warning: training API not loaded: {e}")

@app.route('/')
def dashboard():
    # Render the dashboard template
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run(debug=app.config.get('DEBUG', False))
