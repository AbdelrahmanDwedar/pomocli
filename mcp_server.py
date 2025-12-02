"""MCP Server for PomoCLI - Model Context Protocol server."""
from mcp_utils.core import MCPServer
from mcp_utils.schema import CallToolResult, GetPromptResult, Message, TextContent

# Initialize the MCP server
mcp = MCPServer("pomocli", "1.0.0")


@mcp.tool()
def start_pomodoro_timer(work_time: int = 25, rest_time: int = 5, work_only: bool = False) -> CallToolResult:
    """Start a Pomodoro timer with specified work and rest times.
    
    Args:
        work_time: Work time in minutes (default: 25)
        rest_time: Rest time in minutes (default: 5)
        work_only: If True, only run work timer without rest (default: False)
    
    Returns:
        CallToolResult with timer status
    """
    # This is a placeholder - integrate with your actual timer logic
    mode = "work-only" if work_only else "normal"
    result = f"Started Pomodoro timer: {work_time} min work, {rest_time} min rest (mode: {mode})"
    return CallToolResult(output=result)


@mcp.tool()
def get_timer_status() -> CallToolResult:
    """Get the current status of the Pomodoro timer.
    
    Returns:
        CallToolResult with current timer status
    """
    # This is a placeholder - integrate with your actual timer logic
    return CallToolResult(output="Timer status: Not running")


@mcp.prompt()
def pomodoro_technique_prompt() -> GetPromptResult:
    """Get information about the Pomodoro technique."""
    return GetPromptResult(
        description="Information about the Pomodoro Technique",
        messages=[
            Message(
                role="user",
                content=TextContent(
                    text="The Pomodoro Technique is a time management method that uses a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks.",
                ),
            )
        ],
    )


# Run the server
if __name__ == "__main__":
    mcp.run()

