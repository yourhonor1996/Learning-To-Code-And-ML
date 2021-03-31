def domain_name(url:str):
    startList = ('https://www.','http://www.','http://','https://','www.',"")
    # if url.startswith(startList):
    for item in startList:
        if url.startswith(item):
            temp = url[len(item):]
            b = temp.find('.')
            # print(temp[:b])
            return temp[:b]
        
a = "https://www.google.com"
domain_name(a)
# print(a.find('.'))