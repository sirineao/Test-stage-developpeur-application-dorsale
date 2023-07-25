import psycopg2, os
from psycopg2.extras import RealDictCursor

def db_connection():
    conn = psycopg2.connect(host=os.environ.get('HOST'),
                            database=os.environ.get('DATABASE'),
                            user=os.environ.get('NAME'),
                            password=os.environ.get('PASSWORD'))
    return conn

def query_from_db():
    conn = db_connection()
    cur = conn.cursor()
    cur.execute('SELECT url, score FROM   louis_v004.crawl, louis_v004.score WHERE louis_v004.crawl.id = louis_v004.score.entity_id')
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data