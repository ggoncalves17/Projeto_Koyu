document.addEventListener("DOMContentLoaded", () => {
    const circle = document.getElementById("circle");
    const textoSuperior = document.getElementById("texto-superior");
    const textoInferior = document.getElementById("texto-inferior");
    const campoNIF = document.getElementById("campo-nif");
    const campoContacto = document.getElementById("campo-contacto");
    const tipoUtilizador = document.getElementById("tipo-utilizador"); // Campo oculto com o tipo do utilizador   
    const historicoContainer = document.querySelector(".historico-treino-container");
    const btnCancelar = document.getElementById("btnCancelar");
    const btnEditar = document.getElementById("btnEditar");

    // Verifica se o utilizador é "Gestor" ou "Utilizador"
    const isGestor = tipoUtilizador.value === "Gestor";
    let isAtivo = false;
    let isUtilizador = true;

    if (isGestor) {
        campoContacto.style.display = "flex";
        campoContacto.style.justifyContent = "center";
        campoContacto.style.alignItems = "center";


    }
    
    
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