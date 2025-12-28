from waitress import serve
from app import app
import main as backend

if __name__ == "__main__":
    # Ensure backend data is loaded
    backend.load_data()
    
    print("Starting production server on http://127.0.0.1:8080")
    serve(app, host='0.0.0.0', port=8080)
