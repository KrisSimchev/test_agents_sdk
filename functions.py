from agents import Agent, Runner, WebSearchTool, function_tool
from prompts import SYSTEM_PROMPT


@function_tool
def track_order(contactInfo: str) -> str:
    """Return a fake order status."""
    return f"Order for {contactInfo} is being processed and will arrive soon."


@function_tool
def add_to_email_list(email: str, first_name: str, last_name: str, phone: str) -> str:
    """Pretend to add the user to an email list."""
    return (
        f"Added {first_name} {last_name} with email {email} and phone {phone} to the email list."
    )


def create_agent() -> Agent:
    """Return an Agent configured with our tools."""
    return Agent(
        name="SportsStoreAssistant",
        instructions=SYSTEM_PROMPT,
        model="gpt-4o",
        tools=[track_order, add_to_email_list, WebSearchTool()],
    )
