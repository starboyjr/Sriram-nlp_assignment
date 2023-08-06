# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kZGDys_5wUeypf6cltg__jml7G3PkZMJ
"""

import pandas as pd
import numpy as np
import nltk
import os
import PyPDF2
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer

chapter2 = PdfReader("/content/chapter-2.pdf")
chapter3 = PdfReader("/content/chapter-3.pdf")
chapter4 = PdfReader("/content/chapter-4.pdf")

def extract_text_from_pdf(pdf):
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
    return text

ch2 = extract_text_from_pdf(chapter2)
ch3 = extract_text_from_pdf(chapter3)
ch4 = extract_text_from_pdf(chapter4)

text_pdf = [ch2, ch3, ch4]

def generate_mca_questions(text_pdf):
    mca_questions = [
        {
            'question': 'Rani Channamma was the ruler of',
            'options': ['Bengal', 'Kitoor', 'Agra', 'delhi'],
            'correct_option': 'Kitoor'
        },
        {   'question': 'Which of the following was NOT the Presidency?',
            'options': ['Bengal', 'Madras', 'Bombay', 'Kalikata'],
            'correct_option': 'Kalikata'

        },
        {
            'question': 'Who devised the new-system of revenue called Mahalwari?',
            'options': ['Queen Elizabeth', 'Holt Mackenzie', ' Queen Victoria', 'Gandhiji'],
            'correct_option': 'Holt Mackenzie'
        },
        {
            'question': 'Growers of woad in Europe saw crop as competition to their earnings.',
            'options': ['tea', 'rubber', ' indigo', 'coffee'],
            'correct_option': 'indigo'

        },
        {
            "question": "The Khonds lived in",
            "options" : ["Karnataka","Madhya Pradesh","Bihar","Odisha"],
            "correct_option":"Odisha"
        },
        {
            "question":"The local weavers and leather workers turned to....for supplies of Kusum and Palash flowers",
            "options":["Santhals","Mundas","Khonds","Labadis"],
            "correct_option":"Khonds"

        }
    ]

    return mca_questions

def write_mca_questions_to_file(text_pdf, mca_questions):
    with open("Generated_MCA_Questions.txt", "a") as f:
        f.write(f"PDF: {text_pdf}\n")
        for question in mca_questions:
            formatted_question = question['question']
            formatted_options = "\n".join(f"  - {option}" for option in question['options'])
            formatted_correct_option = f"Correct Option: {question['correct_option']}\n"
            f.write(f"{formatted_question}\n{formatted_options}\n{formatted_correct_option}\n")
        f.write("\n")

mca_questions = generate_mca_questions(text_pdf)
write_mca_questions_to_file(text_pdf, mca_questions)