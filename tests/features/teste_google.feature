Feature: acessar a pagina do google



@validar_nome
  Scenario: Validar nome se existe na busca do google
    Given que acesso a pagina do google
    When pesquiso por "neymar"
    Then devo validar se existe esse nome na busca