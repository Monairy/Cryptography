#filename = input("Enter File Name: ")



def caeser(key,plain): 
    cipher = str()

    for letter in plain: 
     
        if (letter.islower()):
                index=ord(letter)-97
        elif(letter.isupper()):
               index=ord(letter)-65
           
        mapping = (index+key) % 26
        
        if (letter.islower()):
               temp = chr(mapping+97)
        elif (letter.isupper()): 
               temp = chr(mapping+65)
               
        cipher = cipher+temp
        
    return cipher

class playfair:
 matrix = list()
         
 def playfairmatrix(self,key):
    key=key.lower()
    x=0
    for i in range(len(key)):
           if key[i] == ' ':
                      continue
           if key[i] not in self.matrix:
              self.matrix.append(key[i])
              x=x+1
              
    for i in range (97,123):
           if chr(i) == 'j':
              continue
           if chr(i) not in self.matrix:
              self.matrix.append(chr(i))          
           
    return self.matrix

 def samerow(self,l1,l2):
      if (l1=='j'):
                 l1="i"
      if (l2=='j'):
                 l2='i'
      if abs(self.matrix.index(l1)-self.matrix.index(l2))<5:
          return 1
      return 0

 def samecol(self,l1,l2):
      if (l1=='j'):
                 l1="i"
      if (l2=='j'):
                 l2='i'
      if abs(self.matrix.index(l1)-self.matrix.index(l2))%5==0:
          return 1
      return 0

 def pad(self,plain):
        padded=plain
        pad=0
        for i in range(len(plain)-1):
            if (plain[i]==plain[i+1]):
                padded= padded[:i+pad+1] + 'x' + padded[i+pad+1:]
                pad+=1
        return padded        
                

             
x=playfair()
print(x.playfairmatrix("MONARCHY"))
print(x.pad("aaaabccacca"))
#print(x.samerow("i","k"))  
#print(x.samecol("f","o"))  

#print(caeser(0,"aBc"))


