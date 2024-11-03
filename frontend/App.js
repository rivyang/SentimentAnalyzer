import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Header from './components/Header';
import SubmitReview from './components/SubmitReview';
import SentimentResults from './components/SentimentResults';
import ReviewHistory from './components/ReviewHistory'; // Assuming you create this new component

function App() {
  return (
    <Router>
      <div>
        <Header />
        <Switch>
          <Route path="/submit-review">
            <SubmitReview />
          </Route>
          <Route path="/results">
            <SentimentResults />
          </Route>
          <Route path="/history">
            <ReviewHistory /> {/* This is the new route for the review history */}
          </Route>
          <Route path="/">
            <SubmitReview />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

export default App;
```

```javascript
// components/ReviewHistory.js
import React, { useEffect, useState } from 'react';

function ReviewHistory() {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    // Assuming you're storing the history in local storage for simplicity
    const savedHistory = JSON.parse(localStorage.getItem('reviewHistory')) || [];
    setHistory(savedHistory);
  }, []);

  return (
    <div>
      <h2>Review History</h2>
      <ul>
        {history.map((entry, index) => (
          <li key={index}>{entry.review} - Sentiment: {entry.sentiment}</li>
        ))}
      </ul>
    </div>
  );
}

export default ReviewHistory;