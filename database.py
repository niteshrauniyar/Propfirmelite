import sqlite3

def init_db():
    conn = sqlite3.connect('prop_data.db', check_same_thread=False)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS firms 
                 (id INTEGER PRIMARY KEY, name TEXT, discount TEXT, 
                  split TEXT, price TEXT, rating REAL, link TEXT, category TEXT)''')
    
    # Insert default data if empty
    c.execute("SELECT count(*) FROM firms")
    if c.fetchone()[0] == 0:
        sample_firms = [
            ('FundingPips', '5% OFF', '80/20', '$399', 4.9, '#', 'Futures'),
            ('FTMO', 'NONE', '90/10', '€540', 4.8, '#', 'Forex'),
            ('Alpha Capital', '10% OFF', '80/20', '$497', 4.7, '#', 'Institutional')
        ]
        c.executemany("INSERT INTO firms (name, discount, split, price, rating, link, category) VALUES (?,?,?,?,?,?,?)", sample_firms)
    conn.commit()
    return conn

def get_all_firms():
    conn = init_db()
    return conn.execute("SELECT * FROM firms").fetchall()
