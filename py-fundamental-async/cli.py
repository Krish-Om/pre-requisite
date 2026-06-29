import requests
import typer


def fetch_json():
    url = "https://api.football-data.org/v4/competitions/"
    try:
        r: requests.Response = requests.get(url)
        r.raise_for_status()
        data = r.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


app = typer.Typer()


@app.command()
def hello(name: str = "User"):
    """Print a hello message with the given name."""
    print(f"Hello from prequisite!{name}")


@app.command()
def goodbye(name: str):
    """Print a goodbye message with the given name."""
    print(f"Goodbye : {name}")


@app.command()
def fetch_competitions():
    """Fetch and print information about the FIFA World Cup competitions."""
    data = fetch_json()
    for comp in data["competitions"]:
        if comp["name"] == "FIFA World Cup":
            currSeason = comp["currentSeason"]
            print(
                f"Current Season Id: {currSeason.get('id')}, Name: {comp.get('name')}"
            )
            print(
                f"start date: {currSeason.get('startDate')}, end date: {currSeason.get('endDate')}"
            )
            print(f"Winner: {currSeason['winner']}")


if __name__ == "__main__":
    app()
