# **Fetch Exchange rates (coinMena)**

Api fetches the btc/usd exchange rates hourly

### Setup

- You should have docker and docker-compose installed
  https://docs.docker.com/get-docker/
- set environment variables, .env.example is given.

### Up the API

- clone the repo

`docker-compose build`

- Run the following cmd to up all the containers

`docker-compose up -d`

### PlayGround
 
- To play with an API, you need to create a user first, I have exposed an endpoint to create users 
  ##### POST `http://localhost:8000/api/v1/users/`
  ````
  {
    "username": "mehdiraza",
    "email": "mehdirazajaffri@gmail.com",
    "password": "Mehdi123"
  }
  
- To generate the Token 
  ##### POST `http://127.0.0.1:8000/user/token/`
  ```
  {
    "username": "mehdi",
    "password": "Mehdi123"
  }
  ```
##### Authentication Required for the following calls
    Authorization : Bearer <Access Token>

- To fetch the exchange Rate
  ##### GET `http://127.0.0.1:8000/api/v1/quotes/`
- To fetch the prices form API
  ##### POST `http://127.0.0.1:8000/api/v1/quotes/`


to support: mehdirazajaffri@gmail.com