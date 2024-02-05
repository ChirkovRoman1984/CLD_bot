import yaml

from dataclasses import dataclass
from typing import Dict, List, Optional
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@dataclass(frozen=True)
class Config:
    data: Dict

    def get_text(self, key) -> Optional[str]:
        return self.data['messages'].get(key, {}).get('message')

    def get_buttons(self, key) -> List[InlineKeyboardButton]:
        btns = self.data['messages'].get(key, {}).get('buttons', [])
        btns = [InlineKeyboardButton(text=btn['text'], callback_data=btn['callback_data']) for btn in btns]
        return btns

    def get_image(self, key) -> Optional[str]:
        img = self.data['messages'].get(key, {}).get('image', {}).get('url')
        if img:
            return self.data['bucket'] + img
        else:
            return img

    def get_caption(self, key) -> Optional[str]:
        return self.data['messages'].get(key, {}).get('image', {}).get('caption')

    def get_markup(self, key) -> InlineKeyboardMarkup:
        markup = InlineKeyboardMarkup(row_width=self.data['messages'].get(key, {}).get('markup_row'))
        btns = self.get_buttons(key)
        markup.add(*btns)
        return markup

    def get_all(self, key):
        return self.get_text(key), self.get_markup(key), self.get_image(key)


with open("app/config.yaml", "r", encoding='utf-8') as file:
    cfg = Config(yaml.safe_load(file))
