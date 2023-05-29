import sqlite3
import time
from datetime import datetime
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.screen import Screen
from kivy.core.window import Window
from kivy.app import App
import pygsheets
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from email.message import EmailMessage
import ssl
import smtplib
