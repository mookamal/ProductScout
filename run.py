import functions as run

# get input word from user 
word = input("write word to searching : ")

if word == "":
    print("Please try again and type the search word")
else:
    data_ebay = run.ebay(word)
    data_etsy = run.etsy(word)
    run.show(data_ebay)
    run.show(data_etsy)