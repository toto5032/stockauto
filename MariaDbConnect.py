import pymysql

def dbconnect():

    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='Investor', charset='utf8')
    return conn

def main():
    conn = dbconnect()
    print('연결완료')
    conn.close()
    print('연결해제')

if __name__ == "__main__":
        main()
