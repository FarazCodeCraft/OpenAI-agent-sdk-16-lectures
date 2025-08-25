# Notes of this class
# Main Agentic Framework Concepts

## 🔹 OpenAI Agents SDK
- Simple toolkit to build **agents** that can use **tools/APIs/functions**.  
- Focus: **ease + official integration**.  

## 🔹 LangChain
- Framework for **LLM apps**.  
- Core ideas: **Chains, Agents, Memory, Data connectors, Tools**.  
- Strong for **RAG + data-heavy apps**.  

## 🔹 AutoGen (Microsoft)
- Focus on **multi-agent collaboration**.  
- Agents can play roles (e.g., “engineer” + “critic”) and talk to each other.  

## 🔹 LangGraph
- **Graph-based orchestration** on top of LangChain.  
- Concepts: **Nodes (steps)** + **Edges (connections)**.  
- Good for loops, branching, retries, and controlled agent workflows.  
- nodes and edges are same as n8n nodes and edges

## 🔹 CrewAI
- Multi-agent framework.  
- Concepts: **Agents, Tasks, Tools, Processes, Crews, Memory/Context**.  
- Crews add: **logging, observability, memory/caching, replay** for reliability.  

---

## 👉 In short
- **OpenAI SDK** → simple agent + tool wiring.  
- **LangChain** → LLM + data workflows.  
- **AutoGen** → multi-agent teamwork.  
- **LangGraph** → graph-style control of agent flows.  
- **CrewAI** → team of agents with memory + logging + orchestration.  