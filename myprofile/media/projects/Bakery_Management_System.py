import pandas as pd
import random as rd
import datetime
date=datetime.datetime.now().date()
class Bakery:
    global item
    def __init__(self,token, cake_orderd,cake_name, price,name,email,date,total_cakes,a,b,c,d,e,f):
        self.token_number=token
        self.email=email
        self.name=name
        self.cake_orderd=cake_orderd
        self.cake_name=cake_name
        self.price=price
        self.date=date
        self.total_cakes=total_cakes
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.e=e 
        self.f=f

    def product(self):
        return self.cake_name,self.price
    def ID(self):
        return self.name,self.email

    def already_token(self):
        swap_tk=self.token_number
        swap_email=swap_tk

        if token_ID==swap_email:
            print(f'You order for {self.cake_name} with Price {self.price}.')
        else:
            print("Not valid Token number")




    def token_generate():
        letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'Z']
        index1 = rd.randint(0, 5)
        index2 = rd.randint(6, 11)
        rnd = rd.randint(100 * 3, 100 ** 6)
        t1 = letter[index1]
        t2 = letter[index2]
        token_number = t1 + t2 + str(rnd)
        return token_number

    def save_data(self):
        data = {'Date': self.date, 'ID': self.token_number, 'Username': self.name, 'email': self.email, "Total price": self.price,'Total Cakes':self.total_cakes,'Chocolate cake':self.a,'Angel cake':self.b,'Banana cake':self.c,"Butter cake":self.d,"Coconut cake":self.e,"Genoise":self.f}
        df = pd.DataFrame([data])
        df.to_csv("C:\\Bakery\\Bakery.csv", mode='a', index=False,header=False)
    def ThankYou(self):
        main_token=self.token_number
        wish=f"Good day {self.name}. You Orderd Cake Price {self.price}.\nThanks For Visiting.\nVed Bakery."
        print(f'You got your token id {main_token}')
        print(wish)
        
        





    def stars():
        for i in range(2):
            i -= 1
            print('    *' * 10)
            if (i % 2 == 0):
                print('    *' * i)
    def start():
        print('\nA :- Chocolate cake\n',
              '\nB :-Angel cake \n',
              '\nC :-Banana cake \n',
              '\nD :-Butter cake \n',
              '\nE :-Coconut cake \n',
              '\nF :-Genoise \n',
              )



Bakery.stars()
print('\t-:Welcome To Ved bakery and Cake center:-\t')
Bakery.stars()

Bakery.start()



cakes = {
    'A': 'Chocolate cake',
    'B': 'Angel cake',
    'C': 'Banana cake',
    'D': 'Butter cake',
    'E': 'Coconut cake',
    'F': 'Genoise',
}

price = {
    'A': 600,
    'B': 230,
    'C': 400,
    'D': 550,
    'E': 120,
    'F': 150,
}
order=''
users=20

while(users>=1):

    users-=1
    tkn=input("Already have Token, press '0'. else '1' ")
    username=''
    cake_orderd=[]
    price_,a,b,c,d,e,f = 0,0,0,0,0,0,0



    if tkn=='0':
        token_ID=input("Enter token ID: ")
        print("Work in construction")

    elif(tkn=='1'):
        username=input("name: ")
        email=input("E-mail: ")
        
        num_of_cake=int(input("How many cake do you want ? "))
        for i in range(num_of_cake):
            order = input("Which Cakes     Note:-(Use Alphabets) ").lower()
            if order == 'a' or 'chocolate' in order:
                price_ += 600
                cake_orderd.append(cakes['A'])
                a+=1

                
            elif order == 'b' or 'angel' in order:
                price_ += 230
                cake_orderd.append(cakes['B'])
                b+=1

            elif order == 'c' or 'banana' in order:
                price_ += 400
                cake_orderd.append(cakes['C'])
                c+=1

            elif order == 'd' or 'butter' in order:
                price_ += 550
                cake_orderd.append(cakes['D'])
                d+=1

            elif order == 'e' or 'coconut' in order:
                price_ += 120
                cake_orderd.append(cakes['E'])
                e+=1
            elif order == 'f' or 'genoise'  in order:
                price_ += 150
                cake_orderd.append(cakes['F'])
                f+=1

            else:
                price_ += 0
            print(f'Your order price is {price_}')
        bakery=Bakery(cake_name=cakes,price=price_,name=username,email=email,token=Bakery.token_generate(),date=date,total_cakes=num_of_cake,a=a,b=b,c=c,d=d,e=e,f=f,cake_orderd=cake_orderd)
        bakery.ThankYou()
        bakery.save_data()
    else:
        print('Give valid Option.')

