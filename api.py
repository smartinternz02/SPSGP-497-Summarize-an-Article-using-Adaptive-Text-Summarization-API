import requests
 
url = "https://textanalysis-text-summarization.p.rapidapi.com/text-summarizer"
 
payload = "{\"url\": \"https://en.wikipedia.org/wiki/Natural_farming\",\"text\": \"\",\"sentnum\": 8}"
payload='''{"url":"https://en.wikipedia.org/wiki/Natural_farming","text":"","sentnum":8}'''
headers = {
     'content-type': "application/json",
     'x-rapidapi-key': "537649ff73msh477f6855911bb13p129cf4jsnd5cb001617b2",
     'x-rapidapi-host': "textanalysis-text-summarization.p.rapidapi.com"
     }
 
response = requests.request("POST", url, data=payload, headers=headers)
 
print(response.text)