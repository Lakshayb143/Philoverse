from langchain_core.messages import RemoveMessage
from langchain_core.runnables import RunnableConfig
from langgraph.prebuilt import ToolNode


from state import PhilosopherState

from config import settings




async def conversation_node(state :PhilosopherState, config: RunnableConfig):
    summary = state.get("summary","")
    conversation_chain = get_philosopher_response_chain()

    response = await conversation_chain.ainvoke(
        {
            "messages": state["messages"],
            "philosopher_context": state["philosopher_context"],
            "philosopher_name": state["philosopher_name"],
            "philosopher_perspective": state["philosopher_perspective"],
            "philosopher style" : state["philosopher_style"],
            "summary" : summary,

        },
        config
    )
    
    return {"messages": response}


async def summarize_conversation_node(state :PhilosopherState):
    summary = state.get("summary","")
    summary_chain = 


async def summarize_context_node(state :PhilosopherState):
    context_summary_chain = get_context_summary_chain()
    
    response = await context_summary_chain.ainvoke(
        {
            "context" : state["messages"][-1].content,
        }
    )

    state["messages"][-1].content = response.content

    return {}

async def connector_node(state :PhilosopherState):
    return {} 