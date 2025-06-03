from langchain_core.messages import RemoveMessage
from langchain_core.runnables import RunnableConfig

from langgraph.prebuilt import ToolNode


from state import PhilosopherState

from config import settings




async def conversation_node(state :PhilosopherState, config: RunnableConfig):
    summary = state.get("summary","")
    conversation_chain = get_philosopher_response_chain()
    