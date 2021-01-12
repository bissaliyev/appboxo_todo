
def _invalidate_cached_data(user_id):
    cache_key = f"todo_{pk}"
    cache.delete(cache_key)


def user_post_save_handler(sender, instance, created, **kwargs):
    if not created:
        _invalidate_cached_data(instance.id)


def user_post_delete_handler(sender, instance, **kwargs):
    _invalidate_cached_data(instance.id)