from typing import Dict
from kafka import KafkaConsumer
from kafka.errors import KafkaError
from common.config import BOOTSTRAP_SERVERS
from common.server import mcp


@mcp.tool()
def get_broker_info() -> Dict:
    """Get broker metadata."""
    try:
        consumer = KafkaConsumer(bootstrap_servers=BOOTSTRAP_SERVERS)
        metadata = consumer._client.cluster
        return {
            "brokers": [
                {"node_id": b.nodeId, "host": b.host, "port": b.port}
                for b in metadata.brokers()
            ]
        }
    except KafkaError as e:
        return {"error": str(e)}