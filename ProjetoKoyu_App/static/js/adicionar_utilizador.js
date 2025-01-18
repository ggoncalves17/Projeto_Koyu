document.addEventListener("DOMContentLoaded", () => {
    const switchElement = document.getElementById("switch");
    const circle = document.getElementById("circle");
    const iconeAtual = document.getElementById("icone-atual");
    const textoSuperior = document.getElementById("texto-superior");
    const textoInferior = document.getElementById("texto-inferior");
    const campoNIF = document.getElementById("campo-nif");
    const campoContacto = document.getElementById("campo-contacto");
    const tipoUtilizador = document.getElementById("tipo-utilizador"); 
    const btnCancelar = document.getElementById("btnCancelar");

    let isUtilizador = true; // Estado inicial (assume que começa como Utilizador)

    switchElement.addEventListener("click", () => {
        if (isUtilizador) {
            // Mudar para Gestor
            circle.style.left = "42.5px";
            iconeAtual.innerHTML = `
                <svg width="15" height="15" viewBox="0 0 32 36" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M16 18C17.78 18 19.5201 17.4722 21.0001 16.4832C22.4802 15.4943 23.6337 14.0887 24.3149 12.4442C24.9961 10.7996 25.1743 8.99002 24.8271 7.24419C24.4798 5.49836 23.6226 3.89472 22.364 2.63604C21.1053 1.37737 19.5016 0.520203 17.7558 0.172937C16.01 -0.17433 14.2004 0.00389957 12.5558 0.685088C10.9113 1.36628 9.50571 2.51983 8.51677 3.99987C7.52784 5.47991 7 7.21997 7 9C7 11.387 7.94821 13.6761 9.63604 15.364C11.3239 17.0518 13.6131 18 16 18ZM22.736 20.292L19.375 33.75L17.125 24.188L19.375 20.251H12.625L14.875 24.189L12.625 33.752L9.264 20.292C6.83994 20.4 4.55071 21.4379 2.87203 23.19C1.19334 24.942 0.254282 27.2735 0.25 29.7L0.25 32.625C0.250265 33.52 0.60593 34.3783 1.23881 35.0112C1.87169 35.6441 2.72998 35.9997 3.625 36H28.375C29.27 35.9997 30.1283 35.6441 30.7612 35.0112C31.3941 34.3783 31.7497 33.52 31.75 32.625V29.7C31.7457 27.2735 30.8067 24.942 29.128 23.19C27.4493 21.4379 25.1601 20.4 22.736 20.292Z" fill="black"/>
                </svg>
            `;
            textoSuperior.classList.remove("ativo");
            textoInferior.classList.add("ativo");
            campoNIF.style.display = "none";
            campoContacto.classList.add("centered");
            tipoUtilizador.value = "Gestor"; 
        } else {
            // Mudar para Utilizador
            circle.style.left = "2.5px";
            iconeAtual.innerHTML = `
                <svg width="15" height="15" viewBox="0 0 50 50" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M25 28C27.7689 28 30.4757 27.1789 32.778 25.6406C35.0803 24.1022 36.8747 21.9157 37.9343 19.3576C38.9939 16.7994 39.2712 13.9845 38.731 11.2687C38.1908 8.55301 36.8574 6.05845 34.8995 4.10051C32.9416 2.14258 30.447 0.809205 27.7313 0.269012C25.0155 -0.271181 22.2006 0.00606608 19.6424 1.06569C17.0843 2.12532 14.8978 3.91973 13.3594 6.22202C11.8211 8.52431 11 11.2311 11 14C10.9947 15.84 11.3532 17.6629 12.0549 19.3638C12.7566 21.0648 13.7877 22.6102 15.0887 23.9113C16.3898 25.2123 17.9353 26.2434 19.6362 26.9451C21.3371 27.6468 23.16 28.0053 25 28ZM38 31H32C29.84 32.1682 27.4511 32.8508 25 33C22.5491 32.8494 20.1605 32.167 18 31H13C9.58166 31.0934 6.32903 32.493 3.911 34.911C1.49297 37.329 0.0933593 40.5817 0 44L0 45C0.0586196 46.3072 0.604221 47.5452 1.5295 48.4705C2.45478 49.3958 3.69277 49.9414 5 50H45C46.3072 49.9414 47.5452 49.3958 48.4705 48.4705C49.3958 47.5452 49.9414 46.3072 50 45V44C50 37.1 44.9 31 38 31Z" fill="black"/>
                </svg>
            `;
            textoSuperior.classList.add("ativo");
            textoInferior.classList.remove("ativo");
            campoNIF.style.display = "flex";
            campoContacto.classList.remove("centered");
            tipoUtilizador.value = "Utilizador";
        }
        isUtilizador = !isUtilizador;
    });

    // Redireciona para listar utilizadores ao clicar no botão Cancelar
    if (btnCancelar) {
        btnCancelar.addEventListener("click", () => {
            const url = btnCancelar.getAttribute("data-url");
            window.location.href = url;
        });
    }
});
