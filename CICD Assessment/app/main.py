# FastAPI app for Azure devops exercise
# Style errors have been included
import os
import socket
from math import sqrt
from typing import Annotated

import uvicorn
from fastapi import FastAPI, Query


def square_root(n=None):
    if n is None:
        raise ValueError("Field required")
    try:
        number = float(n)
    except ValueError as e:
        raise ValueError("Input should be a valid number") from e
    if number < 0:
        raise ValueError("Input should be greater than or equal to 0")
    return f"Square Root of {number} is {sqrt(number)}"


app = FastAPI()


# Use the following url to get the result replacing <IP> with the external IP
# for example, http://20.76.191.125:8000
@app.get("/")
def hello_world():
    try:
        # to get the hostname
        host = socket.gethostname()
        # to get the host ip
        ip = socket.gethostbyname(host)
    except socket.gaierror:
        host = "unkown"
        ip = "unknown"
    message = os.getenv("MESSAGE", "FastAPI Demo")
    return f"{message} on host {host} ({ip})"


# Use the following url to get the result replacing <IP> with the external IP
# for example, http://20.76.191.125:8000/square_root?number=2
@app.get("/square_root")
def square_number(number: Annotated[float, Query(ge=0)]):
    return square_root(number)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=os.getenv("PORT", 8000),
        reload=True,
    )
