// Function to show the pop-up
function showPopup() {
    document.getElementById('popup').style.display = 'block';
}

// Function to hide the pop-up
function hidePopup() {
    document.getElementById('popup').style.display = 'none';
}

// Event listener for the close button
document.getElementById('closePopup').addEventListener('click', hidePopup);

// Optionally, you can show the popup when the page loads or based on some condition
window.onload = showPopup; // Uncomment to show the popup on page load
