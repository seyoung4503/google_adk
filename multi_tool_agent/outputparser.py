from pydantic import BaseModel, Field
from typing import List

class SituationAnalysis(BaseModel):
    """Holds the structured analysis of a given situation for joke generation."""
    situation_summary: str = Field(
        description="A concise, one-sentence summary of the situation."
    )
    joke_type: str = Field(
        description="The most suitable type of joke. Must be one of: 'pun', 'observational_humor', or 'sarcasm'."
    )
    keywords: List[str] = Field(
        description="A list of 2-4 key nouns or concepts from the situation to build a joke around."
    )


class GeneratedJoke(BaseModel):
    """Holds the final joke and the reasoning behind it."""
    joke: str = Field(description="The final, witty joke to be presented to the user.")
    
    reasoning: str = Field(description="A brief, one-sentence explanation of why this joke is funny or relevant to the situation.")