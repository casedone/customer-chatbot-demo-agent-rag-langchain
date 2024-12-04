# customer-chatbot-demo-agent-rag-langchain

> This repo has been updated to use LangGraph instead of legacy LangChain's AgentExecutor. Additionally, Ollama is used instead of OpenAI. [Dec 4, 2024].

"Tutorial on building customer chatbot for coffee shop with Agent LLM and RAG".
This is a repo that we demo on our YouTube video [Tutorial - Build a Customer Contact Chatbot with Gen-AI: LangChain, Chroma, & Gradio](https://youtu.be/KFmPgeSCxRs)

![UI Example](asset/UI%20Example.png)

## Why This Video:
- Embark on this journey with us to explore the potential of Generative AI in enhancing customer service through an intelligent chatbot. Let's build, learn, and innovate together!
- This step-by-step tutorial is ideal for software and AI developers, forward-thinking business managers, and tech enthusiasts, this video guides you through creating a demo of an intelligent chatbot for a mock-up coffee shop scenario, from inception to a fully functional demo.

## What You'll Learn:
- Project Setup: Developing a chatbot that provides store information, coffee product details, and helps customers choose the right coffee beans. We do that using text and CSV files.
- Technology Insights: Agent-based workflow with LLM and RAG (Retrieval Augmented Generation).
- Coding Session: Hands-on walkthrough using Python, featuring LangChain for its LLM prowess, Chroma for information storage, and Gradio for a quich chatbot interface for a demo.
- Demo Showcase: Experience the chatbot in action, demonstrating its capability to manage customer interactions, perform small talks, and handle product inquiries seamlessly.

## Connect with Us:
👍 Like | 🔗 Share | 📢 Subscribe    
Follow us on [YouTube](https://www.youtube.com/@CaseDonebyAI), [LinkedIn](www.linkedin.com/company/casedonebyai), and [Facebook](https://www.facebook.com/casedonebyai/)! Look for *@casedonebyai*   
💬 Comments? Questions? We value your feedback and look forward to engaging with you!

## Time in YouTube
0:10 Scenario: Mock-up Coffee Shop   
0:40 RAG review and quick intro   
1:52 Coding session starts from here   
2:00 Documents needed for RAG   
7:23 RAG Step 1: Indexing and Saving to Chroma index   
14:43 RAG Step 2: Retrieval, Loading Chroma index, and Using Retriever   
21:26 In LangChain, Build LLM-based Agent and Register RAG tool in LangChain   
28:39 Launch and test chatbot demo interface with Gradio!   
37:56 Briefly seeing 'verbose' from LLM agent action   
39:20 Wrapping up and summary   

## FYI:
[RAG intro on our YouTube](https://youtube.com/playlist?list=PLP50mZI6LSxNNTNhavyvqONaUBkeRv1ZJ)

## NOTES
1. Make sure you use the appropriate environment. You can install modules using `requirements.txt`.
2. If you find an error about OpenAI, it could be that you need to specifcy OpenAI API key. Make a file called `openai_api_key` in `secret` folder and keep your key there.
3. Ollama with Llama3.2-3B should be running. You can set up by:
```shell
ollama pull llama3.2
ollama serve
```