# Trending

This command is used to get the currently trending movies or TV shows in your region.

```
python3 main.py trending TYPE --flags
```

*TYPE* must be `movie` or `tv`.

This command supports three flags, all of which are optional:
- **-p, --page** `integer`: The index of the page to return<sup>1</sup>
- **-r, --results** `integer`: The number of results to return<sup>2</sup>
- **--json**: Create a `trending.json` file containing the API response

<sup>1</sup> *A page is created for every 20 results*
<br>
<sup>2</sup> *The maximum number of results is 100 (TODO: check on this)*
