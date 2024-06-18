from objectpack.actions import ObjectPack
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType

from django import forms
from objectpack.ui import ModelEditWindow
from .ui import UserAddWindow, UserEditWindow, GroupAddWindow


# Создание ActionPack для каждой модели
class ContentTypePack(ObjectPack):
    model = ContentType
    add_to_menu = True
    add_to_desktop = True

    add_window = ModelEditWindow.fabricate(model=model)
    edit_window = ModelEditWindow.fabricate(model=model)


class UserPack(ObjectPack):
    model = User
    add_to_menu = True
    add_to_desktop = True

    # add_window = ModelEditWindow.fabricate(model=model)
    # edit_window = ModelEditWindow.fabricate(model=model)
    edit_window = UserEditWindow
    add_window = UserAddWindow


class GroupPack(ObjectPack):
    model = Group
    add_to_menu = True
    add_to_desktop = True

    # add_window = ModelEditWindow.fabricate(model=model)
    add_window = GroupAddWindow
    # edit_window = ModelEditWindow.fabricate(model=model)
    edit_window = GroupAddWindow

class PermissionPack(ObjectPack):
    model = Permission
    add_to_menu = True
    add_to_desktop = True

    add_window = ModelEditWindow.fabricate(model=model)
    edit_window = ModelEditWindow.fabricate(model=model)


