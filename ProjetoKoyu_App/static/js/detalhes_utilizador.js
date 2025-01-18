document.addEventListener("DOMContentLoaded", () => {
    const botaoHistorico = document.getElementById("botao-historico");
    const textoHistorico = document.getElementById("texto-historico");
    const switchElement = document.getElementById("switch");
    const textoSuperior = document.getElementById("texto-superior");
    const textoInferior = document.getElementById("texto-inferior");
    const historicoContainer = document.querySelector(".historico-treino-container");
    const btnCancelar = document.getElementById("btnCancelar");
    const btnEditar = document.getElementById("btnEditar");

    let isAtivo = false;
    let isUtilizador = true;

    // Verificar o tipo atual (Utilizador ou Administrador) e ajustar visibilidade do histórico
    const atualizarVisibilidadeHistorico = () => {
        if (isUtilizador) {
            historicoContainer.style.display = "flex";
        } else {
            historicoContainer.style.display = "none";
        }
    };

    // Alternar entre Utilizador e Administrador
    switchElement.addEventListener("click", () => {
        isUtilizador = !isUtilizador;
        if (isUtilizador) {
            textoSuperior.classList.add("ativo");
            textoInferior.classList.remove("ativo");
        } else {
            textoSuperior.classList.remove("ativo");
            textoInferior.classList.add("ativo");
        }
        atualizarVisibilidadeHistorico();
    });

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