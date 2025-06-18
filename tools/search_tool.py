# # tools/search_tool.py

# def simple_search(query, docs, top_k=3):
#     """
#     A dummy search tool - ranks docs by keyword count in content.
#     Replace with proper search in production.
#     """
#     scored = []
#     for doc in docs:
#         score = doc.page_content.lower().count(query.lower())
#         scored.append((score, doc))
#     scored.sort(key=lambda x: x[0], reverse=True)
#     return [doc for score, doc in scored[:top_k]]

# tools/search_tool.py

# from crewai.tools import BaseTool
# from typing import Optional
# from pydantic import Field

# class SimpleSearchTool(BaseTool):
#     name: str = Field(default="SimpleSearch")
#     description: str = Field(default="Tool for retrieving legal info or news based on query.")

#     def _run(self, query: str) -> str:
#         # You can connect this to Tavily or anything later
#         return f"[Mock Search Result] You asked: {query}"

from langchain_community.tools.tavily_search import TavilySearchResults
from crewai.tools import BaseTool
from pydantic import Field

search = TavilySearchResults()

class SearchTool(BaseTool):
    name: str = "Search"
    description: str = "Useful for search-based queries. Use this to find current information about latest legal trends and news."
    search: TavilySearchResults = Field(default_factory=TavilySearchResults)

    def _run(self, query: str) -> str:
        """Execute the search query and return results"""
        try:
            return self.search.run(query)
        except Exception as e:
            return f"Error performing search: {str(e)}"
        
        
web_search_tool = SearchTool()