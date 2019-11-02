<h2 align="center">Terraforming Mars Stats</h2>

* [Deployment](#-deployment)
  * [Initial data import](initial-data-import)

## 🚀 Deployment
```
make build
make migrate
make up
```

Navigate to `localhost:8000` or `<your docker machine ip>:8000` if you use `docker-machine`

To stop the containers, run `make down`

### Initial data import
* Make sure you have the `terra-mars-initial-data.csv` in the `terra_mars/games/initial_import` folder
* Run `make import-initial-data`

