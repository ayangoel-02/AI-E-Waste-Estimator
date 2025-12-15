from mangum import Mangum
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from src.app import app

#handler = Mangum(app)
handler = Mangum(app, api_gateway_base_path="/api")

