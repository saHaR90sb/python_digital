#dictionary

my_dict={"www.google.com":"8.8.8.8.,"www.facebook.com":7.7.7.7","www.youtube.com":["5.5.5.5","4.4.4.4"]}
my_dict2={"www.nrt4uc.com":"33.33.33.33","www.groo.co.il":"88.88.88.88"}
print(my_dict)
print(my_dict2)
my_dict.update(my_dict2)
print(my_dict)

print("number of entries: " + str(len(my_dict)))
print(my_dict["www.google.com"])
print(my_dict.values())
my_dict["www.google.com"]="8.8.4.4"
print(my_dict["www.google.com"])