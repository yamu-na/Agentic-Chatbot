from langgraph.graph import StateGraph
from src.langgraphAgenticAI.state.state import State
from langgraph.graph import START,END
from src.langgraphAgenticAI.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraphAgenticAI.tools.search_tool import get_tools,create_tool_node
from langgraph.prebuilt import tools_condition,ToolNode
from src.langgraphAgenticAI.nodes.chatbot_with_tool_node import ChatbotwithToolNode
from src.langgraphAgenticAI.nodes.ai_news_node import AINewsNode



class GraphBuilder:
    def __init__(self,model,tavily_api_key=None):
        self.llm=model
        self.tavily_api_key = tavily_api_key
        self.graph_builder=StateGraph(State)
    
    def basic_chatbot_build_graph(self):
        """
        Build a basic chatbot graph with the provided Langraph.
        This methos initilaizes a chatbot node using the 'BasicChatbotModel' class and 
        integrates it into the graph.The chatbot node is set as both the entry ans exit point of the graph

        """
        self.basic_chatbot_node = BasicChatbotNode(self.llm)
        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)
    
    def chatbot_with_tools_build_graph(self):
        """
        Builds an advanced chatbot graph with tool integrration.
        """
        # print("Building Chatbot with Web graph...")
        ##defining tool and tool node
        tools=get_tools(self.tavily_api_key)
        tool_node=create_tool_node(tools)

        ##define the llm 
        llm=self.llm

        ##define the chatbot
        obj_chatbot_with_node=ChatbotwithToolNode(llm)
        chatbot_node=obj_chatbot_with_node.create_cahtbot(tools)

        ## Add Node
        self.graph_builder.add_node("chatbot",chatbot_node)
        self.graph_builder.add_node("tools",tool_node)
        ## Conditional and Direct edges
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_conditional_edges("chatbot",tools_condition)
        self.graph_builder.add_edge("tools","chatbot")
        self.graph_builder.add_edge("chatbot",END)


    def ai_news_builder_graph(self):
        ai_news_node=AINewsNode(self.llm)

        ##added the nodes
        self.graph_builder.add_node("fetch_news",ai_news_node.fetch_news)
        self.graph_builder.add_node("summarize_news",ai_news_node.summarize_news)
        self.graph_builder.add_node("save_result",ai_news_node.save_result)
        ##added the edges
        self.graph_builder.set_entry_point("fetch_news")
        self.graph_builder.add_edge("fetch_news","summarize_news")
        self.graph_builder.add_edge("summarize_news","save_result")
        self.graph_builder.add_edge("save_result",END)


    def setup_graph(self, usecase):
        """
        Set up the graph based on the selected use case.
        Currently, only the 'Basic Chatbot' use case is supported.
        """
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        if usecase == "Chatbot with Web":
            self.chatbot_with_tools_build_graph()
        if usecase == "AI News":
            self.ai_news_builder_graph()
        return self.graph_builder.compile()
        