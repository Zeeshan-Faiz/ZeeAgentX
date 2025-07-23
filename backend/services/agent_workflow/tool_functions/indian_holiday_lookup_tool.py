import datetime
import holidays

# Tool: Lookup Indian holidays using the 'holidays' library
def lookup_indian_holidays(query: str) -> str:
    """Answers questions about Indian holidays using the 'holidays' library."""
    try:
        today = datetime.date.today()
        india_holidays = holidays.country_holidays('IN', years=range(today.year, today.year + 2))

        query_lower = query.lower()

        if "today" in query_lower:
            return f"✅ Today is a holiday: {india_holidays.get(today)}" if today in india_holidays else "❌ Today is not a holiday in India."

        elif "tomorrow" in query_lower:
            tomorrow = today + datetime.timedelta(days=1)
            return f"✅ Tomorrow is a holiday: {india_holidays.get(tomorrow)}" if tomorrow in india_holidays else "❌ Tomorrow is not a holiday in India."

        elif "this month" in query_lower:
            holidays_this_month = {
                date: name for date, name in india_holidays.items()
                if date.month == today.month and date >= today
            }
            if not holidays_this_month:
                return "No holidays remaining this month in India."
            return "📅 Holidays this month:\n" + "\n".join([f"{date.strftime('%d %b %Y')}: {name}" for date, name in holidays_this_month.items()])

        elif any(char.isdigit() for char in query):  # if there's a specific date
            from dateutil import parser
            try:
                target_date = parser.parse(query, fuzzy=True).date()
                if target_date in india_holidays:
                    return f"✅ {target_date.strftime('%d %b %Y')} is a holiday: {india_holidays.get(target_date)}"
                else:
                    return f"❌ {target_date.strftime('%d %b %Y')} is not a public holiday in India."
            except:
                return "Couldn't understand the date. Please rephrase."

        else:
            # Default: show next 5 upcoming holidays
            upcoming = sorted([d for d in india_holidays if d >= today])[:5]
            return "🗓️ Next 5 public holidays in India:\n" + "\n".join(
                [f"{d.strftime('%d %b %Y')}: {india_holidays[d]}" for d in upcoming]
            )

    except Exception as e:
        return f"Error checking holidays: {str(e)}"