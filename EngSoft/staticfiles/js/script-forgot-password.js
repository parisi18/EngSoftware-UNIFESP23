// Vai manipular a visualização do container que contém o input de email de recuperação e mensagem de confirmação de senha
document.getElementById('login-button-id').addEventListener('click', () => {
    var email = document.getElementById('email-address-input').value;
    var csrfToken = document.querySelector('input[name=csrfmiddlewaretoken]').value;

    var xhr = new XMLHttpRequest();

    route = 'alguma-rota-para-recuperar-senha/'; // Precisa ser implementado ainda

    xhr.open('POST', route, true);

    // Define o cabeçalho X-CSRFToken para o token CSRF
    xhr.setRequestHeader('X-CSRFToken', csrfToken);

    data = new FormData();
    data.append('email', email);

    // Envio a requisição
    xhr.send(data);

    var form = document.getElementById('form-fp-id');
    var msg = document.getElementById('inside-main-fp-id');

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                // Exibe um alerta se a solicitação for bem-sucedida
                alert('Email de recuperação enviado com sucesso!');

                // Quando o modelo de usuários for implementado esse bloco de identação deve ser melhorado contemplando a lógica para confirmar que o email pertence a um usuário no banco de dados
                form.classList.add('hide-element');
                form.classList.remove('show-element');
                msg.classList.remove('hide-element');
                msg.classList.add('show-element');
            }
            else {
                // Exibe um alerta se ocorrer um erro na solicitação
                alert('Erro ao enviar o email de recuperação');
                alert('Aguarde 10 segundos para o redirecionamento!');

                // Quando o modelo de usuários for implementado essas 4 linhas abaixo devem ser apagadas e a lógica para lidar com emails não cadastrados deve ser implementada
                form.classList.add('hide-element');
                form.classList.remove('show-element');
                msg.classList.remove('hide-element');
                msg.classList.add('show-element');
            }
        }
    };

    // Lida provisoriamente com a recuperacao de senha em "esqueceu a senha?"
    var redirectionRoute = 'nova-senha/';

    setTimeout(() => { window.location.href = redirectionRoute }, 10000);

    // ATENÇÃO AQUI!!!!!! ESSA FUNÇÃO SERÁ RESPONSÁVEL POR CRIAR UM OBJETO POST E ENVIAR OS DADOS DO FORMULÁRIO PARA ONDE TIVER QUE SER PROCESSADO (PEGA EMAIL DE RECUPERAÇÃO ENVIA PRO USUÁRIO AS INFORMAÇÕES DE RECUPERAÇÃO)

    // Antes dessa operação de envio seria legal que o email fosse verificado como listado no banco de usuários
});