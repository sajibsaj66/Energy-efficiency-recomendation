import requests

if __name__ == '__main__':

    text = " "

    text = {"text": text}
    api_url = "http://127.0.0.1:5000/energy_recomendation"
    response = requests.post(api_url, json=text)

    if response.status_code == 200:
        data = response.json()
        text = data.get("response", "No response")
        print(f"---------------------------{text}------------------")

    else:
        print(f"response-----------{response.status_code}")
