import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ReviewForm = () => {
  const [review, setReview] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault(); 

    const cancelTokenSource = axios.CancelToken.source();

    try {
      const response = await axios.post(`${process.env.REACT_APP_BACKEND_URL}/analyze-sentiment`, { review }, { cancelToken: cancelTokenSource.token });

      console.log('Sentiment Analysis Result:', response.data);
      setReview('');
    } catch (error) {
      console.error('Error submitting review:', error);
    }

    return () => {
      cancelTokenSource.cancel();
    };
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