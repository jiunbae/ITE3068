from flask import Flask
import memcache
import MySQLdb
import redis
import random

app = Flask(__name__)

testsize = 100000

db = MySQLdb.Connect(host='127.0.0.1', port=3306, user='maybe', passwd='password', db='ite3068')
cursor = db.cursor()
nbase = redis.StrictRedis(port=6000)
arcus = memcache.Client(["127.0.0.1:11211"])

@app.route('/')
def main():
    return 'Main page'

@app.route('/init')
def init():
    cursor.execute('drop table if exists testset');
    cursor.execute('create table testset ( id int, data int );')
    for i in range(testsize):
        cursor.execute('insert into testset values(%s,%s)'%(i + 1, random.randint(0, testsize)))
    db.commit()
    return 'Initialization finished'

@app.route('/mysql')
def mysql(id = None):
    id = id if id != None else random.randint(1, testsize)
    query = 'select * from testset where id=%s' % id
    cursor.execute(query)
    res = cursor.fetchone()
    return res

@app.route('/arcus')
def arcus_(id = None):
    id = id if id != None else random.randint(1, testsize)
    res = arcus.get(str(id))
    if res:
        return 'Cache Hit: ' + str(res)
    else:
        res = mysql(id)
        print ('Cache Miss: MySQL returns', res)
        arcus.set(str(id), res[1])
        return 'Cache Miss: ' + str(res)

@app.route('/nbase')
def nbase_(id = None):
    id = id if id != None else random.randint(1, testsize)
    res = nbase.get(id)
    if res:
        return 'Cache Hit: ' + str(res)
    else:
        res = mysql(id)
        print ('Cache Miss: MySQL returns', res)
        nbase.set(id, res[1])
        return 'Cache Miss: ' + str(res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

