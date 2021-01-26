S_BOX = [
            0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67,
            0x2b, 0xfe, 0xd7, 0xab, 0x76, 0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59,
            0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0, 0xb7,
            0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1,
            0x71, 0xd8, 0x31, 0x15, 0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05,
            0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75, 0x09, 0x83,
            0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29,
            0xe3, 0x2f, 0x84, 0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b,
            0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf, 0xd0, 0xef, 0xaa,
            0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c,
            0x9f, 0xa8, 0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc,
            0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2, 0xcd, 0x0c, 0x13, 0xec,
            0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19,
            0x73, 0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee,
            0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb, 0xe0, 0x32, 0x3a, 0x0a, 0x49,
            0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
            0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4,
            0xea, 0x65, 0x7a, 0xae, 0x08, 0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6,
            0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a, 0x70,
            0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9,
            0x86, 0xc1, 0x1d, 0x9e, 0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e,
            0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf, 0x8c, 0xa1,
            0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0,
            0x54, 0xbb, 0x16]

Mix_Col = [
           [2,3,1,1],
           [1,2,3,1],
           [1,1,2,3],
           [3,1,1,2]]

R_CON=[0x1,0x2,0x4,0x8,0x10,0x20,0x40,0x80,0x1b,0x36]

def subBytes(matrix):
   out=[[],[],[],[]]
   for row in range(0,4):
    for col in range(0,4):
        cell=matrix[row][col]
        index=int(cell[0],16)*16 + int(cell[1],16)
        out[row].append('{:02x}'.format(S_BOX[index]))
   return out

def shiftRows(matrix):
  out=[[],[],[],[]]
  shamt=0
  for row in range(0,4):
      out[row]=matrix[row][shamt:]+matrix[row][0:shamt]
      shamt+=1

  return out


def mixColumns(matrix):
    out=[[],[],[],[]]
    
    for col_ip in range(0,4):
               
        currentCol=[]
        for i in range(0,4): currentCol.append(int(matrix[i][col_ip],16))
        
        for row_mc in range(0,4): #row mix_col
            cell=0
            
            for col_mc in range(0,4): #col mix_col
                       
                if Mix_Col[row_mc][col_mc]==1:
                    cell= cell ^ currentCol[col_mc]
                    
                elif (Mix_Col[row_mc][col_mc]==2): #shift left 1
                    temp=(currentCol[col_mc]<<1) 
                    if (temp > 0xff): #1b MSB shifted
                        temp &= 0xff  #make temp 8 bits only
                        temp ^= 0x1b  #xor with field polyn
                    cell^=temp
                    
                elif (Mix_Col[row_mc][col_mc]==3):  #shift left 1
                    temp = (currentCol[col_mc] << 1)
                    if (temp > 0xff): #1b MSB shifted
                        temp &= 0xff  #make temp 8 bits only
                        temp ^= 0x1b  #xor with field polyn
                    temp^=currentCol[col_mc]  #add self
                    cell ^= temp
                    
            out[row_mc].append('{:02x}'.format(cell))
            
    return out

def addRoundKey(matrix,key):
   out=[[],[],[],[]]

   for col in range(0,4):
       matrixCol=[]
       keyCol=[]
       
       for row in range(0,4):#generate col
           matrixCol.append(int(matrix[row][col],16))
           keyCol.append(int(key[row][col],16))
           
       for i in range(0,4):
            xor= matrixCol[i] ^ keyCol[i]
            out[i].append('{:02x}'.format(xor)) #append to each row list

   return out         

def getCol(matrix,colindex):#get Col as HexaDecimal
   matrixCol=[]
   for row in range(0,4):#generate col
       matrixCol.append(matrix[row][colindex])
   return matrixCol 


def keyExpansion(key,rnd):         
    out=[[],[],[],[]]
    
    for colNew in range(0,4):
      wi_4=getCol(key,colNew)

      if(colNew==0):
        wi_1=getCol(key,3)
      else:
        wi_1=getCol(out,colNew-1)
        
      #print(wi_1)

      if(colNew==0):
        wi_1=wi_1[1:]+wi_1[:1]  #rot
        for i in range(0,4): #sBOX
          val=wi_1[i]
          index=int(val[0],16)*16 + int(val[1],16)
          wi_1[i]='{:02x}'.format(S_BOX[index])
      
      w=list()
      for i in range(0,4):
       xor= int(wi_4[i],16) ^ int(wi_1[i],16)
       if(i==0 and colNew==0):
           xor = xor  ^ R_CON[rnd-1]
       w.append('{:02x}'.format(xor))
      
     
      for rowNew in range(0,4):  
        out[rowNew].append(w[rowNew])
    return(out)
    #print(out)

def encrypt(plainMatrix,keyMatrix):
   cipher=addRoundKey(plainMatrix,keyMatrix)
  
   for rnd in range(1,11):
      keyMatrix=keyExpansion(keyMatrix,rnd)
      if (rnd==10):
          cipher=addRoundKey(shiftRows(subBytes(cipher)),keyMatrix)
      else:   
          cipher=addRoundKey(mixColumns(shiftRows(subBytes(cipher))),keyMatrix)

   print(cipher)

arr=[['01','89','fe','76'],
     ['23','ab','dc','54'],
     ['45','cd','ba','32'],
     ['67','ef','98','10']]

roundKey=[['0f','47','0c','af'],
          ['15','d9','b7','7f'],
          ['71','e8','ad','67'],
          ['c9','59','d6','98']]

encrypt(arr,roundKey)
#keyExpansion(roundKey,2)

#print(addRoundKey(mixColumns(shiftRows(subBytes(arr))),roundKey))

