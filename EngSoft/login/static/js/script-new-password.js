// Lida com esconder ou mostrar a senha
document.getElementById('new-password-button').addEventListener('click', () => {
    const password = document.getElementById('new-password-input');

    if(password.type == 'password')
        password.type = 'text';
    else
        password.type = 'password';
});

// Verifica se as senhas são iguais ou não
document.getElementsByClassName('login-button')[0].addEventListener('click', () => {
    var firstPassword = document.getElementById('new-password-input');
    var secondPassword = document.getElementById('new-password-input-confirmation');
    
    if(firstPassword.value === secondPassword.value)
        alert('Senha alterada com sucesso!');
    else
        alert('As senhas devem ser iguais!');
});