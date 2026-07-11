// Display welcome message
window.onload = function () {
    console.log("AI-Based Student Career Guidance System Loaded");
};

// Form validation
function validateForm() {

    let inputs = document.querySelectorAll("input[required], select[required]");

    for (let i = 0; i < inputs.length; i++) {

        if (inputs[i].value.trim() === "") {

            alert("Please fill all required fields.");

            inputs[i].focus();

            return false;
        }
    }

    return true;
}

// Confirm before logout
function confirmLogout() {

    return confirm("Are you sure you want to logout?");
}

// Show success message after adding study task
function taskAdded() {
    alert("Study task added successfully!");
}

// Highlight active navigation link
document.addEventListener("DOMContentLoaded", function () {

    let links = document.querySelectorAll("nav a");

    links.forEach(link => {

        if (link.href === window.location.href) {

            link.style.color = "yellow";
            link.style.fontWeight = "bold";

        }

    });

});