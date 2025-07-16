from google.adk.agents import Agent

from .config import MODEL_GEMINI_2_0_FLASH, MODEL_GEMINI_2_5_FLASH
from .tools import get_tavily_search_results
from .sub_agents.situation_analysis_agent.agent import situation_analysis_agent
from .sub_agents.jokle_generator_agent.agent import joke_generator_agent
from google.adk.tools.agent_tool import AgentTool


coordinator_instruction = (
    "You are the master coordinator for generating witty, situational humor. "
    "Follow these steps precisely:\n"
    "1. First, call the `situation_analysis_agent` tool with the user's input to analyze the situation. "
    "This will give you a structured analysis including a summary, joke type, and keywords.\n"
    "2. **DO NOT** make up a joke yourself. Instead, take the full output from the analysis step.\n"
    "3. Next, call the `joke_generator_agent` tool, passing the analysis result as its input.\n"
    "4. Finally, present the joke returned by the generator agent to the user in a fun and engaging way."
)

coordinator_agent = Agent(
    name="coordinator_agent",
    model=MODEL_GEMINI_2_5_FLASH,
    description="A master agent that orchestrates situational joke generation.",
    instruction=coordinator_instruction,
    
    tools=[
        AgentTool(agent=situation_analysis_agent),
        AgentTool(agent=joke_generator_agent),
    ],
)

root_agent = coordinator_agent