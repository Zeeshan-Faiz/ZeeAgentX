
# Tool: Search Amazon and Flipkart products using SerpAPI
def e_commerce_search(query: str) -> str:
    """Searches Amazon and Flipkart via SerpAPI and combines results with product links."""
    from serpapi import GoogleSearch
    import os

    serpapi_key = os.environ["SERPAPI_API_KEY"]

    def fetch_results(site: str):
        search = GoogleSearch({
            "q": f"{query} site:{site}",
            "api_key": serpapi_key
        })
        results = search.get_dict()
        items = []
        for r in results.get("organic_results", [])[:3]:
            title = r.get("title", "No title")
            link = r.get("link", "")
            snippet = r.get("snippet", "")
            
            item_str = (
                f"**{title}**\n"
                f"{snippet}\n"
                f"[🛒 View Product]({link})\n"
                f"---"
            )
            items.append(item_str)
        return items

    try:
        amazon_results = fetch_results("amazon.in")
        flipkart_results = fetch_results("flipkart.com")

        all_results = [
            "### 🛒 Amazon Results:\n",
            *amazon_results,
            "\n### 🛍️ Flipkart Results:\n",
            *flipkart_results
        ]

        return "\n\n".join(all_results)
    
    except Exception as e:
        return f"❌ Error fetching product info: {str(e)}"