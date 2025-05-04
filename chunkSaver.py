import requests, time, os, shutil

def extract_data_between_quotes(lines):
    result = []
    for line in lines:
        start = line.find('"')
        end = line.rfind('"')
        if start != -1 and end != -1 and start != end:
            result.append(line[start + 1:end])
    return result

def get_lines_between(lines):
    start_index, end_index = (None,)*2

    # We love hard set vars that will prob change someday
    start_str = "Promise.all(Object.keys"
    end_str = ".chunk.css\", "

    for i, line in enumerate(lines):
        if start_str in line and start_index is None:
            start_index = i+1
        elif end_str in line and start_index is not None:
            end_index = i-1
            break
    
    print(f"Start index: {start_index}, End index: {end_index}")
    if start_index is not None and end_index is not None:
        return lines[start_index:end_index + 1]
    else:
        return []

def get_the_chunks(lines:str,prefix:str):
    # Delete and create the chunks folder just incase he changes chunks to be lower
    if os.path.exists('chunks'): shutil.rmtree('chunks')
    os.makedirs('chunks', exist_ok=True)

    lines = lines.splitlines()
    lines_between = get_lines_between(lines)
    data_between_quotes = extract_data_between_quotes(lines_between)

    for i, line in enumerate(data_between_quotes):
        print(f"{i+1}: {prefix}.{i+1}.{line}.chunk.js")
        time.sleep(0.1) # Just to not send them super fast (prob doesn't even matter tbh)
        request = requests.get(f'https://bloxd.io/static/js/{prefix}.{i+1}.{line}.chunk.js')
        with open(f'chunks/{i+1}.chunk.js', 'wb') as f:
            f.write(request.content)
