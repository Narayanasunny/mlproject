import logging
import os
from datetime import datetime

# 1. Create a folder named "logs" if it doesn't exist
LOG_FOLDER = "logs"
os.makedirs(LOG_FOLDER, exist_ok=True)

# 2. Create a log file with current date and time inside logs folder
LOG_FILE = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_FOLDER, LOG_FILE)

# 3. Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

