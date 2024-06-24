# Created by rafael.pantoja at 15/05/2024
Feature: acessar a pagina do google




@validar_nome
  Scenario: Validar nome se existe na busca do google
    Given que acesso a pagina do google
    When pesquiso por "neymar"
    Then eu vejo o resultado da pesquisa