# Testing
The testing approach(described in detail in this testing readme) is as follows:
1. Automated unit testing using the Django unit test framework
2. Manual testing using emulators and real devices

## Unit testing information
- I wrote a number of unit tests(INSERT NUMBER HERE) using the Django unit test framework
- These test cases are structured in a number of suites(INSERT NUMBERE HERE)
- The structure of the unit test is based on the model/form/view structure, for example test_views.py, test_model.py and test_forms.py on a per-app basis
- I used coverage(coverage.py) for code coverage and to ensure a high code coverage was met on all python files in the project
- An overall report image is available at the following link [Coverage Report](readme/misc/coverage_full_report.png)
- To run the unit tests click on Run "Test with Coverage" in your IDE, or at the command line "python manage.py test"
<br>![Unit test run 1](readme/misc/unit_test1.PNG)
- A test database is created and deleted for the test run, and each suite has a set-up:<code>def setUp(self):</code> and teardown:<code>def tearDown(self):</code> methods to create
the relevant objects needed for the test suite
<br>![Unit test run 2](readme/misc/unit_test2.PNG)

### Unit testing information for the Bag app
- For the bag app one suite was written to test the views
- The bag app does not have any forms or models
- The views' suite contains 8 unit tests testing add/removing items from the bag
<br>![Suite](readme/unit_tests/bag_test_views.PNG)
- In terms of coverage when run as part of the 13 suites, it gives the following code coverage
<br>![Coverage](readme/unit_tests/bag_coverage.PNG)

### Unit testing information for the Checkout app
- For the checkout app three suites were written to test the views, form and models
- The suites contain 3 unit tests testing the order creation and forms
<br>![Suite](readme/unit_tests/checkout_suites.PNG)
- In terms of coverage when run as part of the 13 suites, it gives the following code coverage
<br>![Coverage](readme/unit_tests/checkout_coverage.PNG)

### Unit testing information for the Home app
- For the home app one suite was written to test the views
- The home app does not have any forms or models
- The suite contains 1 unit tests testing the home page template
<br>![Suite](readme/unit_tests/home_test_views.PNG)
- In terms of coverage when run as part of the 13 suites, it gives the following code coverage
<br>![Coverage](readme/unit_tests/home_coverage.PNG)

### Unit testing information for the Products app
- For the product's app two suites were written to test the views and models
- The forms are tested as part of these suites
- The two suites contain 24 unit tests testing add/modify/views and delete of reviews and products
<br>![Suite](readme/unit_tests/products_suites.PNG)
- In terms of coverage when run as part of the 13 suites, it gives the following code coverage
<br>![Coverage](readme/unit_tests/products_coverage.PNG)

### Unit testing information for the Profile app
- For the product's app two suites were written to test the views and models
- The forms are tested as part of these suites
- The two suites contain 4 unit tests testing the users profile and profile updates
<br>![Suite](readme/unit_tests/profiles_suites.PNG)
- In terms of coverage when run as part of the 13 suites, it gives the following code coverage
<br>![Coverage](readme/unit_tests/profiles_coverage.PNG)

### Unit testing information for the Events App
- For the Events's app two suites were written to test the views and models
- The forms are tested as part of these suites
<br>![Suite](readme/unit_tests/profiles_suites.PNG)
- In terms of coverage when run as part of the 13 suites, it gives the following code coverage
<br>![Coverage](readme/unit_tests/profiles_coverage.PNG)

Device Number | Physical/Emulator | Device Name | Device Type | Browser |
------------ | ------------ | ------------- | ------------- | ------------- |
1 | Physical | Galaxy Note 3 | Phone |  Chrome |
2 | Physical | iPhone 8 | Mobile |Safari |
3 | Physical | Iphone 14 Pro | Mobile | Safari |
4 | Physical | Lenovo | Desktop | IE Edge |
5 | Physical | Macbook Pro 14 | Desktop | Mozilla Firefox |
6 | Physical | Imac | Desktop | Chrome |
7 | Emulator | Ipad Air | Tablet | Chrome |
8 | Emulator | Surface Pro 2 | Tablet | Chrome |
9 | Emulator | Pixel 2 | Tablet | Chrome |

## Responsiveness Testing

I made a very thorough check on responsiveness on all devices on the the google chrome emulator, and also on the physical devices I own personally which are stated in the table above.  Screen shots are included off all these devices below for each page.

### Homepage

<details><summary>Blackberry playbook - home</summary>
<img src="binge_reviews/static/images/readme/testing/responsivness-testing/home/blackberry-playbook-home.png">
</details>
<br>

<details><summary>Blackberry Z30 - Home</summary>
<img src="binge_reviews/static/images/readme/testing/responsivness-testing/home/blackberryz30-home.png">
</details>
<br>

<details><summary>Desktop 1000px - Home</summary>
<img src="binge_reviews/static/images/readme/testing/responsivness-testing/home/desktop-1000-pixels-home.png">
</details>
<br>

<details><summary>Desktop 1600px - Home</summary>
<img src="binge_reviews/static/images/readme/testing/responsivness-testing/home/desktop-1600-pixels-home.png">
</details>
<br>

<details><summary>Desktop 2500px - Home</summary>
<img src="binge_reviews/static/images/readme/testing/responsivness-testing/home/desktop-2500-pixels-home.png">
</details>
<br>

<details><summary>Galaxy 8 - Home<</summary>
<img src="binge_reviews/static/images/readme/testing/responsivness-testing/home/galaxy-8-home.png">
</details>
<br>

<details><summary>Galaxy Fold - Home</summary>
<img src="binge_reviews/static/images/readme/testing/responsivness-testing/home/galaxy-fold-home.png">
</details>
<br>

<details><summary>Galaxy Net Hub - Home</summary>
<img src="binge_reviews/static/images/readme/testing/responsivness-testing/home/galaxy-nest-hub-home.png">
</details>
<br>

<details><summary>Galaxy note 3 - Home</summary>
<img src="binge_reviews/static/images/readme/testing/responsivness-testing/home/galaxy-note-3-home.png">
</details>
<br>

<details><summary>Galaxy S5 - Home</summary>
<img src="binge_reviews/static/images/readme/testing/responsivness-testing/home/galaxy-s5-home.png">
</details>
<br>

<details><summary>Galaxy S9 plus - Home</summary>
<img src="binge_reviews/static/images/readme/testing/responsivness-testing/home/glaxy-s9plus-home.png">
</details>
<br>

<details><summary>Ipad Air - Home</summary>
<img src="binge_reviews/static/images/readme/testing/responsivness-testing/home/ipad-air-home.png">
</details>
<br>

<details><summary>Ipad Mini - Home</summary>
<img src="binge_reviews/static/images/readme/testing/responsivness-testing/home/ipad-mini-home.png">
</details>
<br>

<details><summary>Ipad Pro - Home</summary>
<img src="binge_reviews/static/images/readme/testing/responsivness-testing/home/ipad-pro-home.png">
</details>
<br>

<details><summary>Iphone4 - Home</summary>
<img src="binge_reviews/static/images/readme/testing/responsivness-testing/home/iphone-4-home.png">
</details>
<br>

<details><summary>Iphone SE - Home</summary>
<img src="binge_reviews/static/images/readme/testing/responsivness-testing/home/iphone-se-home.png">
</details>
<br>

<details><summary>Iphone XR - Home</summary>
<img src="binge_reviews/static/images/readme/testing/responsivness-testing/home/iphone-xr-home.png">
</details>
<br>

<details><summary>Pixel3 XL - Home</summary>
<img src="binge_reviews/static/images/readme/testing/responsivness-testing/home/pixel3-xl-home.png">
</details>
<br>


<details><summary>Samsung Galaxy S20 Ultra - Home</summary>
<img src="binge_reviews/static/images/readme/testing/responsivness-testing/home/samsung-glaxy-s20ultra-home.png">
</details>
<br>

<details><summary>Samsung Pro Duo - Home</summary>
<img src="binge_reviews/static/images/readme/testing/responsivness-testing/home/surface-pro-duo-home.png">
</details>
<br>

<details><summary>Samsung Pro 7 - Home</summary>
<img src="binge_reviews/static/images/readme/testing/responsivness-testing/home/surface-pro7-home.png">
</details>
<br>

###  Form Pages Login/Register/Add Review/Edit Review


<details><summary>Blackberry Playbook - form </summary>
<img src="binge_reviews/static/images/readme/testing/responsivness-testing/forms/blackberry-playbook-login.png">
</details>
<br>

<details><summary>Blackberry Z30 - form </summary>
<img src="binge_reviews/static/images/readme/testing/responsivness-testing/forms/blackberry-z30-login.png">
</details>
<br>

<details><summary>Desktop 1600px - form </summary>
<img src="binge_reviews/static/images/readme/testing/responsivness-testing/forms/desktop-1600ox-register.png">
</details>
<br>

<details><summary>Desktop 1000px - form </summary>
<img src="binge_reviews/static/images/readme/testing/responsivness-testing/forms/desktop-1000px-login.png">
</details>
<br>

<details><summary>Desktop 2500px - form </summary>
<img src="binge_reviews/static/images/readme/testing/responsivness-testing/forms/desktop-2500px-register.png">
</details>
<br>

<details><summary>Galaxy 8 - form </summary>
<img src="binge_reviews/static/images/readme/testing/responsivness-testing/forms/galaxy-8-register.png">
</details>
<br>

<details><summary>Galaxy Note 3 - form </summary>
<img src="binge_reviews/static/images/readme/testing/responsivness-testing/forms/galaxy-note-3-add-review.png">
</details>
<br>

<details><summary>Nest- Form</summary>
<img src="binge_reviews/static/images/readme/testing/responsivness-testing/forms/nest-hub-register.png">
</details>
<br>

### Feature 1 Navigation & Homepage
#### Description feature 2
- User Story 1.1: As an admin/regular user the navigation bar is displayed with a logo on all pages with a search box, My account and shopping bag icons on a desktop device
- User Story 1.2: As an admin/regular user the navigation bar is displayed on all pages with a search box, My account and shopping bag icons on a mobile/tablet device
- User Story 1.3: As a regular user not logged in, I see a Register/Login link under the My Account dropdown
- User Story 1.4: As a regular user logged in/not logged in, I am brought to my shopping bag if I click on the Bag icon
- User Story 1.5: As a regular/admin user logged in, I see a "My Profile"/Logout under the My Account dropdown
- User Story 1.6: As a regular/admin user logged in, if I click on the My Profile under My Account I am brought to the My Profile page
- User Story 1.7: As a regular/admin user logged in, if I click on the My Profile under My Account I am brought to the Logout page. If I click Logout I am Logged out. If I click cancel I am brought back to the homepage
- User Story 1.8: As a regular/admin user I can view the Home link in the header, and clicking it will bring the user to the homepage
- User Story 1.9: As a regular/admin user I can click on the "All Products" filter, click By Price, and will be brought to the Products page, with products price low to high displayed
- User Story 1.10: As a regular/admin user I can click on the "All Products" filter, click By Rating, and will be brought to the Products page, with products rating high to low displayed
- User Story 1.11: As a regular/admin user I can click on the "All Products" filter, click By Category, and will be brought to the Products page, with products category a-z displayed
- User Story 1.12: As a regular/admin user I can click on the "Meal Kits" filer and filter by Mild, Medium, Hot, Very Hot, All Meal Kits
- User Story 1.13: As a regular/admin user I can click on the "Drinks" filter and filter by Tequila, Soft Drinks, Beers, All Drinks
- User Story 1.14: As a regular/admin user I can click on the "Sauces & Spices" filter and filter by Sauces, Spices
- User Story 1.15: As a regular/admin user I can click on the "Events" Tab and be directing to the events booking page.
- User Story 1.16: As a regular/admin user if I encounter an error on the site, I will be navigated to the applicable 400, 403, 404 or 500 error page

#### User Stories Steps 1
1. Navigate to https://taco-y-tequila-c6ff831b9a3a.herokuapp.com, and click on the My Account link as a regular user
2. Login to the website with a valid username and password, and click on the My Account link
3. Navigate to the "All Products" filter, and then click By Price
4. Navigate to the "All Products" filter, and then click By Spice Rating
5. Navigate to the "All Products" filter, and then click By Category
6. Navigate to the "Meal Kits" filter, and filter by Adidas 'Mild'
7. Navigate to the "Drinks" filter, and filter by 'Tequila'
8. Navigate to the "Sauces & Spices" filter, and filter by 'Spices'
9. Navigate to the page https://taco-y-tequila-c6ff831b9a3a.herokuapp.com/nosuchpage
10. Click the Logout link under My profile and logout
11. Login as an admin user

#### User Story Testing Results 1
Step| Result | Desktop | Tablet | Mobile | Status
------------ | ------------ | ------------- | ------------- | ------------- | -------------
Step 1 | The homepage is displayed, Login and Register links are displayed under My Account | [Desktop](readme/testing/feature_1/feature-1-step1-desktop.png)  | [Tablet](readme/testing/feature_1/feature-1-step1-tablet.png)  | [Mobile](readme/testing/feature_1/feature-1-step1-mobile.png)  | Passed |
Step 2 | The homepage is displayed with a header logo(desktop), search box(expands on tablet/mobile), My account and shopping bag icons. My Profile/Logout is visible under My Account.   | [Desktop](readme/testing/feature_1/feature-1-step2-desktop.png)  | [Tablet](readme/testing/feature_1/feature-1-step2-tablet.png)  | [Mobile](readme/testing/feature_1/feature-1-step2-mobile.png)  | Passed |
Step 3 | Products on the page are filtered by Price (Low-High) | [Desktop](readme/testing/feature_1/feature-1-step3-desktop.png)  | [Tablet](readme/testing/feature_1/feature-1-step3-tablet.png)  | [Mobile](readme/testing/feature_1/feature-1-step3-mobile.png)  | Passed |
Step 4 | Products on the page are filtered by Rating (High-Low) | [Desktop](readme/testing/feature_1/feature-1-step4-desktop.png)  | [Tablet](readme/testing/feature_1/feature-1-step4-tablet.png)  | [Mobile](readme/testing/feature_1/feature-1-step4-mobile.png)  | Passed |
Step 5 | Products on the page are filtered by Category (A-Z) | [Desktop](readme/testing/feature_1/feature-1-step5-desktop.png)  | [Tablet](readme/testing/feature_1/feature-1-step5-tablet.png)  | [Mobile](readme/testing/feature_1/feature-1-step5-mobile.png)  | Passed |

### Feature 2 Footer
#### Description feature 2
- User Story 2.1: As a regular user the footer is displayed with a logo, 'About us links', 'Events' and 'Newsletter' sign up
- User Story 2.2: As a regular user I can sign up for a newsletter by entering my email address and clicking Signup. I will receive an email after signing up

#### User Stories Steps 1
1. As a regular/admin user scroll down to the footer on the homepage

#### User Story Testing Results 1
Step| Result | Desktop | Tablet | Mobile | Status
------------ | ------------ | ------------- | ------------- | ------------- | -------------
Step 1 | The homepage is displayed, Login and Register links are displayed under My Account | [Desktop](readme/testing/feature_2/feature-2-step2-desktop.png)  | [Tablet](readme/testing/feature_2/feature-2-step1-tablet.png)  | [Mobile](readme/testing/feature_2/feature-2-step1-mobile.png)  | Passed |

### Feature 3 Register
#### Description feature 3
- User Story 3.1: As a regular user I can register on the website by providing an email address, email address(confirmation), username, password, password confirmation
- User Story 3.1: As a regular user I will receive an email to verify my account after registering
- User Story 3.1: As a regular user I can log in to my account once I click on the verification link in the email I receive regarding my registration

#### User Stories Steps 1
1. As a regular user, navigate to the registration page, fill in email address, email address(confirmation), username, password, password confirmation and click Sign Up
2. Open the email received
3. Click on the verification link in the email received

#### User Story Testing Results 1
Step| Result | Desktop | Tablet | Mobile | Status
------------ | ------------ | ------------- | ------------- | ------------- | -------------
Step 1 | User registers for an account | [Desktop](readme/testing/feature_4/feature-3-step1-desktop.png)  | [Tablet](readme/testing/feature_3/feature-3-step1-tablet.png)  | [Mobile](readme/testing/feature_3/feature-3-step1-mobile.png)  | Passed |
Step 2 | User registers for an account | [Desktop](readme/testing/feature_3/feature-3-step2-desktop.png)  | [Tablet](readme/testing/feature_3/feature-3-step2-tablet.png)  | [Mobile](readme/testing/feature_3/feature-3-step2-mobile.png)  | Passed |
Step 3 | User registers for an account | [Desktop](readme/testing/feature_3/feature-3-step3-desktop.png)  | [Tablet](readme/testing/feature_3/feature-3-step3-desktop.png)  | [Mobile](readme/testing/feature_3/feature-3-step3-desktop.png)  | Passed |

### Feature 4 Login
#### Description feature 4
- User Story 4.1: As an admin/regular user I can log in to the website using my username or email address and password. Both fields are mandatory. Once correct, I will be navigated to the homepage and a message displayed
- User Story 4.2: As an admin/regular user I can request a new password if I forget my current password. I will receive an email to reset my password. Once I reset I can log in

#### User Stories Steps 1
1. Attempt to log in to the website with an account that does not exist or an incorrect password
2. Request a new password
3. Login to the site with the correct account details

#### User Story Testing Results 1
Step| Result | Desktop | Tablet | Mobile | Status
------------ | ------------ | ------------- | ------------- | ------------- | -------------
Step 1 | A message is displayed to the user | [Desktop](readme/testing/feature_4/feature-4-step1-desktop.png)  | [Tablet](readme/testing/feature_4/feature-4-step1-tablet.png)  | [Mobile](readme/testing/feature_4/feature-4-step1-mobile.png)  | Passed |
Step 2 | The user receives an email where they can reset their password | [Desktop](readme/testing/feature_4/feature-4-step2-desktop.png)  | [Tablet](readme/testing/feature_4/feature-4-step2-desktop.png)  | [Mobile](readme/testing/feature_4/feature-4-step2-desktop.png)  | Passed |
Step 3 | The user can successfully log in | [Desktop](readme/testing/feature_4/feature-4-step3-desktop.png)  | [Tablet](readme/testing/feature_4/feature-4-step3-tablet.png)  | [Mobile](readme/testing/feature_4/feature-4-step3-mobile.png)  | Passed |

### Feature 5 Login
#### Description feature 5
- User Story 5.1: As a regular user I can view the products page with product count and with each product image, title, spice rating, category the product is in.
- User Story 5.2: As a regular user I can sort the products by Price(high to low, low to high), Spice Rating(high to low, low to high), Name(A-Z, Z-A), Category(A-Z, Z-A)
- User Story 5.3: As a regular user if I click on a product I will be navigated to the product detail page
- User Story 5.4: As a regular user I can view the product image, description, sku, spice rating, category
- User Story 5.5: As a regular user I can click on the Keep Shopping button on the product detail page, and it will navigate the user to the products page
- User Story 5.6: As a regular user I can set the product size(if applicable for the product) and quantity for a product (one plus)
- User Story 5.10: As an admin user I can view the Add product page by clicking on the Product Management link.
- User Story 5.11: As an admin user I can view the Edit product page by clicking on the Edit button on the product.
- User Story 5.12: As an admin user I can click on a product, and I am navigated to the product detail page. I can edit or delete the product by clicking on the Edit or Delete links on the page
- User Story 5.13: As an admin user I can delete a review a regular user has added

#### User Stories Steps 1
1. As a regular user login to the website and navigate to the products page
2. Sort the products from Price(High to Low)
3. Click on a product
4. Add a product
5. As an admin user login and click on the add product(Product Management)
6. Click on the edit button on the products page or in the product detail page and edit the product

#### User Story Testing Results 1
Step| Result | Desktop | Tablet | Mobile | Status
------------ | ------------ | ------------- | ------------- | ------------- | -------------
Step 1 | The products page is displayed | [Desktop](readme/testing/feature_5/feature-5-step1-desktop.png)  | [Tablet](readme/testing/feature_5/feature-5-step1-tablet.png)  | [Mobile](readme/testing/feature_5/feature-5-step1-mobile.png)  | Passed |
Step 2 | The products are sorted High to Low | [Desktop](readme/testing/feature_5/feature-5-step2-desktop.png)  | [Tablet](readme/testing/feature_5/feature-5-step2-tablet.png)  | [Mobile](readme/testing/feature_5/feature-5-step2-mobile.png)  | Passed |
Step 3 | The product detail is displayed | [Desktop](readme/testing/feature_5/feature-5-step3-desktop.png)  | [Tablet](readme/testing/feature_5/feature-5-step3-tablet.png)  | [Mobile](readme/testing/feature_5/feature-5-step3-mobile.png)  | Passed |
Step 4 | The add product page is displayed | [Desktop](readme/testing/feature_5/feature-5-step4-desktop.png)  | [Tablet](readme/testing/feature_5/feature-5-step4-tablet.png)  | [Mobile](readme/testing/feature_5/feature-5-step4-mobile.png)  | Passed |
Step 5 | The edit product page is displayed | [Desktop](readme/testing/feature_5/feature-5-step5-desktop.png)  | [Tablet](readme/testing/feature_5/feature-5-step5-tablet.png)  | [Mobile](readme/testing/feature_5/feature-5-step5-mobile.png)  | Passed |



