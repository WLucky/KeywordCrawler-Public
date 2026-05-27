# -*- coding: utf-8 -*-
# Copyright (c) 2025 relakkes@gmail.com
#
# This file is part of MediaCrawler project.
# Repository: https://github.com/NanmiCoder/MediaCrawler/blob/main/store/douyin/douyin_store_media.py
# GitHub: https://github.com/NanmiCoder
# Licensed under NON-COMMERCIAL LEARNING LICENSE 1.1
#

# 声明：本代码仅供学习和研究目的使用。使用者应遵守以下原则：
# 1. 不得用于任何商业用途。
# 2. 使用时应遵守目标平台的使用条款和robots.txt规则。
# 3. 不得进行大规模爬取或对平台造成运营干扰。
# 4. 应合理控制请求频率，避免给目标平台带来不必要的负担。
# 5. 不得用于任何非法或不当的用途。
#
# 详细许可条款请参阅项目根目录下的LICENSE文件。
# 使用本代码即表示您同意遵守上述原则和LICENSE中的所有条款。

import json
import pathlib
from typing import Dict

import aiofiles

from base.base_crawler import AbstractStoreImage, AbstractStoreVideo
from tools import utils
import config


class DouYinImage(AbstractStoreImage):
    def __init__(self):
        if config.SAVE_DATA_PATH:
            self.image_store_path = f"{config.SAVE_DATA_PATH}/douyin/images"
        else:
            self.image_store_path = "data/douyin/images"

    async def store_image(self, image_content_item: Dict):
        """
        store content

        Args:
            image_content_item:

        Returns:

        """
        await self.save_image(image_content_item.get("aweme_id"), image_content_item.get("pic_content"), image_content_item.get("extension_file_name"))

    def make_save_file_name(self, aweme_id: str, extension_file_name: str) -> str:
        """
        make save file name by store type

        Args:
            aweme_id: aweme id
            extension_file_name: image filename with extension

        Returns:

        """
        return f"{self.image_store_path}/{aweme_id}/{extension_file_name}"

    async def save_image(self, aweme_id: str, pic_content: str, extension_file_name):
        """
        save image to local

        Args:
            aweme_id: aweme id
            pic_content: image content
            extension_file_name: image filename with extension

        Returns:

        """
        try:
            pathlib.Path(self.image_store_path + "/" + aweme_id).mkdir(parents=True, exist_ok=True)
            save_file_name = self.make_save_file_name(aweme_id, extension_file_name)
            async with aiofiles.open(save_file_name, 'wb') as f:
                await f.write(pic_content)
                utils.logger.info(f"[DouYinImageStoreImplement.save_image] save image {save_file_name} success ...")
        except Exception as e:
            utils.logger.error(f"[DouYinImageStoreImplement.save_image] Failed to save image: {e}")


class DouYinVideo(AbstractStoreVideo):
    VIDEO_CONFIG_FILE = "data/video/video_config.json"

    def __init__(self):
        if config.SAVE_DATA_PATH:
            self.video_store_path = f"{config.SAVE_DATA_PATH}/video"
        else:
            self.video_store_path = "data/video"

    @classmethod
    def _load_video_config(cls) -> Dict[str, str]:
        """Load video config from JSON file"""
        try:
            if pathlib.Path(cls.VIDEO_CONFIG_FILE).exists():
                with open(cls.VIDEO_CONFIG_FILE, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception as e:
            utils.logger.warning(f"[DouYinVideo] Failed to load video config: {e}")
        return {}

    @classmethod
    def _save_video_config(cls, config_data: Dict[str, str]) -> None:
        """Save video config to JSON file"""
        try:
            config_file_path = pathlib.Path(cls.VIDEO_CONFIG_FILE)
            config_file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(cls.VIDEO_CONFIG_FILE, 'w', encoding='utf-8') as f:
                json.dump(config_data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            utils.logger.error(f"[DouYinVideo] Failed to save video config: {e}")

    @classmethod
    def _update_video_config(cls, aweme_id: str, video_filename: str) -> None:
        """Update video config with new video mapping"""
        config_data = cls._load_video_config()
        config_data[aweme_id] = video_filename
        cls._save_video_config(config_data)

    async def store_video(self, video_content_item: Dict):
        """
        store content

        Args:
            video_content_item:

        Returns:

        """
        await self.save_video(video_content_item.get("aweme_id"), video_content_item.get("video_content"), video_content_item.get("extension_file_name"))

    def make_save_file_name(self, aweme_id: str, extension_file_name: str) -> str:
        """
        make save file name by store type

        Args:
            aweme_id: aweme id
            extension_file_name: video filename with extension

        Returns:

        """
        return f"{self.video_store_path}/dy_{aweme_id}.mp4"

    async def save_video(self, aweme_id: str, video_content: str, extension_file_name):
        """
        save video to local

        Args:
            aweme_id: aweme id
            video_content: video content
            extension_file_name: video filename with extension

        Returns:

        """
        try:
            pathlib.Path(self.video_store_path).mkdir(parents=True, exist_ok=True)
            save_file_name = self.make_save_file_name(aweme_id, extension_file_name)
            async with aiofiles.open(save_file_name, 'wb') as f:
                await f.write(video_content)
                utils.logger.info(f"[DouYinVideoStoreImplement.save_video] save video {save_file_name} success ...")

            self._update_video_config(aweme_id, f"dy_{aweme_id}.mp4")
        except Exception as e:
            utils.logger.error(f"[DouYinVideoStoreImplement.save_video] Failed to save video: {e}")
