#!/usr/bin/env python3.6
import random
from user import User
from credential import Credential

#functions for user_account
def create_user(fname,lname,phone,email):
  '''
  Function to create a new user
  '''
  new_user = User(fname,lname,phone,email)
  return new_user
def save_user(user):
  '''
  Function to save user
  '''
  user.save_user()

def del_user(user):
  '''
  Function to delete a user
  '''
  user.delete_user()

def copy_email(user,number):
  '''
  Function to delete a user
  '''
  user.copy_email(number)

def find_user(number):
  '''
  Function that finds a user by number and returns the user
  '''
  return User.find_by_number(number)

def check_existing_user(number):
  '''
  Function that check if user exists with number and returns a Boolean
  '''
  return User.user_exist(number)

def display_users():
  '''
  Function that returns all the saved users
  '''
  return User.display_users()
#functions for user_credential
def create_credential(uname,password,phone):
  '''
  Function to create a new credential
  '''
  new_credential = Credential(uname,password,phone)
  return new_credential

def save_credential(credential):
  '''
  Function to save credential
  '''
  credential.save_credential()

def del_credential(credential):
  '''
  Function to delete a credential
  '''
  credential.delete_credential()
