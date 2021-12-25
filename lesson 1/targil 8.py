while(true):
    choice = input("menu:\n----------\n1.insert number and ** it by 3\n2.insert 4 IPs to a list and print it\n3.insert 4 entries to DNS_Dictionary and print it\n4.check if a string is Polindrom\n")
    if (choice == "1"):
         print("THE new nuber is: " + str((int(input("enter a number: "))) ** 3))
         break
    elif (choice == "2"):
        list_ip = []
        list_ip.append(input("enter new ip: "))
        list_ip.append(input("enter new ip: "))
        list_ip.append(input("enter new ip: "))
        list_ip.append(input("enter new ip: "))
        print("\nTHE new list:\n----------------\n" + str(list_ip" ))
        break
    elif (choice=="3"):
        dns_dict = {}
        dns_dict.update({input("enter a URL: "): input("enter IP ")})
        dns_dict.update({input("enter a URL: "): input("enter IP ")})
        dns_dict.update({input("enter a URL: "): input("enter IP ")})
        dns_dict.update({input("enter a URL: "): input("enter IP ")})
        print("\nTHE new dns_dict:\n-------------\n" + str(dns_dict))
        break
    elif (choice=="4"):
        word = input("enter a word: ")
        if (word == word[::-1]):
            print("this is polindrow!")
        else:
            print("this is polindrow!")
        break
    else:
        print("enter 1-4 only!!...\n")


  exit=input("Do you want to exit? y/n")
  if(exit=="y" or exit=="yes"):
      break
  else:
      print("Welcome back!\n")


print("Thank you and bye bye")


