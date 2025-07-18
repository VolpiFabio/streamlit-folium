from dotenv import load_dotenv
import os

load_dotenv()

def geoserver_url():
    return os.getenv("GEOSERVER_URL")
