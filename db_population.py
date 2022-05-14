import sqlite3


db_locale = 'students.db'

connie = sqlite3.connect(db_locale)
c = connie.cursor()


c.execute("""
INSERT INTO contact_details (firstname, surname, street_address, suburb) VALUES 
('David', 'Bowie', '11 Stardust Way', 'Wynnum'),
('Johny', 'Cash', '1 Dark Way', 'Blackall'),
('Joni', 'Mitchell', '2 Sides Lane', 'Canadia')
""")


connie.commit()
connie.close()