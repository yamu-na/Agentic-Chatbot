import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage


class DisplayResultStreamlit:

    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):

        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message

        if usecase == "Basic Chatbot":

            # Display user message
            with st.chat_message("user"):
                st.write(user_message)

            # Run the graph
            for event in graph.stream(
                {"messages": [HumanMessage(content=user_message)]}
            ):

                for value in event.values():

                    assistant_message = value["messages"][-1]

                    with st.chat_message("assistant"):
                        st.write(assistant_message.content)


        elif usecase == "Chatbot with Web":

            # Initial graph state
            initial_state = {
                "messages": [HumanMessage(content=user_message)]
            }

            # Execute graph
            result = graph.invoke(initial_state)

            # Display every message returned by graph
            for message in result["messages"]:

                if isinstance(message, HumanMessage):

                    with st.chat_message("user"):
                        st.write(message.content)

                elif isinstance(message, ToolMessage):

                    with st.chat_message("assistant"):
                        st.info("Tool Call Started")
                        st.write(message.content)
                        st.info("Tool Call Finished")

                elif isinstance(message, AIMessage):

                    if message.content:

                        with st.chat_message("assistant"):
                            st.write(message.content)
        
        elif usecase == "AI News":
            frequency = self.user_message
            with st.spinner("Fetching and summarizing news... ⏳"):
                result = graph.invoke({"messages": [HumanMessage(content=frequency)]})
                try:
                     
                    AI_NEWS_PATH = f"./AINews/{frequency.lower()}_summary.md"
                    with open(AI_NEWS_PATH, "r") as file:
                        markdown_content = file.read()
                    st.markdown(markdown_content, unsafe_allow_html=True)
                except FileNotFoundError:
                    st.error(f"News Not Generated or File not found: {AI_NEWS_PATH}")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")


                        
                        

          


