import os
import time
import pandas as pd
from sqlalchemy import create_engine, text

CSV_URL = os.getenv("CSV_URL")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
DB_NAME = os.getenv("DB_NAME", "bank")
TABLE_NAME = os.getenv("TABLE_NAME", "clients")

def make_engine():
    url = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    return create_engine(url, pool_pre_ping=True)

def wait_for_db(engine, retries=30, sleep_s=2):
    for i in range(retries):
        try:
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            return
        except Exception as e:
            print(f"[wait_for_db] intento {i+1}/{retries} falló: {e}")
            time.sleep(sleep_s)
    raise RuntimeError("No se pudo conectar a la DB a tiempo.")

def main():
    if not CSV_URL:
        raise ValueError("Falta CSV_URL")

    print(f"Leyendo CSV: {CSV_URL}")
    df = pd.read_csv(CSV_URL, sep=";")  # este dataset viene con ';'

    engine = make_engine()
    wait_for_db(engine)

    print(f"Escribiendo en {DB_NAME}.{TABLE_NAME} (overwrite)...")
    # if_exists='replace' => sobreescribe la tabla cada corrida
    df.to_sql(TABLE_NAME, engine, if_exists="replace", index=False)

    print("OK ✅")

if __name__ == "__main__":
    main()
