import sqlite3 as sq
import json as js
con = sq.connect("data.db")

cur = con.cursor()

'''cur.execute("""CREATE TABLE customers(
    first_name text,
    last_name text,
    email text
)""")'''

'''many_customers = [
                    ('Wes', 'Brown', 'west@yahoo.com'), 
                    ('Eric', 'Zhang', 'khekwok@connect.ust.hk')
                  ]

cur.execute("INSERT INTO customers VALUES('Jason', 'Kwok', 'jk@gmail.com')")
print("inserted")

cur.executemany("INSERT INTO customers VALUES(?, ?, ?)", many_customers)
print("inserted many")'''



cur.execute("SELECT ID, post_content FROM wp_posts WHERE post_content LIKE '[%' ")


def split(record):
    result = []
    items = ''
    end = 0
    for i in range(len(record)):
        if record[i] == '\n':
            result.append(items)
            items = ''
            continue
        items = items + record[i]
        end += 1
    return result


def format(lists):
    result = {}
    flag = 0
    key = ''
    item = ''
    for i in range(1, len(lists)):
        if lists[i] == ']':
            flag = 1
            continue
        if flag == 0:
            key = key + lists[i]
        else:
            item = item + lists[i]
    if key != item:
        result[key] = item
    return result

def makeDictionary(input, db):
    ID_dict = {}
    for records_index in range(len(input)):
        if db == "posts":
            splits = split(input[records_index][1])
        elif db == "tagthis":
            splits = input[records_index][1]
        output = []
        if type(splits) is list:
            for i in range(len(splits)):
                result = format(splits[i])
                if result != {}:
                    output.append(result)
        elif type(splits) == str:
            result = format(splits)
            if result != {}:
                    output.append(result)
        ID_dict[int(input[records_index][0])] = output
    return ID_dict
        
input = cur.fetchall()

output = makeDictionary(input, "posts")
with open("result_post.json", "w") as f:
    js.dump(output, f, indent=4)

cur.execute("SELECT id, tag FROM wp_tagthis WHERE tag LIKE '[%' ")

input = cur.fetchall()

output = makeDictionary(input, "tagthis")
with open("result_tagthis.json", "w") as f:
    js.dump(output, f, indent=4)

with open("result_tagthis.json", encoding="utf-8") as f:
    print(js.load(f))



con.commit()

con.close()




