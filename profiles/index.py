import algoliasearch_django as algoliasearch

from .models import Profile
from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

algoliasearch.register(Profile)
