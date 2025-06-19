from kafka import TopicPartition
from kafka.admin import KafkaAdminClient
from typing import Dict
from kafka import KafkaConsumer
from kafka.errors import KafkaError
from common.config import BOOTSTRAP_SERVERS
from common.server import mcp


@mcp.tool()
def get_group_offsets(group_id: str) -> Dict:
    """Fetch committed offsets for a consumer group."""
    try:
        admin = KafkaAdminClient(bootstrap_servers=BOOTSTRAP_SERVERS)
        offsets = admin.list_consumer_group_offsets(group_id)
        results = {}
        for tp, meta in offsets.items():
            results[f"{tp.topic}-{tp.partition}"] = meta.offset
        return results
    except KafkaError as e:
        return {"error": str(e)}


@mcp.tool()
def reset_group_offset(group_id: str, topic: str, to: str = "earliest") -> str:
    """
    Reset offset of a group for a topic. `to` must be 'earliest' or 'latest'.
    """
    try:
        consumer = KafkaConsumer(
            topic,
            group_id=group_id,
            bootstrap_servers=BOOTSTRAP_SERVERS,
            enable_auto_commit=False
        )
        partitions = consumer.partitions_for_topic(topic)
        if not partitions:
            return f"Topic '{topic}' has no partitions."

        tps = [TopicPartition(topic, p) for p in partitions]
        consumer.assign(tps)

        if to == "earliest":
            consumer.seek_to_beginning(*tps)
        elif to == "latest":
            consumer.seek_to_end(*tps)
        else:
            return f"Invalid reset point: {to}"

        new_offsets = {f"{tp.topic}-{tp.partition}": consumer.position(tp) for tp in tps}
        return f"Offsets reset: {new_offsets}"
    except KafkaError as e:
        return f"Error: {str(e)}"