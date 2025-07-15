import os

from dotenv import load_dotenv
from tavily import TavilyClient

def get_tavily_search_results(query: str) -> str:
    """
    Search the web for the latest news and information on a given topic.
    """

    try:
        client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
        response = client.search(query=query, search_depth="basic", max_results=3)

        formatted_results = []
        for item in response['results']:
            formatted_results.append(
                f"Title: {item['title']}\n"
                f"Link: {item['url']}\n"
                f"Content: {item['content']}\n"
            )
            
        if not formatted_results:
            return "No search results found."
            
        return "\n---\n".join(formatted_results)
        
    except Exception as e:
        return f"An error occurred during search: {e}"
    
def get_joke() -> dict:
    """Returns a random joke."""

    return {
        "status": "success", 
        "joke": "Why did the chicken cross the road? To get to the other side."
    }


if __name__ == "__main__":
    load_dotenv()
    print(get_tavily_search_results("tell me about killing joke"))