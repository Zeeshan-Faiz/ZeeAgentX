
# Tool: Search YouTube videos using SerpAPI  
def search_youtube_videos(query: str) -> str:
    """Uses SerpAPI to search YouTube and return top 2–3 recent videos."""
    from serpapi import GoogleSearch
    import os

    search = GoogleSearch({
        "q": f"{query} site:youtube.com",
        "api_key": os.environ["SERPAPI_API_KEY"]
    })

    try:
        results = search.get_dict()
        video_links = []
        for result in results.get("organic_results", [])[:3]:
            title = result.get("title")
            link = result.get("link")
            snippet = result.get("snippet", "")
            video_links.append(f"**{title}**\n{snippet}\n🔗 {link}\n")
        
        return "\n".join(video_links) if video_links else "No videos found."
    except Exception as e:
        return f"Error fetching YouTube videos: {str(e)}"