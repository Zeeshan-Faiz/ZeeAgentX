from serpapi import GoogleSearch
import os

# Tool: Web Search using SerpAPI
def serpapi_search(query: str) -> str:
    search = GoogleSearch({
        "q": query,
        "api_key": os.environ["SERPAPI_API_KEY"],
        "num": 3
    })
    results = search.get_dict()
    try:
        return "\n".join([r["snippet"] for r in results["organic_results"][:3]])
    except:
        return "No relevant results found."