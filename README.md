# Deployable Model

An dockerised API that holds the trained model.  To run in bash:

download the repo
```bash
git clone https://github.com/AerialArmourAquisition/Deployable_Model
cd Deployable_Model
```

run the docker image:
```bash
sudo docker-compose build
sudo docker-compose up
```

this should result in a lot of system out ending in
```bash
app_1  | INFO:     Started server process [1]
app_1  | INFO:     Waiting for application startup.
app_1  | INFO:     Application startup complete.
app_1  | INFO:     Uvicorn running on http://127.0.0.1:5000 (Press CTRL+C to quit)
```

to test API calls open your localhost in the browser and add `/docs` 
```
http://127.0.0.1:5000/docs
```

you'll be greeted by all of the API calls and can test them live

![API_Calls_demo]()
