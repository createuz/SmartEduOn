from rest_framework import routers

from home.viewset import *

router = routers.DefaultRouter()
router.register('country', CountryViewset)
router.register('region', RegionViewset)
router.register('rank-course', RankCourseViewset)
router.register('video-course', VideoCourseViewset)
router.register('user-edit', UsersEditViewset)
router.register('speaker', SpeakerViewset)
router.register('foydalanuvchi', UsersViewset)
router.register('like-or-dislike', LikeOrDislikeViewset)
router.register('category', CategoryViewset)
router.register('rank', RankViewset)
router.register('views-count', VideoViewsViewset)
router.register('course', CourseViewset)
router.register('top-course', TopCourseViewset)
router.register('eduon-tafsiyasi', EduonTafsiyasiViewset)
router.register('favorite-course', FavoriteCourseViewset)
router.register('payment', PaymentHistoryViewset)
router.register('order', OrderViewset)
router.register('comment', CommentViewset)
router.register('comment-course', CommentCourseViewset)
