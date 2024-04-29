from fastapi import FastAPI


from models import QueryItem
from chat.llm_task import search_courses

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/courses")
async def get_courses(item: QueryItem):
    """
    query - search text
    k - return courses count
    """
    print(item)
    courses = search_courses(query=item.query, k=item.k)
    return {
        "message": "successful",
        "courses": courses
    }
