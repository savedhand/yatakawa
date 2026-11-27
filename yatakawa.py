import numpy
import math
import sys
import random
d=input("Code: ")
numbers=[]
i = 0
while i < len(d):
    if d[i] == "A":
        if i+1 >= len(d) or not ('0' <= d[i+1] <= '9'):
	        print(f"Huh? : invalid number length at char {i}")
        else:
            length = int(d[i+1])
            number = int(d[i+2:i+2+length],36)
            i += length + 2
            numbers.append(number)
    elif '0' <= d[i] <= '9':
        numbers.append(int(d[i]))
        i += 1
    elif d[i] == ",":
    	if not numbers:
    		print(f"Huh? : char {i} says to print nothing")
    	else:
    		print(numbers[-1])
    	i+=1
    elif d[i] == '"':
    	start=i+1
    	qe=start
    	i+=1
    	while i < len(d) and d[i] != '"':
    		i+=1
    		
    	if i>=len(d):
    		print(f"Huh? : unclosed quotation marks, opening quotation mark position : {qe}")
    		break
    	string=d[start:i]
    	numbers.append(string)
    	i+=1
    elif d[i]=="ô":
    	numbers.append("")
    	i+=1
    elif d[i]=="q":
    	numbers.append(numpy.pi)
    	i+=1
    elif d[i]=="w":
    	numbers.append(numpy.e)
    	i+=1
    elif d[i]=="e":
    	numbers.append(numpy.pi * 2)
    	i+=1
    elif d[i]=="¶":
    	print(numbers)
    	i+=1
    elif d[i]=="%":
    	if not numbers:
    		print(f"Huh? : char {i} says to print nothing")
    	else:
    		print(numbers[-1],end="")
    	i+=1
    elif d[i]=="?":
    	numbers.append(input())
    	i+=1
    elif d[i]=="ż":
        numbers.append("bcdfghjklmnpqrstvwxyz")
        i+=1
    elif d[i]=="Ż":
        numbers.append("aeiou")
        i+=1
    elif d[i]=="Ź":
        numbers.append("1234567890")
        i+=1
    elif d[i]=="ź":
        numbers.append("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        i+=1
    elif d[i]=="Ž":
        numbers.append("abcdefghijklmnopqrstuvwxyzėêëēèęéōøœõòôöóäæãåāąáàâśßšłżźžçćčñń")
        i+=1
    elif d[i]=="ž":
        numbers.append("abcdefghijklmnopqrstuvwxyz")
        i+=1
    elif d[i]=="ण":
        if not numbers:
            print("Huh? : char {i} says to edit nothing")
        elif not isinstance(numbers[-1], str):
            print("Huh? : using a str command on a non-str variable? pathetic")
        else:
            numbers.append(numbers[-1][::-1])
        i+=1
    elif d[i]=="Л":
        numbers.append(len(numbers[-1]))
        i+=1
    elif d[i]==":":
        numbers.append("Hello, world!")
        i+=1
    elif d[i]=="#":
        numbers.append(True)
        i+=1
    elif d[i]==">":
        numbers.append(False)
        i+=1
    elif d[i]=="C":
        if i+1<len(d):
            if d[i+1]!="[":
                print(f"Huh? : ok I'm getting tired of typing these errors. {i} {d[i]} check it yourself, unopened [")
            elif d[i+2]=="]":
                print("Huh? : ununderstandable ] spawned in a [ command")
            else:
                parsen=d[i:]
                if "]" not in parsen:
                    print("Huh? : unclosed [")
                else:
                    parsenerofparsen=parsen[2:parsen.find("]")]
                    try:
                        parsenererofparsenerofparsentheking=int(parsenerofparsen)
                    except ValueError:
                        print("Huh? : you added a letter somewhere, or it isn't a int value, yeah the code can't decide literally but the compiler memory changing is multi-digit, don't add A anywhere")
                    else:
                        try:
                            numbers.append(numbers[parsenererofparsenerofparsentheking])
                        except IndexError:
                            print("Huh? : error, out of range the index")
                            
            i+=parsen.find("]")+1
        else:
            print("Huh? : debug the code, C is obviously for memory-indexing")
            i+=1
    elif d[i]=="N":
        if not numbers:
            print("The CM is empty!")
        else :
            n=numbers[-1]
            if not isinstance(n, (int, float)):
                print("Negatating a non-numbers? just use ण if you wanna reverse a string")
                break
            n=n*(-1)
            numbers.pop()
            numbers.append(n)
        i+=1
    elif d[i] == "©":
        if CM:
            s = str(CM[-1])
            if s:
                CM.append(s[-1])
        i += 1
    
    elif d[i] == "®":
        if CM:
            s = str(CM[-1])
            if s:
                CM.append(s[0])
        i += 1
    elif d[i] == "^":
        end = d.find("^", i + 1)
    
        if end == -1:
            i = len(d)
        else:
            i = end + 1
    elif d[i]=="ę":
        if numbers:
            numbers.append(numbers[0])
        i+=1
    elif d[i]=="Ę":
        if numbers:
            numbers.append(numbers[-1])
        i+=1
    elif d[i] == "!":
        if not numbers:
            pass
        elif isinstance(numbers[-1], int):
            if numbers[-1] < 0:
                numbers.append(None)
            else:
                numbers.append(math.factorial(numbers[-1]))
        i+=1
    elif d[i]=="q":
        sys.exit()
    elif d[i]=="℅":
        if type(numbers[-1]) in (int, float) and type(numbers[-2]) in (int, float):
            if numbers[-2]>numbers[-1]:
                numbers.append(True)
            else:
                numbers.append(False)
        else:
            print("℅ Is for comparison of ints!")
        i+=1
    elif d[i]=="٪":
        if type(numbers[-1]) in (int, float) and type(numbers[-2]) in (int, float):
            if numbers[-2]<numbers[-1]:
                numbers.append(True)
            else:
                numbers.append(False)
        else:
            print("٪ Is for comparison of ints!")
        i+=1
    elif d[i]=="¢":
        numbers.append(str(numbers[-1]))
        i+=1
    elif d[i]=="$":
        try:
            numbers.append(int(numbers.pop()))
        except ValueError:
            print("Huh? : non-number on a int-ify command")
        i+=1
    elif d[i] == "¥":
        numbers.append(random.randint(0, 100))
    elif d[i]=="€":
        if type(numbers[-1]) == int and type(numbers[-2]) == int:
            x=numbers[-2]
            y=numbers[-1]
            numbers.append("".join(chr(i) for i in range(x, y + 1)))
        else:
            print(" Hih? : cannot range up from a non-int or a float")
        i+=1
    else:
    	print(f"Huh? : char {i+1} is not a valid command")
    	i+=1
