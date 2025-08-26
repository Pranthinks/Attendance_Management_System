# Face Recognition Attendance System

A web-based attendance management system that uses advanced face recognition technology to automatically track student/employee attendance. Built with Django and deployed on AWS.

## 🚀 Features

- **Real-time Face Detection & Recognition**: Uses CNN and HOG algorithms for accurate face identification
- **Automatic Attendance Tracking**: Records check-in and check-out times automatically
- **Student Registration**: Register new users with face encoding storage
- **Attendance Analytics**: View daily attendance records and absent students
- **Admin Dashboard**: Manage users, attendance records, and absentee tracking
- **Cloud Deployment**: Fully deployed on AWS for scalability and reliability

## 🛠️ Technology Stack

- **Backend**: Django (Python)
- **Face Recognition**: 
  - OpenCV for image processing
  - dlib for face detection
  - face_recognition library with CNN and HOG models
- **Database**: Django ORM (SQLite/PostgreSQL)
- **Frontend**: HTML, CSS, JavaScript with camera integration
- **Deployment**: AWS (Amazon Web Services)
- **Image Processing**: NumPy, Matplotlib

## 📋 Prerequisites

Before running this project, make sure you have:

- Python 3.8+
- Django 4.x
- OpenCV
- dlib
- face_recognition
- NumPy
- A webcam or camera for face capture

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd face-recognition-attendance
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   pip install opencv-python
   pip install dlib
   pip install face-recognition
   pip install numpy
   pip install matplotlib
   ```

4. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

## 🎯 How It Works

### Face Recognition Algorithm
The system uses two powerful algorithms:
- **HOG (Histogram of Oriented Gradients)**: For initial face detection
- **CNN (Convolutional Neural Network)**: For accurate face encoding and recognition

### Process Flow
1. **Registration**: Students register by capturing their face image
2. **Face Encoding**: The system creates a unique 128-dimensional face encoding
3. **Storage**: Face encodings are stored in the database
4. **Attendance**: When taking attendance, the system:
   - Captures live camera feed
   - Detects faces using HOG algorithm
   - Generates face encodings using CNN
   - Compares with stored encodings (tolerance: 0.4)
   - Records attendance with timestamp

## 📱 Usage

### For Students/Employees:
1. **Registration**: Visit `/register` and capture your face image with your details
2. **Attendance**: Visit `/attendance` and look into the camera for automatic recognition

### For Administrators:
1. Access admin panel at `/admin`
2. View all attendance records at `/storage`
3. Check daily absentees at `/absenties`
4. View complete absentee history at `/absentrecord`

## 🏗️ Project Structure

```
face-recognition-attendance/
├── home/
│   ├── models.py          # Database models (User, Attendance, Absentie)
│   ├── views.py           # Core logic and face recognition
│   ├── urls.py            # URL routing
│   ├── admin.py           # Admin panel configuration
│   └── apps.py            # App configuration
├── templates/
│   ├── home.html          # Landing page
│   ├── register.html      # Student registration
│   ├── attendance.html    # Attendance marking
│   ├── storage.html       # Attendance records
│   ├── absenties.html     # Daily absentees
│   └── absentrecord.html  # Absentee history
└── manage.py
```

## 📊 Database Models

### User Model
- `name`: Student/Employee name
- `timein`: Check-in time
- `timeout`: Check-out time
- `date`: Attendance date

### Attendance Model
- `nam`: Registered user name
- `phon`: Phone number
- `emaill`: Email address
- `image`: Face encoding (128-dimensional array)

### Absentie Model
- `namee`: Name of absent person
- `dat`: Date of absence

## ⚙️ Configuration

### Face Recognition Settings
- **Tolerance**: 0.4 (adjustable for recognition sensitivity)
- **Upsampling**: 2x for better face detection
- **Model**: Large model with 10 jitters for accuracy
- **Color Space**: RGB for processing

### Security Features
- Face encodings are stored as JSON arrays
- Admin panel restricted access
- Input validation for all forms

## 🌐 AWS Deployment

This project is successfully deployed on AWS with:
- **EC2**: For hosting the Django application
- **RDS**: For database management (if using PostgreSQL)
- **S3**: For static file storage
- **Elastic Load Balancer**: For traffic distribution
- **CloudWatch**: For monitoring

## 🚨 Troubleshooting

### Common Issues:
1. **Camera not working**: Ensure browser permissions for camera access
2. **Face not recognized**: Adjust lighting conditions and face positioning
3. **Installation errors**: Make sure all dependencies are correctly installed
4. **Database errors**: Run migrations after model changes

### Performance Tips:
- Ensure good lighting for better face detection
- Position face clearly in camera frame
- Avoid multiple faces in frame during attendance

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Praneeth**
- Database Administrator Access
- Full system architecture and implementation

## 📞 Support

For support and queries:
- Create an issue in this repository
- Contact the development team

## 🔮 Future Enhancements

- [ ] Mobile app integration
- [ ] Real-time notifications
- [ ] Advanced analytics dashboard
- [ ] Multi-location support
- [ ] API endpoints for external integration
- [ ] Bulk user registration
- [ ] Export attendance reports

---

**Note**: This system uses state-of-the-art face recognition technology. Ensure proper privacy compliance and user consent before deployment in production environments.
