import streamlit as st
from reviews.repository import RepositoryReviews


class ServiceReviews:

    def __init__(self):
        self.reviews=RepositoryReviews()

    def get_reviews(self):
        if 'reviews' in st.session_state:
            return st.session_state.reviews
        reviews=self.reviews.get_reviews()
        st.session_state.reviews=reviews
        return reviews

    def create_reviews(self, movie, stars, comment):
        review={'movie': movie, 'stars': stars, 'comment': comment}
        new_reviews=self.reviews.create_reviews(review)
        st.session_state.reviews.append(new_reviews)
        return new_reviews