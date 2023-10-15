// Lida provisoriamente com a recuperacao de senha em "esqueceu a senha?"
window.onload = () => {
    alert('Aguarde 10 segundos para o redirecionamento!');

    var redirectionRoute = 'nova-senha/';

    setTimeout(() => { window.location.href = redirectionRoute }, 10000);
};