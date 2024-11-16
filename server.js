// server.js
const express = require('express');
const app = express();
const port = 3000;

// Define the route
app.get('/majesty', (req, res) => {
  const response = {
    title: "The Unparalleled Majesty of 'The Lord of the Rings'",
    subtitle: "Archmage",
    description: "Valar",
    details: {
      link: "https://lotr.fandom.com/wiki/Main_Page",
      text: "wiki here"
    }
  };
  
  // Send the JSON response
  res.json(response);
});

// Start the server
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});

module.exports = app; // Export the app for testing

