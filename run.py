import pytest
from utils.file_path import file_path_url
from utils.send_email import send_mails
import os
if __name__ == '__main__':
    pytest.main(["./wddy/case/test_xdgp.py","-s","--alluredir","./temp","--clean-alluredir"])
    os.system("allure generate ./temp -o allure_report --clean")
    # send_mails([file_path_url+r"\allure_report\index.html"])
    # pytest.main(["./wddy/case/test_xiadan2.py"])
    



    