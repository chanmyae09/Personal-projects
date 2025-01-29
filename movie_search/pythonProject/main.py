import requests


url = "https://api.themoviedb.org/3/search/movie"

api_key = "98f27e87a43244c554bfeb8e07d24eec"
api_access_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5OGYyN2U4N2E0MzI0NGM1NTRiZmViOGUwN2QyNGVlYyIsIm5iZiI6MTczODEyODM1MS43MzQwMDAyLCJzdWIiOiI2Nzk5YmJkZmIwOTM1OWU1Y2NhOTZjZDkiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.y2r8OCfOTxCkjgtr2FSSlSdeBMfKbgv_6k8j_ogyXgE"


header = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_access_token}"
}
params = {
    "query":"Pulp Fiction",

}

response = requests.get(url,headers =header,params=params)
# print(response.status_code)
for results in response.json()["results"]:
    print(results["original_title"])