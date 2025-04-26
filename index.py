import re
import jsbeautifier
from requests import session
requests = session()

mainsite = requests.get('https://bloxd.io').text

def use_regex(input_text):
    pattern = re.compile(r'/[^"]*\.js', re.IGNORECASE)
    return pattern.search(input_text).group()

mainsite = mainsite.replace('/manifest.js','') # Hacky
mainsite = mainsite.replace('recaptcha.net/recaptcha/api.js','') # Hacky
for line in mainsite.split('\n'):
    if '"/static/js' in line and '.js' in line:
        js_name = use_regex(line.strip())
        print(js_name.strip())
        link = f'https://bloxd.io{js_name}'

js_code_raw = requests.get(link)
changed_day = js_code_raw.headers['date']
js_code = js_code_raw.text

with open('gamecode/main.js','w', encoding="utf-8") as f:
    f.write(js_code)

with open('gamecode/main formated.js','w', encoding="utf-8") as f:
    formatted_code = jsbeautifier.beautify(js_code)
    f.write(formatted_code)

with open('temp_commit.txt','w') as f:
    data = f'{changed_day} {js_name}'
    print(data)
    f.write(data)
