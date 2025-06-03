# from langgraph.graph import MessagesState, StateGraph, START, END
# from langchain_core.runnables import RunnableConfig
# from typing import Literal

# import asyncio

# class PhilosopherState(MessagesState):
#     summary :str


# def create_simple_workflow_graph() -> StateGraph:
#     graph_builder = StateGraph(PhilosopherState)

#     """Adding the essential nodes"""
#     graph_builder.add_node("conversation_node", conversation_node)
#     graph_builder.add_node("summarize_conversation_node", summarize_conversation_node)


#     """Defining the flow of the conversation"""
#     graph_builder.add_edge(START, "conversation_node")
#     graph_builder.add_conditional_edges(
#         "conversation_node",
#         should_summarize_conversation,
#     )

#     graph_builder.add_edge("summarize_conversation_node", END)
#     return graph_builder


# async def conversation_node(state: PhilosopherState, config : RunnableConfig) -> PhilosopherState:
#     summary = state.get("summary","")
#     converstaion_chain = get_philosopher_response_chain()
#     response = await conversation_chain.ainvoke(
#         {
#             "messages": state["messages"],
#             "summary" : summary
#         },
#         config
#     )

#     return {"messages": response}


# async def summarize_conversation_node(state: PhilosopherState):
#     summary = state.get("summary","")
#     summary_chain = get_conversation_summary_chain(summary)

#     response = await summary_chain.ainvoke(
#         {
#             "messages" : state["messages"],
#             "philosopher_name" : state["philosopher_name"],
#             "summary" : summary

#         }
#     )

#     delete_message = [
#         RemoveMessage(id=m.id)
#         for m in state['messages'][:-settings.TOTAL_MESSAGES_AFTER_SUMMARY]

#     ]

#     return {"summary" : response.content, "messages" : delete_message}


# def should_summarize_conversation(state : PhilosopherState) -> Literal["summarize_conversation_node","__end__"]:
#     messages = state["messages"]

#     if len(messages) > setings.TOTAL_MESSAGES_AFTER_SUMMARY:
#         return "summarize_conversation_node"
#     return END


# graph_builder = create_simple_workflow_graph()
# graph = graph_builder.compile()


# async def main():
#     messages = await graph.ainvoke(
#         {
#             "messages" : ["Hello, How are you ?"]
#         }
#     )

#     for message in messages:
#         print(message)


# asyncio.run(main())
    
