import sqlite3, csv

con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("CREATE TABLE person (personid STR,age STR,sex STR,primary_voting_address_id STR,state_code STR,state_fips STR,county_name STR,county_fips STR,city STR,zipcode STR, zip4 STR,  PRIMARY KEY(personid))") 

with open('person.csv','r') as person_table: # 'with' statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(person_table) # comma is default delimiter
#personid   age sex primary_voting_address_id   state_code  state_fips  county_name county_fips city    zipcode zip4
    to_db = [(i['personid'], i['age'], i['sex'], i['primary_voting_address_id'], i['state_code'], i['state_flips'], i['county_name'], i['county_fips'], i['city'], i['zipcode'], i['zip4']) for i in dr]

cur.executemany("INSERT INTO t (age, sex) VALUES (?, ?);", to_db)
con.commit()