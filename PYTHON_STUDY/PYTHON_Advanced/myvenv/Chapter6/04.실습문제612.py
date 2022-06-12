import re

datas = {
    'startcoding@maver.com',
    'start-coding@maver.com',
    'start_coding@maver.co.kr',
    'startcoding@k-mail.com',
    '@maver.com',
    'startcoding?@k-mail.com',
    'startcoding@k-mail',
    'startcoding@maver'
}

regex = re.compile('^[\w-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

for data in datas:
    matchObj = regex.match(data)
    result = (lambda x : True if x != None else False)(matchObj)
    print(f'{data} {result}')