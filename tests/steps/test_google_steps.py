from pytest_bdd.parsers import parse
from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import expect
from pytest_playwright.pytest_playwright import Page

scenarios('../features/teste_google.feature')


@given('que acesso a pagina do google')
def entro_na_pagina_google(browser: Page):
    browser.goto('https://www.google.com')


@when(parse('pesquiso por "neymar"'), converters=dict(texto=str))
def pesquiso_por_teste(browser: Page):
    browser.locator('[name="q"]').fill('neymar')
    browser.keyboard.press('Enter')


@then(parse("eu vejo o resultado da pesquisa"), converters=dict(texto=str))
def valido_se_existe_o_nome_teste(browser: Page):
    expect(browser.get_by_text("neymar"))
