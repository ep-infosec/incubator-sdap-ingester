import asyncio
import os
import time
import unittest
from datetime import datetime
from unittest.mock import Mock

from config_operator.config_source import LocalDirConfig
from config_operator.config_source.exceptions import UnreadableFileException


class TestLocalDirConfig(unittest.TestCase):
    def test_get_files(self):
        local_dir = os.path.join(os.path.dirname(__file__), "../resources/localDirTest")
        local_dir_config = LocalDirConfig(local_dir)
        files = local_dir_config.get_files()
        self.assertEqual(len(files), 1)
        self.assertEqual(files[0], 'collections.yml')

    def test_get_good_file_content(self):
        local_dir = os.path.join(os.path.dirname(__file__), "../resources/localDirTest")
        local_dir_config = LocalDirConfig(local_dir)
        files = local_dir_config.get_files()
        content = local_dir_config.get_file_content(files[0])
        self.assertEqual(content.strip(), 'test: 1')

    def test_get_bad_file_content(self):
        unreadable_file = False
        try:
            local_dir = os.path.join(os.path.dirname(__file__), "../resources/localDirBadTest")
            local_dir_config = LocalDirConfig(local_dir)
            files = local_dir_config.get_files()
            content = local_dir_config.get_file_content(files[0])
        except UnreadableFileException as e:
            unreadable_file = True

        finally:
            self.assertTrue(unreadable_file)

    def test_when_updated(self):

        callback = Mock()
        local_dir = os.path.join(os.path.dirname(__file__), "../resources/localDirTest")

        local_dir_config = LocalDirConfig(local_dir,
                                          update_every_seconds=0.25,
                                          update_date_fun=lambda x: datetime.now().timestamp())

        asyncio.run(local_dir_config.when_updated(callback))

        time.sleep(2)

        assert callback.called

    def test_when_not_updated(self):

        callback = Mock()
        local_dir = os.path.join(os.path.dirname(__file__), "../resources/localDirTest")

        local_dir_config = LocalDirConfig(local_dir,
                                          update_every_seconds=0.25,
                                          update_date_fun=lambda x: 0)

        asyncio.run(local_dir_config.when_updated(callback))

        time.sleep(2)

        assert not callback.called


if __name__ == '__main__':
    unittest.main()
