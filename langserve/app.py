from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq  
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    logger.error("GROQ_API_KEY is not set in the environment variables.")
    raise EnvironmentError("Missing GROQ_API_KEY in environment variables.")
 

# Initialize the Groq model (using Llama model)
model = ChatGroq(model="llama3-8b-8192", api_key=GROQ_API_KEY)

# Define prompts
prompt = ChatPromptTemplate.from_template("provide me an history about {topic}")
prompt1 = ChatPromptTemplate.from_template("provide me a stats about {topic}")

app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server"
)

# Add routes for different endpoints
add_routes(
    app,
    model,  # Use the Groq model directly
    path="/groq"
)

# Route for generating an essay
add_routes(
    app,
    prompt | model,  # Combine the prompt and model
    path="/history"
)

# Route for generating a poem
add_routes(
    app,
    prompt1 | model,  # Combine the prompt and model
    path="/stats"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
