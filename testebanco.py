from bdcontatos import insert
from conexaobd import connect

mydb = connect()

insert(mydb,'Teste','email@email.com', '9999-9999','2024-05-24')

