import requests, os

AVIATIONSTACK_KEY = os.getenv("AVIATIONSTACK_KEY")

# Tool: Get flight status
def get_flight_status(flight_query: str) -> str:
    """
    Query flight status using Aviationstack.
    Input examples: "UA246", "AI101"
    """
    url = "http://api.aviationstack.com/v1/flights"
    params = {"access_key": AVIATIONSTACK_KEY, "flight_iata": flight_query}
    try:
        res = requests.get(url, params=params)
        data = res.json()
        flights = data.get("data", [])
        if not flights:
            return "No flight found for that code."

        flight = flights[0]
        dep = flight["departure"]
        arr = flight["arrival"]
        return (
            f"✈️ Flight **{flight['flight']['iata']} ({flight['airline']['name']})**\n"
            f"Departure: {dep['airport']} at {dep['scheduled']}\n"
            f"Arrival: {arr['airport']} at {arr['scheduled']}\n"
            f"Status: {flight['flight_status']}"
        )
    except Exception as e:
        return f"Error fetching flight data: {e}"