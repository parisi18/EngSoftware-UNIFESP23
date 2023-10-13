// Processa o email
function enviarEmail() {
    var email = document.getElementById("email").value;

    // Apenas visualizo o email na tela, nada demais
    alert("Email a ser enviado: " + email);
}

// Esconde a imagem quando o email estiver no input
document.addEventListener('DOMContentLoaded', function () {
    var emailInput = document.getElementById('email');
    var backgroundImage = emailInput.style.backgroundImage;

    emailInput.addEventListener('input', function () {
        if (emailInput.value.trim() !== '') {
            emailInput.style.backgroundImage = 'none';
        } else {
            emailInput.style.backgroundImage = backgroundImage;
        }
    });
});