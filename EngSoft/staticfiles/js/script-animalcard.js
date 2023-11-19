// pego o botao adicionar do topo
const postShowFormButton = document.getElementById('post-show-form-button');

// pego o botao adicionar de cada ficha
const getShowFormButton = document.getElementsByClassName('get-show-form-button')

// pego a tag dialog, corpo do formulario de envio
const postPopupForm = document.getElementById('post-popup-form');

// pego a tag dialog, corpo do formulario de udpate
const getPopupForm = document.getElementsByClassName('get-popup-form')

// escuta do botao adicionar, para mostrar o popup
postShowFormButton.addEventListener('click', () => {
    postPopupForm.showModal(); // show popup when the button is activated
});

// Temos mais de um botao para exibicao do modal, portanto 
for (const button of getShowFormButton) {
    button.addEventListener('click', () => {
        getPopupForm[0].showModal();
    });
};

// Função responsável por fechar a dialog
function closePopup() {
    postPopupForm.close();
    getPopupForm[0].close();
};

// ouvinte de eventos ao formulário para ocultar o popup quando o formulário for enviado
postPopupForm.querySelector('form').addEventListener('submit', closePopup);
const closePopupVec = document.getElementsByClassName('close-popup-button');
closePopupVec[0].addEventListener('click', closePopup);
closePopupVec[1].addEventListener('click', closePopup);

// Funcao que lida com a delegação correta de animal_id para o formulário de atualização de infos do card
for (const button of getShowFormButton) {
    button.addEventListener('click', () => {
        const animalID = button.getAttribute('data-animal-id');
        const editForm = document.getElementById('edit-form');
        const editAction = 'editcard/' + animalID + '/';
        editForm.action = editAction; // Passo dinamicamente a rota edit_url com uuid:animal_id
        getPopupForm.showModal();
    });
};
