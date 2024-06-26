from conexaobd import connect

mydb = connect()

def insert(mydb, nome, email, numero, nascimento):
    mycursor = mydb.cursor()

    sql = "INSERT INTO contato(nome, email, numero, nascimento) VALUES (%s,%s,%s,%s)"
    val = (nome, email, numero, nascimento)
    mycursor.execute(sql, val)

    mydb.commit()
    print(mycursor.rowcount, "Contato inserido com sucesso!")

    mycursor.close()