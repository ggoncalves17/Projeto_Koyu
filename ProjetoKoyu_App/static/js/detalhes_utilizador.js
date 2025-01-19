document.addEventListener("DOMContentLoaded", () => {
    const botaoHistorico = document.getElementById("botao-historico");
    const textoHistorico = document.getElementById("texto-historico");
    const switchElement = document.getElementById("switch");
    const textoSuperior = document.getElementById("texto-superior");
    const textoInferior = document.getElementById("texto-inferior");
    const historicoContainer = document.querySelector(".historico-treino-container");
    const btnCancelar = document.getElementById("btnCancelar");
    const btnEditar = document.getElementById("btnEditar");
    const tipoUtilizador = document.getElementById("tipo-utilizador").value;
    const circle = document.getElementById("circle");
    const switchBackground = document.querySelector('.switch-background');
    const iconeAtual = document.getElementById("icone-atual");

    if (tipoUtilizador == "Utilizador") {
        textoSuperior.classList.add("ativo");
        textoInferior.classList.remove("ativo");
        circle.style.left = "2.5px";
    } 
    else {
        textoSuperior.classList.remove("ativo");
        textoInferior.classList.add("ativo");
        circle.style.left = "42.5px";
        iconeAtual.innerHTML = `
                <svg width="15" height="15" viewBox="0 0 32 36" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M16 18C17.78 18 19.5201 17.4722 21.0001 16.4832C22.4802 15.4943 23.6337 14.0887 24.3149 12.4442C24.9961 10.7996 25.1743 8.99002 24.8271 7.24419C24.4798 5.49836 23.6226 3.89472 22.364 2.63604C21.1053 1.37737 19.5016 0.520203 17.7558 0.172937C16.01 -0.17433 14.2004 0.00389957 12.5558 0.685088C10.9113 1.36628 9.50571 2.51983 8.51677 3.99987C7.52784 5.47991 7 7.21997 7 9C7 11.387 7.94821 13.6761 9.63604 15.364C11.3239 17.0518 13.6131 18 16 18ZM22.736 20.292L19.375 33.75L17.125 24.188L19.375 20.251H12.625L14.875 24.189L12.625 33.752L9.264 20.292C6.83994 20.4 4.55071 21.4379 2.87203 23.19C1.19334 24.942 0.254282 27.2735 0.25 29.7L0.25 32.625C0.250265 33.52 0.60593 34.3783 1.23881 35.0112C1.87169 35.6441 2.72998 35.9997 3.625 36H28.375C29.27 35.9997 30.1283 35.6441 30.7612 35.0112C31.3941 34.3783 31.7497 33.52 31.75 32.625V29.7C31.7457 27.2735 30.8067 24.942 29.128 23.19C27.4493 21.4379 25.1601 20.4 22.736 20.292Z" fill="black"/>
                </svg>
            `;
    }
    
    let isAtivo = false;

    // Verificar o tipo atual (Utilizador ou Administrador) e ajustar visibilidade do histórico
    const atualizarVisibilidadeHistorico = () => {
        if (tipoUtilizador == "Utilizador") {
            historicoContainer.style.display = "flex";
        } else {
            historicoContainer.style.display = "none";
        }
    };
    
    // Alternar estado do histórico de treino (apenas quando visível)
    botaoHistorico.addEventListener("click", () => {
        if (!isAtivo) {
            botaoHistorico.classList.add("ativo");
            textoHistorico.textContent = "";
        } else {
            botaoHistorico.classList.remove("ativo");
            textoHistorico.textContent = "Histórico de Treino";
        }
        isAtivo = !isAtivo;
    });

    // Inicializar a visibilidade do botão com base no estado inicial
    atualizarVisibilidadeHistorico();

    // Redireciona para listar utilizadores ao clicar no botão Editar
    if (btnEditar) {
        btnEditar.addEventListener("click", () => {
            const url = btnEditar.getAttribute("data-url");
            window.location.href = url;
        });
    }

    // Redireciona para listar utilizadores ao clicar no botão Cancelar
    if (btnCancelar) {
        btnCancelar.addEventListener("click", () => {
            const url = btnCancelar.getAttribute("data-url");
            window.location.href = url;
        });
    }
});