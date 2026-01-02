import os
from pathlib import Path
from dotenv import load_dotenv

# Get the project root directory (one level up from task/)
PROJECT_ROOT = Path(__file__).parent.parent.absolute()

# Load environment variables from .env file in project root
env_path = PROJECT_ROOT / ".env"
# Try loading from project root, if not found, try current directory
loaded = load_dotenv(dotenv_path=env_path)
if not loaded:
    # Fallback: try loading from current directory
    load_dotenv()

DIAL_URL = "https://ai-proxy.lab.epam.com"
API_KEY = os.getenv("DIAL_API_KEY", "")
