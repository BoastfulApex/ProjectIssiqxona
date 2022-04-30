from rest_framework import routers
from issiqxona.views import *

router = routers.DefaultRouter()

router.register(r'products', ProductView, basename="products")
router.register(r'questions', QuestionView, basename="questions")
router.register(r'categories', CategoryView, basename="categories")
router.register(r'links', LinkView, basename="links")
router.register(r'blogs', BlogView, basename="blogs")
router.register(r'images', ImageView, basename="images")
router.register(r'partners', PartnerView, basename="partners")
router.register(r'image_by_blog', ImageByBlog, basename="image_by_blog")
