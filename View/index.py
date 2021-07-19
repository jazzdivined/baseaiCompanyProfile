from flask import Flask, render_template, url_for, abort, redirect


def load_section():
    raise NotImplementedError("Implement this please...")


def index():
    return render_template('Index/index.html', sections=load_section())
