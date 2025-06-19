from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP(
    "Kafka MCP Server",
    dependencies=["kafka", "dotenv", "zookeeper"]
)
