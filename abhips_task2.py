import random

c=0
score=10
d=''
y=''
word=[]

print("welcome to the game")
clubname=["avc","emotica","souls","vibranz","pixels"]

club=random.choice(clubname)
a=len(club)
word.extend(club)
for i in range(a):
    word[i]="*"
print(word)
print("hint-")
x=clubname.index(club)
if (x==0):
    print('where writngs are turned into cinema')
elif(x==1):
    print('perfroms theatricals')
elif(x==2):
    print('speaks through music')
elif(x==3):
    print('makes music alive')
else :print('it freezes the memories for us')
print("you have two ways to play, choose any one of them")
print("1.guess the letter one by one")
print("2,guess the entire word ")
print("enter your choice")
y=int(input())
print('score=10')
if (y==1):
 while(score>0):
        print("guess a letter=")
        d=(input())
        d=d.lower()
        if d in club:
           if d in word:
              print("letter is already done")
              score-=2
              print("score=",score)
           if d not in word:
             for i in range(a):
              if (club[i]==d):
                word[i]=d
                c+=1
             print("correct guess\n")
             print("word=",word)
             score+=3
             print("score=",score)
            
        if d not in club:
               print("wrong guess")
               score-=2
               print("score=",score)
        if (c==a):
          break    
for i in range(a):
        if club[i]==word[i]:
          print("you won")
        break
        if (score<=0):
          print("you lost")
          break
else:
    print("wrong choice")
if(y==2):
       while(score>0):
        print("guess the word:")
        d=str(input())
        d=d.lower()
        if(d==club):
              print(" word is ",club)
              print("you won\n")
              score+=5
              print("score=",score)
              break
        else:
                score-=3
                print("score=",score)
                print("wrong guess")
       if(score<=0):
            print('you lose')
            print("correct word is",club)

print("thanks")          
