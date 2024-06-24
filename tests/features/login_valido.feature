Feature: Entrar no sistema com uma credencial
  valida.

  Scenario: Login valido
    Given que o usuário está na página de login
    When o usuário preenche o campo de usuario e senha
    Then o usuário é redirecionado para a página home




