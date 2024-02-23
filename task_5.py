

def func(search_queries):
    i=0;
    h=[]
    rez=[]
    while i<len(search_queries):
     
            b=search_queries[i].split()    
            h.append(len(b))
            i += 1
    i=0;

    Len_h=len(h)
    perc = 100/len(search_queries)
    

    while i<len(h):
        
        
      
        g=str(h[i]) +(' слово ' if h[i]<2 else (' слов ' if 5<h[i] else ' слова ')) + str(round(h.count(h[i])*perc,2)) + ' %'
       
        if rez.count(g)==0:
            rez.append(g)
            print(g)
        
        i += 1
    


func(['watch new movies', 'coffee near me', 'how to find the determinant', 'python', 'data science jobs in UK', 'courses for data science', 'taxi', 'google', 'yandex', 'bing','foreign exchange rates USD/BYN', 'Netflix movies watch online free',  'Statistics courses online from top universities'])



