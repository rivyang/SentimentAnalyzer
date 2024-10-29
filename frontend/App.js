import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Header from './components/Header';
import SubmitReview from './components/SubmitReview';
import SentimentResults from './components/SentimentResults';

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
          <Route path="/">
            <SubmitReview />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

export default App;