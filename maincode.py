import requests
import json
from datetime import date,datetime
import psycopg2
import pytz 

conn = psycopg2.connect(database="postgres",
                        host="database-1.cawfssevh4on.ap-northeast-1.rds.amazonaws.com",
                        user="postgres",
                        password="postgres",
                        port="5432")


cursor = conn.cursor()
UTC = pytz.utc
IST = pytz.timezone('Asia/Kolkata')
datetime_ist = datetime.now(IST)
#gets date

date_ = datetime_ist.strftime('%Y-%m-%d')
#print(date_)

#gets time
current_time = datetime_ist.strftime('%H:%M:%S')
#print(current_time)


cities = ['Hyderabad','Chennai','Kochi','Mumbai','Delhi','Kolkata','Jaipur','Pune','Bangalore','Ahmedabad']
url = '''https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=c8609d0b95808cae2c99e99a09cd48d3'''

for city in cities:
        city_url = url.format(city)
        response_API = requests.get(city_url)
        data = response_API.text
        parse_json=json.loads(data)


        sql = 'INSERT INTO weatherapi VALUES(%s,%s,%s,%s,%s,%s)'
        val = [date_,current_time,parse_json['name'],parse_json['main']['temp'],
                  parse_json['main']['humidity'],
                  parse_json['main']['pressure'],
                 ]
        cursor.execute(sql,val)
        conn.commit()
print('Done')