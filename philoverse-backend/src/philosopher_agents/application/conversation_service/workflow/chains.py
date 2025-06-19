from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq

from philosopher_agents.application.conversation_service.workflow.tools import tools
from philosopher_agents.config import settings

from philosopher_agents.domain.prompts import (
    PHILOSOPHER_CHARACTER_CARD,
    SUMMARY_PROMPT,
    EXTEND_SUMMARY_PROMPT,
    CONTEXT_SUMMARY_PROMPT,

)

def get_chat_model(temperature :float = 0.65, model_name :str = settings.GRQO_LLM_MODEL) -> ChatGroq:
    return ChatGroq(
        api_key=settings.GROQ_API_KEY,
        model_name = model_name,
        temperature= temperature,
    )


def get_philosopher_response_chain():
    model = get_chat_model()
    model.bind_tools(tools)
    system_message = PHILOSOPHER_CHARACTER_CARD

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system",system_message.prompt),
            MessagesPlaceholder(variable_name="messages")
        ],
        template_format="jinja2"
    )

    return prompt | model


def get_conversation_summary_chain(summary :str = ""):
    model = get_chat_model()
    summary_message = EXTEND_SUMMARY_PROMPT if summary else SUMMARY_PROMPT

    prompt = ChatPromptTemplate.from_messages(
        [
            MessagesPlaceholder(variable_name="messages"),
            ("human", summary_message.prompt),

        ],
        template_format="jinja2"
    )

    return prompt | model


def get_context_summary_chain():
    model = get_chat_model(model_name=settings.GROQ_LLM_MODEL_CONTEXT_SUMMARY)
    prompt = ChatPromptTemplate.from_messages(
        [
            ("human", CONTEXT_SUMMARY_PROMPT.prompt),
        ],
        template_format="jinja2"
    )

    return prompt | model