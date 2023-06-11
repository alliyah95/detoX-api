let id = 1;
const content =
    "I will support your decisions babies  but sorry to say  Mar Roxas is not fit to be president! ??";
const interval = 500;

function sendAPIRequest() {
    setInterval(() => {
        fetch(`http://127.0.0.1:8000/api/v1/detect?id=${id}&content=${content}`)
            .then((response) => response.json())
            .then((data) => {
                // Process the response data
                console.log(data);
            })
            .catch((error) => {
                // Handle any errors that occur during the API request
                console.error("Error:", error);
            });
        id++;
    }, interval);
}

sendAPIRequest();
