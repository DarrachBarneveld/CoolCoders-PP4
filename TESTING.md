# Table of Contents

- [User Story Testing](#user-story-testing)
- [Code Validation](#code-validation)
  - [HTML](#html)
  - [CSS](#css)
  - [JavaScript](#JavaScript)
  - [Python](#python)
- [Responsiveness](#Responsiveness)
- [Browser Testing](#browser-testing)
- [Device Testing](#device-testing)
- [Lighthouse](#Lighthouse)
- [Manual Testing](#manual-testing)
  - [Site Navigation](#site-navigation)
  - [Home Page](#home-page)
  - [Category Page](#category-page)
  - [Article Preview Card](#article-preview-card)
  - [Add Post Page](#add-post-page)
  - [Edit Post Page](#edit-post-page)
  - [Delete Confirmation Modal](#delete-confirmation-modal)
  - [Profile Page](#profile-page)
  - [Update Profile Page](#update-profile-page)
  - [Sign Up Page](#sign-up-page)
  - [Sign In Page](#sign-in-page)
  - [Log Out Page](#log-out-page)

## User Story Testing

| User Story                                                                                                                                                                                                                        | Screenshot                                                                                                              | Result           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ---------------- |
| As a developer I can setup a new Django project so that I can create the project's structure                                                                                                                                      | The project was set up successfully                                                                                     | <mark>PASS<mark> |
| As a developer I can connect database and media storage so that the user's stored data is stored successfully                                                                                                                     | Database and storage set up succesfully                                                                                 | <mark>PASS<mark> |
| As a developer, I can perform an early deployment of the application to verify the functionality of the initial setup so that I can continue testing the application as it evolves during development.                            | Live site was hosted with no errors                                                                                     | <mark>PASS<mark> |
| As a developer I can layout wireframes so that I have a clear idea of the sites structure and theme                                                                                                                               | Wireframers were planned and created as referenced in the [README](./README.md)                                         | <mark>PASS<mark> |
| As a developer I can choose a colour theme so that all pages have a consistent feel and style.                                                                                                                                    | A colour theme was chosen for the website as referenced in the [README](./README.md)                                    | <mark>PASS<mark> |
| As a user I want the website to be responsive so I can view it on multiple devices                                                                                                                                                | <details><summary>Responsive</summary><img src="./documentation/testing/responsive.png"></details>                      | <mark>PASS<mark> |
| As a User I can intuitively navigate through the website so that I can view all content with ease.                                                                                                                                | <details><summary>Navigation Bar</summary><img src="./documentation/images/features/navauth.png"></details>             | <mark>PASS<mark> |
| As a User, I can create an account so that I can post, save and edit content                                                                                                                                                      | <details><summary>Registration</summary><img src="./documentation/images/features/signin.png"></details>                | <mark>PASS<mark> |
| As a User, I can access my account so that I can create and edit content and view my saved information                                                                                                                            | <details><summary>Profile Edit</summary><img src="./documentation/images/features/editprofile.png"></details>           | <mark>PASS<mark> |
| As a User, I can log out so that I can secure my account from potential hacks                                                                                                                                                     | <details><summary>Sign Out</summary><img src="./documentation/images/features/signout.png"></details>                   | <mark>PASS<mark> |
| As a User, I can view my profile page so that I can update my information                                                                                                                                                         | <details><summary>Profile Page</summary><img src="./documentation/images/features/profile.png"></details>               | <mark>PASS<mark> |
| As a User, I can post an article so that I can share my insights with the community.                                                                                                                                              | <details><summary>Add Post</summary><img src="./documentation/images/features/addeditpost.png"></details>               | <mark>PASS<mark> |
| As a User, I can edit my articles as the author, so that I can keep my content up to date.                                                                                                                                        | <details><summary>Edit Post</summary><img src="./documentation/images/features/editpost.png"></details>                 | <mark>PASS<mark> |
| As a User, I can create comments on articles, so that I can engage with the content and share my thoughts.                                                                                                                        | <details><summary>Comment Form</summary><img src="./documentation/images/features/commentform.png"></details>           | <mark>PASS<mark> |
| As a User, I can delete my own comments, so that I can remove unwanted opinions.                                                                                                                                                  | <details><summary>Delete Comment</summary><img src="./documentation/images/features/commentcard.png"></details>         | <mark>PASS<mark> |
| As a User, I can view content on the home page so that I can stay informed and explore engaging topics.                                                                                                                           | <details><summary>Home Page</summary><img src="./documentation/images/features/homepage.png"></details>                 | <mark>PASS<mark> |
| As a User, I can view a selected article with its comments, as well as related articles, so that I can explore in-depth content and engage with the community.                                                                    | <details><summary>Post Detail Page</summary><img src="./documentation/images/features/postdetail.png"></details>        | <mark>PASS<mark> |
| As a User, I can view articles in a specific category, so that I can explore content that interests me.                                                                                                                           | <details><summary>Category Page</summary><img src="./documentation/images/features/categories.png"></details>           | <mark>PASS<mark> |
| As a User, I can view a user's profile page, displaying their posts, favourites and basic information so that I can learn more about the user and their contributions.                                                            | <details><summary>Profile Page</summary><img src="./documentation/images/features/profile.png"></details>               | <mark>PASS<mark> |
| As a User, I can view my favourites on my profile detail page so that I can reread my favourite articles                                                                                                                          | <details><summary>Favourites</summary><img src="./documentation/images/features/favourites.png"></details>              | <mark>PASS<mark> |
| As a Developer, I can created a standardised article preview card for each article, providing key information at a glance so that users can quickly understand the context of an article                                          | <details><summary>Article Card</summary><img src="./documentation/images/features/articlecard.png"></details>           | <mark>PASS<mark> |
| As a User, I can add articles to my favourites so that I can save my most enjoyed articles for future reference.                                                                                                                  | <details><summary>Toggle Favourites</summary><img src="./documentation/images/features/togglefavourites.png"></details> | <mark>PASS<mark> |
| As a Site Owner, I can have the capability to perform all CRUD (Create, Read, Update, Delete) functionality within the website's admin interface so that I can manually create and edit content.                                  | <details><summary>Admin Crud</summary><img src="./documentation/images/features/admincrud.png"></details>               | <mark>PASS<mark> |
| As the Site Owner, I can approve user created content so that I can manually oversee and manage content creation and edits.                                                                                                       | <details><summary>Approval</summary><img src="./documentation/images/features/adminapproval.png"></details>             | <mark>PASS<mark> |
| As a Site Owner, I can delete user profiles and all associated content from the platform so I can minimise harmful users.                                                                                                         | <details><summary>Delete Users</summary><img src="./documentation/images/features/deleteuser.png"></details>            | <mark>PASS<mark> |
| As a User I can see notification messages when performing CRUD operations or login/logout, signup so that informed about the outcome of the action taken.                                                                         | <details><summary>Notifications</summary><img src="./documentation/images/features/notifications.png"></details>        | <mark>PASS<mark> |
| As the Site Owner, I can view users and their profiles/content through the website's admin interface, allowing me to manage site users.                                                                                           | <details><summary>Admin Content</summary><img src="./documentation/images/features/admincontent.png"></details>         | <mark>PASS<mark> |
| As a User, I want to view comments on an article so that I can see the discussions going on a particular topic.                                                                                                                   | <details><summary>Comments</summary><img src="./documentation/images/features/commentcard.png"></details>               | <mark>PASS<mark> |
| As a Developer, I want to ensure the styling and theme of the website are consistent, free from CSS errors, and provide an intuitive and easy-to-use UI/UX so that users easily digest content and perform all actions with ease. | <details><summary>Website theme</summary><img src="./documentation/images/theme/websitetheme.png"></details>            | <mark>PASS<mark> |
| As a User, I can level up based on the number of posts I have contributed, so that I can be recognised for my active participation and contributions to the community.                                                            | <details><summary>Level Up</summary><img src="./documentation/images/features/level.png"></details>                     | <mark>PASS<mark> |
| As a User, I can delete my account so that I can remove myself, details and all content from the live website                                                                                                                     | <details><summary>Delete Account</summary><img src="./documentation/images/features/deleteaccount.png"></details>       | <mark>PASS<mark> |
| As a developer, I can show custom error pages redirect the user to the home page, so that I have a consistent experience even when encountering errors on the website.                                                            | <details><summary>Error Page</summary><img src="./documentation/images/features/errorpage.png"></details>               | <mark>PASS<mark> |

## Code Validation

### HTML

All HTML pages were run through the [W3C HTML Validator](https://validator.w3.org/). See results in below table.

| Page        | Validator                                                                                                                  | Result            |
| ----------- | -------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| Home        | <details><summary>Home Page</summary><img src="./documentation/testing/validation/html/homehtml.png"></details>            | <mark>PASS</mark> |
| Category    | <details><summary>Category Page</summary><img src="./documentation/testing/validation/html/categoryhtml.png"></details>    | <mark>PASS</mark> |
| Post Detail | <details><summary>Post Detail Page</summary><img src="./documentation/testing/validation/html/categoryhtml.png"></details> | <mark>PASS</mark> |
| Profile     | <details><summary>Profile Page</summary><img src="./documentation/testing/validation/html/profilehtml.png"></details>      | <mark>PASS</mark> |
| Sign In     | <details><summary>Sign In</summary><img src="./documentation/testing/validation/html/loginhtml.png"></details>             | <mark>PASS</mark> |
| Sign Up     | <details><summary>Sign Up</summary><img src="./documentation/testing/validation/html/signuphtml.png"></details>            | <mark>PASS</mark> |

### CSS

Test Results CSS <mark>PASS<mark>
<img src="./documentation/testing/validation/css/cssvalidation.png">

### JavaScript

The only JS used in this project was refactored from Code Institute's I Think Therefore I Blog project into a seperate JS file.

### Python

| File     | Validator                                                                                                              | Result            |
| -------- | ---------------------------------------------------------------------------------------------------------------------- | ----------------- |
| Models   | <details><summary>Models</summary><img src="./documentation/testing/validation/python/modelspython.png"></details>     | <mark>PASS</mark> |
| Views    | <details><summary>Views</summary><img src="./documentation/testing/validation/python/viewspython.png"></details>       | <mark>PASS</mark> |
| Forms    | <details><summary>Forms</summary><img src="./documentation/testing/validation/python/formspython.png"></details>       | <mark>PASS</mark> |
| Urls     | <details><summary>Urls</summary><img src="./documentation/testing/validation/python/urlpython.png.png"></details>      | <mark>PASS</mark> |
| Admin    | <details><summary>Admin</summary><img src="./documentation/testing/validation/python/adminpython.png"></details>       | <mark>PASS</mark> |
| Settings | <details><summary>Settings</summary><img src="./documentation/testing/validation/python/settingspython.png"></details> | <mark>PASS</mark> |

Settings.py validation errors of line to line are as a result of the original django configuration set up and not custom code.

## Responsiveness

Throughout the development process, each page underwent testing using Google Chrome's developer tools. The approach focused on verifying that every page would seamlessly adjust to a variety of screen sizes wider than 320px, rather than being limited by predetermined, device-specific widths.

Further testing was done on a real mobile device to confirm all is working as expected.

| Device         |     Pass/Fail     |               Comment                |
| -------------- | :---------------: | :----------------------------------: |
| Huawei p30 pro | <mark>PASS</mark> | All elements are displayed correctly |

## Browser Testing

The Website was tested on Google Chrome, Firefox, Safari and Chrome Canary browsers with no issues noted.

## Device Testing

The website was tested on a variety of devices, including Desktop, Laptop, Huawei P30 Pro, and Samsung tablet, to ensure that it displayed well on screens of different sizes, both in portrait and landscape orientations. The website functioned as expected, and its responsive design was validated using Chrome developer tools on various devices, ensuring that the layout remained structurally sound across different screen dimensions.

### Lighthouse

Lighthouse validation was run on all pages (both mobile and desktop) in order to check accessibility and performance. At first I received the warning _'Background and foreground colors do not have a sufficient contrast ratio'_ in relation to buttons where I had used the Bootstrap class `btn-info`. After I updated the button styling I received the below scores.

| Page           | Performance | Accessibility | Best Practices | SEO | Screenshot                                                                                                                  |
| -------------- | :---------: | :-----------: | :------------: | :-: | --------------------------------------------------------------------------------------------------------------------------- |
|                |             |               |                |     |
| **Desktop**    |             |               |                |     |
| Home           |     98      |      100      |      100       | 100 | <details><summary>Home</summary><img src="./documentation/testing/lighthouse/homedesktop.png"></details>                    |
| Category       |     98      |      100      |      100       | 100 | <details><summary>Category</summary><img src="./documentation/testing/lighthouse/categorydesktop.png"></details>            |
| Post Detail    |     97      |      100      |      100       | 100 | <details><summary>Post Detail </summary><img src="./documentation/testing/lighthouse/postdetaildesktop.png"></details>      |
| Profile        |     96      |      100      |      100       | 100 | <details><summary>Profile</summary><img src="./documentation/testing/lighthouse/profiledesktop.png"></details>              |
| Add Post       |     99      |      96       |      100       | 100 | <details><summary>Add Post</summary><img src="./documentation/testing/lighthouse/addpostdesktop.png"></details>             |
| Edit Post      |     99      |      96       |      100       | 100 | <details><summary>Edit Post</summary><img src="./documentation/testing/lighthouse/editpostdesktop.png"></details>           |
| Update Profile |     100     |      100      |      100       | 100 | <details><summary>Update Profile</summary><img src="./documentation/testing/lighthouse/updateprofiledesktop.png"></details> |
| Sign Up        |     99      |      100      |      100       | 100 | <details><summary>Sign Up</summary><img src="./documentation/testing/lighthouse/signindesktop.png"></details>               |
| Sign In        |     100     |      100      |      100       | 100 | <details><summary>Sign In</summary><img src="./documentation/testing/lighthouse/signindesktop.png"></details>               |
| Sign Out       |     100     |      100      |      100       | 100 | <details><summary>Sign Out</summary><img src="./documentation/testing/lighthouse/signoutdesktop.png"></details>             |
|                |             |               |                |     |
| **Mobile**     |             |               |                |     |
| Home           |     90      |      100      |      100       | 100 | <details><summary>Home</summary><img src="./documentation/testing/lighthouse/homemobile.png"></details>                     |
| Category       |     91      |      100      |      100       | 100 | <details><summary>Category</summary><img src="./documentation/testing/lighthouse/categorymobile.png"></details>             |
| Post Detail    |     95      |      100      |      100       | 100 | <details><summary>Post Detail</summary><img src="./documentation/testing/lighthouse/postdetailmobile.png"></details>        |
| Profile        |     90      |      100      |      100       | 100 | <details><summary>Profile</summary><img src="./documentation/testing/lighthouse/profilemobile.png"></details>               |
| Add Post       |     86      |      95       |      100       | 100 | <details><summary>Add Post</summary><img src="./documentation/testing/lighthouse/addpostmobile.png"></details>              |
| Edit Post      |     87      |      95       |      100       | 100 | <details><summary>Edit Post</summary><img src="./documentation/testing/lighthouse/editpostdesktop.png"></details>           |
| Update Profile |     98      |      100      |      100       | 100 | <details><summary>Update Profile</summary><img src="./documentation/testing/lighthouse/updateprofilemobile.png"></details>  |
| Sign Up        |     98      |      100      |      100       | 100 | <details><summary>Sign Up</summary><img src="./documentation/testing/lighthouse/signupmobile.png"></details>                |
| Sign In        |     99      |      100      |      100       | 100 | <details><summary>Sign In</summary><img src="./documentation/testing/lighthouse/signinmobile.png"></details>                |
| Sign Out       |     98      |      100      |      100       | 100 | <details><summary>Sign Out</summary><img src="./documentation/testing/lighthouse/signoutmobile.png"></details>              |

## Manual Testing

### Site Navigation

| Element                | Action      | Expected Result                                         | Pass/Fail         |
| ---------------------- | ----------- | ------------------------------------------------------- | ----------------- |
| Logo                   | Click       | Redirect to Home page                                   | <mark>Pass</mark> |
| Home Link              | Click       | Redirect to Home page                                   | <mark>Pass</mark> |
| Category Button        | Click       | Render a dropdown menu of all categories                | <mark>Pass</mark> |
| Category Dropdown Link | Click       | Redirect to selected category page                      | <mark>Pass</mark> |
| Add Post Link          | Click       | Redirect to selected add post page                      | <mark>Pass</mark> |
| Register Link          | Click       | Redirect to sign up page                                | <mark>Pass</mark> |
| Log in Link            | Click       | Redirect to sign in page                                | <mark>Pass</mark> |
| Log out Link           | Click       | Redirect to log out page                                | <mark>Pass</mark> |
| Profile Link           | Click       | Redirect to profile page                                | <mark>Pass</mark> |
| Hamburger Menu         | Click       | Render a dropdown menu of all links                     | <mark>Pass</mark> |
| Footer Socials         | Click       | Redirect in a new tab to all respective media platforms | <mark>Pass</mark> |
| Register Link          | Display     | Render for non authenticated users                      | <mark>Pass</mark> |
| Log in Link            | Display     | Render for non authenticated users                      | <mark>Pass</mark> |
| Add Post Link          | Display     | Render only if user is authenticated                    | <mark>Pass</mark> |
| Log out Link           | Display     | Render only if user is authenticated                    | <mark>Pass</mark> |
| Profile Link           | Display     | Render only if user is authenticated                    | <mark>Pass</mark> |
| Nav Link               | Hover/Focus | Display a green underline border, lighten text          | <mark>Pass</mark> |

### Home Page

| Element          | Action      | Expected Result                          | Pass/Fail         |
| ---------------- | ----------- | ---------------------------------------- | ----------------- |
| Category Widgets | Click       | Redirect to selected category page       | <mark>Pass</mark> |
| Editors Pick     | Display     | Editors Pick Post Card viewable          | <mark>Pass</mark> |
| Trending         | Display     | Trending Post Snippets viewable          | <mark>Pass</mark> |
| Popular Post     | Display     | Popular Post Post Card viewable          | <mark>Pass</mark> |
| Category Widgets | Hover/Focus | Background turns green, text turns white | <mark>Pass</mark> |

### Category Page

| Element          | Action      | Expected Result                                               | Pass/Fail         |
| ---------------- | ----------- | ------------------------------------------------------------- | ----------------- |
| Category Widgets | Click       | Redirect to selected category page                            | <mark>Pass</mark> |
| Article Cards    | Display     | All Category Post Cards Rendered in grid layout               | <mark>Pass</mark> |
| Article Cards    | Pagination  | Pagination occurs on over 6 cards to a page                   | <mark>Pass</mark> |
| Paginator        | Click       | All navigations buttons redirect to correct paginated results | <mark>Pass</mark> |
| Category Widgets | Hover/Focus | Background turns green, text turns white                      | <mark>Pass</mark> |

### Article Preview Card

| Element        | Action      | Expected Result                           | Pass/Fail         |
| -------------- | ----------- | ----------------------------------------- | ----------------- |
| Title Link     | Click       | Redirect to post detail page              | <mark>Pass</mark> |
| Explore Button | Click       | Redirect to post detail page              | <mark>Pass</mark> |
| Author Link    | Click       | Redirect to authors profile page          | <mark>Pass</mark> |
| Edit Button    | Click       | Redirect to edit post page profile page   | <mark>Pass</mark> |
| Edit Button    | Display     | Render for only authneticated post author | <mark>Pass</mark> |
| Title Link     | Hover/Focus | Darken Text                               | <mark>Pass</mark> |
| Author Link    | Hover/Focus | Darken Text                               | <mark>Pass</mark> |
| Explore Button | Hover/Focus | Background blue, text white               | <mark>Pass</mark> |
| Edit Button    | Hover/Focus | Darken Background                         | <mark>Pass</mark> |

### Add Post Page

| Element               | Action         | Expected Result                                    | Pass/Fail         |
| --------------------- | -------------- | -------------------------------------------------- | ----------------- |
| Page                  | Authentication | Unauthneticated users routed to sign in page       | <mark>Pass</mark> |
| Text Input Required   | None           | On Submit: Warning appears, form won't submit      | <mark>Pass</mark> |
| Image Input           | Click          | Open device file storage                           | <mark>Pass</mark> |
| Image Input           | Selected       | Display selected image name                        | <mark>Pass</mark> |
| Image Input           | None           | Placeholder image selected                         | <mark>Pass</mark> |
| Submit Input(Invalid) | Click          | Form is not submitted and error messages appear    | <mark>Pass</mark> |
| Submit Input(Invalid) | Click          | Toast notification error message appears           | <mark>Pass</mark> |
| Submit Input(Valid)   | Click          | Form is submitted and notification message appears | <mark>Pass</mark> |
| Submit Input(Valid)   | Click          | User is redirected to home page                    | <mark>Pass</mark> |
| Post Title            | Click          | No duplicated titles are allowed                   | <mark>Pass</mark> |
| Error Context         | Submit         | If user forces submit error contexts are displayed | <mark>Pass</mark> |
| Submit Button         | Hover/Focus    | Darken Background                                  | <mark>Pass</mark> |

### Edit Post Page

| Element               | Action         | Expected Result                                    | Pass/Fail         |
| --------------------- | -------------- | -------------------------------------------------- | ----------------- |
| Page                  | Authentication | Unauthneticated users routed to sign in page       | <mark>Pass</mark> |
| Page                  | Authentication | Non Authour users show 403 page                    | <mark>Pass</mark> |
| Page                  | Display        | Post content is rendered to the UI                 | <mark>Pass</mark> |
| Text Input Required   | None           | On Submit: Warning appears, form won't submit      | <mark>Pass</mark> |
| Image Input           | Click          | Open device file storage                           | <mark>Pass</mark> |
| Image Input           | Selected       | Display selected image name                        | <mark>Pass</mark> |
| Image Input           | None           | Current image selected                             | <mark>Pass</mark> |
| Current Image         | None           | Current image link is displayed                    | <mark>Pass</mark> |
| Submit Input(Invalid) | Click          | Form is not submitted and error messages appear    | <mark>Pass</mark> |
| Submit Input(Invalid) | Click          | Toast notification error message appears           | <mark>Pass</mark> |
| Submit Input(Valid)   | Click          | Form is submitted and notification message appears | <mark>Pass</mark> |
| Submit Input(Valid)   | Click          | User is redirected to home page                    | <mark>Pass</mark> |
| Delete Button         | Click          | Delete Confirmation Modal appears                  | <mark>Pass</mark> |
| Post Title            | Click          | No duplicated titles are allowed                   | <mark>Pass</mark> |
| Error Context         | Submit         | If user forces submit error contexts are displayed | <mark>Pass</mark> |
| Submit Button         | Hover/Focus    | Darken Background                                  | <mark>Pass</mark> |
| Delete Button         | Hover/Focus    | Darken Background                                  | <mark>Pass</mark> |

### Delete Confirmation Modal

| Element               | Action      | Expected Result                       | Pass/Fail         |
| --------------------- | ----------- | ------------------------------------- | ----------------- |
| Close Button          | Click       | Modal and opacic background disappear | <mark>Pass</mark> |
| Confirm Delete Button | Click       | Context item is delete from database  | <mark>Pass</mark> |
| Close Button          | Hover/Focus | Darken Background                     | <mark>Pass</mark> |
| Confirm Delete Button | Hover/Focus | Darken Background                     | <mark>Pass</mark> |

### Profile Page

| Element              | Action      | Expected Result                                               | Pass/Fail         |
| -------------------- | ----------- | ------------------------------------------------------------- | ----------------- |
| Page                 | Display     | All User Profile Details Rendered                             | <mark>Pass</mark> |
| Settings Button      | Click       | Redirect to update profile page                               | <mark>Pass</mark> |
| Settings Button      | Display     | Render only if authenticated user is the profile page owner   | <mark>Pass</mark> |
| Settings Button      | Hover/Focus | Lighten Background                                            | <mark>Pass</mark> |
| Statistics           | Display     | All User Statisitics Details Rendered                         | <mark>Pass</mark> |
| User Posts           | Display     | All User Posts Rendered                                       | <mark>Pass</mark> |
| User Favourites      | Display     | All User Favourites Rendered                                  | <mark>Pass</mark> |
| User Posts           | Pagination  | Pagination occurs on over 4 cards to a list                   | <mark>Pass</mark> |
| User Favourites      | Pagination  | Pagination occurs on over 4 cards to a list                   | <mark>Pass</mark> |
| Posts Paginator      | Click       | All navigations buttons redirect to correct paginated results | <mark>Pass</mark> |
| Favourites Paginator | Click       | All navigations buttons redirect to correct paginated results | <mark>Pass</mark> |
| Posts                | Display     | If no post render No Posts UI                                 | <mark>Pass</mark> |
| Favourites           | Display     | If no favourites render No Favourites UI                      | <mark>Pass</mark> |
| Article Cards        | Links       | All rendered Article Cards are correctly linked               | <mark>Pass</mark> |

### Update Profile Page

| Element                   | Action         | Expected Result                               | Pass/Fail         |
| ------------------------- | -------------- | --------------------------------------------- | ----------------- |
| Page                      | Authentication | Unauthneticated users routed to sign in page  | <mark>Pass</mark> |
| Page                      | Display        | User Information Rendered to Inputs           | <mark>Pass</mark> |
| Text Input Required       | None           | On Submit: Warning appears, form won't submit | <mark>Pass</mark> |
| Username Title            | Submit         | No duplicated usernames are allowed           | <mark>Pass</mark> |
| User Submit (Valid)       | Submit         | Information updated in database               | <mark>Pass</mark> |
| User Submit (Valid)       | Submit         | Toast notification message received           | <mark>Pass</mark> |
| User Submit (Valid)       | Submit         | Redirected to profile page                    | <mark>Pass</mark> |
| User Submit (Invalid)     | Submit         | Error context rendered to UI                  | <mark>Pass</mark> |
| User Submit (Invalid)     | Submit         | Toast notification error message received     | <mark>Pass</mark> |
| Bio Submit (Valid)        | Submit         | Information updated in database               | <mark>Pass</mark> |
| Bio Submit (Valid)        | Submit         | Toast notification message received           | <mark>Pass</mark> |
| Bio Submit (Valid)        | Submit         | Redirected to profile page                    | <mark>Pass</mark> |
| Bio Submit (Invalid)      | Submit         | Error context rendered to UI                  | <mark>Pass</mark> |
| Bio Submit (Invalid)      | Submit         | Toast notification error message received     | <mark>Pass</mark> |
| Password Submit (Valid)   | Submit         | Information updated in database               | <mark>Pass</mark> |
| Password Submit (Valid)   | Submit         | Toast notification message received           | <mark>Pass</mark> |
| Password Submit (Valid)   | Submit         | Redirected to profile page                    | <mark>Pass</mark> |
| Password Submit (Invalid) | Submit         | Error context rendered to UI                  | <mark>Pass</mark> |
| Password Submit (Invalid) | Submit         | Toast notification error message received     | <mark>Pass</mark> |
| Delete Account Button     | Click          | Delete confirmation modal displayed           | <mark>Pass</mark> |

### Sign Up Page

| Element       | Action         | Expected Result                             | Pass/Fail         |
| ------------- | -------------- | ------------------------------------------- | ----------------- |
| Page          | Authentication | Authenticated users redirected to Home page | <mark>Pass</mark> |
| Form(Valid)   | Submit         | Redirected to Home page                     | <mark>Pass</mark> |
| Form(Valid)   | Submit         | Sign up in Notification received            | <mark>Pass</mark> |
| Form(Invalid) | Submit         | Error Context rendered to UI                | <mark>Pass</mark> |
| Form(Invalid) | Submit         | Error Notification received                 | <mark>Pass</mark> |
| Login Link    | Click          | Redirect to Login Page                      | <mark>Pass</mark> |

### Sign In Page

| Element       | Action         | Expected Result                             | Pass/Fail         |
| ------------- | -------------- | ------------------------------------------- | ----------------- |
| Page          | Authentication | Authenticated users redirected to Home page | <mark>Pass</mark> |
| Form(Valid)   | Submit         | Redirected to Home page                     | <mark>Pass</mark> |
| Form(Valid)   | Submit         | Sign up in Notification received            | <mark>Pass</mark> |
| Form(Invalid) | Submit         | Error Context rendered to UI                | <mark>Pass</mark> |
| Form(Invalid) | Submit         | Error Notification received                 | <mark>Pass</mark> |
| Register Link | Click          | Redirect to Sign In Page                    | <mark>Pass</mark> |

### Log Out Page

| Element       | Action         | Expected Result                                | Pass/Fail         |
| ------------- | -------------- | ---------------------------------------------- | ----------------- |
| Page          | Authentication | Un-authenticated users redirected to Home page | <mark>Pass</mark> |
| Logout Button | Click          | User session is Logged out                     | <mark>Pass</mark> |
| Logout Button | Click          | Redirected to Home page                        | <mark>Pass</mark> |
