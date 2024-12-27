"""
Basic test to check that the ChatAgent works as expected.
"""
from langroid.agent.chat_agent import ChatAgent, ChatAgentConfig
from langroid.agent.task import Task
from langroid.cachedb.redis_cachedb import RedisCacheConfig
from langroid.language_models.openai_gpt import OpenAIGPTConfig
from langroid.mytypes import Entity
from langroid.prompts.prompts_config import PromptsConfig


class _TestChatAgentConfig(ChatAgentConfig):
    max_tokens: int = 200
    llm: OpenAIGPTConfig = OpenAIGPTConfig(
        cache_config=RedisCacheConfig(fake=False),
        use_chat_for_completion=True,
    )
    prompts: PromptsConfig = PromptsConfig(
        max_tokens=200,
    )


def test_chat_agent():
    cfg = _TestChatAgentConfig()
    # just testing that these don't fail
    agent = ChatAgent(cfg)
    response = agent.llm_response("what is the capital of France?")
    assert "Paris" in response.content


def test_responses():
    cfg = _TestChatAgentConfig()
    agent = ChatAgent(cfg)

    # direct LLM response to query
    response = agent.llm_response("what is the capital of France?")
    assert "Paris" in response.content

    # human is prompted for input, and we specify the default response
    agent.default_human_response = "What about England?"
    response = agent.user_response()
    assert "England" in response.content

    response = agent.llm_response("what about England?")
    assert "London" in response.content

    # agent attempts to handle the query, but has no response since
    # the message is not a structured msg that matches an enabled ToolMessage.
    response = agent.agent_response("What is the capital of France?")
    assert response is None




def test_simple_task():
    cfg = _TestChatAgentConfig()
    agent = ChatAgent(cfg)
    task = Task(
        agent,
        interactive=False,
        done_if_response=[Entity.LLM],
        system_message="""
        User will give you a number, respond with the square of the number.
        """,
    )

    response = task.run(msg="5")
    assert "25" in response.content

    # create new task with SAME agent, and restart=True,
    # verify that this works fine, i.e. does not use previous state of agent

    task = Task(
        agent,
        interactive=False,
        done_if_response=[Entity.LLM],
        restart=True,
        system_message="""
        User will give you a number, respond with the square of the number.
        """,
    )

    response = task.run(msg="7")
    assert "49" in response.content

