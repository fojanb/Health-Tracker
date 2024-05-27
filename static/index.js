let baseURL = "http://127.0.0.1:5000"
document.getElementById("username").addEventListener("change", (e) => {
    let username = e.target.value;
    document.querySelector("form").addEventListener("submit", () => {
        document.querySelector("form").action = `${baseURL}/repositories?username=${username}`;
    })
})