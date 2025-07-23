import requests, os

RAPIDAPI_KEY = os.environ.get("RAPIDAPI_KEY")
RAPIDAPI_HOST = "irctc1.p.rapidapi.com"

# Tool: Get PNR status
def get_pnr_status(pnr_number: str) -> str:
    """Fetches the PNR status using IRCTC1 API."""
    url = "https://irctc1.p.rapidapi.com/api/v3/getPNRStatus"
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": RAPIDAPI_HOST,
    }
    params = {"pnrNumber": pnr_number}

    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        if not data.get("status", False):
            return f"❌ Could not fetch PNR status. Reason: {data.get('message', 'Unknown error')}"

        d = data["data"]
        train_info = f"🚆 {d['train_number']} - {d['train_name']}"
        journey = f"{d['boarding_point']} → {d['reservation_upto']}"
        date = d["journey_date"]
        passengers = "\n".join([
            f"👤 Passenger {p['no']}: {p['booking_status']} ➡ {p['current_status']}"
            for p in d["passengers"]
        ])

        return (
            f"📋 **PNR: {pnr_number}**\n{train_info}\n📅 Date: {date}\n🛤 Route: {journey}\n{passengers}"
        )
    except Exception as e:
        return f"⚠️ Error fetching PNR status: {str(e)}"