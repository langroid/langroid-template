import langroid as lr
import langroid.language_models as lm
from fire import Fire

def run(model:str=""):
    agent = lr.ChatAgent(
        lr.ChatAgentConfig(
            name="bot",
            llm=lm.OpenAIGPTConfig(
                chat_model = model or lm.OpenAIChatModel.GPT4o,
            ),
            system_message = f"""
            You are a helpful assistant. Be concise.
            """
        )
    )
    task = lr.Task(agent, interactive=True)
    task.run("get started")

if __name__ == "__main__":
    Fire(run)

