document.addEventListener("DOMContentLoaded", function () {
    const loginForm = document.querySelector("form");
    const usernameField = document.querySelector("input[name='username']");
    const passwordField = document.querySelector("input[name='password']");
    const loginButton = document.querySelector("button[type='submit']");

    // Evento de submissão do formulário
    loginForm.addEventListener("submit", function (event) {
        // Evita o envio automático do formulário
        event.preventDefault();
    
        const username = usernameField.value.trim();
        const password = passwordField.value.trim();
    
        if (username === "admin" && password === "1234") {
            alert("Login realizado com sucesso!");
            window.location.href = "/dashboard";
        } else {
            alert("Utilizador ou palavra-passe incorretos.");
        }
    });
    
});
