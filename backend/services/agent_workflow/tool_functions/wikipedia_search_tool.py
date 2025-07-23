from wikipedia import summary, exceptions

# Tool: Search Wikipedia
def search_wikipedia(query: str) -> str:
    """Searches Wikipedia and returns the summary of the first result."""

    try:
        return summary(query, sentences=2)
    except exceptions.DisambiguationError as e:
        return f"The query was too broad. Possible options: {', '.join(e.options[:5])}"
    except exceptions.PageError:
        return "I couldn't find any information on that topic."
    except Exception as e:
        return f"Something went wrong: {str(e)}"