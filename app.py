from flask import Flask, render_template, request
import pickle
import os
import numpy as np

app = Flask(__name__)

# Load the data
try:
    with open('popular.pkl', 'rb') as f:
        popular_df = pickle.load(f)
    # Load other necessary data
    with open('pt.pkl', 'rb') as f:
        pt = pickle.load(f)
    with open('similarity_scores.pkl', 'rb') as f:
        similarity_scores = pickle.load(f)
    with open('books.pkl', 'rb') as f:
        books = pickle.load(f)
except (FileNotFoundError, pickle.UnpicklingError) as e:
    popular_df = pt = similarity_scores = books = None
    print(f"Error loading data: {e}")


@app.route('/')
def index():
    # Check if popular_df is loaded successfully
    if popular_df is not None:
        return render_template(
            "index.html",
            book_name=list(popular_df['Book-Title'].values),
            author=list(popular_df['Book-Author'].values),
            image=list(popular_df['Image-URL-M'].values),
            votes=list(popular_df['num_ratings'].values),
            rating=list(popular_df['avg_rating'].values)
        )
    else:
        return "Error: Data could not be loaded."

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input')

    if user_input not in pt.index:
        return "Error: Book not found in recommendations."

    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[0:5]
                                                     # if list is [0:5] it will include book it self also

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)

    # Pass `data` to `recommend.html`
    return render_template('recommend.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
