from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://ace-tau-gules.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/temp")
def get_temperature(celsius: float = Query(...)):
    kelvin = celsius + 273.15
    fahrenheit = (celsius * 1.8) + 32
    return {"celsius": celsius, "kelvin": kelvin, "fahrenheit": fahrenheit}

@app.get("/prime")
def get_primes(limit: int = Query(..., le=10000)):
    sieve = [True] * (limit + 1)
    sieve[0], sieve[1] = False, False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit + 1, i):
                sieve[j] = False
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    return {"prime numbers in the defined range": primes}

@app.get("/number")
def get_number(n: int = Query(..., ge=0, le=50)):
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
    result = fibonacci(n)
    return {"fibonacci-number": result}