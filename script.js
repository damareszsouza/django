document.getElementById('propostaForm').addEventListener('submit', function(event) {
  // Impede que o formulário seja enviado normalmente
  event.preventDefault();

  // Obtém os valores dos campos do formulário
  var nome = document.getElementById('nome').value;
  var cpf = document.getElementById('cpf').value;
  var valor_solicitado = document.getElementById('valor_solicitado').value;

  // Envia os dados para a API ou realiza outras ações necessárias
  // ...

  // Limpa os campos do formulário
  document.getElementById('nome').value = '';
  document.getElementById('cpf').value = '';
  document.getElementById('valor_solicitado').value = '';
});