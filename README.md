## Check my Bike
Check my bike is a prototype application that uses a simple predictive techniques to notify an user the precise time to leave before she runs out of CitiBike docks or bikes.


## Data Sources
* Historical data: http://www.citibikenyc.com/system-data
* Live station feed: http://www.citibikenyc.com/stations/json
* Status key: http://www.citibikenyc.com/stations/status_json

## Build and Run
To build, test, and run the application locally, run:

```
$ make build
$ make test
$ make run
```

## Development
If you are interested in contributing, run the following to setup your development environment:

```
$ make setup
```

(*For now, this is the only part working.*)

## Test
```
$ make test
```


## Secrets
The [`config/secrets.json`](config/secrets.json) file should contain both information about the Pushbullets API and the Mailgun API. The file should look like this:

```json
{
  "pushbullet_key": "YOUR_PUSHBULLET_KEY",
  "mailgun_key": "YOUR_MAILGUN_KEY",
  "mailgun_domain": "YOUR_MAILGUN_DOMAIN"
}

```
