from functools import lru_cache


from state import PhilosopherState
from langgraph.graph import StateGraph, START, END


NODES = {
    "conversation_node": conversation_node,
    "retrieve_philosopher_context": retriever_node,
    "summarize_conversation_node": summarize_conversation_node,
    "summarize_context_node": summarize_context_node,
    "connector_node": connector_node,
}

class PhilosopherDialougeWorkflow:
    def __init__(self):
        self.graph_builder = StateGraph(PhilosopherState)

