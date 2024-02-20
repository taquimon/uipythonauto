import logging

from behave import *

from utils.logger import get_logger

# use_step_matcher("re")
LOGGER = get_logger(__name__, logging.DEBUG)


@when("we visit {site} site")
def step_impl(context, site):
    """
    :type context: behave.runner.Context
    """
    context.driver.get(site)
    LOGGER.info(f'STEP: When we visit {site}')


@step('it should have a title {title}')
def step_impl(context, title):
    """
    :type context: behave.runner.Context
    """
    LOGGER.info(f'STEP: Then it should have a title "Google"')