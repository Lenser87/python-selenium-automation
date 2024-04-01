#1. Logo element search by Xpath:
driver.find_element(By XPATH, "//i[@class='a-icon a-icon-logo']")

#2. Email field search by ID:
driver.find_element(By ID, 'ap_email')

#3. Continue button search by Xpath:
driver.find_element(By XPATH, "//input[@id='continue']")

#4. Conditions of use link search by Xpath:
driver.find_element(By XPATH, "//a[contains(@href, 'ignin_notification_condition_of_use?ie=UTF8&nodeId=508088')]")

#5. Privacy Notice link search by Xpath:
driver.find_element(By XPATH, "//a[contains(@href, 'ref=ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496')]")

#6. Need help link search by Xpath:
driver.find_element(By XPATH, "//span[@class='a-expander-prompt']")

#7. Forgot your password link and Other issues with Sign-In link
# do not exist for current page, but there are other links

#8. Buying for work? string search by Xpath:
driver.find_element(By XPATH, "//span[@class='a-text-bold']")

#9. Create your Amazon account button by ID:
driver.find_element(By ID, 'createAccountSubmit')