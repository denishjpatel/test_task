from fastapi import FastAPI
from controllers import user_controller, post_controllers

app = FastAPI()

app.include_router(user_controller.router)
app.include_router(post_controllers.router)
