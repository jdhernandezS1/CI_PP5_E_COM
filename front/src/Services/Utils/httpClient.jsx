import axios from 'axios';

// Create a reusable function for making GET requests
export async function fetchDataFromApi(path) {
  try {
    // const apiUrl = `https://markexpress-a63194cbc386.herokuapp.com/api/${path}`; // Replace with your API base URL
    const apiUrl = `http://127.0.0.1:8000/api/${path}`; // Replace with your API base URL
    const response = await axios.get(apiUrl, { withCredentials: true });

    // Return the response data
    return response.data;
  } catch (error) {
    // Handle errors here
    throw error;
  }
}
