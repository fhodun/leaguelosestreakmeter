from riotwatcher import LolWatcher, ApiError


def losestreak(token, region, summoner_name):
    lol_watcher = LolWatcher(token)

    try:
        summoner = lol_watcher.summoner.by_name(region, summoner_name)
    except ApiError as err:
        if err.response.status_code == 429:
            raise Exception("you should retry in {} seconds".format(
                err.response.headers["Retry-After"]), err.response.headers["Retry-After"])
        elif err.response.status_code == 404:
            raise Exception("summoner with that ridiculous name not found")
        else:
            raise Exception("unknow summoner fetching error ocurred")

    matches = lol_watcher.match.matchlist_by_account(
        region, summoner["accountId"], queue=420)

    losestreak = 0
    for match in matches["matches"]:
        champion_id = match["champion"]
        true_match = lol_watcher.match.by_id(region, match["gameId"])

        for participant in true_match["participants"]:
            if participant["championId"] == champion_id:
                victim = participant["teamId"]
                break

        for team in true_match["teams"]:
            if team["teamId"] == victim:
                if team["win"] == "Fail":
                    losestreak += 1
                elif team["win"] == "Win":
                    return losestreak
                else:
                    raise Exception("lose detection failed")
