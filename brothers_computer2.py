ciphertext = "rrd ehtHa #tcao sd ea#oe crihewg#Mhe mf ahsm#yeinpobyaoe# rveuri.sms#b ewt r  e.#"
key = "CMPT175"
cipher_columns = ciphertext.split('#')

sorted_key = sorted(key)

columns = list()
for letter in key:
    col_index = sorted_key.index(letter)
    column = cipher_columns[col_index]
    columns.append(column)

message = str()
for row_index in range(len(columns[0])):
    for column in columns:
        if row_index < len(column):
            message = message + column[row_index]
print(message)
        

