from pytest_bdd.parsers import parse
from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import expect
from pytest_playwright.pytest_playwright import Page

scenarios('../features/login_valido.feature')


@given('que o usuário está na página de login')
def acesso_pagina_saucedemo(browser: Page):
    browser.goto('https://www.saucedemo.com/')


@when(parse("o usuário preenche o campo de usuario e senha"), converters=dict(texto=str))
def step_preencher_usuario_e_senha(browser: Page):
    browser.locator('[placeholder="Username"]').fill('standard_user')
    browser.locator('[placeholder="Password"]').fill('secret_sauce')
    browser.locator('[type="submit"]').click()


@then(parse("o usuário é redirecionado para a página home"), converters=dict(texto=str))
def step_validar_tela_home(browser: Page):
    expect(browser.get_by_text('Products', exact=True)).to_be_visible()



