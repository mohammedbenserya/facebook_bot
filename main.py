from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
import tkinter as tk
import threading
import random






def stop():
    global running
    running = False
    tk.Button(root, text="Continue",  command=cont ,height = 2, width = 13).place(x=350, y=300)

def start():
    global running
    running = True
    

def cont():
    global running
    running = True
    tk.Button(root, text="Stop",  command=stop ,height = 2, width = 13).place(x=350, y=300)

def interface():
    
    def ok():
            start()
            uname = e1.get()
            password = e2.get()
            group = grp.get()
            message = text_area.get("1.0", tk.END)

            if(uname != "" and password != "") :
                t1 = threading.Thread(target=facebook, args=(uname,password,group,message))
                t1.start()

            else :
                
                messagebox.showinfo("", "Blank Not allowed")

    global root
    root = tk.Tk()
    root.title("Login")
    root.geometry("700x400")
    global e1,e2,grp,text_area

    
    Label(root, text="Email").place(x=10, y=10)
    Label(root, text="Password").place(x=10, y=40)
    Label(root, text="Groupe").place(x=10, y=70)
    Label(root, text="Message").place(x=10, y=100)


    e1 = Entry(root,width=50)
    e1.place(x=200, y=10)

    e2 = Entry(root,width=50)
    e2.place(x=200, y=40)
    e2.config(show="*")

    grp = Entry(root,width=50)
    grp.place(x=200,y=70)

    text_area = scrolledtext.ScrolledText(root, 
                                      wrap = tk.WORD, 
                                      width = 38, 
                                      height = 10, )
  
    #text_area.grid(column = 0, pady = 10, padx = 10)

    text_area.place(x=200,y=100)


    btn = tk.Button(root, text="Start",height = 2, width = 13,command=ok)
    btn.place(x=200, y=300)
    tk.Button(root, text="Stop",  command=stop ,height = 2, width = 13).place(x=350, y=300)


        



    root.mainloop()



#https://web.facebook.com/ u_0_j_b3
def facebook(email,password,group,MESSAGE):

    driver = webdriver.Chrome()
    driver.get("https://web.facebook.com/")
    try:
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div/div[3]/button[2]"))).click()
        
    except Exception as e :
        print(e)
        pass
    email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email"))).send_keys(email)
    password = driver.find_element(By.ID,"pass").send_keys(password)
    btn = driver.find_element(By.XPATH,'//button[@data-testid="royal_login_button"]')
    ActionChains(driver).click(btn).perform()

    time.sleep(10)
    if "?" in group:
        group=group.split("/?")[0]
    driver.get(f"{group}/members")
    time.sleep(5)
    """try:
        numbre = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/div/div/div/div/div/div[2]/span/div/div[3]")

        numbre=numbre.text.split(' ')[0]
        numbre=int(numbre.replace(" ",""))
        print("old")
    except :
        #/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div/div/div/div[1]/div/div[2]/span/div/div[3]
        numbre = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div[1]/h2/span/span/span/strong")
        numbre=numbre.text.split('· ')[1]

        numbre=int(numbre.replace(" ",""))

    print((numbre))"""
    links=[]
    i=0
    count = 1
    while True:
        
        if running:

            
            
            
            try:
                # #//*[@id="mount_0_0_ps"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[4]/div/div/div/div/div/div/div/div/div/div/div[2]/div[16]/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div/div/div[1]/span/span/span/a
                element_to_hover_over = driver.find_elements(By.XPATH,'//span[@class="nc684nl6"]/a[@role="link"]')
                link=(element_to_hover_over[i].get_attribute("href"))
                if "user" in link == False :
                    i+=1

                    continue
                
                if link in links:
                        i+=1

                        continue
                print(link)
                links.append(link)

            except :
                ele =driver.find_element(By.TAG_NAME,'body')
                ele.send_keys(Keys.END)
                time.sleep(3)
                continue
            #/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[21]/div/div[2]/div/div[17]/div/div/div[2]/div[1]/div/div/div[1]/span/span/span/div
            
            #/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[21]/div/div[2]/div/div[149]/div/div/div[2]/div[1]/div/div/div[1]/span/span/span/a

            #/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[21]/div/div[2]/div/div[206]/div/div/div[2]/div[1]/div/div/div[1]/span/span/span/a
            try:

                hover = ActionChains(driver).move_to_element(element_to_hover_over[i])
                count +=1
                hover.perform()
                time.sleep(1)
                xpath = '//div[@class="k4urcfbm"]/div[@aria-label="Message"]'
                msg = driver.find_element(By.XPATH,(xpath))
                if (msg.get_attribute('aria-label') )!="Message":
                    raise 
                ActionChains(driver).click(msg).perform()
                #/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div[2]/div[4]/div[2]/div/div/div[1]
                #MESSAGE = MESSAGE.replace("\n", (Keys.SHIFT + Keys.ENTER))
                ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div[2]/div[4]/div[2]/div/div/div")))
                #/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div[2]/div[4]/div[2]/div/div/div
                #elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div[1]/div[2]/div/div/div/div/div/div[2]/div/div[2]/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div/div/div/div/div/span/span")))
                for part in MESSAGE.split('\n'):
                    ele.send_keys((Keys.SHIFT + Keys.ENTER))
                    ele.send_keys(part)
                #driver.execute_script(JS_ADD_TEXT_TO_INPUT, elem, u''+MESSAGE)
                    #ActionChains(driver).click(elem).perform()

                ele.send_keys(Keys.ENTER)
                xpath = '/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/span[4]/div'
                close = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,(xpath))))
                ActionChains(driver).click(close).perform()
                i+=1
                time.sleep(random.randint(2, 15))
            except Exception as e :
                print(e)
                i+=1
                continue

            """if count == numbre:
                break"""
            #/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div/div/div/div[1]/div/div
            #/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div/div/div/div[1]/div/div
            #//*[@id="mount_0_0_/Y"]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]

            
            #/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div

            #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div"))).send_keys("0608056292")

            #/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div/div[3]/span[4]/div
            #//*[@id="mount_0_0_/Y"]/div/div[1]/div/div[5]/div/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div/div[3]/span[4]/div
            #/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/form/div/div[3]/span[2]/div
        
        #https://web.facebook.com/groups/meme.ki9tal
if __name__ == '__main__':
    interface()