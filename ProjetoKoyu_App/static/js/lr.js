const registerButton = document.getElementById('register');
const loginButton = document.getElementById('login');
const index = document.getElementById('index');

registerButton.addEventListener('click', () => {
    index.classList.add("right-panel-active");
});

loginButton.addEventListener('click', () => {
	index.classList.remove("right-panel-active");
});