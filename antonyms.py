dic={"hot":"cold","black":"white","up":"down"}
state="yes"
while(state=="yes"):
    name=input("enter the word: ")
    if(name in dic):
         print ("opposite:",dic[name])
    if(name not in dic):
         print("opposite dosent exist do you know? ")
         an=input()
         if(an=="yes"):
             op=input("enter the word ")
             dic[name]=op
         if(an=="no"):
             print("ok then ")
    state=input("do you want try again? ")
    
    
