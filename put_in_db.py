from datetime import date
from pony.orm import *


db = Database()


class InvPrice(db.Entity):
    id = PrimaryKey(int, auto=True)
    Name = Required(str)
    Price = Required(float)
    Num = Required(int)
    Date = Required(date)


db.bind("sqlite", ":memory:")
db.generate_mapping(create_tables=True)
