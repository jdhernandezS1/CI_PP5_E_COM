export function pathDefinition(path) {
    // const apiUrl = `https://markexpress-a63194cbc386.herokuapp.com/api/${path}`; // Remote Server
    const apiUrl = `http://127.0.0.1:8000/api/${path}`; // Local Server
    return apiUrl;
}
export default pathDefinition;
