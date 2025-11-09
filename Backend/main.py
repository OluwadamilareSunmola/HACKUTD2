from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

# -------------------- App setup --------------------
app = FastAPI(
    title="Hackathon API",
    description="Simple API for stories and tickets (in-memory)",
    version="1.0.0",
)

# Allow all origins for frontend testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------- In-memory storage --------------------
stories = []
tickets = []

# -------------------- Pydantic Models --------------------
class Story(BaseModel):
    title: str
    content: str

class Ticket(BaseModel):
    name: str
    email: str
    message: str

# -------------------- Routes --------------------

@app.get("/")
async def root():
    return {"message": "Welcome to the Hackathon API!"}

# ---------- Stories ----------
@app.post("/stories")
async def create_story(story: Story):
    story_id = len(stories) + 1
    new_story = {"id": story_id, "title": story.title, "content": story.content}
    stories.append(new_story)
    return {"status": "success", "story": new_story}

@app.get("/stories")
async def get_stories():
    return {"stories": stories}

@app.get("/stories/{story_id}")
async def get_story(story_id: int):
    for story in stories:
        if story["id"] == story_id:
            return story
    return {"error": "Story not found"}

# ---------- Tickets ----------
@app.post("/tickets")
async def create_ticket(ticket: Ticket):
    ticket_id = len(tickets) + 1
    new_ticket = {
        "id": ticket_id,
        "name": ticket.name,
        "email": ticket.email,
        "message": ticket.message,
    }
    tickets.append(new_ticket)
    return {"status": "success", "ticket": new_ticket}

@app.get("/tickets")
async def list_tickets():
    return {"tickets": tickets}

@app.get("/tickets/{ticket_id}")
async def get_ticket(ticket_id: int):
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            return ticket
    return {"error": "Ticket not found"}
