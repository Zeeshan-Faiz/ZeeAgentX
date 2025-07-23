import os, re, requests

# Tool: Convert currency using exchangerate-api.com
def convert_currency(query: str) -> str:
    """
    Converts currency using exchangerate-api.com
    Format: '100 USD to INR'
    """
    match = re.search(r"(\d+(?:\.\d+)?)\s*([A-Za-z]{3})\s+(?:to|in)\s+([A-Za-z]{3})", query)
    if not match:
        return "Please format your query like '100 USD to INR'."

    amount, from_curr, to_curr = match.groups()
    from_curr = from_curr.upper()
    to_curr = to_curr.upper()
    api_key = os.environ.get("EXCHANGE_RATE_API_KEY")

    if not api_key:
        return "Currency API key not set. Please configure EXCHANGE_RATE_API_KEY."

    try:
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_curr}/{to_curr}/{amount}"
        response = requests.get(url)
        data = response.json()

        if data["result"] == "success":
            converted = data["conversion_result"]
            return f"As of today's exchange rates,{amount} {from_curr} is approximately {converted:.2f} {to_curr}."
        else:
            return f"Failed to convert from {from_curr} to {to_curr}. Error: {data.get('error-type', 'Unknown error')}"

    except Exception as e:
        return f"Error during currency conversion: {str(e)}"