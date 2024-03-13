import sqlite3
import pandas as pd

con = sqlite3.connect("data.db")

df = pd.read_sql_query("SELECT * FROM  wp_posts", con)

print(df)
# cur.execute("SELECT post_content, ID FROM wp_posts WHERE post_content LIKE '[%' ")

# def split(record):
#     result = []
#     items = ''
#     end = 0
#     for i in range(len(record)):
#         if record[i] == '\n':
#             result.append(items)
#             items = ''
#             continue
#         items = items + record[i]
#         end += 1
#     return result

# def format(lists):
#     result = {}
#     flag = 0
#     key = ''
#     item = ''
#     for i in range(1, len(lists)):
#         if lists[i] == ']':
#             flag = 1
#             continue
#         if flag == 0:
#             key = key + lists[i]
#         else:
#             item = item + lists[i]
#     result[key] = item
#     return result

# def makeID(input):
#     result = []
#     output = {}
#     for records in input:
#         splits = split(records[0])
#         for i in range(len(splits)):
#             result.append(format(splits[i]))
#     print(output)

# input = cur.fetchall()
# print(input)
'''makeID(input)'''


# print(cur.fetchall())

# con.close()