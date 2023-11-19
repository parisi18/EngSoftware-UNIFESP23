// document.getElementById('open-call-btn').addEventListener('click', (Event) => {
//     Event.preventDefault();

//     const name = document.querySelector('input[name="name"]').value;
//     const email = document.querySelector('input[name="email"]').value;
//     const cpfCnpj = document.querySelector('input[name="cpf-cnpj"]').value;
//     const typeRequest = document.getElementById('help-dropdown').value;
//     const number = document.querySelector('input[name="phone"]').value;
//     const city = document.querySelector('input[name="city"]').value;
//     const description = document.querySelector('textarea[name="description"]').value;
//     const msg = "CPF ou CNPJ: " + cpfCnpj + "\nTelefone: " + number + "\nCidade: " + city + "\nDescrição: " + description;
//     const subject = "[" + name + "] " + typeRequest;

//     Email.send({
//         Host: "smtp.elasticemail.com",
//         Username: "petscan.ia.engsoft@gmail.com",
//         Password: "DAD33C36284E52F428EAFDB65E7F28DE4164", 
//         To: "petscan.ia.engsoft@gmail.com",
//         From: email, Subject: subject, Body: msg,
//     }).then(
//         message => alert("Chamado aberto com sucesso, verifique sua caixa de email!"));
// });