import React from 'react';
import { Link } from 'react-router-dom';
import './Header.css';

const Header = () => {
  const submitReviewPath = process.env.REACT_APP_SUBMIT_REVIEW_PATH;
  const viewResultsPath = process.env.REACT_APP_VIEW_RESULTS_PATH;

  return (
    <header className="headerContainer">
      <div className="logo">
        <h1>App Name</h1>
      </div>
      <nav>
        <ul>
          <li><Link to={submitReviewPath}>Submit Review</Link></li>
          <li><Link to={viewResultsPath}>View Results</Link></li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;