'''
<Made by Owino-Mike Version 1.0.0/>

I͓̽ M͓̽ P͓̽ O͓̽ R͓̽ T͓̽ A͓̽ N͓̽ T͓̽   N͓̽ O͓̽ T͓̽ E͓̽ :

THIS IS JUST THE 1.0.0 VERSION!
SO IT MAY HAVE SOME BUGS OR IT MAY NOT TRANSLATE EVERYTHING HOW IT SHOULD TO BE RIGHT!
IF I MISSED SOMETHING, PLEASE SUGGEST IT IN THE COMMENTS. Thank you very much!

WHAT THIS CODE DOES:
You can just put your name or any word in (please only one word each to prevent fails) and this code will try to give you the japanese pronunciation of it.

'''
inp=input()
name=inp.lower()

double_letter = ("aa","bb","cc","dd","ee","ff","gg","hh","ii","jj","kk","ll","mm","nn","oo","pp","qq","rr","ss","tt","uu","vv","ww","xx","yy","zz")
consonant = ("b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z")
abc = ("a","b","c","d","e","f","g","h","j","i","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
exc=("wi","vi","ph","ds","uc","l","ck","v","sch","ing","ny","ä","ü","ö","q","j","c","tz","gh","th")
ins=("bi","bi","f","ts","us","r", "k", "w","sh","in","nu","e","u","o","k","y","k","z","h","s")
        
for i in double_letter:
   if i in name:
        name=name.replace(i,i[0])

end_exc = ("er","de","ke")
end_ins = ("a","d","k")
end_u_exc = ("h","n")
for i in range (len(end_exc)):
    if name.endswith(end_exc[i]):
        name=name.replace(end_exc[i],end_ins[i])
    
for i in range(len(exc)):
    if exc[i] in name:
        name=name.replace(exc[i], ins[i])   

def getPos(combination):
    pos=(name.index(combination))+1
    return pos
  
def y_combo_tester(y_combo,name):  
    if y_combo in name:
        pos=getPos(y_combo)
        try:
            y_combo_test=name[pos]+name[pos+1]
        except:
            y_combo_test=y_combo
        return y_combo_test

combination_exc = ("nb","sh","nd","nt","np","ts","ya","yu","yo")
    
    
def y_combination():
    global name
    for i in abc:
        y_combo = i+"y"
        y_combo2 = "y"+i 
        if y_combo_tester(y_combo,name) not in combination_exc:
            while y_combo in name:
                pos=getPos(y_combo)
                name=name[:pos]+"i"+name[(pos+1):]
        
        elif y_combo2 not in combination_exc:
            while y_combo2 in name:
                pos=getPos(y_combo)
                name=name[:(pos)-1]+"i"+name[pos:]             
               
y_combination()
    
def inserter(combination_1):
    global name
    for i in consonant:
        combination = i+consonant[combination_1 ]
        if combination not in combination_exc:
            while combination in name:
                if combination.endswith("h"):
                    pos=getPos(combination)
                    name=name[:pos]+name[(pos+1):]
                elif combination.startswith("h"):
                    pos=getPos(combination)
                    name=name[:(pos-1)]+name[pos:]
                else:
                    pos=getPos(combination)
                    name=name[:pos]+"u"+name[pos:]
                    
def combination_maker():
    for combination_1 in range(0,(len(consonant ))):
        inserter(combination_1)
                    
for i in range(0,2):
    combination_maker()
    
if name.endswith(consonant):
    if not name.endswith(end_u_exc):
        name=name+"u"


print('''
-----------------------------------
THANK YOU FOR:
- \"CODE OF THE DAY\"
- \"TOP 10 MOST POPULAR CODES ON SOLOLEARN\"!
-----------------------------------

Your original name/word:''',inp,'''
Japanese pronunciation of it:''',name,'''

-----------------------------------

And if you liked my code,
don't forget to give it a (+1) like :D

BTW: It would be awesome if all of you could post the word which you put in and the pronunciation the code gave back!

This way we can improve this code faster!
Thanks a lot for your help!

-----------------------------------

Made by Owino'''
)