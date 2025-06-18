# from crewai.tools.tool import tool

# def create_chroma_retriever_tool(retriever):
#     @tool("ChromaRetriever")
#     def chroma_retriever_tool(query: str) -> str:
#         """Retrieves relevant documents from the Chroma vector store."""
#         try:
#             docs = retriever.invoke(query)
#             return "\n\n".join([doc.page_content for doc in docs])
#         except Exception as e:
#             return f"[Retriever Error] {str(e)}"
    
#     return chroma_retriever_tool

from crewai.tools import BaseTool
from pydantic import Field
from typing import Any

class ChromaRetrieverTool(BaseTool):
    name: str = "ChromaRetriever"
    description: str = "Retrieves relevant documents from the Chroma vector store for a given query."
    
    retriever: Any = Field(...)

    def _run(self, query: str) -> str:
        """Run the query against the Chroma retriever and return combined content."""
        try:
            docs = self.retriever.invoke(query)
            return "\n\n".join([doc.page_content for doc in docs])
        except Exception as e:
            return f"[Chroma Retrieval Error] {str(e)}"