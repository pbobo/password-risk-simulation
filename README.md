# 🔐 Password Risk Simulation – Brute Force Demo

## About This Project

This is a simple brute-force password cracker I built to demonstrate how fast and easy it can be to guess weak passwords. It targets 4-character passwords using only lowercase letters (`a–z`), and randomly generates guesses until it finds the correct one.

The goal here isn’t to break into anything—this is purely educational. I wanted to show how even a basic script with just a few lines of Python can expose the risks of short, simple passwords.

## What It Does

- Prompts the user to enter a password (e.g., `abcd`)
- Randomly generates guesses using lowercase letters
- Continues until it matches the password
- Tracks how long it takes to crack it

## Why It Matters

This demo proves that passwords like `abcd`, `test`, or `love` are incredibly easy to brute-force—even without fancy tools. If a 4-character password can be cracked in seconds
