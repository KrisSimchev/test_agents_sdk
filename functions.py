import json
from typing import List, Dict
import requests


def track_order(contactInfo: str) -> str:
    """Return a fake order status."""
    return f"Order for {contactInfo} is being processed and will arrive soon."


def add_to_email_list(email: str, first_name: str, last_name: str, phone: str) -> str:
    """Pretend to add the user to an email list."""
    return (
        f"Added {first_name} {last_name} with email {email} and phone {phone} to the email list."
    )


def search_products(query: str) -> str:
    """Search ballistic-sport.com for products matching the query."""
    url = (
        "https://ballistic-sport.com/search/suggest.json?q="
        + requests.utils.quote(query)
        + "&resources%5Btype%5D=product"
    )
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()
    except Exception as exc:
        return f"Failed to search products: {exc}"

    products = (
        data.get("resources", {})
        .get("results", {})
        .get("products", [])
    )

    if not products:
        return "No products found."

    lines = []
    for item in products[:5]:
        title = item.get("title")
        url = item.get("url")
        if url and not url.startswith("http"):
            url = "https://ballistic-sport.com" + url
        lines.append(f"{title} - {url}")
    return "\n".join(lines)


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
        {
            "name": "search_products",
            "description": "Search ballistic-sport.com for products and return recommendations",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Product search query"}
                },
                "required": ["query"],
            },
        },
    ]
