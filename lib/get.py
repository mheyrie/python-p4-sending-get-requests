import requests
import json

# url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/locations.json"
url = "https://moringa.instructure.com/courses/356/pages/useful-reading-and-exploration?module_item_id=64467"

response = requests.get(url)

# json_content = json.loads(response.content)

# print(json.dumps(json_content, indent=4, sort_keys=True))
print(response.text)
# print(response.content)
# print(json_content)