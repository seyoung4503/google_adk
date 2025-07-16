from google.adk.agents import Agent

from ...config import MODEL_GEMINI_2_0_FLASH
from ...outputparser import SituationAnalysis
from ...tools import get_tavily_search_results






agent_description = (
    "Analyzes a user-provided situation to identify its core elements, "
    "determines the most appropriate type of humor, and extracts "
    "key topics for joke generation."
)

agent_instruction = (
    "Your task is to analyze the user's description of a situation. "
    "Read the situation carefully, then break it down into its essential components. "
    "First, summarize the situation in a single sentence. "
    "Second, decide which style of humor ('pun', 'observational_humor', 'sarcasm') would be most effective. "
    "Third, identify 2-4 primary keywords from the situation. "
    "You MUST format your output strictly according to the 'SituationAnalysis' model."
)

situation_analysis_agent = Agent(
    name="situation_analysis_agent",
    model=MODEL_GEMINI_2_0_FLASH,
    description=agent_description,
    instruction=agent_instruction,
    output_schema=SituationAnalysis,
    output_key="situation_analysis",
    tools=[],
)