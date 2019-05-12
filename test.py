from selenium import webdriver

# You need to download the google chrome driver https://sites.google.com/a/chromium.org/chromedriver/
# Provide a path to the google chrome webdriver, thats the path you downloaded it to
driver = webdriver.Chrome("/Users/ephraimkgwele/Desktop/pytest/chromedriver")

# The URL your script must visit
driver.get("https://www.instagram.com/")

# click the login with facebook button
fb_login_btn = driver.find_element_by_class_name("sqdOP")
fb_login_btn.click()

# Find the email and password fields
email_input = driver.find_element_by_id("email")
pass_input = driver.find_element_by_id("pass")
cnt_submit = driver.find_element_by_id("loginbutton")

# Fill in your login details to login
# For the script to be able to login you need to supply your login details
email_input.send_keys("YOUR FACEBOOK EMAIL HERE")
pass_input.send_keys("YOUR FACEBOOK PASSWORD HERE")

# Submit login form
cnt_submit.click()

# Wait for page to load everything
driver.implicitly_wait(10)

# Click not now on the instagram pop up
notNow = driver.find_element_by_class_name("HoLwm")
notNow.click()

# Find the search box
search_input = driver.find_element_by_class_name("x3qfX")

# Enter my name in the search box
search_input.send_keys("ephraim kgwele")

# Wait for search results to load
driver.implicitly_wait(10)

# Follow link to my profile
link = driver.find_element_by_xpath("//div[@class='fuqBx']/a[@href='/if_rhymes/']")
link.click()

# Click the follow button on my profile
follow_btn = driver.find_element_by_xpath('//button[text()="Follow Back"]')
follow_btn.click()

# Open first post
post_1 = driver.find_element_by_xpath("//a[@href='/p/BupNhJ9g494/']")
post_1.click()

# Find and Save all posts to a list

all_posts = driver.find_elements_by_class_name("v1Nh3")

# Loop though all the posts
for single_post in all_posts:

    # Wait for the post to load
    driver.implicitly_wait(10)

    # Like the post
    like_post = driver.find_element_by_xpath("//span[@class='fr66n']")
    like_post.click()

    driver.implicitly_wait(10)

    # Go to next post
    next_post = driver.find_element_by_class_name("coreSpriteRightPaginationArrow")
    next_post.click()

