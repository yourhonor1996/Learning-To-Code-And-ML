def rgb(r:int,g:int,b:int):
    #this method uses min() and max to ensure that 0 <= {r,g,b} <= 255
    def clamp(x): 
        return max(0, min(x, 255))
    
    
    return "#{0:02x}{1:02x}{2:02x}".format(clamp(r), clamp(g), clamp(b))

print('dfgkh')
# print("#{0:02x}{1:02x}{2:02x}".format(12,36,64))
# print("{>}".format("dsgasg"))