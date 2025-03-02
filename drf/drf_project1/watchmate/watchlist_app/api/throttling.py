from rest_framework.throttling import UserRateThrottle

class ReviewCreateViewThrottle(UserRateThrottle):
    scope = 'revie-create'

class ReviewlistViewThrottle(UserRateThrottle):
    scope = 'review-list'