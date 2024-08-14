from langchain_community.llms import OpenLLM

llm = OpenLLM(server_url='http://localhost:3000')
llm.invoke("What is the difference between a duck and a goose?")