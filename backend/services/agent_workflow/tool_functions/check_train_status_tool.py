import os, requests
from pydantic import BaseModel

# Tool: Get live train status
class TrainStatusInput(BaseModel):
    train_number: str
    start_day: str = "1"

RAPIDAPI_KEY = os.environ.get("RAPIDAPI_KEY")
RAPIDAPI_HOST = "irctc1.p.rapidapi.com"

# Tool: Get live train status
def get_train_live_status(train_number: str, start_day: str = "1") -> str:
    """Fetches the live running status of a train with enriched details."""
    url = "https://irctc1.p.rapidapi.com/api/v1/liveTrainStatus"
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": RAPIDAPI_HOST,
    }
    params = {"trainNo": train_number, "startDay": start_day}

    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        if not data.get("status", False):
            return f"❌ Could not fetch live status. Reason: {data.get('message', 'Unknown error')}"

        d = data["data"]

        # Format journey time from minutes to "x hrs y mins"
        journey_mins = d.get("journey_time", 0)
        hours = journey_mins // 60
        minutes = journey_mins % 60
        journey_time_str = f"{hours} hrs {minutes} mins"

        # Handle platform and pantry info
        platform = d.get("platform_number")
        platform_str = str(platform) if platform and platform > 0 else "Not assigned"
        pantry = "Yes" if d.get("pantry_available", False) else "No"

        return (
            f"🚆 **Train {d['train_number']} - {d['train_name']}**\n"
            f"📅 Run Days: {d.get('run_days', 'N/A')}\n"
            f"🛤️ Route: {d.get('source_stn_name', 'N/A')} ➝ {d.get('dest_stn_name', 'N/A')}\n"
            f"⏱️ Departure Time: {d.get('std', 'N/A')}\n"
            f"⌛ Journey Time: {journey_time_str}\n"
            f"🍱 Pantry Available: {pantry}\n\n"
            f"📍 **Current Station**: {d.get('current_station_name', 'N/A')}\n"
            f"🕒 ETA: {d.get('eta', 'N/A')} | Scheduled: {d.get('cur_stn_sta', 'N/A')}\n"
            f"🔄 Delay: {d.get('delay', 'N/A')} mins\n"
            f"📏 Ahead Distance: {d.get('ahead_distance_text', 'N/A')}\n"
            f"🛑 Platform: {platform_str}\n"
            f"🕓 Last Updated: {d.get('status_as_of', 'N/A')}"
        )

    except Exception as e:
        return f"⚠️ Error fetching train status: {str(e)}"