def set(args):
    # TODO: add support for region, base_url, and img_url, and allow each var to be updated without overwrite
    if args.set == "region":
        print("We gotta set the region here...")
    else:
        with open(".env", "w") as f:
            f.write(f"API_KEY={args.value}\n")
        print("API key set successfully!")