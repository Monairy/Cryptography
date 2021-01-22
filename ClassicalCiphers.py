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
 matrix=list()
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
      index1=self.matrix.index(l1)
      index2=self.matrix.index(l2)
      for i in range(0,21,5):
            if (index1<i+5 and index2<i+5):
              if(index1>=i and index2>=i):
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

 def getmaprow(self,letter):
     if ((self.matrix.index(letter)+1)%5==0):
            c = self.matrix[self.matrix.index(letter)-4]
     else:
           c = self.matrix[self.matrix.index(letter)+1]
     return c

 def getmapcol(self,letter):
     if ((self.matrix.index(letter))>=20):
            c = self.matrix[self.matrix.index(letter)-20]
     else:
           c = self.matrix[self.matrix.index(letter)+5]
     return c

 def getmapgeneral(self,l1,l2):
      for i in range (len(self.matrix)):
            if (self.samerow(l1,self.matrix[i])):
                if (self.samecol(l2,self.matrix[i])):
                           c = self.matrix[i]
                           break
      return c

 def pad(self,plain):
        padded=plain
        pad=0
        for i in range(len(plain)-1):
            if (plain[i]==plain[i+1]):
                padded= padded[:i+pad+1] + 'x' + padded[i+pad+1:]
                pad+=1
        if (len(padded)%2 != 0 ):
                   padded= padded+'x'
        return padded

 def encrypt(self,key,plain):
         self.playfairmatrix(key)
         plain=plain.replace('j','i')
         plain=plain.replace(' ', '')
         plain=plain.lower()
         plain=self.pad(plain)
         cipher=""
         for i in range(0,len(plain),2):
             p1=plain[i]
             p2=plain[i+1]
             if (self.samerow(p1,p2)):
                     c1=self.getmaprow(p1)
                     c2=self.getmaprow(p2)
             elif (self.samecol(p1,p2)):
                      c1=self.getmapcol(p1)
                      c2=self.getmapcol(p2)
             else:
                      c1=self.getmapgeneral(p1,p2)
                      c2=self.getmapgeneral(p2,p1)
             cipher+=c1+c2 
         return cipher


def vigenere(key,plain,mode):
    cipher=""
    if(mode):
           key=key+plain
    k=0
    for i in range(len(plain)):
            cipher+= caeser(ord(key[k])-97,plain[i])
            k=k+1
            if(k==len(key) and not mode):
               k=0 
    return cipher
def vernam(key,plain):
    cipher=""
    key=key.upper()
    plain=plain.upper()
    for i in range(len(plain)):
               #print((ord('A')-65)^(ord('D')-65))
               
               cipher+= chr( (ord(key[i])-65) ^ ( ord(plain[i])-65) + 65 )
    return cipher         
x=playfair()
#print(x.playfairmatrix("MONARCHY"))
#print(x.encrypt("playfair example","Hide the gold in the tree stump"))
#print(x.pad("aab"))
#print(x.samerow("i","k"))  
#print(x.samecol("f","o"))  
#print(caeser(0,"aBc"))

print(vigenere("deceptive","wearediscoveredsaveyourself",0))

print(vernam("SPARTANS","PXPTYRFJ"))
