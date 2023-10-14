// Formata o email para o app de newsletter fazer o envio para a mailchimp
function sendEmail() {
    var email = document.getElementById("email").value;
    var subscribeEmailUrl = emailInput.getAttribute('data-subscribe-email-url');

    alert("email:" + email)

    // Cria um objeto XMLHttpRequest para fazer a solicitação POST
    var xhr = new XMLHttpRequest();

    // Abre a solicitação POST para a URL definida
    xhr.open('POST', subscribeEmailUrl, true);

    // Define o cabeçalho X-CSRFToken para o token CSRF (substitua pelo valor real)
    xhr.setRequestHeader('X-CSRFToken', csrf_token);

    // Define uma função a ser chamada quando a solicitação for concluída
    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4) {
        if (xhr.status === 200) {
          // Exibe um alerta se a solicitação for bem-sucedida
          alert('Email enviado com sucesso!');
        } else {
          // Exibe um alerta se ocorrer um erro na solicitação
          alert('Erro ao enviar o email');
        }
      }
    };

    // Cria um objeto FormData e anexa o valor do email a ele
    var data = new FormData();
    data.append('email', email);

    // Envia a solicitação POST com os dados do FormData
    xhr.send(data);
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