

import streamlit as st
from src.langgraphAgenticAI.UI.uiconfigfile import config

from src.langgraphAgenticAI.UI.streamlitui.loadui import LoadStreamlitUI
from src.langgraphAgenticAI.UI.streamlitui.display_result import DisplayResultStreamlit

from src.langgraphAgenticAI.LLMS.groqllm import GroqLLM
from src.langgraphAgenticAI.graph.graph_builder import GraphBuilder


def load_langgrapg_agenticai_app():

    ui_loader = LoadStreamlitUI()
    user_input = ui_loader.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI")
        return
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe
    else:
        user_message=st.chat_input("Enter your message")

    
    if user_message:

        try:

            # Configure LLM
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error(
                    "Error: Failed to initialize the LLM model. Please check your API key."
                )
                return

            # Selected Usecase
            usecase = user_input.get("selected_usecase")

            if not usecase:
                st.error("Error: No use case selected.")
                return
            # print("Usecase:", usecase)
            # print("Tavily Key:", user_input.get("TAVILY_API_KEY"))

            # Build Graph
            graph_builder = GraphBuilder(
                model=model,
                tavily_api_key=user_input.get("TAVILY_API_KEY")
            )

            graph = graph_builder.setup_graph(usecase)

            # Display Result
            display = DisplayResultStreamlit(
                usecase=usecase,
                graph=graph,
                user_message=user_message
            )

            display.display_result_on_ui()

        except Exception as e:
            st.error(f"Error: {e}")