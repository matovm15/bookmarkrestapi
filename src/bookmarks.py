from flask import Blueprint, request

bookmarks = Blueprint("bookmarks", __name__, url_prefix="/api/v1/bookmarks")
