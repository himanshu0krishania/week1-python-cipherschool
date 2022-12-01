user_name = str(input("enter your name please: "))
user_age = int(input("enter your age please: "))
# user_age = int(user_age)
if user_age >= 10 and (user_name[0]=="a" or user_name[0]=="A"):
  print("you can watch coco movie")
else:
  print("sorry,you cannot watch vedio")