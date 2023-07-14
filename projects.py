print("Insert your card")
print("Processing...")
p=int(input("enter your pin"))
val=2345
Balance= 20000

if(val==p):
  print("enter the choice")
  print("1. Withdraw\n2.check balance" )
  v=int(input())
  if(v==1):
      amount=int(input(("enter the amount")))
      if(amount<Balance):
        Balance-=amount
        print("processing...\nAmount withdrawal")
        print("Your updated balance is",Balance)
        print("Visit again..")
      else:
        print("Not Enough Balance\nEnter amoun t again")
        
  if(v==2):
      print("your balance is",Balance)
else:
    print("enter correct pin")
    