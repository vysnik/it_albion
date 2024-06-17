from objectpack.actions import ObjectPack
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType

from django import forms
from objectpack.ui import ModelEditWindow
from .ui import UserAddWindow, UserEditWindow

class PermissionForm(forms.ModelForm):
    class Meta:
        model = Permission
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


# Создание ActionPack для каждой модели
class ContentTypePack(ObjectPack):
    model = ContentType
    add_to_menu = True
    menu_title = "ContentType"
    menu_group = "Security"
    action_model = "ContentType"
    add_window = ModelEditWindow.fabricate(model=model)
    edit_window = ModelEditWindow.fabricate(model=model)


class UserPack(ObjectPack):
    model = User
    add_to_menu = True
    menu_title = "User"
    menu_group = "Security"
    action_model = "User"
    # add_window = ModelEditWindow.fabricate(model=model)
    # edit_window = ModelEditWindow.fabricate(model=model)
    edit_window = UserEditWindow
    add_window = UserAddWindow


class GroupPack(ObjectPack):
    model = Group
    add_to_menu = True
    menu_title = "Group"
    menu_group = "Security"
    action_model = "Group"
    add_window = ModelEditWindow.fabricate(model=model)
    edit_window = ModelEditWindow.fabricate(model=model)

class PermissionPack(ObjectPack):
    model = Permission
    add_to_menu = True
    menu_title = "Permissions"
    menu_group = "Security"
    action_model = "Permission"
    add_window = ModelEditWindow.fabricate(model=model)
    edit_window = ModelEditWindow.fabricate(model=model)

