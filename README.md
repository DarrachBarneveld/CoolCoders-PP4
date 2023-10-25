# CoolCoders-PP4

[Link to deployed site](https://coolcoders-b69260c4617a.herokuapp.com/)

<hr>
Cool Coders is your go-to hub for all things tech, offering a wealth of insightful posts on coding, industry trends, gadgets and more. Engage with a global community by favoriting posts, leaving comments, and sparking discussions. Share your own tech experiences through user-generated posts. Join Cool Coders today and immerse yourself in the dynamic world of technology.

![CoolCoders Image](./documentation/images/banner-image.png)

# Table Of Content

- [User Experience](#user-experience)
  - [User Stories](#user-stories)
  - [Site Goals](#site-goals)
  - [Scope](#scope)
- [Design](#design)
  - [Colour Scheme](#colour-scheme)
  - [Database Schema](#database-schema)
  - [Fonts](#fonts)
  - [Wireframes](#wireframes)
  - [Agile Methodology](#agile-methodology)
    - [Overview](#overview)
    - [EPICS(Milestones)](#epics---milestones)
    - [User Stories Issues](#user-stories---issues)
    - [MoSCoW prioritization](#moscow-prioritization)
    - [GitHub Projects](#github-projectskanban)

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

### Wireframes

#### Desktop

- Home
  ![Home](./documentation/images/wireframes/desktop/homepage-desktop.png)
- Category
  ![Category](./documentation/images/wireframes/desktop/categorypage-desktop.png)
- Post Detail
  ![Post-Detail](./documentation/images/wireframes/desktop/postdetailpage-desktop.png)
- Add Post
  ![Add-Post](./documentation/images/wireframes/desktop/addpostpage-desktop.png)
- Edit Post
  ![Edit-Post](./documentation/images/wireframes/desktop/editpostpage-desktop.png)
- Profile
  ![Profile](./documentation/images/wireframes/desktop/profilepage-desktop.png)
- Edit Profile
  ![Edit-Profile](./documentation/images/wireframes/desktop/editprofilepage-desktop.png)
- Login/Register
  ![Edit-Profile](./documentation/images/wireframes/desktop/login-register-desktop.png)

  #### Mobile

- Home
  ![Home](./documentation/images/wireframes/mobile/homepage-mobile.png)
- Category
  ![Category](./documentation/images/wireframes/mobile/categorypage-mobile.png)
- Post Detail
  ![Post-Detail](./documentation/images/wireframes/mobile/profiledetalpage-mobile.png)
- Add/Edit Post
  ![Add-Post](./documentation/images/wireframes/mobile/add-editpostpage-mobile.png)
- Profile
  ![Profile](./documentation/images/wireframes/desktop/profilepage-desktop.png)
- Edit Profile
  ![Edit-Profile](./documentation/images/wireframes/desktop/editprofilepage-desktop.png)
- Navbar
  ![Navbar](./documentation/images/wireframes/mobile/navbar-mobile.png)

  #### Components/UI

- Confirm Modal
  ![Modal](./documentation/images/wireframes/modal.png)
- Article Preview Card
  ![Preview-Card](./documentation/images/wireframes/articlepreviewcard.png)

### Agile Methodology

#### Overview

This project was developed following agile principles. Employing the agile methodology enabled me to meticulously map out the website's features by crafting user stories, each of which came with defined acceptance criteria and tasks. Grouping each of these stories into EPIC milestones allowed me to focus on the key elements of the site one by one. These elements served to distinctly delineate the necessary prerequisites for the successful implementation of each feature.

#### EPICS - Milestones

Within the Agile methodology framework, user stories are organized into eight EPICS or Milestones. Additionally, there is also additional Milestones known as Error Handling that was created for the sole purpose of handling any errors that came up during testing, development or tweaking site elements with more refactored coded or enchancements.

![Milestones](./documentation/images/epicmilestones.png)

#### User Stories - Issues

The user story issue format consists of the user story itself, as well as acceptance criteria and tasks that outline the essential steps for addressing the issue. When possible, during the development process, commit messages are associated with their corresponding issues. This practice ensures the relevance of each commit and also provides a visual representation of the progress made on each project issue. These issues are monitored using milestones, Kanban boards, and other Agile tools.

![User Story](./documentation/images/userstories.png)

#### MoSCoW Prioritization

The project employed the "MoSCoW" technique to effectively categorize and prioritize its features and requirements based on their importance. "MoSCoW" stands for "Must have, Should have, Could have, and Won't have," with each category contributing to the organization and prioritization of features. This approach acts as a guiding principle for the development process, ensuring that the most crucial elements are addressed as a top priority.

![MoSCoW](./documentation/images/moscow.png)

#### GitHub Projects/Kanban

The project adopted a basic Kanban Board structure, which was divided into columns such as Todo, In Progress and Done. This setup provided a clear and organized way to track the progress of tasks, making it easier to visualize and manage the workflow throughout the development process. The GitHub project Kanban was linked to the repo for consistant reference.
![Kanban](./documentation/images/kanban.png)

## Features

### Navigation Header

The navigation bar is a consistent element across all pages, designed using Bootstrap and optimized for full responsiveness. The left is centered around navigation of content while the right hand side is related to user authentication. Authenticated users can also see create posts and view profile links while unauthenticated users only see a prompt to login/register.

The mobile version of the navbar has all the content rendered when a hamburger icon is clicked. When clicked a dropdown display is rendered showing all navigation links.

### Footer

The footer is a miniinmalist footer designed to link users to cool coders social links. The link are only for educational purposes as just link to the social platforms base url.

### Home Page

The Home Hero Section on Cool Coders features carefully curated tech-related content with three components: Popular Posts, highlighting articles with active user comments; Trending Posts, showcasing popular content based on user likes; and Editor's Choice, handpicked by the editorial team. Each post is displayed as a card with a link to the full article, accompanied by engagement metrics like comments and likes. Users can also access the author's profile, promoting community interaction and enhancing the user experience. Additionally, tag links are displayed to showcase posts from various categories, further enhancing content discovery.

### Categories Page

The Category Page on Cool Coders is a dedicated space where users can explore a comprehensive collection of articles grouped by specific tech-related categories. Each category page is thoughtfully organized, presenting users with a wealth of content tailored to their interests. The articles are neatly paginated, with up to six articles displayed per page for easy navigation and efficient content browsing. This design allows users to delve deeply into the topics that intrigue them most, making it a valuable resource for in-depth exploration of various tech-related subjects within the Cool Coders community.

### Post Detail Page

The Post Detail Page on Cool Coders is an immersive experience designed to provide users with in-depth access to an article's content and foster engagement. Here's what users can expect on this page:

1. Article Content: The central focus of the page is the article itself. Users can read the full content of the post, gaining insights into the topic, industry trends, or tech-related experiences shared by the author.
2. Comments Section: A dedicated comments section accompanies the article, displaying all user-generated comments related to the post. Users can participate in discussions, share their thoughts, and engage with the Cool Coders community by leaving comments or replies.
3. Comment Form: Below the comments section, a user-friendly comment form is readily available. Users can easily contribute to the conversation by typing and submitting their comments, which will appear alongside existing discussions.
4. Popular Posts in Category: To encourage further exploration within the same category, the page also showcases a selection of popular posts from the related category. This feature helps users discover additional relevant content, offering a seamless navigation experience.

The Post Detail Page serves as a hub for knowledge sharing and community interaction, ensuring that users not only have access to insightful content but can also actively engage, discuss, and explore more related posts within the category.

### Profile Page

The Profile Page on Cool Coders is an essential space for users to showcase their tech passions and contributions while also gaining insights into their own engagement within the community. Here's what you'll find on a user's profile:

#### Profile Info

1. Username, First Name and Last Name: Users' first and last names, adding a personal touch to their profiles.
2. Bio: A brief bio or description, allowing users to share more about themselves, their interests, or their professional background.
3. Email Address: The user's contact information, enabling communication with other community members.
4. Member Since:The date the user joined Cool Coders, providing a sense of their tenure within the community.

#### Post Info

1. Total Posts: The cumulative number of posts by the user.
2. Total Likes: The cumulative number of likes received by the user across all their posts, reflecting their content's popularity.
3. Total Comments: The overall count of comments made on the user's posts, indicating engagement and interaction with their content.
4. Total Favourites: The cumulative number of favourited posts of the user.
5. Posts: A paginated list of all the users posts
6. Favourites: A paginated list of all the users favourite posts

If the user is viewing their own profile, they have the ability to edit their posts and profile information, ensuring their profile remains up-to-date and their posts are well-maintained.
Users can also access their list of favorited posts, making it convenient to revisit their favorite content.

The Profile Page serves as an information-rich hub, where users can introduce themselves, showcase their contributions, and gain insights into their impact within the Cool Coders community. It fosters a sense of belonging and encourages active participation while enabling users to manage their own content and profile details.

### Add/Edit Post Page

The Add/Edit Post Page on Cool Coders is a versatile platform that empowers users to craft and refine their tech-related articles with ease. Here's what this feature offers:

1. Create and Edit Articles: Users can compose new articles or edit existing ones, maintaining control over their content and insights.
2. Title: A clear and captivating title helps users convey the article's main theme, attracting readers and providing a structured entry point.
3. Content: The page provides a dedicated space for users to input the full content of their articles, allowing for in-depth exploration of tech topics.
4. Excerpt: Users can include a concise and engaging excerpt that provides a preview of the article's key points, enticing readers to delve further.
5. Image: The option to upload an image enhances visual appeal and adds context to the article, creating a more engaging reading experience.
   6.Category: Users can assign their articles to specific tech-related categories, ensuring they are appropriately classified and easily discoverable by others.
6. Delete Post Button (Edit Mode): In edit mode, users have the ability to delete their posts using a dedicated "Delete Post" button, granting full control over their content's management.

The Add/Edit Post Page is a user-friendly tool designed to facilitate content creation and refinement, enabling users to share their tech insights and knowledge within the Cool Coders community.

### Edit Profile Page

The Edit User Profile Page on Cool Coders is a user-centric feature that empowers users to manage and customize their personal information seamlessly. Here's what this page offers:

1. Edit User Profile Information: Users can conveniently update their First Name, Last Name, Username, Email, and Bio, ensuring that their profile accurately reflects their identity and interests.
   2.Password Change: This feature allows users to modify their password, enhancing account security and ensuring they maintain control over their login credentials.
2. Account Deletion: For those who choose to do so, the option to delete their account is available, allowing users to exercise control over their Cool Coders membership. Users will be prompted to confirm their action with a modal popup.

The Edit User Profile Page ensures a personalized and adaptable user experience, enabling individuals to make changes to their profile and account settings as needed while prioritizing their data security and personalization options.

### Sign Up page

This page comprises a form with fields for entering a username and password. Beneath the form is the sign up button which submits the form. Below the form is a redirect to the register page if the user does not have an account. Click the remember me checkbox to remain logged in as a session.

### Sign In page

It features a form with fields for inputting name, email, username, password, and password confirmation. Underneath the form, there is a link to log in for users with existing accounts, followed by the signup button. After signup, users receive a welcome email at the provided email address and are then directed to the profile page update form, where they can personalize their profiles.

### Sign out page

Upon clicking the "log out" link in the navigation, users are directed to a confirmation page. This page includes a cautionary message and two buttons: one for returning and one for logging out.

#### Article Preview Card

The Article Card on Cool Coders is a concise yet informative snapshot of a user's post within a specific tech-related category. It includes the following key elements:

1. Author Profile: A visual representation of the author's profile picture and username, providing a quick way to identify the content creator.
2. Likes: The number of likes the post has received, offering a sense of its popularity and engagement.
3. Comments: The count of comments on the post, indicating the level of community discussion and interaction.
4. Category: Clearly indicating the tech category to which the post belongs, helping users quickly identify the content's subject matter.
5. Post Date: The date when the article was published, offering a reference for the recency of the content.
6. Title: The headline of the post, serving as a captivating entry point to the article's content.
7. Excerpt: A brief summary or excerpt from the article, providing users with a glimpse of the post's key points and enticing them to read further.

Together, these elements create a Category Card that is both visually appealing and informative, allowing users to make informed choices about which posts to explore further within a specific category.

### Notification Messages

Notification messages were user every time the user performs CRUD operation, sign in, and sign out.

### Confirmation Modal

This modal appears whenever a users is performing a delete CRUD operation. It ensures the user must confirm their action before the permanent deletion of an item/account
