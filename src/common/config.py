from dotenv import load_dotenv
import os

load_dotenv()

MCP_TRANSPORT = os.getenv('MCP_TRANSPORT', 'stdio')

BOOTSTRAP_SERVERS = os.getenv('BOOTSTRAP_SERVER', 'localhost:9092')
