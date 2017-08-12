import sqlite3
from datetime import timedelta
from datetime import datetime
from dateutil.relativedelta import relativedelta


class GruppenkassenDB():
    
    conn = sqlite3.connect("gruppenkasse.db")
    
    def __init__(self):
        self.create_db()
        
        
    def create_db(self):
        cur = self.conn.cursor()
        
        table_childs = "CREATE TABLE IF NOT EXISTS childs (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \
        name VARCHAR(255), bezahlt_bis DATE, erstellt_am DATE, geld INTEGER)"
        
        table_ausgaben = "CREATE TABLE IF NOT EXISTS ausgaben (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \
        verwendungszweck VARCHAR(255), preis DECIMAL(6,2), datum DATE)"
        
        cur.execute(table_childs)
        cur.execute(table_ausgaben)
        
        cur.close()
    
    
    def set_data_into_childs(self, **kwargs):
        cur = self.conn.cursor()
        try: 
            name = kwargs['name']
        except KeyError:
            name = "NULL"
        try:
            bezahlt_bis = kwargs['bezahlt_bis']
        except KeyError:
            bezahlt_bis = "NULL"
        try:
            erstellt_am = kwargs['erstellt_am']
        except KeyError:
            erstellt_am = "NULL"
        try:
            geld = kwargs['geld']
        except KeyError:
            geld = "NULL"
        
        query = "INSERT INTO childs VALUES (NULL, ?, ?, ?, ?);"
        
        cur.execute(query,(name, bezahlt_bis, erstellt_am, geld,))
        self.conn.commit()
        cur.close()
    
    
    def update_child_data(self, **kwargs):
        cur = self.conn.cursor()
        old_data = ""
        old_money = 0
        erstellt_am = ""
        bezahlt_bis = ""
        if "name" in kwargs:
            name = kwargs['name']
            old_data = self.get_data_table_childs(kwargs['name'])
            old_money = old_data[4]
            erstellt_am = old_data[3]
            bezahlt_bis = old_data[2]
        else:
            raise Exception('name must be defined')
        
        try:
            geld = kwargs['geld']
        except KeyError:
            raise Exception("Geld must be defined")
    
        if bezahlt_bis != "NULL":
            bezahlt_bis = datetime.strftime(datetime.strptime(bezahlt_bis, "%Y-%m-%d") + relativedelta(months=+int(geld)), "%Y-%m-%d")
        else:
            bezahlt_bis = datetime.strftime(datetime.strptime(erstellt_am, "%Y-%m-%d") + relativedelta(months=int(geld)), "%Y-%m-%d")
            
        
        query = "UPDATE childs SET geld=?, bezahlt_bis=? WHERE name=?";
        
        cur.execute(query, (str(int(geld) + old_money), bezahlt_bis, name,))
        self.conn.commit()
        cur.close()
    
    
    def get_data_table_childs(self, name="*"):
        cur = self.conn.cursor()
        
        if name == '*':
            cur.execute("SELECT * FROM childs")
            query = cur.fetchall()
            cur.close()
            return query
                
        elif name != '':
            cur.execute("SELECT * FROM childs WHERE name=?;", (name,))
            query = cur.fetchone()
            cur.close()
            return query
        else:
            pass
            
    
    def create_ausgabe(self, **kwargs):
        cur = self.conn.cursor()
        try:
            verwendungszweck = kwargs['verwendungszweck']
        except KeyError:
            pass
        try:
            preis = kwargs['preis']
        except KeyError:
            pass
        try:
            datum = kwargs['datum']
        except KeyError:
            pass        
        
        query = "INSERT INTO ausgaben VALUES (NULL, ?, ?, ?)"
        
        cur.execute(query, (verwendungszweck, preis, datum,))
        self.conn.commit()
        cur.close()
    
    
    def get_ausgaben(self):
        cur = self.conn.cursor()
        data = ""
        query = "SELECT * FROM ausgaben"
        
        cur.execute(query)
        data = cur.fetchall()
        
        cur.close()
        return data
    
    
    def query_to_dic(self, query):
        data = []
        if len(query[0]) == 5:
            for q in query:
                data.append(
                    {'id':q[0], 'name': q[1], 'bezahlt_bis': q[2], 'erstellt_am': q[3], 'geld':q[4]}
                )
        else:
            for q in query:
                data.append(
                    {'id':q[0], 'verwendungszweck': q[1], 'preis': q[2], 'datum': q[3]}
                )            
        return data
    