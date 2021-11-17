class Address:
    addresses=[]

    def __init__(self,city_name,ave_name,number,postal_code):
        self.city_name=city_name
        self.ave_name=ave_name
        self.number=number
        self.postal_code=postal_code
        self.address=''

    def display(self):
        self.address=f"city:{self.city_name}avenue:{self.ave_name}pelak:{self.number}postal_code:{self.postal_code}"
        return self.address

    def edit_address(self,option_name,option_value):
        if option_name=='city_name':
            self.city_name=option_value
        elif option_name=='ave_name':
            self.ave_name=option_value
        elif option_name=='plak_number':
            self.number=option_value
        elif option_name=='postal_code':
            self.postal_code=option_value

    def edit_info(self, **kwargs):
        self.__dict__.update((k, v) for k, v in kwargs.items())
        return self



    @staticmethod
    def generate_id(*args):
        args=list(args)
        new_args=[str(i).lower() for i in args]
        unique_id=','.join(new_args)
        return unique_id
    @classmethod
    def add_address(cls,city_name,ave_name,plak_number,postal_code):
        address=Address.generate_id(city_name,ave_name,plak_number,postal_code)
        if address in cls.addresses:
            print("you can not add this address cause this address exists in the list!")
        else:
            cls.addresses.append(address)
            return cls(city_name,ave_name,plak_number,postal_code)

class Person:
    persons=[]
    def __init__(self,f_name,l_name,email_address,p_code,phone_number):
        self.f_name=f_name
        self.l_name=l_name
        self.email_address=email_address
        self.p_code=p_code
        self.phone_number=phone_number
    @staticmethod
    def email_validation(email):
        email_address=str(email)
        if '@' in email_address:
            text=email_address[-4:]
            if text=='.com':
                return True
            else:
                return False
        else:
            return False

    def p_code_validation(self):
        if len(self.p_code)==10:
            return True
        else:
            return False

    def person_edit(self,option_name,option_value):
        if option_name=='first_name':
            self.f_name=option_value
        elif option_name=='last_name':
            self.l_name=option_value
        elif option_name=='email_address':
            self.email_address=option_value
        elif option_name == 'p_code':
            self.p_code = option_value
        elif option_name == 'phone_number':
            self.phone_number = option_value

    @classmethod
    def add_person(cls,first_name,last_name):
        email_address=input('please enter email address:')
        if Person.email_validation(email_address)==False:
            email_address=input("entered email address was not valid please enter the correct email address:")
        p_code=input("please enter your national code:")
        phone_number=input("please enter your phone number:")
        name=Address.generate_id(first_name,last_name)
        if name in cls.persons:
            print("you can not add this nme to the persons list!")
        else:
            cls.persons.append(name)
            return cls(first_name,last_name,email_address,p_code,phone_number)


    def __str__(self):
        return f"first name is:{self.f_name} and last name is:{self.l_name}"

class Apartment:
    apartments=[]
    def __init__(self,owner,tenant,number_of_rooms,metragh,floor,number_of_floors,address,phone_number,
                 active,amount_of_bond,amount_of_rent,amount_of_sell,selable,rentable,parking):
        self.owner_namelist=str(owner).split(' ')
        self.owner= Person.add_person(self.owner_namelist[0],self.owner_namelist[1])
        if selable==1:
            self.tenant='null'
            self.selable='its for sale'
            self.rentable=''
        elif rentable==1:
            self.rentable='its for rent'
            self.selable=''
            self.tenant_namelist=str(tenant).split('')
            self.tenant=Person.add_person(self.tenant_namelist[0],self.tenant_namelist[1])
        self.number_of_rooms=number_of_rooms
        self.metragh =metragh
        self.floor =floor
        self.number_of_floors=number_of_floors
        self.address_list=str(address).split(',')
        city_name=self.address_list[0]
        ave_name=self.address_list[1]
        plak_number=self.address_list[2]
        postal_code=self.address_list[3]
        self.address=Address.add_address(city_name,ave_name,plak_number,postal_code)
        self.phone_number =phone_number
        self.amount_of_bond =amount_of_bond
        self.amount_of_rent =amount_of_rent
        self.amount_of_sell = amount_of_sell
        self.parking =parking
        if active==1:
            self.active='active'
        else:
            self.active='deactive'

    def apartment_edit(self,option_name,option_value):
        if option_name=='owner':
            self.owner=option_value
        elif option_name=='tenant':
            self.tenant=option_value
        elif option_name=='number_of_rooms':
            self.number_of_rooms=option_value
        elif option_name=='address':
            self.address=option_value
        elif option_name=='metragh':
            self.metragh=option_value
        elif option_name=='floor':
            self.floor=option_value
        elif option_name=='number of floors':
            self.number_of_floors=option_value
        elif option_name=='phone number':
            self.phone_number=option_value
        elif option_name=='active':
            self.active=option_value
        elif option_name=='amount of bond':
            self.amount_of_bond=option_value
        elif option_name=='amount of rent':
            self.amount_of_rent=option_value

    @classmethod
    def add_apartment(cls,owner,tenant,metragh,address,selable,rentable,amount_of_bond,amount_of_rent,amount_of_sell,number_of_rooms,
    floor,number_of_floors,phone_number,active,parking):
        apartment= Address.generate_id(owner,tenant,metragh,address)
        if apartment in cls.apartments:
            print("you can not add this name to apartment list!")
        else:
            cls.apartments.append(apartment)
            return cls(owner=owner,tenant=tenant,metragh=metragh,address=address,selable=selable,
            rentable=rentable,amount_of_bond=amount_of_bond,amount_of_rent=amount_of_rent,
            amount_of_sell=amount_of_sell,number_of_rooms=number_of_rooms,floor=floor,number_of_floors=number_of_floors,
            phone_number=phone_number,active=active,parking=parking)

    def __str__(self):
        return f"the owner is:{self.owner} the tenant is:{self.tenant} number of rooms:{self.number_of_rooms}" \
               f"and the metragh is:{self.metragh}the apartment is on the{self.floor}and it has{self.number_of_floors} floors" \
               f"the address is:{self.address} and the phone number is:{self.phone_number} this house is{self.active}" \
               f"amount of bond is:{self.amount_of_bond} and amount of rent is:{self.amount_of_rent} amount of sell is:{self.amount_of_sell}" \
               f"{self.selable}{self.rentable}and it has{self.parking} parkings."


class House(Apartment):
    def __init__(self,owner,tenant,number_of_rooms,metragh,floor,number_of_floors,address,phone_number,
                 active,amount_of_bond,amount_of_rent,amount_of_sell,selable,rentable,parking,yard_metragh):
        self.yard_metragh=yard_metragh
        Apartment.__init__(self,owner,tenant,number_of_rooms,metragh,floor,number_of_floors,address,phone_number,
                 active,amount_of_bond,amount_of_rent,amount_of_sell,selable,rentable,parking)


class Store(Apartment):
    def __init__(self,owner,tenant,number_of_rooms,metragh,floor,number_of_floors,address,phone_number,
                 active,amount_of_bond,amount_of_rent,amount_of_sell,selable,rentable,parking):
        Apartment.__init__(self,owner,tenant,number_of_rooms,metragh,floor,number_of_floors,address,phone_number,
                 active,amount_of_bond,amount_of_rent,amount_of_sell,selable,rentable,parking)

class EstateCounselor:
    def __init__(self):
        self.search_results=[]
    def search_estate(self,option,option_value):
        if option=='metragh':
            for item in Apartment.apartments:
                if item.metragh==option_value:
                    self.search_results.append(item)
            if self.search_results==[]:
                print('there is no results.')
            else:
                print(self.search_results)
        if option=='rentable':
            for item in Apartment.apartments:
                if item.rentable==option_value:
                    self.search_results.append(item)
            if self.search_results==[]:
                print('there is no results.')
            else:
                print(self.search_results)
        if option=='selable':
            for item in Apartment.apartments:
                if item.selable==option_value:
                    self.search_results.append(item)
            if self.search_results==[]:
                print('there is no results.')
            else:
                print(self.search_results)
        if option=='amount_of_bond':
            for item in Apartment.apartments:
                if item.amount_of_bond==option_value:
                    self.search_results.append(item)
            if self.search_results==[]:
                print('there is no results.')
            else:
                print(self.search_results)
        if option=='amount_of_rent':
            for item in Apartment.apartments:
                if item.amount_of_rent==option_value:
                    self.search_results.append(item)
            if self.search_results==[]:
                print('there is no results.')
            else:
                print(self.search_results)
        if option=='amount_of_sell':
            for item in Apartment.apartments:
                if item. amount_of_sell==option_value:
                    self.search_results.append(item)
            if self.search_results==[]:
                print('there is no results.')
            else:
                print(self.search_results)


class Bargain:
    def __init__(self,buyer,owner,bargain_expiration,contract_date):
        buyer_first_name,buyer_last_name=str(buyer).split()
        self.buyer = Person.add_person(buyer_first_name, buyer_last_name)
        owner_first_name,owner_last_name = str(owner).split()
        self.owner =Person.add_person(owner_first_name,owner_last_name)
        self.bargain_expiration=str(bargain_expiration)
        self.contract_date=str(contract_date)

    def rent(self,estate):
        if estate.tenant=='null':
            print("this estate is not for rent")
        else:
            estate.active='deactive'
            estate.apartment_edit('tenant',self.buyer)

    def sell(self,estate):
        if estate.tenant!='null':
            print("this estate is not for sell")
        else:
            estate.active='deactive'
            estate.apartment_edit('owner',self.buyer)

    def __str__(self):
        return f"in this contract the former owners name is {self.owner} and the buyers name is {self.buyer} "



    




         




                  
                 
         
             
         
             
            
         





        












