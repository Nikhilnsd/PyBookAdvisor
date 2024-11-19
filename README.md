# PyBookAdvisor

**PyBookAdvisor** is a book recommendation system designed to provide a personalized and engaging experience for book enthusiasts. Using Python and Flask, it combines collaborative filtering, content similarity, and popularity-based algorithms to suggest books tailored to user preferences. The system integrates a book dataset and offers a sleek, responsive front-end built with **HTML** and **Bootstrap**, ensuring usability across devices.

---

## Features

### 📚 Personalized Recommendations:
- Delivers book suggestions based on collaborative filtering and content similarity.
- Adjusts recommendations to match user preferences dynamically.

### ⭐ Popularity-Based Suggestions:
- Highlights trending and highly-rated books.

### 💻 Responsive User Interface:
- Modern, user-friendly design with Bootstrap.
- Optimized for desktop, tablet, and mobile devices.

### 🔍 Detailed Book Information:
- Displays key metadata: book title, author, and average rating.

---

## Dataset Overview

### Files Used:
1. **Books.csv**:
   - Contains details about books, including title, author, year, and image URLs.
2. **Users.csv**:
   - User demographic details like ID, location, and age.
3. **Ratings.csv**:
   - User ratings of books, forming the backbone of the recommendation system.

### Data Insights:
- **Books Dataset**: `(271,360, 8)` entries with minimal missing data.
- **Users Dataset**: `(278,858, 3)` entries; `Age` column contains 110,762 null values.
- **Ratings Dataset**: `(1,149,780, 3)` entries with no null values.

---

## Recommendation Algorithms

### Popularity-Based:
- Books are ranked based on the number of ratings and their average score.
- Suitable for general users and discovering trending books.

### Content-Based:
- Uses **cosine similarity** to identify books with similar attributes (title, genre, etc.).
- Ensures personalized suggestions tailored to user input.

---

## How It Works

### Input Example
The user selects or searches for a book they like.  
Example input: **"1984"** by George Orwell.

### Processing
1. **Content Similarity**: Finds books similar to the input book based on features like title and metadata.
2. **Popularity-Based**: Retrieves top-rated and frequently reviewed books.

### Output Example
The system recommends books based on the input.

#### **Recommendations for "1984":**
1. *Animal Farm* by George Orwell  
2. *Brave New World* by Aldous Huxley  
3. *The Handmaid’s Tale* by Margaret Atwood  
4. *Fahrenheit 451* by Ray Bradbury  

#### Sample Output UI:


![alt text](images/Top50.png)
![alt text](<images/Harry Potter.png>)
![alt text](<images/Life of Pi.png>)
---

## Technologies Used

### Back-End:
- **Python**: Flask framework for app logic.
- **Pandas, NumPy**: Data manipulation and preprocessing.
- **Scikit-learn**: Computing similarity and building recommendation algorithms.

### Front-End:
- **HTML, CSS, JavaScript**: Core structure and interactivity.
- **Bootstrap**: Responsive and visually appealing UI.

### Database:
- A structured book dataset with user ratings.

---

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Flask
- Required libraries: Pandas, NumPy, Scikit-learn


# test
