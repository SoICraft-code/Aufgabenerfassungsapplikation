from setuptools import setup, find_packages
import os

# Bestimmen Sie den Pfad zur README-Datei relativ zu setup.py
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="task_manager_app",  # Der Name des Pakets
    version="0.1.0",  # Die Version des Pakets
    author="Lukas Domke",  # Ihr Name oder der Name des Autors
    author_email="lukas.domke@edu.fhdw.de",  # Ihre E-Mail-Adresse
    description="Eine Aufgabenerfassungsapplikation zur Verwaltung von Aufgaben",  # Kurzbeschreibung des Pakets
    long_description=long_description,  # Langbeschreibung des Pakets aus der README-Datei
    long_description_content_type="text/markdown",  # Der Typ der Langbeschreibung (in diesem Fall Markdown)
    url="https://github.com/SoICraft-code/Aufgabenerfassungsapplikation.git",  # URL zu Ihrem GitHub-Repository oder Ihrer Projektseite
    packages=find_packages(),  # Automatisches Finden aller Pakete und Unterpakete
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Mindestanforderung für die Python-Version
    install_requires=[
        # Abhängigkeiten hier angeben, falls vorhanden
        # Beispiel: 'requests', 'numpy'
    ],
    entry_points={
        'console_scripts': [
            'task_manager=main:main',
        ],
    },
)
