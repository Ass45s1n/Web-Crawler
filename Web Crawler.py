from urllib import request
url = 'https://www.w3schools.com/python/'
base = 'https://www.w3schools.com'
con = request.urlopen(url).read().decode()
data = con.split()
for i in data:
    if i.startswith('href'):
        i = i.replace("'",'"')
        start = i.find('"') + 1
        end = i.rfind('"')
        i = i[start:end]
        if i.startswith('http'):
            print(i)
        elif i.startswith('//'):
            print('https:'+i)
        elif i.startswith('/'):
            print(base+i)
        else:
            print(url+i)