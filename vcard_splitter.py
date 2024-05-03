#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
vcard_splitter.py

_created_ 04/23/2018 08:13a
_owner_ jtferro3
_summary_
    Splits Apple exported VCard into individual VCards.
'''

import os
import sys

# Load DATA from FILE
def load_file(filename):
    lines = list()
    try:
        file = open(filename, 'r')
    except:
        print("Failed to load.")
    else:
        for line in file:
            lines.append(line)

        file.close()
    return lines

# Save DATA to FILE
def save_file(filename, data, mode):
    file = open(filename, mode)
    file.write(data)
    file.close()

# create list of list of CONTACTS
def create_list(data):
    contacts = list()
    for line in data:
        if line == 'BEGIN:VCARD\n':
            contact = list()
            contacts.append(contact)
        contact.append(line)
    return contacts

# save each CONTACT in separate FILE
def export_contact(contacts, filepath):
    for i,contact in enumerate(contacts):
        for line in contact:
            save_file(os.path.join(filepath, str(i) + '.vcf'), line, 'a')

def main():
    file = input("Enter name of file with PATH: ")
    filepath = os.path.dirname(file)
    lines = load_file(file)
    contacts = create_list(lines)
    export_contact(contacts, filepath)
    exit()

if __name__ == '__main__':
    main()
