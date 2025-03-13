import React, { useState } from 'react';
import axios from 'axios';

const ReviewForm = () => {
  const [review, setReview] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault(); 

    try {
      const response = await axios.post(`${process.env.REACT_APP_BACKEND_URL}/analyze-sentiment`, { review });

      console.log('Sentiment Analysis Result:', response.data);

      setReview('');
    } catch (error) {
      console.error('Error submitting review:', error);
    }
  };

  const handleInputChange = (e) => {
    setReview(e.target.value);
  };

  return (
    <form onSubmit={handleSubmit}>
      <textarea 
        value={review} 
        onChange={handleInputChange} 
        placeholder="Write your review here..."
        required
      />
      <button type="submit">Submit Review</button>
    </form>
  );
};

export default ReviewForm;