import re, jsbeautifier
from requests import session
requests = session()

#region
mainsite = requests.get('https://bloxd.io').text

def use_regex(input_text):
    pattern = re.compile(r'/[^"]*\.js', re.IGNORECASE)
    return pattern.search(input_text).group()

# Hacky prevent logging the wrong files
mainsite = mainsite.replace('/manifest.js','')
mainsite = mainsite.replace('recaptcha.net/recaptcha/api.js','')
for line in mainsite.split('\n'):
    if '"/static/js' in line and '.js' in line:
        js_name = use_regex(line.strip())
        print(js_name.strip())
        link = f'https://bloxd.io{js_name}'

js_code_raw = requests.get(link)
changed_day = js_code_raw.headers['date'] # Sadly no last changed headers
js_code = js_code_raw.text

# imma save github some work and not deal with sending 50+ requests every hour lmao
try:
    with open('gamecode/main.js','r', encoding="utf-8") as f:
        old_js_code = f.read()
except FileNotFoundError:
    old_js_code = ''

if js_code == old_js_code: exit()

with open('gamecode/main.js','w', encoding="utf-8") as f:
    f.write(js_code)

with open('gamecode/main formatted.js','w', encoding="utf-8") as f:
    formatted_code = jsbeautifier.beautify(js_code)
    f.write(formatted_code)

with open('temp_commit.txt','w') as f:
    import email.utils as utils
    parsed_time = utils.parsedate_to_datetime(changed_day)
    discord_timestamp = int(parsed_time.timestamp())
    formatted = f"<t:{discord_timestamp}>"
    data = f'{formatted} {js_name}\n{changed_day}'
    print(data)
    f.write(data)
#endregion

prefix = js_name.split('/')[-1].split('.')[0]
import chunkSaver
chunkSaver.get_the_chunks(formatted_code,prefix)
