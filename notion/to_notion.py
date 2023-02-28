import os
from bs4 import BeautifulSoup
import json
import markdown2
import requests


NOTION_API_KEY=os.environ['NOTION_API_KEY']
NOTION_DATABASE_ID=os.environ['NOTION_DATABASE_ID']


get_icon_url=lambda x:"https://static.solved.ac/tier_small/%d.svg"%x
teir_dict={'Bronze':0, 'Silver':1,'Gold':2, 'Platinum':3,'Diamond':4,'Ruby':5}
language_dict={'py':"python",'java':"java"}

def  Roman2Number(roman):
    rdict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    nv = roman[0]
    number=rdict[nv]
    for i in range(1,len(roman)):
        bv = nv
        nv = roman[i]
        if(rdict[bv]>=rdict[nv]):
            number += rdict[nv]
        else:
            number += rdict[nv] - 2*rdict[bv]
    return number


def parse_markdown_to_dict(markdown_file, answer_file):
    with open(markdown_file, "r",encoding='utf8') as f:
        markdown_text = f.read()
        html = markdown2.markdown(markdown_text)
    with open(answer_file, "r",encoding='utf8') as f:
        answer=f.read()

    with open("notion/template.json", 'r',encoding="UTF-8") as json_file:
        json_data =json.load(json_file)
    
    soup = BeautifulSoup(html, 'html.parser')
    teir,title=soup.find('h1').get_text().replace('[',"").split(']')
    
    teir,grade=teir.split()
    
    grade_num=Roman2Number(grade)
    link=soup.find('a').attrs['href']
    icon=get_icon_url(teir_dict[teir]*5-grade_num+6)

    p=soup.find_all('p',limit=3)
    memory,time=map(lambda x: x.split(': ')[1],p[1].get_text().replace("[",'').split(", "))

    category=p[2].get_text().split(', ')
    category=[{"name": c }for c in category]
    
    json_data['parent']['database_id']=NOTION_DATABASE_ID

    json_data['icon']['external']['url']=icon
    json_data['properties']['Title']['title']=[{'text': {'content': title}}]
    json_data['properties']['URL']['url']=link
    json_data['properties']['Tier']['select']['name']=teir
    json_data['properties']['Grade']['select']['name']=grade   
    json_data['properties']['Category']['multi_select']=category

    json_data['children'][3]["code"]['rich_text'][0]['text']['content']=answer
    json_data['children'][3]["code"]['language']=language_dict[os.path.splitext(answer_file)[1][1:]]

    json_data['children'][1]["table"]['children'][1]['table_row']['cells'][0][0]['text']['content']=memory
    json_data['children'][1]["table"]['children'][1]['table_row']['cells'][1][0]['text']['content']=time

    return json_data


headers = {
    "Authorization": "Bearer " + NOTION_API_KEY,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
} 

with open("notion/problems.json", 'r',encoding="UTF-8") as problems_file:
    problems =json.load(problems_file)
    already=problems['problems']

for (root, directories, files) in os.walk("백준"):
    for d in directories:
        d_path = os.path.join(root, d)
        if d_path not in already:
            readme,answer="",""
            for i in os.listdir(d_path):
                if "README.md" == i:
                    readme=os.path.join(d_path, i)
                else:
                    answer=os.path.join(d_path, i)
            if readme !="":
                print(answer)
                already.append(d_path)
                markdown_dict = parse_markdown_to_dict(readme,answer)
                res =requests.post('https://api.notion.com/v1/pages', data=json.dumps(markdown_dict), headers=headers)    

problems['problems']=already
with open("notion/problems.json", 'w',encoding="UTF-8") as f:
    f.write(json.dumps(problems, ensure_ascii=False))
