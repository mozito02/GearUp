
# GearUp: A Platform for Student Projects

**GearUp** is a web application designed to provide a collaborative space for school students to showcase their projects. Students can easily create, edit, and delete their posts, share links, and inspire each other within a vibrant community.

### Visit the Website :  https://gearup-deploy.onrender.com/

## Purpose

GearUp aims to foster creativity and collaboration among students by offering a platform where they can:

- **Showcase Projects**: Post their projects with titles, descriptions, links, and images.
- **Edit Posts**: Modify their existing posts to update information or images.
- **Delete Posts**: Remove posts if necessary.
- **Manage Profiles**: Create and manage user accounts.
- **Authenticate**: Secure login and registration for user authentication.
- **Experience Responsiveness**: Enjoy a seamless experience across various devices and screen sizes.

## Features

- **Project Posting**: 
  - Title
  - Description
  - Project Link
  - Image
- **Post Editing**: Modify title, description, link, or image of existing posts.
- **Post Deletion**: Remove posts from the platform.
- **User Accounts**: Create and manage user profiles.
- **Login and Registration**: Secure authentication for users.
- **Responsive Design**: Optimized for all device sizes.
- **Flowbite Components**: Modern UI components for a sleek interface.

## Technology Stack

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript (with Flowbite components)
- **Database**: SQLite3

## Installation and Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/mozito02/GearUp.git
   cd GearUp
   ```

2. **Set Up Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: `venv\Scripts\activate`
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```


5. **Run the Application:**

   ```bash
   python manage.py runserver
   ```

   Open your browser and navigate to `http://127.0.0.1:8000/` to use the application.

## Contributing

Contributions to GearUp are welcome! Please follow these guidelines:

1. **Fork the Repository.**
2. **Create a New Branch** for your feature or bug fix:
   ```bash
   git checkout -b feature/your-feature
   ```
3. **Make Your Changes** and commit them:
   ```bash
   git add .
   git commit -m "Add new feature or fix bug"
   ```
4. **Push Your Changes** to your fork:
   ```bash
   git push origin feature/your-feature
   ```
5. **Submit a Pull Request** to the main repository.

## License

GearUp is released under the [MIT License](LICENSE). See the LICENSE file for details.

