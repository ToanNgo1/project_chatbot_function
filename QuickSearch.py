#quick search for twitch
'''def google_search(user_input,category):             #the main search core is from geekforgeek, however the handle of data and it types are my code.
    try:                                #this use to check to make sure you have install google packet 
        from googlesearch import search
    except ImportError: 
        print("No module named 'google' found")   
    # to search
    #print(user_input)
    out_list=[]
    user_input=user_input.strip()
    category=category.strip()
    #conver_input=input("category: ")
    if (category=='') :
        category="General question" 
    combine=category+": "+user_input
    #print(combine)
    #langue=input("please enter the language en or es ").lower().strip()                    this modtify the language of the search 
    #print(langue)
    query = combine
    
    for j in search(query, tld="co.in",lang='en', num=2 , stop=3, pause=2.5):               #if i where to change the speed too fast google will block this !
        out_list.append(j)
    return out_list

tracker=input("search: ")
tracker2=input("category: ")
respond=google_search(tracker,tracker2)
print(respond)'''
def google_sc(user_input):  
    #input_user=input("please enter the thing to search: ")
    try:                                #this use to check to make sure you have install google packet 
        from googlesearch import search
    except ImportError: 
        print("No module named 'google' found")   
    # to search
    print(user_input)
    return_list=[]
    user_input=user_input.strip()
    #category=category.strip()
    #conver_input=input("category: ")
    #if (category=='') :
    #    category="General question" 
    combine=user_input
    print(combine)
    #langue=input("please enter the language en or es ").lower().strip()
    #conver=""+join(input_user.split())
    #print(langue)
    query = combine
    
    #context=input("enter a context of the question if need:")
    #quextion=input("please enter the question here ? ")
    for j in search(query, tld="co.in",lang='es', num=4 ,start=4, stop=4, pause=3):
        print(f' this is a content search check: {j}')
        return_list.append(j)
    return return_list

if __name__=="__main__":
    input_track=input("enter something")
    respond=google_sc(input_track)
    print(respond)
