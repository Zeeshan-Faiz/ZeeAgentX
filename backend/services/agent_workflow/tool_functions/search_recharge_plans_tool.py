import os
from serpapi import GoogleSearch

# Tool: Search real-time recharge plans
def search_recharge_plans(operator_and_amount: str) -> str:
    """
    Search real-time recharge plans for telecom operators using SerpAPI.
    e.g., "Airtel prepaid recharge plans under 500"
    """
    api_key = os.getenv("SERPAPI_API_KEY")
    q = f"{operator_and_amount} recharge plans site:paytm.com OR site:airtel.in OR site:jio.com"
    
    search = GoogleSearch({"q": q, "api_key": api_key, "num": 3})
    try:
        results = search.get_dict()
        items = []
        for r in results.get("organic_results", []):
            title = r.get("title", "")
            snippet = r.get("snippet", "")
            link = r.get("link", "")
            items.append(f"**{title}**\n{snippet}\n🔗 {link}")
        return "\n\n".join(items) if items else "No real-time recharge data found."
    except Exception as e:
        return f"Error fetching recharge plans: {e}"