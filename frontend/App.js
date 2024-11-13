import React, { useEffect, useState } from 'react';

const readHistoryFromLocalStorage = () => {
  const savedHistory = localStorage.getItem('reviewHistory');
  return savedHistory ? JSON.parse(savedHistory) : [];
};

function ReviewHistory() {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    const savedHistory = readHistoryFromLocalStorage();
    setHistory(savedHistory);
  }, []);

  if (history.length === 0) {
    return <div><h2>Review History</h2><p>No reviews yet.</p></div>;
  }

  return (
    <div>
      <h2>Review History</h2>
      <ul>
        {history.map((entry, index) => {
          const sentimentDisplayText = `${entry.review} - Sentiment: ${entry.sentiment}`;
          return <li key={index}>{sentimentDisplayText}</li>;
        })}
      </ul>
    </div>
  );
}

export default ReviewHistory;