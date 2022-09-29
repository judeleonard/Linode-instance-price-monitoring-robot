from typing import Optional
from dotenv import load_dotenv
import os

load_dotenv()

SENDER: Optional[str] = os.environ.get("SENDER")
PASSWORD: Optional[str] = os.environ.get("PASSWORD")
TARGET_WEBSITE: Optional[str] = os.environ.get("TARGET_WEBSITE")
