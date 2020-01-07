import json
import re

def process_data(text):
    groups = re.match(r'.*?\((.*)\)', text)
    data_json = json.loads(groups[1])
    context = data_json['data']['archives']
    print(len(context))
    for item in context:
        print(item['title'], item['ctime'])
if __name__ == "__main__":
    f = open("data1.txt", 'r')
    data = f.read()
    process_data(data)