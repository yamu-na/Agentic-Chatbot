from src.langgraphAgenticAI.state.state import State

class BasicChatbotNode:
    """
    A basic chatbot node that can be used in a graph-based AI system.
    This node is responsible for handling user input and generating responses.
    """

    def __init__(self,model):
        self.llm=model
    
    def process(self, state: State):
        return {
            "messages": [self.llm.invoke(state["messages"])]
        }

    