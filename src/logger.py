import logging
import os
from datetime import datetime

#file name is created with this format
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
#create log file with path
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
#even though there is a file keep on appending on that folder
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)

