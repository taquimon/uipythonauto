import logging

import requests

from libraries.browser_manager import BrowserManager
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


def before_all(context):
    """
    method to define variables that will be used in steps definitions
    :param context:   object     Context object to store and get variables
    """
    # context.session = requests.Session()
    # context.headers = HEADERS
    # context.project_list = []
    # context.section_list = []
    # context.task_list = []
    # # context.resource_list = {
    # #     "tasks": [],
    # #     "sections": [],
    # #     "projects": [],
    # # }

    # context.url = BASE_URL
    LOGGER.debug("before all")
    # projects = get_all_projects(context)
    # LOGGER.debug(projects)
    # context.project_id_from_all = projects["body"][1]["id"]


def before_feature(context, feature):
    """
    Method to be executed before each feature
    :param context:     object      Contains context information
    :param feature:     object      Contains feature information
    """
    LOGGER.debug("Before feature")
    # cleanup lists
    # context.resource_list = {
    #     "tasks": [],
    #     "sections": [],
    #     "projects": [],
    # }
    # context.feature_name = feature.name.lower()
    driver_type = context.config.userdata['browser']
    LOGGER.info(driver_type)
    driver = BrowserManager().launch_browser(driver_type)
    driver.maximize_window()
    context.driver = driver


def before_scenario(context, scenario):
    """
    Method to be called before scenario
    :param context:
    :param scenario:
    """
    LOGGER.debug("Scenario tags: %s", scenario.tags)
    LOGGER.debug("Scenario Name: %s", scenario.name)

    # if "project_id" in scenario.tags:
    #
    #     response = create_project(context=context, name_project="project x")
    #     context.project_id = response["body"]["id"]
    #     LOGGER.debug("Project id created: %s", context.project_id)
    #     context.resource_list["projects"].append(context.project_id)
    #
    # if "section_id" in scenario.tags:
    #
    #     response = create_section(context=context, project_id=context.project_id_from_all,
    #                               section_name="section x")
    #     context.section_id = response["body"]["id"]
    #     LOGGER.debug("Section id created: %s", context.section_id)
    #     context.resource_list["sections"].append(context.section_id)
    #
    # if "task_id" in scenario.tags:
    #
    #     response = create_task(context=context)
    #     context.task_id = response["body"]["id"]
    #     LOGGER.debug("Task id created: %s", context.task_id)
    #     context.resource_list["tasks"].append(context.task_id)


# def after_scenario(context, scenario):
#     """
#     Method to execute instructions after scenario
#     :param context:
#     :param scenario:
#     :return:
#     """
#     client = get_influx()
#     write_api = client.write_api(write_options=SYNCHRONOUS)
#     bucket = "todo_bucket"
#     LOGGER.debug("after scenario")
#     p = (Point("test_case_execution").tag("id_tc", scenario.tags)
#          .tag("feature", context.feature_name)
#          .tag("test_case_name", scenario.name)
#          .tag("status", scenario.status)
#          .field("duration", scenario.duration)
#          )
#     write_api.write(bucket=bucket, record=p)


def after_feature(context, feature):
    """
    Method to execute instructions after feature
    :param context:
    :param feature:
    :return:
    """
    LOGGER.debug("After feature")
    context.driver.close()
    # delete_resources(context)


def after_all(context):
    """
    Method to execute instructions after all features
    :param context:
    :return:
    """
    LOGGER.debug("After all")

# def create_project(context, name_project):
#     """
#     Method to create project
#     :param context:
#     :param name_project:
#     :return:
#     """
#     body_project = {
#         "name": name_project
#     }
#     response = RestClient().send_request(method_name="post", session=context.session,
#                                          url=context.url+"projects", headers=context.headers,
#                                          data=body_project)
#     return response
#
#
# def create_section(context, project_id, section_name):
#     """
#     Method to create section
#     :param context:
#     :param project_id:
#     :param section_name:
#     :return:
#     """
#     body_section = {
#         "project_id": project_id,
#         "name": section_name
#     }
#     response = RestClient().send_request(method_name="post", session=context.session,
#                                          url=context.url+"sections", headers=context.headers,
#                                          data=body_section)
#     return response
#
#
# def get_all_projects(context):
#     """
#     Method to get all projects
#     :param context:   object    Store contextual information about test
#     :return:
#     """
#     response = RestClient().send_request(method_name="get", session=context.session,
#                                          url=context.url + "projects", headers=context.headers)
#
#     return response
#
#
# def create_task(context, project_id=None, section_id=None):
#     """
#     Method to create a task
#     :param context:
#     :param project_id:
#     :param section_id:
#     :return:
#     """
#     data = {
#         "content": "Task created in feature",
#         "due_string": "tomorrow at 11:00",
#         "due_lang": "en",
#         "priority": 4
#     }
#     if project_id:
#         data["project_id"] = project_id
#     if section_id:
#         data["section_id"] = section_id
#
#     response = RestClient().send_request(method_name="post", session=context.session,
#                                          headers=context.headers,
#                                          url=context.url + "tasks", data=data)
#
#     return response

#
# def delete_resources(context):
#     LOGGER.debug("Resources: %s", context.resource_list)
#     for resource in context.resource_list:
#         LOGGER.debug("Resource: %s", resource)
#         for res in context.resource_list[resource]:
#             # i.e https://api.todoist.com/rest/v2/ projects / project_id
#             url = f"{context.url}{resource}/{res}"
#             RestClient().send_request(method_name="delete", session=context.session,
#                                       url=url, headers=context.headers)
#             LOGGER.info("Deleting %s: %s", resource, res)
