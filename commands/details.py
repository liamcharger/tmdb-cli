import requests
from utils import environment, json, imgcat

def fetch(args):
    url = f"{environment.base_url()}/{args.type}/{args.id}?api_key={environment.api_key()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        title = data.get("title") or data.get("name")
        release_date = data.get("release_date") or data.get("first_air_date")
        overview = data.get("overview")
        poster_path = data.get("poster_path")

        if poster_path:
            imgcat.print(f"{environment.img_url()}{poster_path}")
        
        print(f"Title: {title}")
        print(f"Release Date: {release_date}")
        print(f"Overview: {overview}")

        if args.json:
            json.save(data, "details.json")
    else:
        print("Failed to fetch details. Please make sure the media ID is correct and try again.")