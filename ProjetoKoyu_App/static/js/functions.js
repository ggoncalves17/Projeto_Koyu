// Dividir este ficheiro em ficheiros por páginas,
// isto porque certas funções nao carregam caso apareça alguma função que n
// esteja presente na página


const buttonCancelar = document.getElementById('buttonCancelar');
buttonCancelar.addEventListener('click', () => {
    // Lógica do botão cancelar
});

const intensidades = document.querySelectorAll('.opItemIntensidade');
intensidades.forEach((intensidade) => {
    intensidade.addEventListener('click', () => {
        if (intensidade.classList.contains('Det')) {
            console.log('Ação bloqueada: a classe "Det" está presente.');
            return;
        }

        intensidades.forEach((item) => item.classList.remove('Selected'));

        intensidade.classList.add('Selected');        
        document.getElementById("intensidadeSelecionada").value = intensidade.innerHTML;
    });
});



const separadores = document.querySelectorAll('.separadorSelector');
// Adiciona o evento de clique para cada separador
separadores.forEach((separador, index) => {
    separador.addEventListener('click', () => {
        if (!separador.classList.contains('Det')) {
            console.log('Ação bloqueada: a classe "Det" não está presente.');
            return;
        }

        if (separador.classList.contains('Selected')) {
            console.log('Ação bloqueada: a classe "Selected" está presente.');
            return;
        }

        separadores.forEach((s) => s.classList.remove('Selected'));

        separador.classList.add('Selected');

        const div1 = document.getElementById('Middle1');
        const div2 = document.getElementById('Middle2');

        if (index === 0) {
            div1.style.display = 'flex';
            div2.style.display = 'none';
        } else if (index === 1) {
            div1.style.display = 'none';
            div2.style.display = 'flex';
        }
    });
});

//Falta fazer para alterar o nome e foto do equipamento
const fotoInput = document.getElementById("fotoCapaInput"); 
const fotoEQInput = document.getElementById("fotoEquipamentoInput");
const divEscolherFoto = document.querySelector(".divEscolherFoto img");
const divEscolherFotoEQ = document.getElementById("fotoEquipamento"); 

// Evento para clicar na divEscolherFoto e acionar o clique no input de arquivo
document.querySelector(".divEscolherFoto").addEventListener("click", function () {
    fotoInput.click(); // Aciona o clique no input file
});

// Evento para quando o arquivo for selecionado
fotoInput.addEventListener("change", function (event) {
    const file = event.target.files[0]; // Obtém o arquivo selecionado
    if (file) {
        const validImageTypes = ['image/jpeg', 'image/png', 'image/gif', 'image/bmp', 'image/webp']; // Tipos de imagem válidos

        // Verifica se o tipo do arquivo é válido
        if (validImageTypes.includes(file.type)) {
            // Cria um novo objeto URL para a imagem e atualiza o src da tag <img>
            const reader = new FileReader();
            reader.onload = function (e) {
                divEscolherFoto.src = e.target.result; // Atualiza o src da imagem com o arquivo selecionado
            };
            reader.readAsDataURL(file); // Lê o arquivo como uma URL de dados para visualização

            // Atualiza o valor do input para o nome do arquivo (caso seja necessário no envio do formulário)
            fotoInput.setAttribute('value', file.name); // Salva o nome do arquivo
        }
    }
});

//Falta fazer para alterar o nome e foto do equipamento
document.querySelector(".popUpFoto").addEventListener("click", function () {
    fotoEQInput.click(); // Aciona o clique no input file
});

fotoEQInput.addEventListener("change", function (event) {
    const file = event.target.files[0]; // Obtém o arquivo selecionado
    if (file) {
        const validImageTypes = ['image/jpeg', 'image/png', 'image/gif', 'image/bmp', 'image/webp']; // Tipos de imagem válidos

        // Verifica se o tipo do arquivo é válido
        if (validImageTypes.includes(file.type)) {
            // Cria um novo objeto URL para a imagem e atualiza o src da tag <img>
            const reader = new FileReader();
            reader.onload = function (e) {
                divEscolherFotoEQ.src = e.target.result; // Atualiza o src da imagem com o arquivo selecionado
            };
            reader.readAsDataURL(file); // Lê o arquivo como uma URL de dados para visualização

            // Atualiza o valor do input para o nome do arquivo (caso seja necessário no envio do formulário)
            fotoEQInput.setAttribute('value', file.name); // Salva o nome do arquivo
        }
    }
});

// Fechar o pop-up ao clicar fora (no shadowBox)
document.querySelector(".shadowBox").addEventListener("click", function (event) {
    // Verifica se o clique foi fora do pop-up (addEquipamentoPop)
    if (event.target === this) {
        this.style.display = "none";  // Oculta o shadowBox
        document.querySelector(".addEquipamentoPop").style.display = "none";  // Oculta o pop-up
    }
});

document.querySelectorAll(".buttonItem").forEach((button) => {
    button.addEventListener("click", function () {
        // Pega o item do equipamento que foi clicado
        const item = this.closest(".itemSelfselect");
        const equipamentoId = item.getAttribute("value");  // ID do equipamento
        const nomeEquipamento = item.querySelector("span").textContent;  // Nome do equipamento
        const fotoEquipamento = item.querySelector(".fotoItemselect").src;  // Foto do equipamento

        // Exibe o shadowBox e o pop-up
        document.querySelector(".shadowBox").style.display = "flex";
        const addEquipamentoPop = document.querySelector(".addEquipamentoPop");
        addEquipamentoPop.style.display = "flex";

        // Preenche o pop-up com os dados do equipamento
        addEquipamentoPop.querySelector(".inputNome input").value = nomeEquipamento;
        addEquipamentoPop.querySelector(".popUpFoto img").style.display = "unset";
        addEquipamentoPop.querySelector(".popUpFoto img").src = fotoEquipamento;

        // Preenche o campo hidden para enviar o ID do equipamento
        document.getElementById("equipamentoSelecionado").value = equipamentoId;
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
    let equipamentoSelecionado = null;
    let categoriasSelecionadas = [];  // Agora temos um Set para categorias selecionadas
    const videoInput = document.getElementById("videoFile"); // Campo de input do vídeo
    const caminhoFicheiro = document.getElementById("caminhoFicheiro"); // Campo onde o caminho será exibido

    // Função para verificar se o arquivo selecionado é um vídeo
    // Função para verificar se o arquivo selecionado é um vídeo
    videoInput.addEventListener("change", function (event) {
        const file = event.target.files[0]; 
        if (file) {
            const validVideoTypes = ['video/mp4', 'video/avi', 'video/mkv', 'video/webm', 'video/ogg']; 

            if (validVideoTypes.includes(file.type)) {
                caminhoFicheiro.innerHTML = file.name; // Exibe o nome do arquivo
                videoInput.setAttribute('value', file.name); // Salva o nome do arquivo
            }
        }
    });

    // Clique em equipamentos
    document.querySelectorAll(".itemSelfselect").forEach((item) => {
        item.addEventListener("click", function (event) {
            // Verifica se o clique não foi no botão buttonItem
            if (!event.target.closest(".buttonItem")) {
                const itemId = this.getAttribute("value");
        
                // Se já houver um equipamento selecionado, desmarque-o antes de marcar o novo
                if (equipamentoSelecionado === itemId) {
                    equipamentoSelecionado = null; // Desmarca o equipamento
                    this.classList.remove("itemSelecionado");
                } else {
                    equipamentoSelecionado = itemId; // Marca o novo equipamento
                    document.querySelectorAll(".itemSelfselect").forEach((e) => e.classList.remove("itemSelecionado"));
                    this.classList.add("itemSelecionado");
                }
        
                document.getElementById("equipamentoSelecionado").value = equipamentoSelecionado;
            }
        });
    });

   // Clique em categorias (permitir múltiplas categorias)
    document.querySelectorAll(".cardCategoria").forEach((item) => {
        item.addEventListener("click", function () {
            const itemId = this.getAttribute("value");

            // Se já houver categoria selecionada, desmarque-a antes de marcar a nova
            if (categoriasSelecionadas.includes(itemId)) {
                // Remove a categoria da lista com filter
                categoriasSelecionadas = categoriasSelecionadas.filter(id => id !== itemId); // Remover o item do array
                this.classList.remove("itemSelecionado");
            } else {
                // Adiciona a categoria à lista
                categoriasSelecionadas.push(itemId); 
                this.classList.add("itemSelecionado");
            }

            // Atualiza o valor do campo oculto com as categorias selecionadas (como texto)
            document.getElementById("categoriasSelecionadas").value = categoriasSelecionadas.join(","); // Converte o array para uma string separada por vírgulas
        });
    });

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

document.getElementById("pesquisarEquipamentos").addEventListener("input", function (event) {
    const searchText = event.target.value.toLowerCase(); // Texto digitado na caixa de pesquisa
    const equipamentos = document.querySelectorAll("#listaEquipamentos .itemSelfselect");

    equipamentos.forEach((equipamento) => {
        const nome = equipamento.querySelector(".nomeEquipamento").textContent.toLowerCase(); // Nome do equipamento
        if (nome.includes(searchText)) {
            equipamento.style.display = ""; // Mostra o equipamento
        } else {
            equipamento.style.display = "none"; // Esconde o equipamento
        }
    });
});


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
