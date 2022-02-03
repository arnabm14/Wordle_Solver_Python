w = open("wordle-answers-alphabetical.txt","r")

#Load_words
l= [i.upper()[:-1] for i in w.readlines()]
w.close()
l[-1]=l[-1] + "L"       #For the last word where there is no \n but the last letter is missed


begin="AUDIO"           #Since this word has 4 vowels and all Black means there is E in the word
                        #Guaranteed 1 hit data

def filter(l,rules):
  copy_l=l[:]
# print("Length of copy_l ",len(copy_l))
  letter=list()

  for r in range(len(rules)):
    sp=str(rules[r]).split(" ")
    if sp[1]=="1":
        # print("Deleting all words where there is : ",sp[0][2:])#, " at the position", sp[2][:-2])
        flag=1
        for j in range(len(rules)):
          if j==r:
            continue
          spp=str(rules[j]).split(" ")
          if  str(sp[0][2:])== str(spp[0][2:]):
            # print(j,r,str(sp[0][2:]),str(spp[0][2:]))
            if int(sp[1]) != 1 or int(spp[1]) != 1:
              flag=0
        if flag==1:
          copy_l=[i for i in copy_l if str(sp[0][2:]) not in i]
    elif sp[1]=="3":
    #   print("Selecting all words where there is : ",sp[0][2:], " at the position", sp[2][:-2])
      copy_l=[i for i in copy_l if str(sp[0][2:])==i[int(sp[2][:-2])]]
    else:
    #   print("Selecting all words where there is : ",sp[0][2:], " but not at the position", sp[2][:-2])
      copy_l=[i for i in copy_l if (str(sp[0][2:]) in i) and (str(sp[0][2:])!=i[int(sp[2][:-2])])]
    letter.append(str(sp[0][2:]))
  # print(letter)
  return copy_l
        
        
rules=[]
guess=[]
d={
    "1":"B",
    "2":"Y",
    "3":"G"
}
for i in range(6):
  
  print("**********************************************")
  print(" Please enter the word : ",begin)
  print(" 1 --> Means Black")
  print(" 2 --> Means Yellow")
  print(" 3 --> Means Green")
  res = input("Enter the Response : ")
  c_string=""
  for j in res:
      c_string=c_string+d[j]
  guess.append(str(begin+" --> "+c_string))
  if res=="33333":
    print("**********************************************")
    print("We Guessed it in ",i+1," tries !")
    break
  for i in range(len(res)):
    rule=[]
    # print(i)
    # print(res[i])
    # if res[i]=="1":
    #   # print(begin[i], d[res[i]],i+1)
    #   rule.append(str(begin[i]+" "+str(res[i])))
      
    # else:
    #   # print(begin[i], d[res[i]])
    rule.append(str(begin[i]+" "+str(res[i])+" "+str(i)))
    rules.append(rule)
#   print(rules)
  l=filter(l,rules)
#   print(len(l))
  begin=l[0]

for i in guess:
  print(i)