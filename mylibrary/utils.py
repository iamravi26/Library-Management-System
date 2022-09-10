# import here 




# Write Code Here

from mylibrary.models import UserProfile


def context(request=None, **kwargs):
    """
    Genrate Context Details
    """

    title = "LMS"
    user = request.user if (request and request.user) else None
    user_profile = UserProfile.objects.get(user=request.user) if (request and request.user) else None

    kwargs.update({
        "title":title,
        "user":user,
        "user_profile":user_profile,
    })

    return kwargs
