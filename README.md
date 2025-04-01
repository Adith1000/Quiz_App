# Quiz App

A web-based quiz application built with Flask for the backend and HTML, CSS, and JavaScript for the view. This project follows the MVC (Model-View-Controller) architecture to ensure a clean separation of concerns. The app leverages several powerful technologies, including Tesseract for text extraction, Supabase for database management, and Groq for querying content.

## Table of Contents

- [Overview](#overview)
- [Technology Stack](#technology-stack)
- [Architecture](#architecture)
- [Installation](#installation)

## Overview

The Quiz App allows users to upload a PDF, processes it using Tesseract to extract text, and then generates a quiz based on the extracted content. The user answers quiz questions using a dynamic interface, and the application records the score and answers.

## Technology Stack

### Backend
- **Flask:** A lightweight web framework for Python used to create the server and handle HTTP requests.
- **Tesseract:** An OCR engine to process PDF files and extract text.
- **Supabase:** Provides a managed PostgreSQL database and API services for storing quiz data.
- **Groq:** Utilized for efficient content querying from the database.

### Frontend
- **HTML/CSS:** For structuring and styling the user interface.
- **JavaScript:** For dynamic content updates and client-side logic.

## Architecture

The project follows the MVC (Model-View-Controller) pattern:

- **Model:** Contains data-related logic, including question data, user answers, and interactions with Supabase.
- **View:** Consists of HTML templates, CSS, and JavaScript files responsible for rendering the UI and handling user interactions.
- **Controller:** Flask routes and functions manage the application logic, process user input, update the model, and determine which view to render.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/quiz-app.git
   cd quiz-app
