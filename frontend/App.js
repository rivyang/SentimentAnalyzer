import React, { useEffect, useState } from 'react';

const retrieveHistoryFromLocalStorage = () => {
  const savedReviews = localStorage.getItem('reviewHistory');
  return savedReviews ? JSON.parse(savedReviews) : [];
};

function ReviewHistory() {
  const [reviewHistory, setReviewHistory] = useState([]);

  useEffect(() => {
    const loadedReviewHistory = retrieveHistoryFromLocalStorage();
    setReviewHistory(loadedReviewHistory);
  }, []);

  if (reviewHistory.length === 0) {
    return (
      <div>
        <h2>Review History</h2>
        <p>No reviews yet.</p>
      </div>
    );
  }

  return (
    <div>
      <h2>Review History</h2>
      <ul>
        {reviewHistory.map((reviewEntry, index) => {
          const displayText = `${reviewEntry.review} - Sentiment: ${reviewEntry.sentiment}`;
          return <li key={index}>{displayText}</li>;
        })}
      </ul>
    </div>
  );
}

export default ReviewHistory;