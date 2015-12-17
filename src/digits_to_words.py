# -*- coding: utf-8 -*-t


# Number_TO_Words() function :
#                           
#                           Consists of Word_Set a dictionary that has set of
#                           <digit,word> key-value pairs for mapping digits 
#                           with equivalent words
#
#       1. Invokes DigitPlace() for extracting individual digits
#       2. Invokes Word_Conversion() to convert digits to words
#       Finally prints the output as a string

def Number_To_Words(num):
    Word_Set = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
             6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', \
            11: 'Eeleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', \
            19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', \
            50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', \
            90: 'ninety', 0:'' }
    if num == 0:
        #print "zero"
        return "zero"
    if num >= 1000000: 
        return ""
    digitval_list = DigitPlace(num)
    Number_in_words=Word_Conversion(digitval_list,Word_Set)
    #print Number_in_words
    return Number_in_words


#
#
#
#
#
def tens_to_word(words, ones, tens = 0): 
    if tens == 0:
        return words[ones]
    if tens == 1:
        temp = tens*10+ones
        return words[temp]
    else: 
        tens = tens*10
        return words[tens]+" "+words[ones]



# Word_Conversion() function :
#                             Converts the digits into words. Basically map
#                             the digit to words in the dictionary object
#                            <digilist> -> contains list of digits(units,tens,
#                             upto 1 lakhs) 
#                            words -> represents the Word_Set{} dictionary

def Word_Conversion(digilist,words):
    wstr=''                     #wstr->word string that holds the digit's word
    count=0                     #count->to keep track of the digit place value
    
    for item in digilist:
       #Check for Unit place 
        if count==0 :
            if item==0 :
                if digilist[count+1]!=0 :
                    count +=1
                    temp=10+item  #temp->to represent 10,11,....19 
                    continue
            if len(digilist)>1 and digilist[count+1]==1 :
                count+=1
                temp=10+item
                continue
            else:
                wstr=words[item]
                
        #Check for the tenth's place        
        if count==1 :
            if item==1 :
                wstr=words[temp]+" "+wstr
            else :
                w=10*item        #w->to represent 20,30,40,....90
                wstr=words[w]+" "+wstr.lower()
        
        #If a 4 digit number, spell as 2-digit and 2-digit 
        if len(digilist) == 4 and digilist[2] != 0: 
            #working on the upper orders
            tens = digilist[3]
            ones = digilist[2]            
            wstr_upper_order = tens_to_word(words, ones, tens)             
            
            #working on the lower orders
            tens = digilist[1]
            ones = digilist[0]
            if ones == 0 and tens == 0: 
                wstr = wstr_upper_order + " hundred"                
            elif tens == 0:     
                wstr = wstr_upper_order +" o "+words[ones]
            else:     
                wstr = wstr_upper_order + " "+tens_to_word(words, ones, tens)
                #wstr = wstr_upper_order+" "+wstr
            return wstr   
        
        #Check for the hundredth place
        if count==2 :
            if item==0 :
                if digilist[count+1]!=0 :
                    count +=1
                    continue
            elif len(digilist)>3 and digilist[count+1]!=0 :
                wstr=words[item]+" "+"hundred"+" "+wstr.lower()
                count+=1
                continue
            else:
                wstr=words[item]+" "+"hundred"+" "+wstr.lower()
        #Check for the thousand place 
        if count==3 :
            if item==0 :
                if digilist[count+1]!=0 :
                    count +=1
                    temp=10+item
                    continue
            if len(digilist)>4 and digilist[count+1]!=0 :
                wstr=words[item]+" "+"thousand"+" "+wstr.lower()
                count+=1
                continue
            else:
                wstr=words[item]+" "+"thousand"+" "+wstr.lower()
        
        #Check for the Ten thousands place        
        if count==4 :
            if item==1 :
                #wstr=words[temp]+" "+"thousand"+" "+wstr.lower()
                wstr=words[item]+" "+"thousand"+" "+wstr.lower()
            else:
                w=10*item
                wstr=words[w]+" "+wstr.lower()
                
        #Check for the one lakh place
        if count==5 :
            if item==0 :
               if digilist[count+1]!=0 :
                    count +=1
                    temp=10+item
                    continue
            else:
                wstr=words[item]+" "+"hundred"+" "+wstr.lower()
                
        #Check for the ten lakh place
        if count==6 :
            if item==1 :
                wstr=words[temp]+" " +"hundred"+" "+wstr.lower()
        count+=1

    return wstr


# DigitPlace() function :
#                        Produces the unit,tenth,hundred upto 1lakh places
#                        digits
#       1. Find the remainder and store it in list object
#       2. Return the list object finally

def DigitPlace(number):
    dlist=[]
    while(number>0):
        rem=number%10
        dlist.append(rem)
        number//=10
    return dlist
