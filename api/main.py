from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins; you can restrict this for production
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods; you can restrict this for production
    allow_headers=["*"],  # Allows all headers; you can restrict this for production
)

# Sample project data
projects = [
    {
        "id": 1,
        "title": "Project One",
        "description": "This is the first project.",
        "image_url": "https://via.placeholder.com/150",
        "project_url": "https://google.com/project1"  # Changed to google.com
    },
    {
        "id": 2,
        "title": "Project Two",
        "description": "This is the second project.",
        "image_url": "https://via.placeholder.com/150",
        "project_url": "https://google.com/project2"  # Changed to google.com
    },
    {
        "id": 3,
        "title": "Project Three",
        "description": "This is the third project.",
        "image_url": "https://via.placeholder.com/150",
        "project_url": "https://google.com/project3"  # Changed to google.com
    },
    {
        "id": 4,
        "title": "Project Four",
        "description": "This is the fourth project.",
        "image_url": "https://via.placeholder.com/150",
        "project_url": "https://google.com/project4"  # Changed to google.com
    },
    {
        "id": 5,
        "title": "Project Five",
        "description": "This is the fifth project.",
        "image_url": "https://via.placeholder.com/150",
        "project_url": "https://google.com/project5"  # Changed to google.com
    }
]

@app.get("/projects")
def get_projects():
    return projects