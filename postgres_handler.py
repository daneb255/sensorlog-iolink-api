import psycopg2
from core.config import POSTGRESPASSWORD, POSTGRES_DB, POSTGRES_HOST, POSTGRES_USER


def write_to_postgres(timestamp, x, y, z, device_id, label):
    try:
        conn = psycopg2.connect(host=POSTGRES_HOST,
                                port=5432,
                                user=POSTGRES_USER,
                                password=POSTGRESPASSWORD,
                                database=POSTGRES_DB)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO motionuseracceleration (device_id, label, date_time, motionuseraccelerationx, motionuseraccelerationy,"
                       " motionuseraccelerationz) VALUES(%s, %s, %s, %s, %s, %s)",
                       (device_id, label, timestamp, x, y, z))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print(e)
