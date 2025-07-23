import requests
from bs4 import BeautifulSoup

# Tool: Get FD rates from BankBazaar
def get_fd_rates(bank_name: str = "") -> str:
    """
    Scrape 1-year FD rates from BankBazaar.
    If a bank name is provided, show its rate + 3 more top banks.
    """
    url = "https://www.bankbazaar.com/fixed-deposit/5years-fd-interest-rates.html"
    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        table = soup.select_one("table")
        rows = table.select("tr")[1:]  # skip table header

        all_rates = []
        matched_bank = []

        for row in rows:
            cols = [c.get_text(strip=True) for c in row.select("td")]
            bank = cols[0]
            general = cols[1]
            senior = cols[2]
            formatted = f"🏦 {bank}: {general} (General), {senior} (Senior)"
            all_rates.append(formatted)

            if bank_name and bank_name.lower() in bank.lower():
                matched_bank.append(formatted)

        if bank_name and matched_bank:
            others = [r for r in all_rates if r not in matched_bank][:3]
            return "\n".join(matched_bank + ["\n📊 Here are a few other banks:"] + others)
        else:
            return "\n".join(all_rates[:5])  # top 5 fallback

    except Exception as e:
        return f"⚠️ Error fetching FD rates: {str(e)}"