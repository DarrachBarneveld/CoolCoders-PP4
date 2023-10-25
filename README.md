# CoolCoders-PP4

[Link to deployed site](https://coolcoders-b69260c4617a.herokuapp.com/)

<hr>
Cool Coders is your go-to hub for all things tech, offering a wealth of insightful posts on coding, industry trends, gadgets and more. Engage with a global community by favoriting posts, leaving comments, and sparking discussions. Share your own tech experiences through user-generated posts. Join Cool Coders today and immerse yourself in the dynamic world of technology.

![CoolCoders Image](./documentation/images/banner-image.png)

# Table Of Content

- [User Experience](#user-experience)
- [User Stories](#user-stories)
- [Site Goals](#site-goals)

## User Experience

### User Stories

#### New User

1. As a user I want the website to be responsive so I can view it on multiple devices
2. As a User I can intuitively navigate through the website so that I can view all content with ease.
3. As a User, I can create an account so that I can post, save and edit content
4. As a User, I can log out so that I can secure my account from potential hacks
5. As a User, I can post an article so that I can share my insights with the community.
6. As a User, I can create comments on articles, so that I can engage with the content and share my thoughts.
7. As a User, I can delete my own comments, so that I can remove unwanted opinions.
8. As a User, I can view content on the home page so that I can stay informed and explore engaging topics.
9. As a User, I can view a selected article with its comments, as well as related articles, so that I can explore in-depth content and engage with the community.
10. As a User, I can filter articles to a specific category, so that I can explore content that interests me.
11. As a User, I can view a user's profile page, displaying their posts, favourites and basic information so that I can learn more about the user and their contributions.
12. As a User, I can add articles to my favourites so that I can save my most enjoyed articles for future reference.
13. As a User I can see notification messages when performing CRUD operations or login/logout, signup so that informed about the outcome of the action taken.
14. As a User, I want to view comments on an article so that I can see the discussions going on a particular topic.

#### Existing User

1. As a User, I can access my account so that I can create and edit content and view my saved information
2. As a User, I can view my profile page so that I can update my information
3. As a User, I can edit my articles as the author, so that I can keep my content up to date.
4. As a User, I can create comments on articles, so that I can engage with the content and share my thoughts.
5. As a User, I can view my favourites on my profile detail page so that I can reread my favourite articles
6. As a User, I can level up based on the number of posts I have contributed, so that I can be recognised for my active participation and contributions to the community.
7. As a User, I can delete my account so that I can remove myself, details and all content from the live website

#### Website Owner/Developer

1. As a developer I can layout wireframes so that I have a clear idea of the sites structure and theme
2. As a Developer I can choose a colour theme so that all pages have a consistent feel and style.
3. As a Developer, I can created a standardised article preview card for each article, providing key information at a glance so that users can quickly understand the context of an article
4. As a Site Owner, I can have the capability to perform all CRUD (Create, Read, Update, Delete) functionality within the website's admin interface so that I can manually create and edit content.
5. As the Site Owner, I can approve user created content so that I can manually oversee and manage content creation and edits.
6. As a Site Owner, I can delete user profiles and all associated content from the platform so I can minimise harmful users.
7. As the Site Owner, I can view users and their profiles/content through the website's admin interface, allowing me to manage site users.
8. As a Developer, I want to ensure the styling and theme of the website are consistent, free from CSS errors, and provide an intuitive and easy-to-use UI/UX so that users easily digest content and perform all actions with ease.

### Site Goals

1. Foster a thriving global tech community
2. Share and discuss the latest tech trends and insights
3. Create a platform for users to contribute their tech knowledge
4. Encourage collaboration and knowledge exchange
5. Connect tech enthusiasts from all backgrounds and expertise levels
6. Promote a love for coding and technology exploration

### Scope

The project's scope is to create and maintain "Cool Coders," an online platform dedicated to tech enthusiasts. Cool Coders will serve as a user-friendly and responsive space for individuals to explore, share, and interact with tech-related content. Development will be assisted by following a number of EPIC stories which will focus on different aspects of the site. The platform will encompass the following key features:

1. EPIC - Initial Set Up:

- Developers can set up a new Django project to create the project's structure.
- Database and media storage will be connected to ensure data storage and retrieval.
- An early deployment of the application will be carried out to confirm the initial setup's functionality.

2. EPIC - UX Design Planning:

- The website will be responsive, allowing users to access it on both desktop and mobile devices.
- The website will have a consistant theming throughout
- The websites navigation will be inituitve and allow multiple methods of accessing content

3. User Authentication:

- Account registration is available for users, granting them full access to coolcoders features.
- Once registered, users can log in to access their profiles, posts, comments, and favourited items.

4. EPIC - Content Creation:

- Users can create, update, read and delete their posts.
- Users can view all their posts from the profile page and by using the navigation functionalities.
- Posts will provide an image and a short excerpt description of the content.
- Users can view all other users posts from their profile pages.
- Users are notified of all CRUD actions taken

5. EPIC - Viewing Content:

- Users can view comments on articles
- Users can visit an article detail page which shows all the relevent information
- Users see a article card which lists the key aspects of an article and its engagement
- Users see a home page and catgory page listing the most popular articles

6. EPIC - Profile Content:

- Users can view their profile and all associated content they have created.
- Users can see engagement metrics
- Users can easily navigated to their favourites, post and visit the editor
- Authenticated users can update their username, fullname and biography
- Users can update their passwords when logged in
- Users can delete their profiles and all associated comments/posts.

7. EPIC - Documentation:

- A comprehensive documentation lists the key aspects/reasons for the applications
- A testing manual is written along side the documentation
- Code documentation of each function/class and module is written for easy legibility/understanding

8. EPIC - Administration:

- Admins can perform all CRUD operations on site content from an admin portal
- Admins must approve user created content before it is live
- Admins can delete and modify users accounts from the administration portal

Benefits of key features and the EPIC Milestone Approach:

1. Prioritizing User Needs: The platform places the user's requirements at the forefront, streamlining the browsing experience, available posts creation and user communication on such posts.
2. Streamlined and Easy Navigation: Users can effortlessly move through various website sections, ensuring convenient and hassle-free access. This is performed by using the category selector, related posts sidebar and browsing user profiles.
3. User Analytics: Users gain valuable insights, allowing them to track and monitor metrics like the number of posts created, comments made, likes received, and favorites accumulated, enhancing their understanding of their contributions and interactions on Cool Coders.

## Design

### Colour Scheme

The website adopts a soothing and polished color scheme, mirroring the iconic colors of the MacBook Pro. These are black, light gray and white. This palette creates an overall professional and user-friendly ambiance, utilizing subtle variations in shade and transparency to direct user attention and elevate the website's visual allure. A hint of glassmorphism can be scene on article cards to futher the illusion of browsing on a tech item.

![Colour Scheme](./documentation/images/theme/colour-theme.png)

### Database Schema

![Database schema](./documentation/images/database-schema.png)

### Models

#### Allauth User Model

The User model is an integral component of Django Allauth, featuring pre-established fields as part of its standard configuration. Among these fields are username, email, name, password, and others. This model primarily serves the purpose of user authentication, which is why it is not recommended to make direct alterations to it. Furthermore, the User model is linked to the Profile model through a one-to-one relationship, facilitating the management of user-specific data and interactions.

#### Profile Model

Profile Model: The Profile Model provides a snapshot of each user's presence on the platform, encapsulating their information, activities, and preferences. It often includes fields for user-specific data such as name, bio and slug. It is has a one to one relationship with the auth User Model

#### Category Model

The Category Model categorizes and organizes posts, ensuring users can easily discover and explore tech topics. It typically includes fields for category name, description, and associations with posts to facilitate content organization and navigation within the platform.

#### Post Model

The Post Model is the core of the content creation process, where users share their tech-related knowledge, experiences, and insights. This model includes fields for post content, author, publication date, category association, and engagement metrics such as likes.

#### Comment Model

The Comment Model serves as the foundation for user engagement on the platform, allowing users to interact with posts by sharing their thoughts and feedback. It includes fields for the comment content, author, timestamp, and a foreign key relationship to associated posts.

### Fonts

The font used in this project is Segoe UI Roboto, which compliments the techical design of the website. <br>
![Font](./documentation/images/theme/font-family.png)
