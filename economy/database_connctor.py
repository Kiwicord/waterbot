import sqlite3

connection = sqlite3.connect('bank.db')
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS members(
    id text,
    wallet integer,
    bank integer
)
""")

async def select_from_database(user_id):
    cursor.execute('SELECT * FROM members WHERE id={}'.format(user_id))
    info = cursor.fetchone()

    connection.commit()
    return info

async def update_wallet(user_id, amount):
    info = await select_from_database(user_id)
    wallet = info[1]
    cursor.execute("""UPDATE members SET wallet = :wallet WHERE id = :id""", {'id': user_id, 'wallet': wallet + amount})
    connection.commit()

async def deposit_amount(user_id, amount):
    info = await select_from_database(user_id)
    wallet = info[1]
    bank = info[2]

    cursor.execute('UPDATE members SET bank = :bank WHERE id = :id', {'id': user_id, 'bank': int(bank) + int(amount)})
    cursor.execute('UPDATE members SET wallet = :wallet WHERE id = :id', {'id': user_id, 'wallet': int(wallet) - int(amount)})
    connection.commit()

async def withdraw_amount(user_id, amount):
    info = await select_from_database(user_id)
    wallet = info[1]
    bank = info[2]

    cursor.execute('UPDATE members SET bank = :bank WHERE id = :id', {'id': user_id, 'bank': int(bank) - int(amount)})
    cursor.execute('UPDATE members SET wallet = :wallet WHERE id = :id', {'id': user_id, 'wallet': int(wallet) + int(amount)})
    connection.commit()

async def check_account(user_id):
    cursor.execute('INSERT INTO members VALUES (:id, :wallet, :bank)', {'id': user_id, 'wallet': 0, 'bank': 0})