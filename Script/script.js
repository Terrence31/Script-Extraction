// Function to log the click event details
function logClick(event) {
    const clickDetails = {
        timestamp: new Date().toISOString(),
        element: event.target.tagName,
        textContent: event.target.innerText,
        x: event.clientX,
        y: event.clientY
    };

    // Check if the clicked element is the specific button
    if (event.target.tagName.toLowerCase() === 'button') {
        clickDetails.elementDetails = 'Specific Button';
    }

    console.log("User Clicked:", clickDetails);

    // You can send this data to a server for storage/processing
    // For example, using fetch or XMLHttpRequest
    
    fetch('http://127.0.0.1:5000/log_click', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(clickDetails)
    }).then(response => response.json())
    .then(data => console.log('Server Respose: ',data))
    .then(error => console.log('Error: ',error));

}

// Add event listener to track clicks on the whole document
document.addEventListener('click', logClick);
