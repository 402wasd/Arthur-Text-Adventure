#REEDUS
import random
import time
import sys

#vocabulary
salutation = ['hey','hello','hi','howdy','yo','sup']
ex = ['bye','get out','you may go','exit']
ques = ['are','is','was','does','did','do','who','what','where','when','how','whose','which','did','why']
ok = ['ok','hmm','ha','yeah','right','fine','okay','alright']
harm = ("kidnap","abduct","kill","harm")
killer =  ['accused','culprit','killer','suspect','murderer','verdict']
#NEW************
music = ['music','singer','band','artist','performer']
friends = ['friends','friend','circle','group','social']
tell = ['tell','speak','describe','say','talk']
hate = ['hate','detest','not like']

print("ARTHUR ELLIOT DISAPPEARED FROM HIS DORM ROOM AT THE STATE UNIVERSITY. IT HAS BEEN OVER 48 HRS. PETER REEDUS WAS HIS ROOMMATE AND CLOSE FRIEND. PETER REEDUS IS THE PRIME SUSPECT.\nYOU WILL NOW INTERVIEW HIM")


def rand(t):
    n = random.randint(0,len(t)-1)
    return t[n]
    pass
def cc(s,l):
    k = s.split(" ")
    for a in k:
        if a in l:
            return True
        else:
            return False
def xx(s):
    global inp
    if s in inp:
        return True
    else:
        return False

#time
def show(s):
    b=""
    for a in s:
        #b+=a
        sys.stdout.write(a)
        time.sleep(0.05)
    print(b)

# system
# 0 - neutral; positive - ,
# negative -
mood = 0


def peter(s):
    global inp
    global mood
    if inp!="":
        print("YOU: "+inp)
        print("PETER REEDUS:",end="")
    if cc(s,salutation):
        show(rand(("Hello","Hi","Hey")))
    elif cc(s,ok):
        show("Yeah.")
    elif cc(s,ex):
        global o
        show("Thank you...")
        o = False
    #TELL About
    elif cc(s,tell):
        if xx("more"):
            show("That's all I can say because that's all I know.")
        else:
            show("Please be specific, what you want to know.")

    elif cc(s,ques) or "?" in s:#NEW************
        if xx("what") and xx("your"):
            if xx("your"):
                if xx("name"):
                    show(rand(("Its Peter. Don't you already know?","I'm Peter. Peter Reedus.")))
                elif xx("favourite") or xx("favorite"):
                    if cc(s,music):
                        show(rand("I really like Coldplay","Coldplay is a good band.","I think it has to be Coldplay. They're really good."))
            else:
                show("I don't know or remember.")
#new method of checking ques, using ? and had? have?

        elif cc(s,friends) or xx("friends"):
            if xx("you"):
                show("Not many. Boney and Tom, I think besides Arthur")
            elif xx("arthur"):
                show("Arthur? Yes, a lot of them. He was a cool guy, everyone went around him. He used to say he didn't want it though. He hated his popularity or probably said so in front of me. In my opinion he was enjoying all the attention he was receiving. He was one of the most popular students in the University.")
                show("Speaking of friends, Arthur was a good friend of mine. He was also close to Amy, Boney and Sid Meyer.")
                show("He used to frequently meet them up at the Red Basement.")
        elif xx("red basement"):
            if xx("arthur"):
                show("I don't know really. What he did or where he went. He was a very mysterious person.")
            else:
                show("It is a closed for students place. Near the Library, an abandoned parking lot. I'd seen Arthur returning late at nights. He'd say he was hanging out at the Red Basement.")
        #%^&*%$#NEW
        elif xx("when") and xx("last") and xx("arthur"):
            show("Today is 11 October. On 9 October, the last time I saw him was at around 11am in the morning in our dorm room. I left for classes, he said he wasn't feeling well. He must've been kidnapped or something during that span of 2 hours. I mean betweeen 11am and 1pm because when I came back to our room, he was no where to be found. He was mildy sick.")
        elif xx("what"):
            if xx("happened") and xx("to arthur"):
                show(rand(("He is missing since 9 October, noon. I hope he returns.","Don't you already know that? he is gone. I hope he returns.")))
        elif xx("where") and xx("arthur"):
            show(rand(("I dont know... I want you to find out. Ask Amy.","I am thinking the same, since his disappearance. Ask Amy.","I can't really tell you that. Because I don't know. Ask Amy.")))
        elif xx("who") or xx("how"):
            if xx("amy"):
                show("Honestly, Arthur did talk about Amy sometimes. He would say how happy he was, with everything in his favour. I mean they both were really close friends.")
                show(rand(("I didn't really know Amy. I mean we'd talked but she wasn't even close to friendly. Arthur was a good friend of hers surprisingly.","She was in our class. Honestly I didn't like her at all. She was close to Peter though.")))
            elif xx("arthur"):
                show(rand(("He is one of my best friends, the only friend I would say","You must be knowing he was my roommate and a fine boy in general","He was very condenscending sometimes. He used to sometimes humiliate me too.")))
            #NEw^%^^%^##$%
            elif xx("boney"):
                show("Boney Rhodes is in our class. Smart I'd say, good grades and very punctual.")
                show(rand(("Used to help me a lot when Arthur sometimes ditched me.","Great friend, used to help me when sometimes Arthur didn't.")))
            elif xx("tom"):
                show("Tom Green is not in our class. He is my senior. Wasn't a friend of Arthur though. We first met online, and didn't even know we were from the same University. Tom is a fun guy, very funny. I like him a lot.")
            elif xx("sid") or xx("meyer"):
                show("Sid Meyer? That guy is a character. Last in class. Doesn't really study at all, is a good friend of Arthur, I don't know how. Sid is rich, yes and has quite a few connections. By connections I mean, he knows people, people at positions. Probably the reason he still is here at this Institute.")
            elif xx("you"):
                show("I think you know that pretty well. I'm certainly not the killer or the culprit.")
            else:
                show("I don't know who you're talking about sir.")
        elif xx("you"):
            if xx("arthur") or cc(s,killer):
                if xx("hate") or xx("fight"):
                    show("I never hated Arthur. Though he was rude to me sometimes, I always respected him. I just wish he returns back. Wherever he is, I hope he comes back. Back to us. Please find him.")
                elif xx("kill") or cc(s,killer):
                    mood+= -1
                    show(rand(("For god's sake, believe me, I did not kill or do anything with Arthur.","Why would I kill or do anything with Arthur, he was my only friend.","No, I didn't kill or do anything with Arthur. I can't even think of doing something of that sort.")))
            elif xx("like") or xx("hate"):
                if xx("amy"):
                    if xx("hate") or xx("don't") or xx("not") or xx("didn't"):
                        show("You ask why?  @@@@@@$$$$$$$$%%%%%%%%*&A long embarrassing incident took place. All because of her. That is why")
                    else:
                        show("She's an okay girl. What do you mean like? She was rude with me the most of times I met her. So I think I shouldn't like her and evidently I don't.")
            elif xx("know") and xx("about"):
                if xx("amy"):
                    show(rand(("Honestly, Arthur did talk about Amy sometimes. He would say how happy he was, with everything in his favour. I mean they both were really close friends.")))
            elif xx("innocent"):
                show("Yes I am innocent.")
        elif xx("arthur"):
            if xx("feeling") or xx("sick"):
                show("He had had a cold for the past seven days. I'd advised him to go see the nurse but strangely he never agreed. He was mumbling something about the Red Basement.")
        #for answers not in memory
    else:
        if inp!="":
            show("I don't think if that is an important question, fact or statement.")

o = True
while o==True:
    print("\nYOU: ",end="")
    inp = input()
    print("")
    inp = inp.lower()
    peter(inp)