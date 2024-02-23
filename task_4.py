class Node:   
    def __init__(self,data):   
        self.data = data;   
        self.previous = None;   
        self.next = None;   
           
class Item_list:   
    def __init__(self):   
        self.head = None;   
        self.tail = None;   
        
    def push(self, data):  # записывает значение в конец списка
        newEndNode = Node(data);
        
        if(self.head == None):   
            self.head = self.tail = newEndNode;   
            self.head.previous = None;   
            self.tail.next = None;   
        else:   
            self.tail.next = newEndNode;   
            newEndNode.previous = self.tail;   
            self.tail = newEndNode;   
            self.tail.next = None;   
            
    def unshift(self, data): # записывает значение в начало списка
        newBegNode = Node(data);
        
        if(self.head == None):   
            self.head = self.tail = newBegNode;   
            self.head.previous = None;   
            self.tail.next = None;   
        else:   
            self.head.previous = newBegNode;
            newBegNode.next = self.head;  
            newBegNode.previous = None;   
            self.head = newBegNode;
            
            
        
    def pop(self): # удаляет значение с конца списка
        
        print("Удаление последнего");
        self.tail=self.tail.previous;
        self.tail.next = None;
       
    def shift(self): # удаляет значение с начала списка
        print("Удаление первого");
         
        self.head=self.head.next;
        self.head.previous = None;    
        
    
      
            

    
  
    
My_List = Item_list();   

My_List.push(5); 
My_List.push(6); 
My_List.push(7); 

 
My_List.unshift(55); 

My_List.pop(); 


 

My_List.shift(); 
