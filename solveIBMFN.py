import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "gTF__TltBqFhSSGBdPw8YkHj69RNQby5ajqJMDiqmB3R"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line

payload_scoring = {"input_data": [{"values" : " I need to eat I am <mask>"}]}

response_scoring = requests.post('https://eu-gb.ml.cloud.ibm.com/ml/v4/deployments/3a48f079-999b-4d88-ad61-ce6aa1283d97/predictions?version=2021-06-22', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print([response_scoring.json()['predictions'][0]['values'][0][i].replace('<s>' , '').replace('</s>' , '') for i in range(4)])