function mostrarpop(nome) {
    document.getElementById(nome).style.display = "flex";
    document.getElementById("pop").style.display = "flex";
}

function fecharpop(nome){
    document.getElementById(nome).style.display = "none";
    document.getElementById("pop").style.display = "none";
}

function fecharpopEventoMostrar(){
    document.getElementById("pop").style.display = "none";
}

function mostrarNot(){
    document.getElementById("notificacoes").style.display = "flex";
}