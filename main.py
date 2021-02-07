from flask import Flask
import json
import random
import linecache

app = Flask (__name__)
 
@app.route('/')
def nq_na():
  with open('list.json', encoding='utf-8') as q:
    json_object = json.load(q)
  
  a = random.randrange(1, 5) # 1 이상 5 미만
  return json_object[str(a)] # json 파일에서는 name이 전부 str이니까

@app.route('/mbti/<num>')
def mbti(num):
  if num == 'all':
    with open("mbti-all.txt", encoding='utf-8') as file:
      output = file.read()
  elif num == 'ran':
    ran = random.randrange(1, 101)
    try:
      with open("mbti-100.txt", encoding='utf-8') as file:
        output = file.readlines()[ran]
    except IndexError:
      output = '''
        <h1>Oops!</h1>
        <p>서버가 잠시 맛이 갔군요...</p>
        <hr>
        <p>n문n답 API</p>
      '''
  else:
    with open("mbti-100.txt", encoding='utf-8') as file:
      output = linecache.getline('mbti-100.txt', int(num)).strip()


  return '%s'%(output)
 
if __name__ == "__main__":
    app.run('0.0.0.0',8080)