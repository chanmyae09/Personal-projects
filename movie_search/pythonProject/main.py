import requests


url = "https://api.themoviedb.org/3/search/movie"

api_key = "98f27e87a43244c554bfeb8e07d24eec"
api_access_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5OGYyN2U4N2E0MzI0NGM1NTRiZmViOGUwN2QyNGVlYyIsIm5iZiI6MTczODEyODM1MS43MzQwMDAyLCJzdWIiOiI2Nzk5YmJkZmIwOTM1OWU1Y2NhOTZjZDkiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.y2r8OCfOTxCkjgtr2FSSlSdeBMfKbgv_6k8j_ogyXgE"


header = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_access_token}"
}
param = {
    "query":"Pulp Fiction",
}
movie_id=  680
# response = requests.get(url,headers =header,params=param)
# print(response.json())

response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}", headers=header, )
print(response.json()["poster_path"])

# for results in response.json()["results"]:
#     print(results["original_title"],results["release_date"])