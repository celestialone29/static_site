// test/majesty.test.js
const request = require('supertest');
const app = require('../server'); // Import the app you created

describe('GET /majesty', () => {
  it('should return a JSON object with the correct content', async () => {
    const res = await request(app).get('/majesty');
    
    // Check that the status code is 200
    expect(res.status).toBe(200);
    
    // Check that the response body is a JSON object with expected content
    expect(res.body).toEqual({
      title: "The Unparalleled Majesty of 'The Lord of the Rings'",
      subtitle: "Archmage",
      description: "Valar",
      details: {
        link: "https://lotr.fandom.com/wiki/Main_Page",
        text: "wiki here"
      }
    });
  });
});

