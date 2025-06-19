from kafka import KafkaConsumer
from kafka.errors import KafkaError
from common.config import BOOTSTRAP_SERVERS
from common.server import mcp

REPLICATION_FACTOR = 1


@mcp.tool()
def topic_exists(name: str) -> bool:
    """Check if a topic exists."""
    try:
        consumer = KafkaConsumer(bootstrap_servers=BOOTSTRAP_SERVERS)
        return name in consumer.topics()
    except KafkaError:
        return False


