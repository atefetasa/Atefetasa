import csv

class Address:
    def __init__(self,city_name,ave_name,number,postal_code):
        address_l=[city_name,ave_name,str(number),str(postal_code)]
        self.city_name=city_name
        self.ave_name=ave_name
        self.number=str(number)
        self.postal_code=str(postal_code)
        self.address=','.join(address_l)

    def edit_info(self, **kwargs):
        self.__dict__.update((k, v) for k, v in kwargs.items())
        return self

    def __str__(self):
        return self.address


class Person:
    def __init__(self,f_name,l_name,email_address,p_code,phone_number):
        self.f_name=f_name
        self.l_name=l_name
        self.email_address=str(email_address)
        self.p_code=str(p_code)
        self.phone_number=str(phone_number)

    @staticmethod
    def email_validation(email):
        email_address=str(email)
        try:
            if '@' in email_address:
                text=email_address[-4:]
                if text=='.com':
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            print(e)
    @staticmethod
    def p_code_validation(p_code):
        if len(str(p_code))==10:
            return True
        else:
            return False

    def edit_person_info(self,**kwargs):
        try:
            if 'email_address' in list(kwargs.keys()):
                while True:
                   if Person.email_validation(kwargs['email_address'])==True:
                       if 'p_code' in list(kwargs.keys()):
                           while True:
                               if Person.p_code_validation(kwargs['p_code'])==True:
                                   self.__dict__.update((k, v) for k, v in kwargs.items())
                                   break
                               else:
                                   kwargs['p_code']=input("please enter a new national code:")
                                   raise ValueError('you have entered an invalid national code.')
                       else:
                           self.__dict__.update((k, v) for k, v in kwargs.items())
                           break
                   else:
                       kwargs['email_address']=input("please enter another new email address:")
                       raise ValueError('you have entered an invalid email address.')
            elif 'p_code' in list(kwargs.keys()):
                while True:
                    if Person.p_code_validation(kwargs['p_code']) == True:
                        self.__dict__.update((k, v) for k, v in kwargs.items())
                        break
                    else:
                        kwargs['p_code'] = input("please enter a new national code:")
                        raise ValueError('you have entered an invalid national code.')
            else:
                self.__dict__.update((k, v) for k, v in kwargs.items())
            return self
        except ValueError as e:
            print(e)
        except Exception as ex:
            print(ex)

    def __str__(self):
        return f"first name is:{self.f_name} and last name is:{self.l_name}"

class Apartment:
    selable_estates_line_counter=0
    rentable_estates_line_counter = 0
    apartments_list=[]

    def __init__(self,owner,tenant,number_of_rooms,metragh,floor,number_of_floors,address,phone_number,
                 active,amount_of_bond,amount_of_rent,amount_of_sell,selable,rentable,parking):
        owner_first_name,owner_last_name=str(owner).split()
        self.owner=Person(owner_first_name,owner_last_name,' ',' ',' ')
        if selable==1:
            self.tenant='null'
            self.selable='its for sale'
            self.rentable=''
        elif rentable==1:
            self.rentable='its for rent'
            self.selable=''
            tenant_first_name,tenant_last_name=str(tenant).split()
            self.tenant=Person(tenant_first_name,tenant_last_name,' ',' ',' ')
        self.number_of_rooms=str(number_of_rooms)
        self.metragh =str(metragh)
        self.floor =str(floor)
        self.number_of_floors=str(number_of_floors)
        city_name,ave_name,plak_number,postal_code=str(address).split(',')
        self.address=Address(city_name,ave_name,plak_number,postal_code)
        self.phone_number =str(phone_number)
        self.amount_of_bond =str(amount_of_bond)
        self.amount_of_rent =str(amount_of_rent)
        self.amount_of_sell =str(amount_of_sell)
        self.parking =str(parking)
        if active==1:
            self.active='active'
        else:
            self.active='deactive'

    def edit_apartment_info(self,**kwargs):
        try:
            if 'owner' in list(kwargs.keys()):
                owner_first_name,owner_last_name=str(kwargs['owner']).split()
                email_address=input("please enter owners email address:")
                p_code= input("please enter owners national code:")
                phone_number= input("please enter owners phone number:")
                new_owner=Person(owner_first_name,owner_last_name,email_address,p_code,phone_number)
                kwargs['owner']=new_owner
            if 'tenant' in list(kwargs.keys()):
                tenant_first_name, tenant_last_name = str(kwargs['tenant']).split()
                email_address = input("please enter tenants email address:")
                p_code = input("please enter tenants national code:")
                phone_number = input("please enter tenants phone number:")
                new_tenant = Person(tenant_first_name, tenant_last_name, email_address, p_code, phone_number)
                kwargs['tenant'] = new_tenant
            if 'address' in list(kwargs.keys()):
                city_name,ave_name,number,postal_code=str(kwargs['address']).split(',')
                new_address=Address(city_name,ave_name,number,postal_code)
                kwargs['address'] = new_address
            self.__dict__.update((k, v) for k, v in kwargs.items())
        except Exception as e:
            print(e)
        else:
            return self

    @classmethod
    def make_apartment_object(cls,owner, tenant, metragh, address, selable, rentable, amount_of_bond,
                   amount_of_rent, amount_of_sell, number_of_rooms,
                   floor, number_of_floors, phone_number, active, parking):
        return cls(owner=owner,tenant=tenant,metragh=metragh,address=address,selable=selable,rentable=rentable,
                   amount_of_bond=amount_of_bond,amount_of_rent=amount_of_rent,amount_of_sell=amount_of_sell,
                   number_of_rooms=number_of_rooms,floor=floor,number_of_floors=number_of_floors,phone_number=phone_number,
                   active=active,parking=parking)

    @staticmethod
    def add_estate(store, house, apartment, owner, tenant, metragh, address, selable, rentable, amount_of_bond,
                   amount_of_rent, amount_of_sell, number_of_rooms,
                   floor, number_of_floors, phone_number, active, parking, yard_metragh=None):
        if apartment==1:
            Apartment.apartments_list.append(Apartment.make_apartment_object(owner, tenant, metragh, address, selable, rentable, amount_of_bond,
                   amount_of_rent, amount_of_sell, number_of_rooms,
                   floor, number_of_floors, phone_number, active, parking))
        elif house==1:
            House.houses_list.append(House.make_house_object(owner, tenant, metragh, address, selable, rentable, amount_of_bond,
                   amount_of_rent, amount_of_sell, number_of_rooms,
                   floor, number_of_floors, phone_number, active, parking,yard_metragh))
        elif store==1:
            Store.stores_list.append(Store.make_store_object(owner, tenant, metragh, address, selable, rentable, amount_of_bond,
                   amount_of_rent, amount_of_sell, number_of_rooms,
                   floor, number_of_floors, phone_number, active, parking))
        if selable==1:
            with open('SelableEstates.csv',mode='a') as csv_file:
                fieldnames=['store','house','apartment','owner','matragh','address',
                            'amount_of_sell','number_of_rooms','floor','number_of_floors',
                            'phone_number','active','parking','yard_metragh']
                item = {'store': store, 'house': house, 'apartment': apartment,
                        'owner':owner,'matragh':metragh, 'address':address,
                        'amount_of_sell':amount_of_sell,'number_of_rooms':number_of_rooms,
                       'floor':floor, 'number_of_floors':number_of_floors,
                       'phone_number':phone_number, 'active':active, 'parking': parking, 'yard_metragh':yard_metragh}
                writer=csv.DictWriter(csv_file,fieldnames=fieldnames)
                if Apartment.selable_estates_line_counter==0:
                    writer.writeheader()
                    writer.writerow(item)
                    Apartment.selable_estates_line_counter=Apartment.selable_estates_line_counter+1
                else:
                    writer.writerow(item)
                    Apartment.selable_estates_line_counter = Apartment.selable_estates_line_counter + 1
        elif rentable==1:
            with open('RentableEstates.csv',mode='a') as csvfile:
                fieldnames=['store','house','apartment','owner','tenant','metragh','address','selable','rentable','amount_of_bond',
                   'amount_of_rent','amount_of_sell','number_of_rooms',
                   'floor','number_of_floors','phone_number','active','parking','yard_metragh']
                item={'store':store,'house':house,'apartment':apartment,'owner':owner,'tenant':tenant,'metragh':metragh,'address':address,
                    'amount_of_bond':amount_of_bond,
                   'amount_of_rent':amount_of_rent,'number_of_rooms':number_of_rooms,
                   'floor':floor,'number_of_floors':number_of_floors,'phone_number':phone_number,'active':active,'parking':parking,'yard_metragh':yard_metragh}
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                if Apartment.rentable_estates_line_counter == 0:
                    writer.writeheader()
                    writer.writerow(item)
                    Apartment.rentable_estates_line_counter = Apartment.rentable_estates_line_counter + 1
                else:
                    writer.writerow(item)
                    Apartment.rentable_estates_line_counter = Apartment.rentable_estates_line_counter + 1

    def __str__(self):
        return f"the owner is:{self.owner} the tenant is:{self.tenant} number of rooms:{self.number_of_rooms}" \
               f"and the metragh is:{self.metragh}the apartment is on the{self.floor}and it has{self.number_of_floors} floors" \
               f"the address is:{self.address} and the phone number is:{self.phone_number} this house is{self.active}" \
               f"amount of bond is:{self.amount_of_bond} and amount of rent is:{self.amount_of_rent} amount of sell is:{self.amount_of_sell}" \
               f"{self.selable}{self.rentable}and it has{self.parking} parkings."


class House(Apartment):
    houses_list=[]
    def __init__(self,owner,tenant,number_of_rooms,metragh,floor,number_of_floors,address,phone_number,
                 active,amount_of_bond,amount_of_rent,amount_of_sell,selable,rentable,parking,yard_metragh):
        self.yard_metragh=yard_metragh
        Apartment.__init__(self,owner,tenant,number_of_rooms,metragh,floor,number_of_floors,address,phone_number,
                 active,amount_of_bond,amount_of_rent,amount_of_sell,selable,rentable,parking)

    @classmethod
    def make_house_object(cls, owner, tenant, metragh, address, selable, rentable, amount_of_bond,
                           amount_of_rent, amount_of_sell, number_of_rooms,
                           floor, number_of_floors, phone_number, active, parking,yard_metragh):
        return cls(owner=owner, tenant=tenant, metragh=metragh, address=address, selable=selable, rentable=rentable,
                   amount_of_bond=amount_of_bond, amount_of_rent=amount_of_rent, amount_of_sell=amount_of_sell,
                   number_of_rooms=number_of_rooms, floor=floor, number_of_floors=number_of_floors,
                   phone_number=phone_number,
                   active=active, parking=parking,yard_metragh=yard_metragh)


class Store(Apartment):
    stores_list=[]
    def __init__(self,owner,tenant,number_of_rooms,metragh,floor,number_of_floors,address,phone_number,
                 active,amount_of_bond,amount_of_rent,amount_of_sell,selable,rentable,parking):
        Apartment.__init__(self,owner,tenant,number_of_rooms,metragh,floor,number_of_floors,address,phone_number,
                 active,amount_of_bond,amount_of_rent,amount_of_sell,selable,rentable,parking)

    @classmethod
    def make_store_object(cls, owner, tenant, metragh, address, selable, rentable, amount_of_bond,
                           amount_of_rent, amount_of_sell, number_of_rooms,
                           floor, number_of_floors, phone_number, active, parking):
        return cls(owner=owner, tenant=tenant, metragh=metragh, address=address, selable=selable, rentable=rentable,
                   amount_of_bond=amount_of_bond, amount_of_rent=amount_of_rent, amount_of_sell=amount_of_sell,
                   number_of_rooms=number_of_rooms, floor=floor, number_of_floors=number_of_floors,
                   phone_number=phone_number,
                   active=active, parking=parking)


class EstateCounselor:
    def __init__(self):
        self.search_results=[]

    def search_estate(self,**kwargs):
        if kwargs['rentable']==1:
            try:
                with open('RentableEstates.csv','r') as csv_file:
                    csv_reader=csv.DictReader(csv_file)
                    for row in csv_reader:
                        row=dict(row)
                        if row['metragh']==kwargs['metragh'] and row['amount_of_rent']==kwargs['amount_of_rent'] and row['amount_of_bond']==kwargs['amount_of_bond']:
                            self.search_results.append(row)
                if self.search_results==[]:
                    raise ValueError("there is no results for your search.")
            except ValueError as e:
                print(e)
            except Exception as ex:
                print(ex)
        if kwargs['selable']==1:
            try:
                with open('SelableEstates.csv','r') as csv_file:
                    csv_reader=csv.DictReader(csv_file)
                    for row in csv_reader:
                        row=dict(row)
                        if row['metragh']==kwargs['metragh'] and row['amount_of_sell']==kwargs['amount_of_sell']:
                            self.search_results.append(row)
                if self.search_results==[]:
                    raise ValueError("there is no results for your search.")
            except ValueError as e:
                print(e)
            except Exception as ex:
                print(ex)

    def __str__(self):
        return self.search_results


class Bargain:
    def __init__(self,buyer,owner,bargain_expiration,contract_date,its_for_sell=1):
        buyer_first_name,buyer_last_name=str(buyer).split()
        owner_first_name,owner_last_name=str(owner).split()
        try:
            if its_for_sell==1:
                buyer_email=input("please enter the buyers email address:")
                buyer_p_code = input("please enter the buyers national code:")
                buyer_phone_number = input("please enter the buyers phone number:")
                self.buyer=Person(buyer_first_name,buyer_last_name,buyer_email,buyer_p_code,buyer_phone_number )
                self.tenant='null'
            elif its_for_sell==0:
                tenant_email = input("please enter the tenants email address:")
                tenant_p_code = input("please enter the tenants national code:")
                tenant_phone_number = input("please enter the tenants phone number:")
                self.tenant = Person(buyer_first_name,buyer_last_name,tenant_email,tenant_p_code,tenant_phone_number)
                self.buyer='null'
            owner_email = input("please enter the owners email address:")
            owner_p_code= input("please enter the owners national code:")
            owner_phone_number = input("please enter the owners phone number:")
            self.owner = Person(owner_first_name,owner_last_name,owner_email,owner_p_code,owner_phone_number)
            self.bargain_expiration=bargain_expiration
            self.contract_date=contract_date
        except TypeError as e:
            print(e)
        except Exception as ex:
            print(ex)

    def rent(self):
        try:
            if self.tenant=='null':
                raise ValueError("this contract is a selling contract not renting!")
            else:
                id=input("enter the estate id you want to rent to the customer:")
                counter=0
                with open('RentableEstates.csv','r') as csvfile:
                    csv_reader=csv.DictReader(csvfile)
                    for row in csv_reader:
                        row=dict(row)
                        counter+=1
                        if counter==id:
                            if row['apartment']==1:
                                for object in Apartment.apartments_list:
                                    if object.phone_number==row['phone_number']:
                                        object.active='deactive'
                                        object.tenant=self.tenant
                with open('RentableEstates.csv','w') as csvfile:
                    fieldnames=['store','house','apartment','owner','tenant','metragh','address','selable','rentable','amount_of_bond',
                   'amount_of_rent','amount_of_sell','number_of_rooms',
                   'floor','number_of_floors','phone_number','active','parking','yard_metragh']
                    csv_writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
                    csv_writer.writeheader()
                    for object in Apartment.apartments_list:
                        if object.rentable==1:
                            item={'store':0,'house':0,'apartment':1,'owner':owner,'tenant':object.tenant,'metragh':object.metragh,'address':object.address,
                                         'amount_of_bond':object.amount_of_bond,
                                         'amount_of_rent':object.amount_of_rent,'number_of_rooms':object.number_of_rooms,
                                         'floor':object.floor,'number_of_floors':object.number_of_floors,'phone_number':object.phone_number,'active':object.active,'parking':object.parking,'yard_metragh':object.yard_metragh}
                            csv_writer.writerow(item)
                    for object in House.houses_list:
                        if object.rentable == 1:
                            item = {'store': 0, 'house': 1, 'apartment': 0, 'owner': owner, 'tenant': object.tenant,
                                    'metragh': object.metragh, 'address': object.address,
                                    'amount_of_bond': object.amount_of_bond,
                                    'amount_of_rent': object.amount_of_rent, 'number_of_rooms': object.number_of_rooms,
                                    'floor': object.floor, 'number_of_floors': object.number_of_floors,
                                    'phone_number': object.phone_number, 'active': object.active, 'parking': object.parking,
                                    'yard_metragh': object.yard_metragh}
                            csv_writer.writerow(item)
                    for object in Store.stores_list:
                        if object.rentable == 1:
                            item = {'store': 1, 'house': 0, 'apartment': 0, 'owner': owner, 'tenant': object.tenant,
                                    'metragh': object.metragh, 'address': object.address,
                                    'amount_of_bond': object.amount_of_bond,
                                    'amount_of_rent': object.amount_of_rent, 'number_of_rooms': object.number_of_rooms,
                                    'floor': object.floor, 'number_of_floors': object.number_of_floors,
                                    'phone_number': object.phone_number, 'active': object.active, 'parking': object.parking,
                                    'yard_metragh': object.yard_metragh}
                            csv_writer.writerow(item)

        except Exception as ex:
            print(ex)
        with open('bargain.csv','a') as file:
            fieldnames=['buyer','owner','tenant','bargain_expiration','contract_date']
            writer=csv.DictWriter(file,fieldnames=fieldnames)
            writer.writeheader()
            item={'buyer':self.buyer,'owner':self.owner,'tenant':self.tenant,'bargain_expiration':self.bargain_expiration,
                  'contract_date':self.contract_date }
            writer.writerow(item)


















    




         




                  
                 
         
             
         
             
            
         





        












