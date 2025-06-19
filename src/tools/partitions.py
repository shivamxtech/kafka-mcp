from kafka import TopicPartition
from typing import Dict, List
from kafka import KafkaConsumer
from kafka.errors import KafkaError
from common.config import BOOTSTRAP_SERVERS
from common.server import mcp


@mcp.tool()
def list_partitions(topic: str) -> List[int]:
    """List partition IDs for a topic."""
    try:
        consumer = KafkaConsumer(bootstrap_servers=BOOTSTRAP_SERVERS)
        partitions = consumer.partitions_for_topic(topic)
        return sorted(partitions) if partitions else []
    except KafkaError as e:
        return [f"Error: {str(e)}"]


@mcp.tool()
def get_partition_offsets(topic: str) -> Dict[int, Dict[str, int]]:
    """Get beginning and end offsets for each partition in a topic."""
    try:
        consumer = KafkaConsumer(bootstrap_servers=BOOTSTRAP_SERVERS)
        partitions = consumer.partitions_for_topic(topic)
        if not partitions:
            return {"error": f"No partitions found for topic '{topic}'."}

        offsets = {}
        for pid in partitions:
            tp = TopicPartition(topic, pid)
            consumer.assign([tp])
            consumer.seek_to_beginning(tp)
            start = consumer.position(tp)
            consumer.seek_to_end(tp)
            end = consumer.position(tp)
            offsets[pid] = {"start": start, "end": end}
        return offsets
    except KafkaError as e:
        return {"error": str(e)}