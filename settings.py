from dotenv import load_dotenv
import os
load_dotenv()


LUMU_CLIENT_KEY=os.getenv("LUMU_CLIENT_KEY")
COLLECTOR_ID=os.getenv("COLLECTOR_ID")
API_URL=os.getenv("API_URL")