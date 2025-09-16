# Use Miniconda base image (best for face recognition libraries)
FROM continuumio/miniconda3

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libpq-dev \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Update conda
RUN conda update -n base -c defaults conda

# Install face recognition libraries via conda (most reliable approach)
RUN conda install -c conda-forge -y \
    dlib \
    opencv \
    numpy \
    matplotlib \
    pillow

# Install face_recognition and models via pip (after dlib is ready)
RUN pip install --no-cache-dir \
    face_recognition==1.3.0 \
    face_recognition_models==0.3.0

# Copy requirements
COPY requirements.txt .

# Install remaining Django dependencies
RUN pip install --no-cache-dir \
    Django==5.2.6 \
    asgiref==3.9.1 \
    click==8.2.1 \
    colorama==0.4.6 \
    contourpy==1.3.2 \
    cycler==0.12.1 \
    fonttools==4.59.2 \
    kiwisolver==1.4.9 \
    packaging==25.0 \
    pyparsing==3.2.4 \
    python-dateutil==2.9.0.post0 \
    six==1.17.0 \
    sqlparse==0.5.3 \
    typing_extensions==4.15.0 \
    tzdata==2025.2 \
    whitenoise \
    gunicorn

# Copy project files
COPY . .

# Create necessary directories
RUN mkdir -p media/uploads static staticfiles

# Configure Django settings for static files
ENV DJANGO_SETTINGS_MODULE=web_project.settings

# Collect static files properly
RUN python manage.py collectstatic --noinput --clear || echo "Static files will be served directly"

# Run Django setup with error handling
RUN python manage.py makemigrations || echo "No new migrations"  
RUN python manage.py migrate || echo "Database will be setup on first run"

# Expose port
EXPOSE 8000

# Start Django using Gunicorn with static file serving
CMD ["gunicorn", "web_project.wsgi:application", "--bind", "0.0.0.0:8000", "--timeout", "120", "--workers", "1"]