class library:
    
    def __init__(self):
        self.no_book=[]
        self.name_book=[]
        self.id=None


    def add_book(self,book,ch_id):
        self.ch_id=ch_id
        self.name_book.append(book)
        self.no_book.append(book)
        
        
    @staticmethod
    def id_check(ch_id):
        if ch_id==1111:
            return True
        return False

    def show(self):
        if library.id_check(self.ch_id):
         x=len(self.no_book)
         print(f'THe name of books {self.name_book}')
         
         print(f'num of boks ={x}')
        else:
            print('id dint matched ')
        

my_obj=library()
while True: 
 
 book=input('Enter the name of book')
 if book=='exit':
    break
 id_address=int(input('enter the id address'))
 my_obj.add_book(book,id_address)
 my_obj.show()
 
 
 
 


 
#self ka andar jo ban raha ah wo objects attributes hain aur jo class method spproach karta ha  ma ban rahay hain ya class ma ban rahay hai  wo class ka attributreshain



        
