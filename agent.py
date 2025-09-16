from google.adk.agents import Agent
from .util import load_instruction_from_file
# Create the ADK agent
root_agent = Agent(
    name="nugenomics_faq_agent",
    model="gemini-2.0-flash",
    description="Customer Support Agent for NuGenomics using only predefined FAQs.",
    instruction=load_instruction_from_file("faq_data.txt"),
)
