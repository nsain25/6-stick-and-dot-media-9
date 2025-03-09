# 6-stick-and-dot-media-9

# Task 1: Prepare Datasets & Document the Process

## Objective
To collect and prepare multiple datasets while documenting the process, ensuring they are structured, cleaned, and stored appropriately.

## Dataset Requirements & Collection Process

### 1️⃣ 1000 Research Papers on Varied Niches
- **Niches**: AI, cybersecurity, climate change, finance, etc.
- **Sources**: arXiv, Semantic Scholar, Google Scholar
- **Metadata Extracted**:
  - Title
  - Abstract
  - Authors
  - Publication year
- **Storage Format**: CSV, JSON, or plain text

### 2️⃣ 5000 Study Material PDFs for Trending Skills
- **Trending Skills**: Data Science, AI, Blockchain, UI/UX, etc.
- **Sources**: Coursera, Udemy, MIT OpenCourseWare, GitHub
- **Processing**:
  - Scrape high-quality PDFs
  - Extract metadata
  - Store in structured format

### 3️⃣ 5000 Food Images Scraped from Social Media
- **Sources**: Instagram, Twitter, Pinterest APIs
- **Hashtags Used**: #FoodPhotography, #HomeCooking
- **Processing**:
  - Apply image quality filters
  - Remove irrelevant images
  
### 4️⃣ 1000 Whitepapers on Varied Niches
- **Sources**: Forrester, Gartner, Company Reports, GitHub Repos
- **Processing**:
  - Extract metadata
  - Store in structured format

## Tools & Technologies
- **Python Libraries**: requests, BeautifulSoup, Selenium, Tweepy, PyPDF2, pdfplumber
- **APIs Used**: arXiv API, Google Scholar API, Instagram API, Twitter API
- **Data Storage**: CSV, JSON, MongoDB

## Deliverables
- Prepared datasets (CSV/JSON)
- Documentation of the data collection process

---

# Task 5: Introspect & Improve the PDF Parser Code

## Objective
Analyze the given PDF parser code and suggest improvements for better efficiency and accuracy.

## Steps for Analysis

### 1️⃣ Review Code Functionality
- Check how the parser extracts text
- Verify handling of structured tables and metadata
- Identify parsing errors (encoding issues, missing data, etc.)

### 2️⃣ Identify Potential Issues
- **Lack of OCR Support**: Implement Tesseract OCR for scanned PDFs
- **Poor Handling of Multi-Column PDFs**: Improve extraction using pdfplumber
- **Inefficient Processing**: Optimize for large PDFs

### 3️⃣ Suggested Improvements
- **Improve Accuracy**: Use PyMuPDF for better text extraction
- **Enhance OCR Capabilities**: Integrate Tesseract-OCR
- **Optimize Performance**: Implement parallel processing
- **Error Handling**: Improve exception handling

## Tools & Technologies
- **Python Libraries**: PyPDF2, pdfplumber, PyMuPDF, Tesseract-OCR

## Deliverables
- Identified issues in the PDF parser
- List of improvements & code enhancements

---

# Task 9: Optimal Delivery Route System

## Objective
Design a logic that assigns optimal routes to delivery vehicles while allowing real-time order allocation.

## Steps to Build the System

### 1️⃣ Define Input Data
- **Orders**: Pickup & drop-off locations, package weight, priority
- **Vehicles**: Capacity, location, speed, fuel efficiency
- **Traffic Conditions**: Real-time updates from Google Maps API

### 2️⃣ Route Optimization Algorithm
- **Techniques Used**:
  - Dijkstra’s Algorithm / A* Algorithm for shortest path
  - Dynamic route updates based on new orders
  - Cost minimization (time, fuel, vehicle capacity usage)

### 3️⃣ Real-Time Order Assignment
- **Process**:
  - Check existing vehicle routes
  - Assign new orders if they match existing routes
  - Dynamically adjust routes if necessary

### 4️⃣ Technology Stack
- **Routing**: Google Maps API / OpenStreetMap
- **Backend**: Python (Flask/Django)
- **Machine Learning**: ETA Prediction

## Deliverables
- Route Optimization Logic
- Algorithm for dynamic order assignment
- API-based real-time routing

---

# README

## Project Overview
This project includes the implementation and documentation of three major tasks:

1. **Dataset Preparation**: Collection and structuring of research papers, study materials, food images, and whitepapers.
2. **PDF Parser Optimization**: Enhancement of an existing PDF parsing system for improved accuracy and efficiency.
3. **Optimal Delivery Route System**: Development of a route optimization algorithm with real-time order allocation.

## Tasks Covered
### 1️⃣ Dataset Preparation
- Research paper collection from scholarly databases
- Scraping and structuring of educational resources
- Food image collection via social media APIs
- Whitepaper extraction and metadata structuring

### 2️⃣ PDF Parser Enhancement
- OCR support for scanned PDFs
- Improved handling of multi-column PDFs
- Performance optimization and error handling

### 3️⃣ Optimal Delivery Route System
- Implementation of routing algorithms
- Real-time order assignment
- Cost optimization techniques

## Technologies Used
- **Python Libraries**: requests, BeautifulSoup, Selenium, Tweepy, PyPDF2, pdfplumber, PyMuPDF
- **APIs**: arXiv API, Google Scholar API, Instagram API, Twitter API, Google Maps API
- **Databases**: CSV, JSON, MongoDB
- **Backend**: Flask/Django

## How to Use
1. **Dataset Preparation**: Use the provided scripts to scrape and structure datasets.
2. **PDF Parser**: Run the optimized parsing script to extract structured text from PDFs.
3. **Delivery Route System**: Deploy the API-based system for dynamic routing.

## Deliverables
- Structured datasets (CSV/JSON)
- Optimized PDF parser code
- Route optimization algorithm

## Contributors
- **Nandini Sain** and Team

## Contact
For any queries, reach out via GitHub Issues or email.

---
This documentation and README provide a comprehensive overview of the project. Let me know if any refinements are needed!

