const buttonFinal = document.getElementById('buttonFinal');
buttonFinal.addEventListener('click', () => {
    const computedStyleDiv1 = window.getComputedStyle(document.getElementById('Middle1')).display; // Obtém o estilo computado de div1

    if (computedStyleDiv1 === 'flex') {
        document.getElementById('Middle1').style.display = 'none';
        document.getElementById('Middle2').style.display = 'flex';
        document.getElementById('buttonVoltar').style.display = 'unset';
        buttonFinal.textContent = 'Guardar';
        document.getElementById('separadorSelector1').classList = "separadorSelector";
        document.getElementById('separadorSelector2').classList = "separadorSelector Selected";
    } else {
        // Lógica do botão para guardar
    }
});


const buttonVoltar = document.getElementById('buttonVoltar');
buttonVoltar.addEventListener('click', () => {
    const computedStyleDiv1 = window.getComputedStyle(document.getElementById('Middle2')).display; // Obtém o estilo computado de div1

    if (computedStyleDiv1 === 'flex') {
        document.getElementById('Middle2').style.display = 'none';
        document.getElementById('Middle1').style.display = 'flex';
        document.getElementById('buttonVoltar').style.display = 'none';
        buttonFinal.textContent = 'Seguinte';
        document.getElementById('separadorSelector1').classList = "separadorSelector Selected";
        document.getElementById('separadorSelector2').classList = "separadorSelector";
    } 
});


const buttonCancelar = document.getElementById('buttonCancelar');
buttonCancelar.addEventListener('click', () => {
        // Lógica do botão cancelar
});


const intensidades = document.querySelectorAll('.opItemIntensidade');
intensidades.forEach((intensidade) => {
    intensidade.addEventListener('click', () => {
        intensidades.forEach((item) => item.classList.remove('Selected'));

        intensidade.classList.add('Selected');
    });
});

// Pop Ups Responser
document.addEventListener('DOMContentLoaded', () => {
    const addModalidade = document.getElementById('addModalidade');
    const addCategoria = document.getElementById('addCategoria');
    const popUpModalidade = document.querySelector('.addModalidadePop');
    const popUpCategoria = document.querySelector('.addCategoriaPop');
    const popUpExercicio = document.querySelector('.addExercicioPop');
    const shadowBox = document.querySelector('.shadowBox');
    const closeButtons = document.querySelectorAll('.popUpButton[id="buttonRemoverPop"], .popUpButton[id="closePopUp"]');
    const exercicioItems = document.querySelectorAll('.containerItems .itemSelfselect');

    // Mostrar o pop-up
    function showPopUp(popUp) {
        shadowBox.style.display = 'flex';
        popUp.style.display = 'flex';
    }

    // Fechar o pop-up
    function closePopUp() {
        shadowBox.style.display = 'none';
        popUpModalidade.style.display = 'none';
        popUpCategoria.style.display = 'none';
        popUpExercicio.style.display = 'none';
    }

    // Eventos para abrir os pop-ups
    addModalidade.addEventListener('click', () => showPopUp(popUpModalidade));
    addCategoria.addEventListener('click', () => showPopUp(popUpCategoria));

    // Eventos para fechar os pop-ups
    closeButtons.forEach(button => {
        button.addEventListener('click', closePopUp);
    });

    // Evento para mostrar o pop-up de exercício
    exercicioItems.forEach((item) => {
        item.addEventListener('click', () => showPopUp(popUpExercicio));
    });

    // Fecha o pop-up ao clicar fora dele
    shadowBox.addEventListener('click', (event) => {
        if (event.target === shadowBox) {
            closePopUp();
        }
    });
});
