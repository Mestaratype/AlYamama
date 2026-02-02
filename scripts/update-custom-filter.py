import requests

GF_Latin_All = "https://raw.githubusercontent.com/googlefonts/glyphsets/refs/heads/main/data/results/plist/CustomFilter_GF_Latin.plist"
dest = "sources/CustomFilter_GF_Latin.plist"

r = requests.get(GF_Latin)
with open(dest, "wb") as f:
    f.write(r.content)
