import requests
from htmlextract import extractTxtFromHtml
from gpt_webtxtanalyst import GptWebsiteAnalyser
import requests
import time
import tiktoken

ip = '212.72.171.178'
url = 'http://212.72.171.178/'
r = requests.get(url,allow_redirects=True)
data = r.text


dataExtracted = extractTxtFromHtml(data)
print(len(dataExtracted))
if len(dataExtracted) > 3000:
        dataExtracted = dataExtracted[:3000]



def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

nbtoken = num_tokens_from_string(dataExtracted, "cl100k_base")
print(nbtoken)

'''response = GptWebsiteAnalyser(dataExtracted)
print(ip + ' : ' +response)
'''