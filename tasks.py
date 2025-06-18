# from crewai import Task
# from agents import (
#     retriever_agent,
#     legal_assistant_agent,
#     evaluation_agent,
#     editor_agent,
# )

# task_retrieve = Task(
#     description="Retrieve relevant parts from the legal PDF related to the user's question.",
#     expected_output="A list of relevant text chunks from the document.",
#     agent=retriever_agent,
# )

# task_answer = Task(
#     description="Using the retrieved chunks, answer the user's legal question.",
#     expected_output="A detailed, accurate response to the user's query.",
#     agent=legal_assistant_agent,
# )

# task_evaluate = Task(
#     description="Evaluate the quality and completeness of the legal assistant's answer.",
#     expected_output="A brief evaluation of the answer's clarity and completeness.",
#     agent=evaluation_agent,
# )

# task_edit = Task(
#     description="Polish and edit the assistant's response for clarity, grammar, and tone.",
#     expected_output="A clean, well-edited answer ready for client delivery.",
#     agent=editor_agent,
# )


from crewai import Task

def get_tasks():
    return [
        Task(
            description="Retrieve relevant legal information for the user query: '{query}'",
            expected_output="Relevant legal context and document snippets",
            agent=None,  # Assigned dynamically in main.py
        ),
        Task(
            description="Generate a detailed legal answer to the query: '{query}' based only on retrieved documents",
            expected_output="A complete, helpful response grounded in retrieved information",
            agent=None,
        ),
        Task(
            description="Evaluate the accuracy and completeness of the generated response for: '{query}'",
            expected_output="A brief report on the quality of the response",
            agent=None,
        ),
        Task(
            description="Polish and refine the response for clarity and professionalism for: '{query}'",
            expected_output="Final cleaned and concise answer",
            agent=None,
        ),
    ]