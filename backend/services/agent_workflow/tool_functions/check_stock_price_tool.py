import yfinance as yf

# Tool: Get stock price using yfinance
def get_stock_price(query: str) -> str:
    """Fetches real-time stock price for a given ticker or company name."""
    try:
        ticker = yf.Ticker(query)
        price = ticker.info.get("regularMarketPrice", None)
        name = ticker.info.get("shortName", query)
        if price:
            return f"The current stock price of {name} ({query.upper()}) is ${price:.2f}."
        else:
            return "I couldn't retrieve the stock price. Please check the ticker symbol."
    except Exception as e:
        return f"Error fetching stock price: {str(e)}"