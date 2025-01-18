document.addEventListener("DOMContentLoaded", () => {
    const switchElement = document.getElementById("switch");
    const circle = document.getElementById("circle");
    const textoSuperior = document.getElementById("texto-superior");
    const textoInferior = document.getElementById("texto-inferior");
    const campoNIF = document.getElementById("campo-nif");
    const campoContacto = document.getElementById("campo-contacto");
    const tipoUtilizador = document.getElementById("tipo-utilizador");
    const btnCancelar = document.getElementById("btnCancelar");

    
    // Define o estado inicial com base no valor de ut_tipo
    let isUtilizador = tipoUtilizador.value === "Utilizador";

    const atualizarEstado = () => {
        if (isUtilizador) {
            // Configuração para Utilizador
            circle.style.left = "2.5px";
            textoSuperior.classList.add("ativo");
            textoInferior.classList.remove("ativo");
            campoNIF.style.display = "flex";
            campoContacto.classList.remove("centered");
            tipoUtilizador.value = "Utilizador";
        } else {
            // Configuração para Gestor
            circle.style.left = "42.5px";
            textoSuperior.classList.remove("ativo");
            textoInferior.classList.add("ativo");
            campoNIF.style.display = "none";
            campoContacto.classList.add("centered");
            tipoUtilizador.value = "Gestor";
        }
    };

    // Inicializa o seletor com base no tipo de utilizador
    atualizarEstado();

    // Alterna o estado ao clicar no switch
    switchElement.addEventListener("click", () => {
        isUtilizador = !isUtilizador;
        atualizarEstado();
    });

    // Redireciona para listar utilizadores ao clicar no botão Cancelar
    if (btnCancelar) {
        btnCancelar.addEventListener("click", () => {
            const url = btnCancelar.getAttribute("data-url");
            window.location.href = url;
        });
    }
});