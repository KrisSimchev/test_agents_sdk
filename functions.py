import json
from typing import List, Dict


def track_order(contactInfo: str) -> str:
    """Return a fake order status."""
    return f"Order for {contactInfo} is being processed and will arrive soon."


def add_to_email_list(email: str, first_name: str, last_name: str, phone: str) -> str:
    """Pretend to add the user to an email list."""
    return (
        f"Added {first_name} {last_name} with email {email} and phone {phone} to the email list."
    )


def create_agent() -> List[Dict]:
    """Return the OpenAI function specifications for the agent."""
    return [
        {
            "name": "track_order",
            "description": "Get order tracking information for a user",
            "parameters": {
                "type": "object",
                "properties": {
                    "contactInfo": {
                        "type": "string",
                        "description": "Email or phone number used for the order",
                    }
                },
                "required": ["contactInfo"],
            },
        },
        {
            "name": "add_to_email_list",
            "description": "Subscribe the user to the marketing email list",
            "parameters": {
                "type": "object",
                "properties": {
                    "email": {"type": "string", "description": "Email address"},
                    "first_name": {"type": "string", "description": "First name"},
                    "last_name": {"type": "string", "description": "Last name"},
                    "phone": {"type": "string", "description": "Phone number"},
                },
                "required": ["email", "first_name", "last_name", "phone"],
            },
        },
    ]
