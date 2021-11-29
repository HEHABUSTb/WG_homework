import logging
import os

import pyautogui
import allure
import pytest
from allure_commons.types import AttachmentType
from TestData.create_fake_data import CreateFakeDB


@pytest.fixture(scope="session")
def setup():
    # path = os.path.abspath('TestData/game_params.db')
    # fake_path = os.path.abspath('TestData/fake_params.db')

    # path_to_game_db = os.getcwd() + '\\TestData\\game_params.db'
    # path_to_fake_db = os.getcwd() + '\\TestData\\fake_params.db'

    path_to_game_db = 'D:\\GIT_Repository\\WG_TEST\\TestData\\game_params.db'
    path_to_fake_db = 'D:\\GIT_Repository\\WG_TEST\\TestData\\fake_params.db'

    update_table = CreateFakeDB()
    update_table.copy_table(path_to_game_db, path_to_fake_db)
    update_table.update_all_fake_table(path_to_fake_db)

    yield
    logging.info('Teardown')


@pytest.mark.hookwrapper
def pytest_runtest_makereport():
    # Automatically take screenshot when test fails and attach to allure report

    outcome = yield
    report = outcome.get_result()
    try:
        if report.when == 'call' or report.when == "setup":
            xfail = hasattr(report, 'wasxfail')
            if (report.skipped and xfail) or (report.failed and not xfail):
                myScreenshot = pyautogui.screenshot()

                file_name = report.nodeid.replace("::", "_") + ".png"
                allure.attach(myScreenshot.save(r'profile/fail.png'), name=file_name,
                              attachment_type=AttachmentType.PNG)
    except Exception as e:
        print(f"The error '{e}' occurred")
