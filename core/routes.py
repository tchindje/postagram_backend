
from rest_framework_nested import routers

from core.user.viewsets import UserViewSet
from core.auth.viewsets import RegisterViewSet, LoginViewSet, RefreshViewSet
from core.post.viewsets import PostViewSet
from core.comment.viewsets import CommentViewSet


# simple router instantiation
router = routers.SimpleRouter()

# route for auth for ViewSet
router.register(r"auth/register", RegisterViewSet, basename="auth-register")
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

# route for  userViewSet of user
router.register(r"users", UserViewSet, basename="users")


# ##################################################################### #
# ################### POSTS   and COMMENTS                ###################### #
# ##################################################################### #

router.register(r'posts', PostViewSet, basename='posts')

posts_router = routers.NestedSimpleRouter(router, r'posts', lookup='posts')
posts_router.register(r'comments', CommentViewSet, basename='post-comments')

urlpatterns = [
    *router.urls,
    *posts_router.urls
]