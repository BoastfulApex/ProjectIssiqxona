from rest_framework import routers
from issiqxona.views import *

router = routers.DefaultRouter()

router.register(r'products', ProductView, basename="products")
router.register(r'questions', QuestionView, basename="questions")
router.register(r'stories', StoryView, basename="stories")
router.register(r'messages', MessageView, basename="messages")
