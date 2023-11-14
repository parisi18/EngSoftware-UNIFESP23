// Lida provisoriamente com o login
const loginButton = document.getElementsByClassName('login-button');

loginButton[0].addEventListener('click', () => {
    alert("Bem vindo novamente à PetScan!");
});

// Lida com esconder ou mostrar a senha
document.getElementById('password-button').addEventListener('click', () => {
    var password = document.getElementById('password-input');

    if(password.type == 'password')
        password.type = 'text';
    else
        password.type = 'password';
});