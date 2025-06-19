from functools import lru_cache



from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import tools_condition


from philosopher_agents.application.conversation_service.workflow.state import PhilosopherState
from philosopher_agents.application.conversation_service.workflow.nodes import(
    conversation_node,
    retriver_node,
    summarize_context_node,
    summarize_conversation_node,
    connector_node
)
from philosopher_agents.application.conversation_service.workflow.edges import should_summarize_conversation

NODES = {
    "conversation_node": conversation_node,
    "retrieve_philosopher_context": retriver_node,
    "summarize_conversation_node": summarize_conversation_node,
    "summarize_context_node": summarize_context_node,
    "connector_node": connector_node,
}

class PhilosopherDialougeWorkflow:
    def __init__(self):
        self.graph_builder = StateGraph(PhilosopherState)

    
    def _add_nodes(self):
        for name, node in NODES.items():
            self.graph_builder.add_node(name,node)

    def _add_edges(self):
        self.graph_builder.add_edge(START, "conversation_node")

        self.graph_builder.add_conditional_edges(
            "conversation_node",
            tools_condition,
            {
                "tools": "retrieve_philosopher_context",
                END : "connector_node"
            }
        )

        self.graph_builder.add_edge("retrieve_philosopher_context","summarize_context_node")
        self.graph_builder.add_edge("summarize_context_node", "conversation_node")
        self.graph_builder.add_conditional_edges("connector_node", should_summarize_conversation)
        self.graph_builder.add_edge("summarize_conversation_node", END)

    @lru_cache(maxsize=1)
    def build(self):
        self._add_nodes()
        self._add_edges()

        return self.graph_builder


@lru_cache(maxsize=1)
def get_graph() -> StateGraph:
    return PhilosopherDialougeWorkflow.build()

