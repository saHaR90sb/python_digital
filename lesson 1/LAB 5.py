dict_names=[{"dudu":25000,"avi":30000,"itay":76000,"ortal":66000,"gal":12000}
print(dict_names)
summay=dict_names["dudu"]+dict_names["gal"]
print("the summary is: " + str(summay))
# dict_names["yoel"]=summay
# print(dict_names)
dict_names.update({"yoel":summay})
print(dict_names)
print("number of entries: " + str(len(dict_names)))
print("yoel" in dict_names)