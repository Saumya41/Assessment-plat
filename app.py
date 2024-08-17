from fastapi import FastAPI, Depends
from auth.jwt_bearer import JWTBearer
from config.config import initiate_database
from routes.admin import router as AdminRouter
from routes.student import router as StudentRouter
from routes.question import router as QuestionRouter
from routes.answer import router as Answerrouter
from routes.quiz import router as Quizrouter

app = FastAPI()

token_listener = JWTBearer()

@app.on_event("startup")
async def start_database():
    await initiate_database()


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to Assessment Platform."}


app.include_router(AdminRouter, tags=["Administrator"], prefix="/admin")
app.include_router(QuestionRouter, prefix="/Question", tags=["Question"],dependencies=[Depends(token_listener)],)
app.include_router(StudentRouter,tags=["Students"],prefix="/student",dependencies=[Depends(token_listener)],)
app.include_router(Answerrouter, prefix="/answers", tags=["answers"])
app.include_router(Quizrouter, prefix="/quiz", tags=["Quiz"])