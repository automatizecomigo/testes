from pytest_bdd.parsers import parse
from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import expect
from pytest_playwright.pytest_playwright import Page

scenarios('../features/iniciar_servico_positivo.feature')


# Acesso a pagina da Positivo.
@given('que esteja na pagina inicial da Positivo')
def entro_na_pagina_google(browser: Page):
    browser.goto('https://servicos.meupositivo.com.br/autoatendimento/index.html#/')


# Preencho o numero de serie.
@when(parse("preencho o campo com o numero de serie e escolho um modulo"), converters=dict(texto=str))
def step_impl(browser: Page):
    browser.locator('[type="text"]').fill('89707602G')
    browser.get_by_text(' Enviar ').click()


# Escolho o modulo e o problema.
@then(parse("deve identificar um problema"), converters=dict(texto=str))
def step_impl(browser: Page):
    browser.get_by_text('Áudio').click()
    browser.get_by_text('Continuar').click()
    browser.get_by_text(' Microfone não funciona ').click()
    browser.get_by_text('Continuar').click()
    browser.get_by_text(' Externo ').click()
    browser.get_by_text('Continuar').click()
    browser.get_by_text("Solucionado", exact=True).click()
    browser.get_by_text('Continuar', exact=True).click()
    browser.get_by_text('9').click()
    browser.get_by_text('Enviar').click()
    expect(browser.get_by_text('Obrigado pela avaliação!')).to_be_visible()
