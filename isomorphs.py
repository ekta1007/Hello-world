# Algorithm :
#1. We will 1st use a  global mapping of chars from one string to another - to optimze only the keys in the string1 are used
#2. Post this is the comparision & mapping from string 2 & storing in dict keys

#define if two words are isomorphs of each other
def isomorphs(string1, string2):
    dict_maps={}
    list_chars=map(chr, range(97, 123))
    flag=0
    #j=0
    """ #initizlizing complete dict
    for j in list_chars:
        dict_maps[j]='0' # this dict will contain mapping of chars from staring 1 to string 2
    """
    for j in string1 : 
        dict_maps[j]='0' # have intitialized the dict keys
    j=0
    if len(string1)==len(string2) :
        for i in string2 :
            if j < len(string1) : #and len(string1)==len(string2) :
                if dict_maps[string1[j]]=='0' and i not in set(dict_maps.values()): # 2nd condition checks if mapping of this value has already occured for another key
                    dict_maps[string1[j]]=i
                elif dict_maps[string1[j]]==i :# a one time mapping has already happened and the char was same
                    pass
                else : # everything else just points that there's a mapping that already exists
                    flag=1
                    message= "Strings are not isomorphs of each other  "
                    break
            j=j+1
    elif len(string1) is not len(string2):
           flag =1
           message= "mapping not possible - strings are of unequal length - Dictionary map is not initialized" 
    if flag ==0:
        message = "strings are isomorphs of each other"
    return dict_maps, message

#string1, string2= 'foodiig', 'appijkl'
string1, string2= 'foodf', 'appik'
dict_maps, message =isomorphs(string1, string2)
print " string 1 %s , string2 %s \n " %(string1, string2)
print dict_maps, '\n \n ', message 
    
