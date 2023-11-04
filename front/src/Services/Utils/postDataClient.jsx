import axios from 'axios';
import pathDefinition from './status';
// Create a reusable function for making POST requests
export async function postDataFromApi(path, data) {
  try {
    // Define your API base URL
    const apiUrl = pathDefinition(path); // Replace with your API base URL
    // Make the POST request with data
    const response = await axios.post(apiUrl, data, {
      withCredentials: true, // Include credentials (cookies) if needed
      headers: {
        'Content-Type': 'application/json', // Set the content type of your request
      },
    });

    // Return the response data
    return response.data;
  } catch (error) {
    // Handle errors here
    throw error;
  }
}
