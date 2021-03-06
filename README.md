# leaguelosestreakmeter

Lose streak meter for League of legends  

Actually checking only Ranked games

## Installing

```sh
pip install leaguelosestreakmeter
```

You also need to have an API key from Riot. Get that from [here](https://developer.riotgames.com/)

## Usage

Easy to use ;)

```python
import leaguelosestreakmeter as llsm

riot_api_key = "<riot-api-key>"
region = "EUN1" # other regions list: https://developer.riotgames.com/docs/lol

nickname = input("Enter nickname: ")

losestreak = llsm.losestreak(riot_api_key, region, nickname)
print("Losestreak: {}".format(losestreak))
```
