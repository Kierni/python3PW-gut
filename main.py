from fastapi import FastAPI

app = FastAPI()

#narzędzie przez któe możemy czymś komunikować działać , np, facebook api pozwala na komunikowanie się z facebookiem, wysysłąmy żadania rewusty i one zawieerająć dane komendy


@app.get("/hello")
async def root():
    return {"message": "Hello World"}
