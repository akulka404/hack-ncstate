from openai import OpenAI

from api import api

my_api_key = api()

client = OpenAI(api_key=my_api_key)

def giveQuery():
    with open('transcription.txt', 'r') as file:
        content = file.read()
    prompt = f"""
    The following are the steps you need to follow to create a summary.
    Perform the following actions:
        1 - Read the transcription and generate one keyword
        2 - Summarize the whole text
        Sentences:
        {content}
        Give the final output with the keyword and the summary in less than 100 characters.
        """
    return prompt


def query_openai(my_api_key, query):
    try:
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=query,
            max_tokens=2048
        )
        return response.choices[0].text
    except Exception as e:
        return str(e)

query = giveQuery()
response = query_openai(my_api_key, query)
response = response.replace("\n", "")
# print(response)