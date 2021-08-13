from selenium import webdriver
import time
import os
from selenium.webdriver.support import expected_conditions as EC







'''
functions

////////////////////////////////////////////////////////////////////////////////


 def find_buttons(self, button_text):
        """
        Finds buttons for following and unfollowing users by filtering follow elements for buttons. Defaults to finding follow buttons.
        Args:
            button_text: Text that the desired button(s) has 
        """

        buttons = self.driver.find_elements_by_xpath("//*[text()='{}']".format(button_text))

        return buttons




////////////////////////////////////////////////////////////////////////////////
'''

class covidPassBot: 

    def __init__(self,username= None,password = None):
        self.username =username
        self.password =password

        # self.driver = webdriver.Chrome('S:\Python\Selenium\chromedriver.exe')
        self.driver = webdriver.Chrome('./chromedriver')
        
       # self.driver.maximize_window()


    def login(self,outside_Or_Inside_Maharashtra = 'inside',passenger_count_1__4_or_2__more = None):

        self.driver.get("https://covid19.mhpolice.in/registration")

        submit_butn =self.driver.find_element_by_id("modal_sumbit")


        time.sleep(2)

        if outside_Or_Inside_Maharashtra.lower() == "inside":
            self.driver.find_element_by_id("is_interstate_no").click()
            submit_butn.click()
            
            

        elif (outside_Or_Inside_Maharashtra.lower() == 'outside'):
            self.driver.find_element_by_id("is_interstate_yes").click()

            time.sleep(1)
            self.driver.find_element_by_id("number_of_people").click()

            

            if (passenger_count_1__4_or_2__more == 1 ):
                #butn1 = self.driver.find_elements_by_xpath("//*[text()='{}']".format('0 to 4 / ५ पेक्षा कमी प्रवास'))
                butn1 = self.driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/div[1]/div[4]/div/h5/select/option[2]')
                butn1[0].click()
                time.sleep(1.5)
                submit_butn.click()

            elif (passenger_count_1__4_or_2__more == 2):
                butn2 =self.driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/div[1]/div[4]/div/h5/select/option[3]')
                butn2[0].click()
                time.sleep(1.5)
                submit_butn.click()


    def formFillUp(self,User_Details,state = None):

        # 1. District 
        self.driver.find_elements_by_xpath('//*[@id="district"]')[0].click()
        # District >> Nagpur (jaripatka)
        time.sleep(0.5)
        self.driver.find_elements_by_xpath('/html/body/div[1]/div[1]/div/div/div/form/div[1]/div/div[1]/div/div[1]/select/option[21]')[0].click()

        #2. Name 
        Name = self.driver.find_elements_by_xpath('//*[@id="name"]')[0]

        Name.send_keys(User_Details["name"])
        
        # 3. Mobile 
        Mobile = self.driver.find_elements_by_xpath('//*[@id="mobile_number"]')[0]

        Mobile.send_keys(User_Details["mobile"])

        #4. Purpose

        purpose = self.driver.find_element_by_xpath('//*[@id="purpose"]')
        
        purpose.send_keys(User_Details["purpose"])

        #5. Vehicle number

        veh_num = self.driver.find_element_by_xpath('//*[@id="vehicle_number"]')

        veh_num.send_keys(User_Details["vehicle_number"])

        #6. Current Address

        cur_Adrss = self.driver.find_element_by_xpath('//*[@id="address"]')

        cur_Adrss.send_keys(User_Details["current_address"])

         #7. Destination Address

        #des_Adrss = self.driver.find_element_by_xpath()

        #des_Adrss.send_keys(User_Details["destination_address"])

        #8. Passenger Count

        passenger_Count = self.driver.find_element_by_xpath('//*[@id="no_co_passenger"]')

        passenger_Count.send_keys(User_Details["passenger_count"])


        #9. Email Id

        Email_ID = self.driver.find_element_by_xpath('//*[@id="email_id"]')

        Email_ID.send_keys(User_Details["email_ID"])


        #10. Travel Type

        travel_type = self.driver.find_element_by_xpath('//*[@id="essential_service_type"]')

        travel_type.click()
        time.sleep(0.5)

        if(state == 'outside'):
            self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/form/div[1]/div/div[2]/div/div[2]/select/option[6]')[0].click()

        elif(state == 'inside'):
            self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/form/div[1]/div/div[2]/div/div[2]/select/option[7]')[0].click()


       

       
        #11. Passenger Names

        self.driver.find_element_by_xpath('//*[@id="co_passenger_names"]').send_keys(User_Details["passenger_names"])

        #12. Vehicle Type

        self.driver.find_element_by_xpath('//*[@id="vehicle_type"]').click()

        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/form/div[1]/div/div[3]/div/div[1]/select/option[5]').click()


        #13. Are you in containment zone

        self.driver.find_element_by_xpath('//*[@id="is_home_quarantine"]').click()

        # NO

        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/form/div[1]/div/div[5]/div/div[2]/select/option[2]').click()









if __name__ == '__main__':

    state =None
    how_many_passengers = None

    usrDetails = { 'Nagpur' : "/html/body/div[1]/div[1]/div/div/div/form/div[1]/div/div[1]/div/div[1]/select/option[21]", "name":"Thakurdas Sachdev","current_address" : "Mukund Society jaripatka" ,"destination_address" : "Raipur" ,"mobile":9922922131,"purpose" :"Agricultural Visit", 'vehicle_number': 'MH 49 BB 0076',"passenger_count": 4,"email_ID" : "sandeshsachdev27@gmail.com","passenger_names" : "Sandesh Sachdev " }

    web = covidPassBot()

    web.login('outside',1)
    web.formFillUp(usrDetails,state)

'''
Where_to_travel = int(input("Where to Travel : Inside or Outside Maharashtra \n1.Inside\n2.Outside\n"))
if Where_to_travel == 1 :
    state = "inside"
else :
    state = "outside"



if state.lower() == 'outside' :
    how_many_passengers = int(input("\n\n1.Less than or Equal to 4\n2.More than 4\n\n"))


    
web.login(state,how_many_passengers)
'''
    