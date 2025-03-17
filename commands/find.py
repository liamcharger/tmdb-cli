import requests
from utils import environment, json, results

def fetch(args):
    external_source = (
        "imdb_id" if args.imdb else
        "facebook_id" if args.facebook else
        "instagram_id" if args.instagram else
        "tvdb_id" if args.tvdb else
        "tiktok_id" if args.tiktok else
        "twitter_id" if args.twitter else
        "wikidata_id" if args.wikidata else
        "youtube_id" if args.youtube else None
    )
    
    if not external_source:
        print("You must specify an external source. Supported: --imdb, --facebook, --instagram, --tvdb, --tiktok, --twitter, --wikidata, and --youtube.")
        return
    
    url = f"{environment.base_url()}/find/{args.id}?api_key={environment.api_key()}&external_source={external_source}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        results_list = (
            data.get("movie_results") or
            data.get("tv_results") or
            data.get("person_results") or
            []
        )

        if not results_list:
            print("No matching results found.")
            return
        
        results.process(results_list, 10) # TODO: add dynamic result count

        if args.json:
            json.save(data, "find.json")
    else:
        print("Failed to find item.")