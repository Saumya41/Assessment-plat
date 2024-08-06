from fastapi import FastAPI, Depends
from auth.jwt_bearer import JWTBearer
from config.config import initiate_database
from routes.admin import router as AdminRouter
from routes.student import router as StudentRouter
from routes.question import router as QuestionRouter

app = FastAPI()

token_listener = JWTBearer()

@app.on_event("startup")
async def start_database():
    await initiate_database()


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to Assessment Platform."}


app.include_router(AdminRouter, tags=["Administrator"], prefix="/admin")
app.include_router(QuestionRouter, prefix="/quiz", tags=["quiz"],dependencies=[Depends(token_listener)],)
app.include_router(StudentRouter,tags=["Students"],prefix="/student",dependencies=[Depends(token_listener)],)
