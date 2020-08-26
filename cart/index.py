import algoliasearch_django as algoliasearch

from .models import Item
from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

algoliasearch.register(Item)
