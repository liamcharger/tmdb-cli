import requests
from utils import environment, json, results

def fetch(args):
    url = f"{environment.base_url()}/search/{args.type}?api_key={environment.api_key()}&query={args.query}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        results_list = data.get("results", [])
        if not results_list:
            print("No results found.")
            return
        
        results.process(results_list, 10) # TODO: add dynamic result count

        if args.json:
            json.save(data, "search.json")
    else:
        print("Failed to search.")