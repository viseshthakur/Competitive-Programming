def BaseConverter(s):
    d={}
    for i in range(len(s)):
        d[i]=s[i]
    return d
short_url_length = 7
short_url_dict={}
full_url_dict={}
count=0
base62=BaseConverter("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
def genShortURL(fullURL):
    if (fullURL in full_url_dict):
        print("ShortURL already Exists"+full_url_dict[fullURL])
        return
    global count
    s=""
    k=count
    count+=1
    if (k==0):
        s="0000000"
        if (s not in short_url_dict):
            short_url_dict[s]=fullURL
            full_url_dict[fullURL]=s
            print("short url for "+fullURL+" is https://ca.ke/"+s)
            return
    while(k!=0):
        s=base62[k%62]+s
        k=k//62
    l=len(s)
    if (l<short_url_length):
        for i in range(short_url_length-l):
            s="0"+s
    if (s not in short_url_dict):
        short_url_dict[s]=fullURL
        full_url_dict[fullURL]=s
    print("short url for "+fullURL+" is https://ca.ke/"+s)

while (True):
    print("Enter \n\t1) generate ShortURL\n\t2)redirect ShortURL")
    userInput=int(input())
    if (userInput==""):
        fullURL=input("Enter an URL to shorten it : ")
        genShortURL(fullURL)
    elif (userInput==2):
        shortURL=input("Enter a short url: ")
        if short_url_dict.get(shortURL,None) is not None:
            print("redirecting to "+short_url_dict[shortURL])
        else:
            print("Doesn't exist")
    else:
        print("Invalid Input")