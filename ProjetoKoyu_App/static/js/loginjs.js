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

        // Validação simples: Verifica se os campos estão preenchidos
        if (!username || !password) {
            alert("Por favor, preencha todos os campos.");
            return;
        }

        // Simulação de autenticação (Substitua por chamada AJAX se necessário)
        if (username === "admin" && password === "1234") {
            alert("Login realizado com sucesso!");
            // Redireciona o utilizador (ajuste o URL conforme necessário)
            window.location.href = "/dashboard";
        } else {
            alert("Utilizador ou palavra-passe incorretos.");
        }
    });

    // Adiciona um efeito hover no botão de login
    loginButton.addEventListener("mouseover", function () {
        loginButton.style.transform = "scale(1.1)";
        loginButton.style.transition = "transform 0.2s";
    });

    loginButton.addEventListener("mouseout", function () {
        loginButton.style.transform = "scale(1)";
    });
});
