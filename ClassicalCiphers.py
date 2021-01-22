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
        for i in range(0,len(plain)-1,2):
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
               cipher+= chr( ((ord(key[i])-65) ^ ( ord(plain[i])-65)) + 65 )
    return cipher

def hill(key,plain):
    cipher=""
    plain=plain.upper()
    for i in range(len(key)):
               key[i]=int(key[i])
               
    if (len(key)==4):
      if(len(plain)%2)!=0:
               plain+="X"
      for i in range(0,len(plain),2):
           c1=key[0]*(ord(plain[i])-65)+key[1]*(ord(plain[i+1])-65)
           c2=key[2]*(ord(plain[i])-65)+key[3]*(ord(plain[i+1])-65)
           cipher+=chr((c1%26) + 65)+chr((c2%26) + 65)
    if (len(key)==9):
      if(len(plain)%3)==1:
               plain+="XX"
      if(len(plain)%3)==2:
               plain+="X"        
      for i in range(0,len(plain),3):
           c1=key[0]*(ord(plain[i])-65)+key[1]*(ord(plain[i+1])-65)+key[2]*(ord(plain[i+2])-65)
           c2=key[3]*(ord(plain[i])-65)+key[4]*(ord(plain[i+1])-65)+key[5]*(ord(plain[i+2])-65)
           c3=key[6]*(ord(plain[i])-65)+key[7]*(ord(plain[i+1])-65)+key[8]*(ord(plain[i+2])-65)
           cipher+=chr((c1%26) + 65)+chr((c2%26) + 65)+chr((c3%26) + 65)           
    return cipher            

#x=playfair()
#print(x.playfairmatrix("MONARCHY"))
#print(x.encrypt("rats","ipmxxpzw"))
#print(x.pad("aab"))
#print(x.samerow("i","k"))  
#print(x.samecol("f","o"))  
#print(caeser(0,"aBc"))

#print(vigenere("pie","dbbadpez",0))

#print(vernam("SPARTANS","PXPTYRFJ"))

def fetchfile(path):
     with open(path,'r') as file:
           lines = file.readlines()
     for i in range(len(lines)):
           lines[i]=lines[i].split("\n")[0]
     return lines

def writefile(path,ciphers):
     with open(path,'w') as file:
          for cipher in ciphers:     
             file.write(cipher+"\n")   
     print("ciphers saved at "+path+"\n")

#print(fetchfile("Input files/caesar_plain.txt"))
             
while(1):
           
  alg = input("choose algorithm 1)Caeser 2)playfair 3)hill 4)vigenere 5)vernam\n")
  if(alg=="1"):
    file = input("Caeser - Enter Filename: ")
    key =  input("Caeser - Enter Key: ")
    try:
               os.remove('Caeser_cipher.txt')
    except:
               pass
    ciphers=list()       
    for plain in fetchfile(file):
       ciphers.append(caeser(int(key),plain))
    writefile('Caeser_cipher.txt',ciphers)

  if(alg=="2"):
    file = input("playfair - Enter Filename: ")
    key =  input("playfair - Enter Key: ")
    try:
               os.remove('playfair_cipher.txt')
    except:
               pass
    ciphers=list()       
    for plain in fetchfile(file):
       x=playfair()
       ciphers.append(x.encrypt(key,plain))
    writefile('playfair_cipher.txt',ciphers)
 
  if(alg=="3"):
    file = input("hill - Enter Filename: ")
    key =  input("hill - Enter Key: ")
    key=key.split(",")
    try:
               os.remove('hill_cihper.txt')
    except:
               pass
    ciphers=list()       
    for plain in fetchfile(file):
       ciphers.append(hill(key,plain))
    writefile('hill_cihper.txt',ciphers)

  if(alg=="4"):
    file = input("vigenere - Enter Filename: ")
    key =  input("vigenere - Enter Key: ")
    mode =  input("vigenere - Enter mode 0)repeating 1)auto: ")

    try:
               os.remove('vigenere_cihper.txt')
    except:
               pass
    ciphers=list()       
    for plain in fetchfile(file):
       ciphers.append(vigenere(key,plain,int(mode)))
    writefile('vigenere_cihper.txt',ciphers)     
     
  if(alg=="5"):
    file = input("vernam - Enter Filename: ")
    key =  input("vernam - Enter Key: ")
    try:
               os.remove('vernam_cihper.txt')
    except:
               pass
    ciphers=list()       
    for plain in fetchfile(file):
       ciphers.append(vernam(key,plain))
    writefile('vernam_cihper.txt',ciphers)

#print(hill([5,17,8,3],"VVMSQFGA"))
#print(hill([2,4,12,9,1,16,7,5,3],"YGREBGHZ"))


