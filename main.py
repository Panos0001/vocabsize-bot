
from ast import While
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time 

#---------------------------------------
#-----------Caesar Cipher---------------
#---------------------------------------
lc = [
  'a', 'b', 'c', 'd', 'e', 'f',
  'g', 'h', 'i', 'j', 'k', 'l',
  'm', 'n', 'o', 'p', 'q', 'r',
  's', 't', 'u', 'v', 'w', 'x',
  'y', 'z'
]
uc = [
  'A', 'B', 'C', 'D', 'E', 'F',
  'G', 'H', 'I', 'J', 'K', 'L',
  'M', 'N', 'O', 'P', 'Q', 'R',
  'S', 'T', 'U', 'V', 'W', 'X',
  'Y', 'Z'
]

alphabet = 'abcdefghijklmnopqrstuvwxyz'
def decode(s, n):
    n = int(n)
    n = n % 26
    word = ''

    for character in s:
        character = character.lower()
        if character not in alphabet:
            word += character
        else:
            lcEncryptIndex = (lc.index(character.lower()) - n) % 26
            word += lc[(lc.index(character.lower()) - n) % 26]
    return word

#__________________________________________________________________________________________________________________________________________

lscy = []
cy = "/html/body/div[2]/div[3]/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[3]/div/div[1]/span[1]"

lshint = []
hint = "/html/body/div[2]/div[3]/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[3]/div/div[1]/span[2]"

lstext = []
text = "/html/body/div[2]/div[3]/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[4]/div/div[1]/div[1]/input"

driver = webdriver.Chrome(r"C:\Users\???\?????\chromedriver.exe")
website = driver.get(r"https://vocabsize.xeersoft.co.th/") 

# Change this to your username and password
Username = ''
Passowrd = ''

#Login Page
driver.find_element(By.ID,"txt_email").send_keys(Username)
driver.find_element(By.ID,"txt_password").send_keys(Passowrd)
driver.find_element(By.ID,"btn_submit").send_keys(Keys.RETURN)

# Wait's for page to load to click on the image
while True:

    try:
        driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div[1]/div/div/div/a/img")
        break

    except NoSuchElementException:
        print("Element does not exist 1")
        time.sleep(0.5)

# Home Page
driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div[1]/div/div/div/a/img").click()

while True:

    # Wait for skip btn
    #In human wait to assign work
    while True:

        try:
            driver.find_element(By.XPATH,"/html/body/div[2]/div[7]/div/div/div/div[1]/button")
            break

        except NoSuchElementException:
            print("Element does not exist 2")
            time.sleep(0.5)

    # Assinged wrok 

    # Skip btn
    driver.find_element(By.XPATH,"/html/body/div[2]/div[7]/div/div/div/div[1]/button").click()

    # Start btn
    driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div/div/div/div[4]/div/button").click()

    NumWords = int(input("Enter amount of words that are in the vocabe size: "))

    for i in range(1, NumWords + 1):

        lscy = []
        lshint = []
        lstext = []

        vocab_word1 = []
        vocab_word2 = []

        for char in cy:
        
            lscy.append(char)

        for char in hint:

            lshint.append(char)

        for char in text:

            lstext.append(char)

        lscy[89] = str(i)
        lshint[89] = str(i)
        lstext[89] = str(i)
        lscy = "".join(lscy)
        lshint = "".join(lshint)
        lstext = "".join(lstext)

        # Find the Cyhered text
        # /html/body/div[2]/div[3]/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[3]/div/div[1]/span[1]
        # /html/body/div[2]/div[3]/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/table/tbody/tr[2]/td[3]/div/div[1]/span[1]
        # /html/body/div[2]/div[3]/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/table/tbody/tr[3]/td[3]/div/div[1]/span[1]

        # Hint Text                                                                                           Diff in span num
        # /html/body/div[2]/div[3]/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[3]/div/div[1]/span[2]
        # /html/body/div[2]/div[3]/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/table/tbody/tr[2]/td[3]/div/div[1]/span[2]
        # /html/body/div[2]/div[3]/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/table/tbody/tr[3]/td[3]/div/div[1]/span[2]

        # Logic on how to get location of the text box
        # /html/body/div[2]/div[3]/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[4]/div/div[1]/div[1]/input
        # /html/body/div[2]/div[3]/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/table/tbody/tr[2]/td[4]/div/div[1]/div[1]/input
        # /html/body/div[2]/div[3]/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/table/tbody/tr[3]/td[4]/div/div[1]/div[1]/input



        # print(driver.find_element(By.XPATH,lscy).get_attribute("vocab_word1"))
        # print(driver.find_element(By.XPATH,lshint).get_attribute("vocab_word2"))


        # Change to vaeiuble bc its too long
        vocab_word1_attribute = driver.find_element(By.XPATH,lscy).get_attribute("vocab_word1")
        vocab_word2_attribute = driver.find_element(By.XPATH,lshint).get_attribute("vocab_word2")

        # Put in list bc easy to use 
        vocab_word1.append(vocab_word1_attribute)
        vocab_word2.append(vocab_word2_attribute)

        print(vocab_word1)
        print(vocab_word2)

        cypher_ascii = ord(vocab_word1[0][0])
        hint_ascii = ord(vocab_word2[0][0])

        key_cypher_ascii = cypher_ascii - hint_ascii

        testing = cypher_ascii - key_cypher_ascii

        print()

        print(key_cypher_ascii)

        def listToString(s): 

            str1 = "" 

            for ele in s: 
                str1 += ele  
        
            return str1 
        
        s = vocab_word1
        # print(listToString(s)) 


        
        #---------------------------------------
        #-----------Caesar Cipher---------------
        #---------------------------------------

        String = listToString(s)
        key = key_cypher_ascii

        answer = decode(String , key)

        driver.find_element(By.XPATH,lstext).send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
        driver.find_element(By.XPATH,lstext).send_keys(answer)

    driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[2]/div/div/div[2]/div[2]/div/div[1]/span").click()

    while True:

        try:
            driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[1]/div/div[1]/div/a").click()
            break

        except NoSuchElementException:
            print("Back btn testin")
            time.sleep(0.5)

    

    
#/html/body/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[3]/input
#/html/body/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/table/tbody/tr[2]/td[3]/input
#/html/body/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/table/tbody/tr[3]/td[3]/input








    
    


