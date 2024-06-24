# Created by rafael.pantoja at 18/06/2024
Feature: Abrir a pagina de suporte da Positivo!

  Scenario: Abrir de uma forma rápida a pagina de suporte da Positivo!
    Given que esteja na pagina inicial da Positivo
    When preencho o campo com o numero de serie e escolho um modulo
    Then deve identificar um problema